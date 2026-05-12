"""Extract structured fields from each thread's text.

Each thread typically has the form:
  <Russian paraphrased title>
  <English original title>
  <authors line>
  Статья: <arxiv url>
  Код: <github url>
  Ревью: <substack url>
  # TL;DR
  ...
  # Мясо
  ...
"""
from __future__ import annotations

import argparse
import re
import sys

from . import db as dbmod

ARXIV_RE = re.compile(r"https?://arxiv\.org/abs/([\w./-]+)", re.I)
GITHUB_RE = re.compile(r"https?://github\.com/([\w./_-]+)", re.I)
SUBSTACK_RE = re.compile(r"https?://[\w-]+\.substack\.com/p/[\w./-]+", re.I)
NATURE_RE = re.compile(r"https?://www\.nature\.com/articles/[\w.-]+", re.I)
HF_RE = re.compile(r"https?://huggingface\.co/[\w./-]+", re.I)

# Section markers used by the channel
SECTION_TLDR = re.compile(r"^#\s*TL;DR", re.M | re.I)
SECTION_MEAT = re.compile(r"^#\s*Мясо", re.M)


def _first(rx: re.Pattern, text: str) -> str | None:
    m = rx.search(text)
    return m.group(0) if m else None


_TITLE_LABEL_RE = re.compile(r"^(?:Title|Название)\s*[:|]\s*(.+)$", re.I)
_AUTHORS_LABEL_RE = re.compile(r"^(?:Authors|Авторы)\s*[:|]\s*(.+)$", re.I)
_PAPER_LABEL_RE = re.compile(r"^(Статья|Код|Ревью|Paper|Code|Review)\s*[:|]", re.I)


