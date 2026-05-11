"""Build the web SPA's data.json from the LLM hierarchy + DB stats."""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

from . import db as dbmod


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--db", required=True)
    p.add_argument("--hierarchy", required=True, help="Path to hierarchy.json")
    p.add_argument("--out", required=True, help="Output JSON path (typically web/public/data.json)")
    args = p.parse_args(argv)

    tree = json.loads(Path(args.hierarchy).read_text(encoding="utf-8"))

    conn = dbmod.connect(args.db)
    n_msgs = conn.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
    oldest = conn.execute("SELECT MIN(posted_at) FROM messages").fetchone()[0]
    newest = conn.execute("SELECT MAX(posted_at) FROM messages").fetchone()[0]

    n_threads = sum(len(c["papers"]) for f in tree["families"] for c in f["clusters"])
    n_clusters = sum(len(f["clusters"]) for f in tree["families"])
    n_families = len(tree["families"])

    # Modality histogram across all papers
    mod_counts: Counter = Counter()
    phase_counts: Counter = Counter()
    for f in tree["families"]:
        for c in f["clusters"]:
            for p in c["papers"]:
                for m in p.get("modalities", []):
                    mod_counts[m] += 1
                ph = p.get("training_phase")
                if ph:
                    phase_counts[ph] += 1

    out = {
        **tree,
        "stats": {
            "messages_total": n_msgs,
            "threads_total": n_threads,
            "clusters_total": n_clusters,
            "families_total": n_families,
            "oldest_post": oldest,
            "newest_post": newest,
            "modality_histogram": mod_counts.most_common(),
            "phase_histogram": phase_counts.most_common(),
            "generated_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        },
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        f"wrote {out_path}  families={n_families}  clusters={n_clusters}  papers={n_threads}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
