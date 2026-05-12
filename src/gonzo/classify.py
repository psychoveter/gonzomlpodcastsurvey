"""Tag each thread with an architecture family (and secondary tags).

Also extract a short summary for each thread (1-3 sentences from the
"ЧТО сделали:" section if present, else the first paragraph of the body).
"""
from __future__ import annotations

import argparse
import re
import sys

from . import db as dbmod
from . import taxonomy as tax


WHAT_RE = re.compile(
    r"(?:ЧТО\s+сделали[:\.\s]*)(.*?)(?=ПОЧЕМУ|Для\s+практик|#\s|$)",
    re.S | re.I,
)
TLDR_RE = re.compile(r"#\s*TL;DR\s*(.*?)(?=#\s*Мясо|#\s*Meat|$)", re.S | re.I)


def short_summary(text: str, max_chars: int = 600) -> str | None:
    """Pick a compact summary: prefer 'ЧТО сделали' bullet, else TL;DR, else
    first informative paragraph."""
    m = WHAT_RE.search(text)
    if m:
        s = m.group(1).strip()
        s = re.sub(r"\s+", " ", s)
        return s[:max_chars].strip()
    m = TLDR_RE.search(text)
    if m:
        s = re.sub(r"\s+", " ", m.group(1)).strip()
        return s[:max_chars].strip() or None
    # Fallback: first meaningful paragraph after the title/authors/link cluster.
    META_PREFIX = re.compile(
        r"^(Статья|Код|Ревью|Paper|Code|Review|Authors|Авторы|Title|Название)\s*[:|]",
        re.I,
    )
    for para in text.split("\n\n"):
        para = para.strip()
        if not para:
            continue
        # Drop paragraphs that look like the metadata cluster: even multi-line
        # blocks where >=half of lines start with Authors:/Paper:/etc.
        lines = [ln.strip() for ln in para.splitlines() if ln.strip()]
        meta_lines = sum(1 for ln in lines if META_PREFIX.match(ln))
        url_lines = sum(1 for ln in lines if "://" in ln)
        if lines and (meta_lines + url_lines) >= max(1, len(lines) // 2):
            continue
        # Drop very short or URL-only paragraphs.
        if len(para) < 80:
            continue
        if META_PREFIX.match(para):
            continue
        return re.sub(r"\s+", " ", para)[:max_chars]
    return None


def classify(text: str) -> dict:
    scores = tax.score(text)
    if not scores:
        return {"arch_family": "uncategorized", "arch_tags": None, "scores": []}
    primary = scores[0][0]
    # Only emit secondary tags whose score is >= 50% of primary OR >= 4 points,
    # excluding meta if any real family fires.
    primary_score = scores[0][1]
    secondaries = []
    for fam, s in scores[1:]:
        if fam.slug == "meta" and primary.slug != "meta":
            continue
        if s >= max(4, primary_score // 2):
            secondaries.append(fam.slug)
    if primary.slug == "meta" and len(scores) > 1:
        # Promote next family if meta was just because of a youtube link
        nxt = scores[1][0]
        if scores[1][1] >= 4:
            primary = nxt
            secondaries = [s for s in secondaries if s != nxt.slug]
            secondaries = ["meta"] + secondaries if scores[0][1] >= 5 else secondaries
    return {
        "arch_family": primary.slug,
        "arch_tags": ", ".join(secondaries) if secondaries else None,
        "scores": [(f.slug, s) for f, s in scores],
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--db", required=True)
    args = p.parse_args(argv)
    conn = dbmod.connect(args.db)
    rows = conn.execute("SELECT channel, first_msg_id, text FROM threads").fetchall()
    n = 0
    for r in rows:
        info = classify(r["text"] or "")
        summary = short_summary(r["text"] or "")
        conn.execute(
            "UPDATE threads SET arch_family=?, arch_tags=?, summary=? "
            "WHERE channel=? AND first_msg_id=?",
            (info["arch_family"], info["arch_tags"], summary,
             r["channel"], r["first_msg_id"]),
        )
        n += 1
    conn.commit()
    print(f"classified {n} threads", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
