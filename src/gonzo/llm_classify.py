"""LLM-driven per-thread classification.

For every thread we ask the model for a single JSON object with these fields:

    family        : top-level architecture family (slug)
    subfamily     : ≤40-char short name for the sub-family, in English
    modalities    : list[str]   (text, vision, video, audio, action, code, math, bio, ...)
    training_phase: pretrain | post-train | inference | interp | theory | evaluation | other
    key_concepts  : list[str]   (3-8 short phrases)
    one_liner     : ≤30-word distinctive contribution
    notes         : optional short remarks (e.g. "borderline, also fits X")

We keep the family slug aligned with the rule-based taxonomy so the LLM and
rule classifiers are interoperable. The model is allowed to introduce a *new*
slug only when no listed slug fits; in that case it must start with
'other:' and be lowercase-kebab.
"""
from __future__ import annotations

import argparse
import json
import re
import sys

from . import db as dbmod
from . import taxonomy as tax
from .llm_client import LLM, map_concurrent


# ---------------------------- prompt construction ----------------------------

def _family_menu() -> str:
    lines = []
    for f in tax.TAXONOMY:
        lines.append(f"- {f.slug:>22}  — {f.name}")
    return "\n".join(lines)


SYSTEM = """\
You classify ML/AI paper-review posts from the channel @gonzo_ML_podcasts into
an architecture-and-methodology taxonomy. The post is written in Russian but
quotes English terminology.

Reply with a SINGLE JSON object. No prose around it. Be precise and concise.

JSON shape:
{
  "family": "<slug from the menu, or 'other:short-kebab' if none fits>",
  "subfamily": "<English short label, 2-5 words>",
  "modalities": ["text"|"vision"|"video"|"audio"|"action"|"code"|"math"|"bio"|"tabular"|"graph"|"3d"|"multimodal"],
  "training_phase": "pretrain"|"post-train"|"inference"|"interp"|"theory"|"evaluation"|"data"|"systems"|"other",
  "key_concepts": ["short phrase", "another short phrase", ...],
  "one_liner": "<≤30 English words: what makes this paper distinct>",
  "notes": "<optional short remark, or empty string>"
}

Rules:
- Choose exactly ONE primary family. If a paper crosses two, pick the one
  that defines its core contribution (e.g. an SSM paper proposing a new
  optimizer is `ssm-mamba`, not `optimizers-training`).
- The subfamily groups similar papers together; reuse common labels when
  possible: e.g. "MLA / latent attention", "DPO/GRPO/IPO", "process reward
  models", "Mamba expressivity analysis", "V-JEPA video", "agentic coding",
  "edge-of-stability", "MoE routing".
- key_concepts must be the most distinguishing terms, not generic ones
  like "LLM" or "transformer".
- one_liner is forward-looking and specific. Don't say "this paper studies".
- For meta/channel-news/podcast posts, family is `meta`.
"""


def make_user_prompt(thread: dict) -> str:
    text = (thread.get("text") or "").strip()
    title = (thread.get("title") or "").strip()
    summary = (thread.get("summary") or "").strip()
    arxiv = thread.get("arxiv_url") or ""
    # Trim body to a budget. Heads (title + TL;DR) carry most signal.
    body_excerpt = text
    if len(body_excerpt) > 4000:
        # Keep the head (title block + TL;DR) plus the start of "Мясо"
        head, _, rest = body_excerpt.partition("# TL;DR")
        if rest:
            tldr, _, meat = rest.partition("# Мясо")
            body_excerpt = (
                head.strip()
                + "\n\n# TL;DR\n"
                + tldr[:1500]
                + ("\n\n# Мясо\n" + meat[:1500] if meat else "")
            )[:4000]
        else:
            body_excerpt = body_excerpt[:4000]
    return (
        "FAMILY MENU (use the slug exactly):\n"
        + _family_menu()
        + "\n\nPOST TITLE:\n"
        + (title or "(missing)")
        + "\n\nARXIV: "
        + (arxiv or "(none)")
        + "\n\nAUTO-EXTRACTED SUMMARY:\n"
        + (summary or "(missing)")
        + "\n\nPOST BODY EXCERPT (truncated):\n"
        + body_excerpt
    )


