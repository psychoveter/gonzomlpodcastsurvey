"""Produce a markdown + JSON classification report of the gonzo channel.

Usage:
    python -m gonzo.report --db data/gonzo.db --out reports/
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from . import db as dbmod
from .taxonomy import TAXONOMY


def _post_url(channel: str, msg_id: int) -> str:
    return f"https://t.me/{channel}/{msg_id}"


def _normalize_title(title: str | None, text: str) -> str:
    """Pick a sensible title for the markdown link.

    Order of preference:
      1. A `Title:` / `Название:` labelled line in the post header.
      2. The existing title if it doesn't look like an author list.
      3. The first English line in the head that isn't a label, author list,
         or URL.
    """
    m = re.search(r"^(?:Title|Название)\s*[:|]\s*(.+)$", text, re.M | re.I)
    if m:
        cand = m.group(1).strip()
        if cand:
            return cand

    def _is_authors(s: str) -> bool:
        if not s or len(s) > 400 or s.count(",") < 1 or re.search(r"[?!\":]", s):
            return False
        parts = [p.strip() for p in s.split(",") if p.strip()]
        if len(parts) < 2:
            return False
        name_like = 0
        for p in parts[:8]:
            if re.match(r"^[A-Za-zА-ЯЁ][\w.\-']{0,20}(?:\s+[\w.\-']{0,25})+$", p):
                name_like += 1
        return name_like >= max(2, len(parts) // 2)

    if title and not _is_authors(title):
        return title

    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    for ln in lines[:8]:
        if re.match(r"^(Статья|Код|Ревью|Paper|Code|Review|Authors|Авторы|Title|Название)\s*[:|]", ln, re.I):
            continue
        if "://" in ln and len(ln) < 200:
            continue
        if _is_authors(ln):
            continue
        if len(ln) < 8:
            continue
        return ln
    return title or "(untitled)"


def family_section(fam, threads: list[dict]) -> str:
    n = len(threads)
    head = f"## {fam.name}  ·  {n} post{'s' if n != 1 else ''}\n"
    head += f"<small>slug: `{fam.slug}`</small>\n\n"
    head += fam.description + "\n\n"
    # Sort by date desc
    threads = sorted(threads, key=lambda t: t["posted_at"], reverse=True)
    lines: list[str] = []
    for t in threads:
        title = _normalize_title(t["title"], t["text"] or "")
        date = (t["posted_at"] or "")[:10]
        url = _post_url(t["channel"], t["first_msg_id"])
        arxiv = t["arxiv_url"]
        github = t["github_url"]
        review = t["review_url"]
        bits = [f"[{title}]({url})"]
        if arxiv:
            bits.append(f"[arXiv]({arxiv})")
        if github:
            bits.append(f"[code]({github})")
        if review:
            bits.append(f"[review]({review})")
        head_line = f"- **{date}** (@{t['channel']}) · " + "  ·  ".join(bits)
        summary = (t["summary"] or "").strip()
        if summary:
            summary_short = summary if len(summary) <= 360 else summary[:357] + "..."
            head_line += f"\n  - {summary_short}"
        tags = (t["arch_tags"] or "").strip()
        if tags:
            head_line += f"\n  - <sub>tags: {tags}</sub>"
        lines.append(head_line)
    return head + "\n".join(lines) + "\n"


def build_markdown(conn) -> str:
    rows = conn.execute(
        "SELECT * FROM threads ORDER BY posted_at DESC"
    ).fetchall()
    rows = [dict(r) for r in rows]

    total = len(rows)
    oldest = min(r["posted_at"] for r in rows)
    newest = max(r["posted_at"] for r in rows)
    n_arxiv = sum(1 for r in rows if r["arxiv_url"])
    n_github = sum(1 for r in rows if r["github_url"])
    n_review = sum(1 for r in rows if r["review_url"])
    channels = sorted({r["channel"] for r in rows})

    by_family: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_family[r["arch_family"] or "uncategorized"].append(r)

    md = []
    md.append("# Architectures and techniques covered in the gonzoML channels")
    md.append("")
    channels_md = ", ".join(f"[`@{c}`](https://t.me/{c})" for c in channels)
    md.append(
        f"Survey of {total} paper-review posts from {channels_md} "
        f"(period {oldest[:10]} – {newest[:10]})."
    )
    md.append("")
    md.append(
        f"**Coverage:** {n_arxiv}/{total} threads link to arXiv "
        f"({n_arxiv*100//total}%), {n_github}/{total} ({n_github*100//total}%) "
        f"link to code on GitHub, and {n_review}/{total} "
        f"({n_review*100//total}%) link to a long-form review on Substack."
    )
    md.append("")
    md.append(f"Generated: {datetime.utcnow().isoformat(timespec='seconds')}Z")
    md.append("")
    md.append("---")
    md.append("")

    md.append("## At-a-glance distribution")
    md.append("")
    md.append("| # | Family | Posts | Slug |")
    md.append("|---:|---|---:|---|")
    rank = 1
    ordered = []
    for fam in TAXONOMY:
        if fam.slug in by_family:
            ordered.append((fam, by_family[fam.slug]))
    # plus uncategorized (real bucket, no Family object)
    if "uncategorized" in by_family:
        from .taxonomy import Family as F
        ordered.append((
            F(slug="uncategorized",
              name="Uncategorized (niche / off-taxonomy)",
              description=(
                "Papers that don't match any of the curated families: e.g. "
                "GNN-specific work, classical-computing-meets-ML, "
                "biomimetic/morphogenetic computing, and one-off theory papers."
              ),
              patterns=[]),
            by_family["uncategorized"]))
    ordered.sort(key=lambda x: -len(x[1]))

    for fam, threads in ordered:
        md.append(f"| {rank} | {fam.name} | {len(threads)} | `{fam.slug}` |")
        rank += 1
    md.append("")
    md.append("---")
    md.append("")

    md.append("## Per-family detail")
    md.append("")
    for fam, threads in ordered:
        md.append(family_section(fam, threads))
        md.append("---")
        md.append("")
    return "\n".join(md)


def build_json(conn) -> dict:
    rows = conn.execute(
        "SELECT * FROM threads ORDER BY channel, first_msg_id"
    ).fetchall()
    rows = [dict(r) for r in rows]
    for r in rows:
        r["url"] = _post_url(r["channel"], r["first_msg_id"])
        r["title"] = _normalize_title(r["title"], r["text"] or "")
        r.pop("text", None)
    families = {f.slug: {"name": f.name, "description": f.description} for f in TAXONOMY}
    families["uncategorized"] = {
        "name": "Uncategorized (niche / off-taxonomy)",
        "description": "Papers that don't match any curated family.",
    }
    channels = sorted({r["channel"] for r in rows})
    return {
        "channels": channels,
        "channel_urls": [f"https://t.me/{c}" for c in channels],
        "generated_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "families": families,
        "threads": rows,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--db", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args(argv)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    conn = dbmod.connect(args.db)
    md = build_markdown(conn)
    js = build_json(conn)
    (out / "classification.md").write_text(md, encoding="utf-8")
    (out / "classification.json").write_text(
        json.dumps(js, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"wrote {out / 'classification.md'} ({len(md):,} bytes)", file=sys.stderr)
    print(f"wrote {out / 'classification.json'}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
