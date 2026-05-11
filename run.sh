#!/usr/bin/env bash
# End-to-end pipeline: scrape -> stitch -> enrich -> classify -> report.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
PY="${PY:-/Users/Oleg.Bukhvalov/miniconda3/envs/pt/bin/python}"
DB="${DB:-$ROOT/data/gonzo.db}"
SINCE="${SINCE:-2024-05-11}"

export PYTHONPATH="$ROOT/src:${PYTHONPATH:-}"

mkdir -p "$ROOT/data" "$ROOT/reports"

echo "[gonzo] scraping since $SINCE -> $DB"
"$PY" -m gonzo.scrape  --db "$DB" --since "$SINCE" --resume

echo "[gonzo] stitching threads"
"$PY" -m gonzo.stitch  --db "$DB"

echo "[gonzo] enriching threads"
"$PY" -m gonzo.enrich  --db "$DB"

echo "[gonzo] classifying threads"
"$PY" -m gonzo.classify --db "$DB"

echo "[gonzo] writing rule-based report"
"$PY" -m gonzo.report   --db "$DB" --out "$ROOT/reports"

if [ -f "$ROOT/.env" ]; then
  echo "[gonzo] LLM classification (only missing rows)"
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