def _looks_like_authors_line(s: str) -> bool:
    """Author lists typically: 'A. B. Cdef, Gh Ij, K. Lm, ...'.
    Heuristic: ≥1 comma AND no terminal punctuation/quotes AND mostly
    Title-Case tokens."""
    if not s or len(s) > 400:
        return False
    if s.count(",") < 1:
        return False
    if re.search(r"[?!\":]", s):
        return False
    # If most comma-separated chunks look like 'First Last' / 'F. Last', it's authors
    parts = [p.strip() for p in s.split(",") if p.strip()]
    if len(parts) < 2:
        return False
    name_like = 0
    for p in parts[:8]:
        if re.match(r"^[A-Z][\w.\-']{0,15}(?:\s+[\w.\-']{0,20})+$", p):
            name_like += 1
        elif re.match(r"^[А-ЯЁ][\w.\-']{0,20}(?:\s+[\w.\-']{0,25})+$", p):
            name_like += 1
    return name_like >= max(2, len(parts) // 2)


def _parse_header(text: str) -> dict:
    """Heuristically pull title/authors from the head of the post.

    Two channel formats are observed:
      (a) Russian-first paraphrase format (most posts after 2024-12):
            <ru paraphrased title>
            <blank>
            <en title>
            <authors line(s)>
            Статья: <url>
      (b) Older English-first format:
            <en title>
            Authors: ...
            Paper: ...
            Code: ...
            Review: ...
            ...
        sometimes prefixed with `Title:` / `Название:` labels.
    """
    out: dict[str, str | None] = {"title_ru": None, "title_en": None, "authors": None}
    lines = [ln.strip() for ln in text.splitlines()]

    # First, scan for explicit Title:/Authors: labels (older format)
    for ln in lines[:12]:
        m = _TITLE_LABEL_RE.match(ln)
        if m and not out["title_en"]:
            out["title_en"] = m.group(1).strip()
        m = _AUTHORS_LABEL_RE.match(ln)
        if m and not out["authors"]:
            out["authors"] = m.group(1).strip()

    # Walk the head block.
    i = 0
    while i < len(lines) and not lines[i]:
        i += 1
    if i >= len(lines):
        return out

    # If a Title: label was found, treat first non-label line as the RU title only
    # if it doesn't itself start with a label and we don't already have title_en.
    head_lines: list[str] = []
    while i < len(lines) and len(head_lines) < 8:
        ln = lines[i]
        i += 1
        if not ln:
            if head_lines and out.get("title_ru") is not None:
                break
            else:
                continue
        if _PAPER_LABEL_RE.match(ln) or _TITLE_LABEL_RE.match(ln) or _AUTHORS_LABEL_RE.match(ln):
            break
        head_lines.append(ln)

    # Apply rules to head_lines.
    if head_lines:
        first = head_lines[0]
        # Heuristic: if first is plainly authors-like and we have no title_en yet,
        # then this older post has no title line above authors — keep title as None.
        if _looks_like_authors_line(first) and not out["authors"]:
            out["authors"] = first
        else:
            out["title_ru"] = first

    if len(head_lines) >= 2 and not out["title_en"]:
        cand = head_lines[1]
        if not _looks_like_authors_line(cand):
            out["title_en"] = cand

    if not out["authors"]:
        # Authors line is the first head line that looks like an authors list,
        # excluding what we've already picked as titles.
        used = {out["title_ru"], out["title_en"]}
        for ln in head_lines[1:]:
            if ln in used:
                continue
            if _looks_like_authors_line(ln):
                out["authors"] = ln
                break

    # Final sanity: if title_ru itself looks like authors, swap it out.
    if out["title_ru"] and _looks_like_authors_line(out["title_ru"]):
        if not out["authors"]:
            out["authors"] = out["title_ru"]
        out["title_ru"] = None

    return out


def _extract_keywords(text: str, max_n: int = 25) -> list[str]:
    """Extract candidate keywords/keyphrases: words inside backticks plus
    capitalized acronyms / model names appearing in the body."""
    kws: list[str] = []
    seen: set[str] = set()
    # backticked code-like identifiers in TL;DR/Мясо: "FADE", "AdamW", `O(d)`, etc.
    for m in re.finditer(r"`([^`\n]{1,60})`", text):
        k = m.group(1).strip()
        if 1 <= len(k) <= 30 and k.lower() not in seen:
            seen.add(k.lower())
            kws.append(k)
    # all-caps acronyms (2-10 letters), e.g. FADE, JEPA, VLM, MoE, SSM
    for m in re.finditer(r"\b([A-Z]{2,10}(?:-[A-Z0-9]{1,6})?)\b", text):
        k = m.group(1)
        if k.lower() in seen:
            continue
        seen.add(k.lower())
        kws.append(k)
        if len(kws) >= max_n:
            break
    return kws[:max_n]


def enrich_thread(text: str) -> dict:
    header = _parse_header(text)
    arxiv = _first(ARXIV_RE, text)
    github = _first(GITHUB_RE, text)
    substack = _first(SUBSTACK_RE, text)
    if not substack:
        # Some posts may put the review elsewhere; nature/HF can be useful fallbacks
        substack = _first(NATURE_RE, text) or _first(HF_RE, text)
    kws = _extract_keywords(text)
    # Prefer the English title (more universally informative), fall back to RU
    title = header.get("title_en") or header.get("title_ru")
    # Final guard: never let an authors-like string slip through as the title.
    if title and _looks_like_authors_line(title):
        title = header.get("title_en") if header.get("title_en") != title else None
    return {
        "title": title,
        "authors": header.get("authors"),
        "arxiv_url": arxiv,
        "github_url": github,
        "review_url": substack,
        "keywords": ", ".join(kws) if kws else None,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--db", required=True)
    args = p.parse_args(argv)
    conn = dbmod.connect(args.db)
    rows = conn.execute("SELECT channel, first_msg_id, text FROM threads").fetchall()
    n = 0
    for r in rows:
        info = enrich_thread(r["text"] or "")
        conn.execute(
            "UPDATE threads SET title=?, authors=?, arxiv_url=?, github_url=?, "
            "review_url=?, keywords=? WHERE channel=? AND first_msg_id=?",
            (
                info["title"],
                info["authors"],
                info["arxiv_url"],
                info["github_url"],
                info["review_url"],
                info["keywords"],
                r["channel"],
                r["first_msg_id"],
            ),
        )
        n += 1
    conn.commit()
    print(f"enriched {n} threads", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
