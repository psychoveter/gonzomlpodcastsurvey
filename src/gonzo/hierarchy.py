"""Build a hierarchical clustering of the corpus *over papers* (not raw threads).

Hierarchy levels (root → leaves):

  root
   └── family             (top-level architecture / methodology family)
        └── cluster       (LLM-consolidated sub-cluster of papers)
             └── paper    (deduped paper; possibly with multiple channel sources)

For every internal node (families and clusters) the LLM produces a
distinguishing description: 2-4 sentences explaining what makes this node
distinct from its SIBLINGS at the same level.

We never re-cluster across families: families come from the per-paper LLM
classification, then within each family the LLM proposes 3-8 coherent
sub-clusters.

Each leaf paper exposes ALL of its telegram sources (gonzo_ML teaser +
gonzo_ML_podcasts review, etc.) under ``sources``.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from . import db as dbmod
from . import taxonomy as tax
from .llm_client import LLM, map_concurrent


# ---------- prompts ---------------------------------------------------------

CLUSTER_SYSTEM = """\
You are organizing a corpus of ML/AI paper reviews into clean sub-clusters
within a single architecture/methodology family. Your job is to:

1. Partition the given papers into a small number (typically 3-8) of
   coherent sub-clusters. Every paper must belong to exactly one sub-cluster.
   If there are very few papers (≤4), produce just 1-2 sub-clusters.
2. For each sub-cluster, produce:
   - slug:   lowercase-kebab, ≤30 chars
   - name:   2-5 English words, Title Case
   - distinguishing: 2-4 sentences explaining what makes this sub-cluster
                     DISTINCT from the OTHER sub-clusters you are proposing
                     in this same family. Be specific about technique,
                     formal property, modality, or methodology that
                     differentiates it.
3. Map each paper id to its sub-cluster slug.

Reply with a SINGLE JSON object of the form:
{
  "clusters": [
    {
      "slug": "...",
      "name": "...",
      "distinguishing": "...",
      "paper_ids": [<int>, <int>, ...]
    },
    ...
  ]
}
- The union of paper_ids must equal the set of input papers (no omissions, no duplicates).
- Cluster slugs must be unique within the response.
- Prefer existing subfamily labels when they are sensible.
- Keep cluster granularity uniform: don't propose 5 huge clusters plus 1 singleton if you can merge it.
"""


FAMILY_DESC_SYSTEM = """\
You write a one-paragraph distinguishing description for a top-level family
of ML/AI papers, contrasting it with the other families listed.

