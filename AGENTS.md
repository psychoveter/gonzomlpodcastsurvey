# gonzo — agent instructions

This project ingests posts from two Telegram channels —
[`@gonzo_ML`](https://t.me/gonzo_ML) and
[`@gonzo_ML_podcasts`](https://t.me/gonzo_ML_podcasts) — into a single SQLite
database, deduplicates them into *papers*, classifies each paper via LLM, and
ships the result as a static SPA in `web/`.

Always read `README.md` for the up-to-date architecture overview; this file
contains operational instructions for the agent.

## Where things live

- Code: `src/gonzo/` — one module per pipeline step.
- DB: `data/gonzo.db` (SQLite, schema versioned via `db.SCHEMA_VERSION`).
- LLM cache: `data/cache/llm.sqlite` (content-keyed, safe to keep across runs).
- Reports: `reports/` (`classification.{md,json}`, `hierarchy.json`).
- SPA payload: `web/public/data.json`.
- Orchestration: `run.sh`.

## Default Python

Use `PY=/Users/Oleg.Bukhvalov/miniconda3/envs/pt/bin/python` and run modules
with `PYTHONPATH=src`. Examples below assume that.

## Updating the database with fresh posts

The recurring task: pull the latest posts from both channels, re-classify only
what's new, regenerate `web/public/data.json`.

### Quick path (recommended)

1. Snapshot the current freshness so we know what to fetch:
   ```bash
   PYTHONPATH=src $PY -c "
   from gonzo import db as dbmod
   conn = dbmod.connect('data/gonzo.db')
   for r in conn.execute(
       'SELECT channel, MAX(id) AS max_id, MAX(posted_at) AS newest, COUNT(*) AS n '
       'FROM messages GROUP BY channel'):
       print(r['channel'], 'n=', r['n'], 'newest=', r['newest'])
   "
   ```
2. **Scrape both channels** with `--since` set a few days *before* the newest
   known `posted_at` (NOT `--resume`; see "Scraper quirk" below):
   ```bash
   PYTHONPATH=src $PY -m gonzo.scrape --db data/gonzo.db \
       --channel gonzo_ML_podcasts --since <YYYY-MM-DD>
   PYTHONPATH=src $PY -m gonzo.scrape --db data/gonzo.db \
       --channel gonzo_ML          --since <YYYY-MM-DD>
   ```
   `INSERT OR REPLACE` makes re-fetching the small overlap harmless.
3. **Re-stitch / enrich / classify / dedup.** `stitch` wipes & rebuilds threads
   per channel, so all four must run together:
   ```bash
   PYTHONPATH=src $PY -m gonzo.stitch  --db data/gonzo.db
   PYTHONPATH=src $PY -m gonzo.enrich  --db data/gonzo.db
   PYTHONPATH=src $PY -m gonzo.classify --db data/gonzo.db
   PYTHONPATH=src $PY -m gonzo.dedup   --db data/gonzo.db
   ```
4. **LLM-classify** new papers. `dedup` rebuilds the `papers` table from
   scratch, so every paper row is "missing" `llm_family` again; the LLM cache
   is content-keyed (hash of `merged_text`) and will serve >95% of calls from
   disk almost instantly. Only genuinely new merged texts hit the API.
   ```bash
   PYTHONPATH=src $PY -m gonzo.llm_classify \
       --db data/gonzo.db --only-missing --workers 12
   ```
5. **Hierarchy + web data:**
   ```bash
   PYTHONPATH=src $PY -m gonzo.hierarchy \
       --db data/gonzo.db --out reports/hierarchy.json
   PYTHONPATH=src $PY -m gonzo.build_web_data \
       --db data/gonzo.db \
       --hierarchy reports/hierarchy.json \
       --out web/public/data.json
   PYTHONPATH=src $PY -m gonzo.report --db data/gonzo.db --out reports
   ```
6. **Verify:** open the SPA, or eyeball `web/public/data.json` newest entries:
   ```bash
   PYTHONPATH=src $PY -c "
   import json
   d = json.load(open('web/public/data.json'))
   s = d['stats']
   print('newest', s['newest_post'], 'papers', s['papers_total'],
         'cross', s['papers_merged_cross_channel'])
   for c in s['channel_stats']: print(c)
   "
   ```

### Full rebuild

Use `./run.sh` for an end-to-end run starting from the project defaults. It
relies on `--resume`, which is fine for the *initial* backfill but is the wrong
mode for refresh-from-the-top (see below). For incremental updates prefer the
manual steps above.

## Scraper quirk: `--resume` is backfill, not refresh

`gonzo.scrape --resume` starts at `MIN(id)` for the channel and walks
*backwards* through Telegram's `?before=<id>` pagination. That's the right
behaviour when you're filling in older history, but it never picks up newer
posts. For incremental refresh, run without `--resume` and pass a `--since`
that overlaps the newest known `posted_at` by a few days. The parser walks
from the top of the channel and stops once it crosses `--since`.

If you find yourself doing this often, consider adding a `--mode refresh`
flag that starts from `MAX(id)+1` instead of `MIN(id)`.

## Failure-mode notes

- `hierarchy.py` does ~34 LLM cluster/describe calls per family. Both
  `_cluster_one` and `_describe` now catch per-family exceptions and fall back
  to a single `core` cluster + curated description, so one stuck LLM call no
  longer kills the whole tree. If you see `[cluster] WARN <slug>: ...` in the
  log, the family was rendered from the fallback.
- The `dedup` step `DELETE FROM papers` + reassigns `paper_id` on every run.
  That's intentional: the canonical-arXiv graph can change as new threads
  arrive. Any code that stores paper ids long-term needs to re-resolve them
  after dedup.
- Schema migrations live in `db._migrate` and run before the main `SCHEMA`
  script. The migration *must* finish before any `CREATE INDEX` referring to
  the new columns is applied.

## SPA / publishing

- Local dev: `cd web && npm run dev` (Vite, default port 5173).
- Production build is driven by `.github/workflows/deploy.yml` at the repo
  root. It builds `web/` with `VITE_BASE=/gonzomlpodcastsurvey/` and deploys to
  GitHub Pages.
- `web/public/data.json` is the only runtime artifact the SPA needs.

## Don'ts

- Don't truncate or rename existing channels in the DB without writing a
  migration step in `db._migrate`.
- Don't bypass `dedup`: classification, hierarchy and the SPA all assume
  papers are the unit of analysis, not threads.
- Don't manually edit `web/public/data.json`; regenerate via
  `gonzo.build_web_data`.
