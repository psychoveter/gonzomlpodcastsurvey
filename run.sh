#!/usr/bin/env bash
# End-to-end pipeline:
#   scrape -> stitch -> enrich -> classify -> dedup -> [LLM] llm_classify -> hierarchy -> web.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
PY="${PY:-/Users/Oleg.Bukhvalov/miniconda3/envs/pt/bin/python}"
DB="${DB:-$ROOT/data/gonzo.db}"

# Default per-channel cutoffs. Each channel has its own --since because they
# have very different histories. Override with PODCASTS_SINCE / GONZOML_SINCE.
PODCASTS_SINCE="${PODCASTS_SINCE:-2024-05-11}"
GONZOML_SINCE="${GONZOML_SINCE:-2019-01-01}"

export PYTHONPATH="$ROOT/src:${PYTHONPATH:-}"

mkdir -p "$ROOT/data" "$ROOT/reports"

echo "[gonzo] scraping @gonzo_ML_podcasts since $PODCASTS_SINCE -> $DB"
"$PY" -m gonzo.scrape  --db "$DB" --channel gonzo_ML_podcasts \
                       --since "$PODCASTS_SINCE" --resume

echo "[gonzo] scraping @gonzo_ML since $GONZOML_SINCE -> $DB"
"$PY" -m gonzo.scrape  --db "$DB" --channel gonzo_ML \
                       --since "$GONZOML_SINCE" --resume

echo "[gonzo] stitching threads (per channel)"
"$PY" -m gonzo.stitch  --db "$DB"

echo "[gonzo] enriching threads"
"$PY" -m gonzo.enrich  --db "$DB"

echo "[gonzo] rule-based classify"
"$PY" -m gonzo.classify --db "$DB"

echo "[gonzo] dedup (group threads into papers)"
"$PY" -m gonzo.dedup    --db "$DB"

echo "[gonzo] writing rule-based report"
"$PY" -m gonzo.report   --db "$DB" --out "$ROOT/reports"

if [ -f "$ROOT/.env" ]; then
  echo "[gonzo] LLM classification of papers (only missing rows)"
  "$PY" -m gonzo.llm_classify --db "$DB" --only-missing

  echo "[gonzo] hierarchical clustering + cluster descriptions"
  "$PY" -m gonzo.hierarchy --db "$DB" --out "$ROOT/reports/hierarchy.json"

  echo "[gonzo] writing web/public/data.json"
  "$PY" -m gonzo.build_web_data \
    --db "$DB" \
    --hierarchy "$ROOT/reports/hierarchy.json" \
    --out "$ROOT/web/public/data.json"
else
  echo "[gonzo] skipping LLM steps (no .env with OPENAI_API_KEY)"
fi

echo "[gonzo] done"