Reply with a SINGLE JSON object:
{
  "description": "2-4 English sentences. Concrete and specific. Focus on what
                  technique, training paradigm, modality, or formal property
                  marks papers in THIS family apart from the others. Avoid
                  vague phrasing like 'this family covers X'; instead say
                  what binds the papers together that no other family does."
}
"""


# ---------- helpers ---------------------------------------------------------

def _cluster_user_prompt(family_slug: str, family_name: str, family_desc: str,
                          papers: list[dict]) -> str:
    paper_lines = []
    for p in papers:
        concepts = ""
        try:
            kc = json.loads(p.get("llm_key_concepts") or "[]")
            concepts = ", ".join(kc[:6])
        except Exception:
            pass
        paper_lines.append(
            f"- id={p['id']}  "
            f"sub='{(p.get('llm_subfamily') or '').strip()}'  "
            f"title='{(p.get('title') or '').strip()[:100]}'  "
            f"one_liner='{(p.get('llm_one_liner') or '').strip()[:200]}'  "
            f"concepts=[{concepts}]"
        )
    return (
        f"FAMILY: {family_name}  (slug: {family_slug})\n"
        f"FAMILY DESCRIPTION: {family_desc}\n\n"
        f"PAPERS ({len(papers)}):\n"
        + "\n".join(paper_lines)
        + "\n\nPropose coherent sub-clusters and a distinguishing description "
          "for each. Partition the paper ids exactly."
    )


def _family_desc_user_prompt(target: tax.Family, all_families: list[tax.Family],
                              clusters: list[dict]) -> str:
    sibling_lines = []
    for f in all_families:
        marker = "  <- TARGET" if f.slug == target.slug else ""
        sibling_lines.append(f"- {f.slug}: {f.name}{marker}")
    cluster_block = ""
    if clusters:
        cluster_block = "Sub-clusters inside the target family:\n" + "\n".join(
            f"  - {c['name']} ({c['slug']}): {c['distinguishing']}"
            for c in clusters
        )
    return (
        "ALL FAMILIES:\n"
        + "\n".join(sibling_lines)
        + "\n\nTARGET FAMILY: "
        + target.name
        + f" (slug: {target.slug})\nCurated description: {target.description}\n\n"
        + cluster_block
        + "\n\nWrite the distinguishing description for the TARGET family vs all others."
    )


def _safe_slug(s: str, used: set[str]) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (s or "cluster").lower()).strip("-") or "cluster"
    base = s
    i = 2
    while s in used:
        s = f"{base}-{i}"
        i += 1
    used.add(s)
    return s


def _coalesce_partition(papers: list[dict], clusters: list[dict]) -> list[dict]:
    valid_ids = {p["id"] for p in papers}
    seen: set[int] = set()
    out: list[dict] = []
    used_slugs: set[str] = set()
    for c in clusters:
        slug = _safe_slug(c.get("slug") or c.get("name", "cluster"), used_slugs)
        ids = []
        for pid in c.get("paper_ids") or []:
            try:
                pid = int(pid)
            except Exception:
                continue
            if pid in valid_ids and pid not in seen:
                ids.append(pid)
                seen.add(pid)
        if not ids and not c.get("name"):
            continue
        out.append({
            "slug": slug,
            "name": (c.get("name") or slug.replace("-", " ").title()).strip(),
            "distinguishing": (c.get("distinguishing") or "").strip(),
            "paper_ids": ids,
        })
    missing = sorted(valid_ids - seen)
    if missing:
        slug = _safe_slug("misc", used_slugs)
        out.append({
            "slug": slug,
            "name": "Miscellaneous",
            "distinguishing": "Papers that did not fit any of the other proposed sub-clusters.",
            "paper_ids": missing,
        })
    return out


# ---------- build tree ------------------------------------------------------

def _family_lookup() -> dict[str, tax.Family]:
    return {f.slug: f for f in tax.TAXONOMY}


def build_clusters_for_family(llm: LLM, family_slug: str, papers: list[dict],
                              fam_lookup: dict[str, tax.Family]) -> list[dict]:
    fam = fam_lookup.get(family_slug)
    fam_name = fam.name if fam else family_slug
    fam_desc = fam.description if fam else ""
    obj = llm.json(
        kind="cluster_family_v1",
        system=CLUSTER_SYSTEM,
        user=_cluster_user_prompt(family_slug, fam_name, fam_desc, papers),
    )
    clusters = obj.get("clusters") or []
    return _coalesce_partition(papers, clusters)


def describe_family(llm: LLM, fam: tax.Family, all_families: list[tax.Family],
                    clusters: list[dict]) -> str:
    obj = llm.json(
        kind="family_desc_v1",
        system=FAMILY_DESC_SYSTEM,
        user=_family_desc_user_prompt(fam, all_families, clusters),
    )
    return (obj.get("description") or "").strip()


def _sources_for_paper(conn, paper_id: int) -> tuple[list[dict], str | None]:
    """Return (sources, best_summary) for a paper.

    Sources are the contributing thread posts (one per channel-post). The
    summary is the longest non-empty rule-based summary among member threads
    — usually the podcast/long-form review when both channels covered it.
    """
    rows = conn.execute(
        "SELECT channel, first_msg_id, posted_at, arxiv_url, github_url, "
        "review_url, summary "
        "FROM threads WHERE paper_id = ? ORDER BY posted_at",
        (paper_id,),
    ).fetchall()
    out: list[dict] = []
    best_summary: str | None = None
    for r in rows:
        ch = r["channel"]
        msg_id = r["first_msg_id"]
        out.append({
            "channel": ch,
            "msg_id": msg_id,
            "posted_at": r["posted_at"],
            "url": f"https://t.me/{ch}/{msg_id}",
            "arxiv_url": r["arxiv_url"],
            "github_url": r["github_url"],
            "review_url": r["review_url"],
        })
        s = (r["summary"] or "").strip()
        if s and (best_summary is None or len(s) > len(best_summary)):
            best_summary = s
    return out, best_summary


def build_hierarchy(conn, llm: LLM, *,
                    min_family_size_for_clustering: int = 3) -> dict:
    papers = [dict(r) for r in conn.execute("SELECT * FROM papers").fetchall()]
    fam_lookup = _family_lookup()

    by_family: dict[str, list[dict]] = defaultdict(list)
    for r in papers:
        f = (r.get("llm_family") or "uncategorized").strip().lower()
        by_family[f].append(r)

    fam_order: list[str] = []
    known_slugs = {f.slug for f in tax.TAXONOMY}
    for fslug in sorted(by_family.keys(),
                        key=lambda s: (s not in known_slugs, -len(by_family[s]))):
        fam_order.append(fslug)

    def _cluster_one(item):
        fslug, ppl = item
        if len(ppl) < min_family_size_for_clustering:
            return fslug, [{
                "slug": "core",
                "name": (fam_lookup[fslug].name if fslug in fam_lookup else fslug).strip(),
                "distinguishing": (
                    "Too few papers (≤2) for meaningful sub-clustering; "
                    "presented as a single group."
                ),
                "paper_ids": [p["id"] for p in ppl],
            }]
        return fslug, build_clusters_for_family(llm, fslug, ppl, fam_lookup)

    items = [(s, by_family[s]) for s in fam_order]
    clustered = map_concurrent(_cluster_one, items, workers=6, desc="cluster")

    all_curated_families = list(tax.TAXONOMY)
    for fslug in fam_order:
        if fslug not in fam_lookup:
            f = tax.Family(slug=fslug, name=fslug.replace("-", " ").title(),
                           description="", patterns=[])
            fam_lookup[fslug] = f
            all_curated_families.append(f)

    def _describe(item):
        fslug, clusters = item
        return fslug, describe_family(llm, fam_lookup[fslug], all_curated_families, clusters)

    descs = dict(map_concurrent(_describe, clustered, workers=6, desc="describe"))

    papers_by_id = {r["id"]: r for r in papers}
    families_out = []
    for fslug, clusters in clustered:
        fam = fam_lookup[fslug]
        cluster_nodes = []
        for c in clusters:
            paper_nodes = []
            for pid in c["paper_ids"]:
                t = papers_by_id.get(pid)
                if not t:
                    continue
                sources, summary = _sources_for_paper(conn, pid)
                paper_nodes.append({
                    "id": t["id"],
                    "title": t.get("title") or "",
                    "posted_at": t.get("earliest_posted_at"),
                    "latest_posted_at": t.get("latest_posted_at"),
                    "canonical_arxiv": t.get("canonical_arxiv"),
                    "arxiv_url": next(
                        (s["arxiv_url"] for s in sources if s["arxiv_url"]), None
                    ),
                    "github_url": next(
                        (s["github_url"] for s in sources if s["github_url"]), None
                    ),
                    "review_url": next(
                        (s["review_url"] for s in sources if s["review_url"]), None
                    ),
                    "one_liner": t.get("llm_one_liner") or "",
                    "subfamily_raw": t.get("llm_subfamily") or "",
                    "modalities": [
                        m.strip() for m in (t.get("llm_modalities") or "").split(",")
                        if m.strip()
                    ],
                    "training_phase": t.get("llm_training_phase") or "",
                    "key_concepts": _safe_json(t.get("llm_key_concepts")),
                    "summary": summary or "",
                    "sources": sources,
                })
            cluster_nodes.append({
                "slug": c["slug"],
                "name": c["name"],
                "distinguishing": c["distinguishing"],
                "papers": paper_nodes,
            })
        families_out.append({
            "slug": fslug,
            "name": fam.name,
            "curated_description": fam.description,
            "distinguishing": descs.get(fslug, ""),
            "clusters": cluster_nodes,
        })

    families_out.sort(key=lambda f: -sum(len(c["papers"]) for c in f["clusters"]))
    channels = sorted({s["channel"] for f in families_out for c in f["clusters"]
                        for p in c["papers"] for s in p["sources"]})
    return {
        "channels": channels,
        "channel_urls": [f"https://t.me/{c}" for c in channels],
        "generated_with": llm.model,
        "families": families_out,
    }


def _safe_json(s: str | None):
    if not s:
        return []
    try:
        v = json.loads(s)
        return v if isinstance(v, list) else []
    except Exception:
        return []


# ---------- CLI -------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--db", required=True)
    p.add_argument("--out", required=True, help="Output JSON path")
    p.add_argument("--model", default=None)
    args = p.parse_args(argv)
    conn = dbmod.connect(args.db)
    llm = LLM(model=args.model)
    tree = build_hierarchy(conn, llm)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(tree, ensure_ascii=False, indent=2), encoding="utf-8")
    n_papers = sum(len(c["papers"]) for f in tree["families"] for c in f["clusters"])
    n_clusters = sum(len(f["clusters"]) for f in tree["families"])
    print(
        f"wrote {out}  families={len(tree['families'])}  "
        f"clusters={n_clusters}  papers={n_papers}  "
        f"channels={tree['channels']}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