# ----------------------------- DB schema helpers ----------------------------

EXTRA_COLS = {
    "llm_family": "TEXT",
    "llm_subfamily": "TEXT",
    "llm_modalities": "TEXT",
    "llm_training_phase": "TEXT",
    "llm_key_concepts": "TEXT",
    "llm_one_liner": "TEXT",
    "llm_notes": "TEXT",
}


def ensure_columns(conn) -> None:
    existing = {row[1] for row in conn.execute("PRAGMA table_info(threads)").fetchall()}
    for col, ty in EXTRA_COLS.items():
        if col not in existing:
            conn.execute(f"ALTER TABLE threads ADD COLUMN {col} {ty}")
    conn.commit()


# ----------------------------- main classify pass ---------------------------

def _normalize_family(slug: str) -> str:
    s = (slug or "").strip().lower()
    s = re.sub(r"[\s_]+", "-", s)
    return s


def classify_thread(llm: LLM, thread: dict) -> dict:
    obj = llm.json(
        kind="classify_v1",
        system=SYSTEM,
        user=make_user_prompt(thread),
    )
    # Sanitize fields
    obj["family"] = _normalize_family(obj.get("family") or "uncategorized")
    obj["subfamily"] = (obj.get("subfamily") or "").strip()[:80]
    mods = obj.get("modalities") or []
    if isinstance(mods, str):
        mods = [m.strip() for m in mods.split(",") if m.strip()]
    obj["modalities"] = [str(m).strip().lower() for m in mods][:6]
    obj["training_phase"] = (obj.get("training_phase") or "").strip().lower()[:30]
    kc = obj.get("key_concepts") or []
    if isinstance(kc, str):
        kc = [k.strip() for k in kc.split(",") if k.strip()]
    obj["key_concepts"] = [str(k).strip() for k in kc][:10]
    obj["one_liner"] = (obj.get("one_liner") or "").strip()
    obj["notes"] = (obj.get("notes") or "").strip()
    obj["id"] = thread["id"]
    return obj


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--db", required=True)
    p.add_argument("--model", default=None, help="OpenAI model (default: gpt-5)")
    p.add_argument("--workers", type=int, default=8)
    p.add_argument(
        "--limit", type=int, default=None, help="Optional cap (for testing)"
    )
    p.add_argument(
        "--only-missing", action="store_true",
        help="Only classify threads that don't yet have llm_family set",
    )
    args = p.parse_args(argv)

    conn = dbmod.connect(args.db)
    ensure_columns(conn)

    q = "SELECT * FROM threads"
    if args.only_missing:
        q += " WHERE llm_family IS NULL OR llm_family = ''"
    rows = [dict(r) for r in conn.execute(q).fetchall()]
    if args.limit:
        rows = rows[: args.limit]
    print(f"classifying {len(rows)} threads with model={args.model or 'gpt-5'}",
          file=sys.stderr)

    llm = LLM(model=args.model)

    def _one(t):
        try:
            return classify_thread(llm, t)
        except Exception as e:
            return {"id": t["id"], "_error": str(e)[:240]}

    results = map_concurrent(_one, rows, workers=args.workers, desc="classify")

    n_ok, n_err = 0, 0
    with conn:
        for r in results:
            if "_error" in r:
                n_err += 1
                continue
            n_ok += 1
            conn.execute(
                "UPDATE threads SET llm_family=?, llm_subfamily=?, llm_modalities=?, "
                "llm_training_phase=?, llm_key_concepts=?, llm_one_liner=?, llm_notes=? "
                "WHERE id=?",
                (
                    r.get("family"),
                    r.get("subfamily"),
                    ", ".join(r.get("modalities") or []),
                    r.get("training_phase"),
                    json.dumps(r.get("key_concepts") or [], ensure_ascii=False),
                    r.get("one_liner"),
                    r.get("notes"),
                    r["id"],
                ),
            )
    print(f"done. ok={n_ok}  errors={n_err}", file=sys.stderr)
    if n_err:
        for r in results:
            if "_error" in r:
                print(f"  err on id={r['id']}: {r['_error']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
