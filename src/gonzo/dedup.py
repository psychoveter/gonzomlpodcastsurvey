"""Group threads (potentially from multiple channels) into *papers*.

Two threads describe the same paper iff:

1. They share the same canonical arXiv id (after normalizing the URL); OR
2. They share a normalized title AND were posted within ±60 days of each
   other (catches papers without an arXiv link).

After running, every thread has a non-NULL ``paper_id`` pointing into the
``papers`` table, and ``papers`` carries aggregate metadata (canonical
arxiv, title, authors, earliest/latest posting, concatenated text).

The LLM-classification step is intentionally re-run *after* dedup, so each
paper is classified once from the union of all member threads' bodies.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta

from . import db as dbmod


# ---------- canonicalization ------------------------------------------------

_ARXIV_NEW_RE = re.compile(
    r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,6})(?:v\d+)?", re.I,
)
_ARXIV_OLD_RE = re.compile(
    r"arxiv\.org/(?:abs|pdf|html)/([a-zA-Z\-\.]+/\d{7})(?:v\d+)?", re.I,
)


def canonical_arxiv(url: str | None) -> str | None:
    if not url:
        return None
    m = _ARXIV_NEW_RE.search(url)
    if m:
        return m.group(1).lower()
    m = _ARXIV_OLD_RE.search(url)
    if m:
        return m.group(1).lower()
    return None


_TITLE_PUNCT_RE = re.compile(r"[^a-z0-9]+")


def normalize_title(s: str | None) -> str:
    if not s:
        return ""
    out = _TITLE_PUNCT_RE.sub(" ", s.lower()).strip()
    out = re.sub(r"\s+", " ", out)
    return out


def _iso_dt(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


# ---------- grouping --------------------------------------------------------

def build_groups(threads: list[dict], *, title_window_days: int = 60) -> list[list[dict]]:
    """Return groups (list of threads) that point at the same paper.

    Primary key: canonical arXiv id.
    Fallback: normalized title within ±title_window_days.
    Threads not in any group end up as singletons.
    """
    # 1) Bucket by canonical arXiv id.
    arxiv_groups: dict[str, list[dict]] = defaultdict(list)
    no_arxiv: list[dict] = []
    for t in threads:
        ax = canonical_arxiv(t.get("arxiv_url"))
        if ax:
            arxiv_groups[ax].append(t)
        else:
            no_arxiv.append(t)

    groups: list[list[dict]] = list(arxiv_groups.values())

    # 2) Title-fuzzed grouping for threads without arXiv. We don't expect huge
    # numbers here, so an O(n^2) sweep is fine.
    used: set[tuple[str, int]] = set()
    for i, t in enumerate(no_arxiv):
        key = (t["channel"], t["first_msg_id"])
        if key in used:
            continue
        norm = normalize_title(t.get("title"))
        # ignore titles that are too short to disambiguate
        if len(norm) < 12:
            groups.append([t])
            used.add(key)
            continue
        ti = _iso_dt(t["posted_at"])
        bucket = [t]
        used.add(key)
        for j in range(i + 1, len(no_arxiv)):
            other = no_arxiv[j]
            other_key = (other["channel"], other["first_msg_id"])
            if other_key in used:
                continue
            other_norm = normalize_title(other.get("title"))
            if other_norm != norm:
                continue
            other_dt = _iso_dt(other["posted_at"])
            if abs((other_dt - ti).days) > title_window_days:
                continue
            bucket.append(other)
            used.add(other_key)
        groups.append(bucket)

    return groups


def _aggregate(group: list[dict]) -> dict:
    """Compute aggregate paper metadata from member threads."""
    # Sort by posted_at to make 'earliest' deterministic.
    sorted_g = sorted(group, key=lambda t: t["posted_at"])
    earliest = sorted_g[0]["posted_at"]
    latest = sorted_g[-1]["posted_at"]

    ax = next(
        (canonical_arxiv(t.get("arxiv_url")) for t in sorted_g
         if canonical_arxiv(t.get("arxiv_url"))),
        None,
    )

    # Primary thread = the one with the most informative text body.
    # Heuristic: longest text usually wins (podcast expansions tend to be
    # significantly longer than the gonzo_ML teasers).
    primary = max(sorted_g, key=lambda t: len(t.get("text") or ""))
    title = primary.get("title") or next(
        (t.get("title") for t in sorted_g if t.get("title")), None
    )
    authors = primary.get("authors") or next(
        (t.get("authors") for t in sorted_g if t.get("authors")), None
    )
    family_hint = primary.get("arch_family") or next(
        (t.get("arch_family") for t in sorted_g if t.get("arch_family")), None
    )

    # Concatenate texts in chronological order with channel headers so the
    # LLM can tell the two versions apart if needed.
    parts: list[str] = []
    for t in sorted_g:
        head = f"[source: @{t['channel']} #{t['first_msg_id']}  posted: {t['posted_at']}]"
        body = (t.get("text") or "").strip()
        if body:
            parts.append(head + "\n" + body)
    merged_text = "\n\n---\n\n".join(parts)

    return {
        "canonical_arxiv": ax,
        "title": title,
        "authors": authors,
        "earliest_posted_at": earliest,
        "latest_posted_at": latest,
        "arch_family_hint": family_hint,
        "merged_text": merged_text,
    }


# ---------- DB sync ---------------------------------------------------------

def run_dedup(conn) -> tuple[int, int, int]:
    """Wipe & rebuild the ``papers`` table and ``threads.paper_id`` links.

    Returns ``(n_threads, n_papers, n_multi_member)``.
    """
    threads = [dict(r) for r in conn.execute(
        "SELECT channel, first_msg_id, last_msg_id, posted_at, text, "
        "title, authors, arxiv_url, github_url, review_url, arch_family "
        "FROM threads"
    ).fetchall()]

    groups = build_groups(threads)
    multi = sum(1 for g in groups if len(g) > 1)

    with conn:
        conn.execute("DELETE FROM papers")
        conn.execute("UPDATE threads SET paper_id = NULL")
        # SQLite resets AUTOINCREMENT only if sqlite_sequence row is removed.
        conn.execute("DELETE FROM sqlite_sequence WHERE name='papers'")

        for g in groups:
            agg = _aggregate(g)
            cur = conn.execute(
                "INSERT INTO papers (canonical_arxiv, title, authors, "
                "earliest_posted_at, latest_posted_at, arch_family_hint, merged_text) "
                "VALUES (?,?,?,?,?,?,?)",
                (
                    agg["canonical_arxiv"], agg["title"], agg["authors"],
                    agg["earliest_posted_at"], agg["latest_posted_at"],
                    agg["arch_family_hint"], agg["merged_text"],
                ),
            )
            pid = cur.lastrowid
            conn.executemany(
                "UPDATE threads SET paper_id = ? WHERE channel = ? AND first_msg_id = ?",
                [(pid, t["channel"], t["first_msg_id"]) for t in g],
            )

    return len(threads), len(groups), multi


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--db", required=True)
    args = p.parse_args(argv)
    conn = dbmod.connect(args.db)
    n_threads, n_papers, n_multi = run_dedup(conn)
    print(
        f"dedup: {n_threads} threads -> {n_papers} papers "
        f"({n_multi} cross-channel duplicates merged)",
        file=sys.stderr,
    )
    # Show a few examples of merged groups for sanity.
    rows = conn.execute(
        "SELECT p.id, p.title, p.canonical_arxiv, "
        "  GROUP_CONCAT(t.channel || '#' || t.first_msg_id, ', ') AS sources "
        "FROM papers p JOIN threads t ON t.paper_id = p.id "
        "GROUP BY p.id HAVING COUNT(*) > 1 "
        "ORDER BY p.earliest_posted_at DESC LIMIT 5"
    ).fetchall()
    for r in rows:
        title = (r["title"] or "")[:80]
        print(f"  merged: {r['canonical_arxiv'] or '(no-arxiv)':<22}  "
              f"{title}  <- {r['sources']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
