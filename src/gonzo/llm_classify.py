"""LLM-driven classification, paper-centric.

We classify each *paper* (a row in the ``papers`` table) — not each individual
thread. A paper's input is its ``merged_text``: the concatenation of all
member-thread bodies. This way, the gonzo_ML teaser and the
gonzo_ML_podcasts long-form review of the same paper are classified together
and get a single consistent label.

For every paper the model produces a single JSON object:

    family        : top-level architecture family (slug)
    subfamily     : ≤40-char short label, English
    modalities    : list[str]   (text, vision, video, audio, ...)
    training_phase: pretrain | post-train | inference | interp | theory | evaluation | other
    key_concepts  : list[str]   (3-8 short phrases)
    one_liner     : ≤30-word distinctive contribution
    notes         : optional remark

Family slugs are kept aligned with the curated taxonomy when possible. The
model is allowed to introduce a new slug (lowercase-kebab) only when no
listed slug fits.
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
You classify ML/AI paper-review posts from the @gonzo_ML / @gonzo_ML_podcasts
Telegram channels into an architecture-and-methodology taxonomy. Posts are
written in Russian but quote English terminology. The input you receive is the
union of one or more channel posts about the same paper (a short teaser plus
an extended long-form review, when available).

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
- For meta / channel-news / podcast-about-the-channel posts, family is `meta`.
"""


def make_user_prompt(paper: dict) -> str:
    text = (paper.get("merged_text") or "").strip()
    title = (paper.get("title") or "").strip()
    arxiv = paper.get("canonical_arxiv") or ""
    # Trim body to a budget. Heads (title + TL;DR) carry most signal.
    body_excerpt = text
    if len(body_excerpt) > 6000:
        # Keep the head plus the TL;DR / Мясо sections if present.
        head, _, rest = body_excerpt.partition("# TL;DR")
        if rest:
            tldr, _, meat = rest.partition("# Мясо")
            body_excerpt = (
                head.strip()
                + "\n\n# TL;DR\n"
                + tldr[:2500]
                + ("\n\n# Мясо\n" + meat[:2500] if meat else "")
            )[:6000]
        else:
            body_excerpt = body_excerpt[:6000]
    return (
        "FAMILY MENU (use the slug exactly):\n"
        + _family_menu()
        + "\n\nPAPER TITLE:\n"
        + (title or "(missing)")
        + "\n\nCANONICAL ARXIV: "
        + (arxiv or "(none)")
        + "\n\nMERGED POST BODY (truncated):\n"
        + body_excerpt
    )


# ----------------------------- classification ------------------------------

def _normalize_family(slug: str) -> str:
    s = (slug or "").strip().lower()
    s = re.sub(r"[\s_]+", "-", s)
    return s


def classify_paper(llm: LLM, paper: dict) -> dict:
    obj = llm.json(
        kind="classify_paper_v1",
        system=SYSTEM,
        user=make_user_prompt(paper),
    )
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
    obj["id"] = paper["id"]
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
        help="Only classify papers that don't yet have llm_family set",
    )
    args = p.parse_args(argv)

    conn = dbmod.connect(args.db)

    q = "SELECT * FROM papers"
    if args.only_missing:
        q += " WHERE llm_family IS NULL OR llm_family = ''"
    rows = [dict(r) for r in conn.execute(q).fetchall()]
    if args.limit:
        rows = rows[: args.limit]
    print(
        f"classifying {len(rows)} papers with model={args.model or 'gpt-5'}",
        file=sys.stderr,
    )

    llm = LLM(model=args.model)

    def _one(p):
        try:
            return classify_paper(llm, p)
        except Exception as e:
            return {"id": p["id"], "_error": str(e)[:240]}

    results = map_concurrent(_one, rows, workers=args.workers, desc="classify")

    n_ok, n_err = 0, 0
    with conn:
        for r in results:
            if "_error" in r:
                n_err += 1
                continue
            n_ok += 1
            conn.execute(
                "UPDATE papers SET llm_family=?, llm_subfamily=?, llm_modalities=?, "
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
                print(f"  err on paper id={r['id']}: {r['_error']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
