# gonzo — Architectures map of the gonzoML Telegram channels

Scrape two public Telegram channels —
[`gonzo_ML`](https://t.me/gonzo_ML) (long-running, 2019→present) and
[`gonzo_ML_podcasts`](https://t.me/gonzo_ML_podcasts) (newer long-form
reviews, 2024-10→present) — into a single local database, **dedupe** papers
that appear in both, and classify the architectures and techniques discussed.

## Pipeline

1. **Scrape** each channel via its public web preview `t.me/s/<channel>`
   (no Telegram API credentials required). The scraper takes `--channel`,
   so the same pipeline ingests `gonzo_ML` and `gonzo_ML_podcasts` into the
   same SQLite file.
2. **Persist** raw posts into SQLite at `data/gonzo.db`. The schema is
   multi-channel: `(channel, id)` is the natural key for `messages`,
   `(channel, first_msg_id)` for `threads`.
3. **Stitch** consecutive messages from one channel into logical "threads"
   (one paper / topic per thread) using a 5-minute proximity rule.
4. **Enrich**: extract arXiv / GitHub / Substack / Nature links, titles,
   authors and keywords from each thread.
5. **Rule-based classify** threads into a 29-family architecture taxonomy
   (`taxonomy.py`) — fast, deterministic, useful as a sanity check.
6. **Dedupe** (`dedup.py`): group threads (across channels) into *papers*.
   Primary signal is the canonical arXiv id (URL normalized, version
   stripped); fallback is a normalized-title match inside a ±60-day window.
   A `papers` table is rebuilt and every thread gets a `paper_id`. A teaser
   on `@gonzo_ML` and the extended review on `@gonzo_ML_podcasts` collapse
   into a single paper.
7. **LLM classify** (`llm_classify.py`): for each *paper* (not thread!),
   gpt-5 reads the merged text from all member threads and emits
   `{family, subfamily, modalities, training_phase, key_concepts,
   one_liner}` in one JSON object. All calls are cached in
   `data/cache/llm.sqlite`.
8. **Hierarchical clustering** (`hierarchy.py`): inside each family the LLM
   merges raw `subfamily` labels into 3–8 coherent sub-clusters and writes
   a 2–4 sentence *distinguishing* description that contrasts each cluster
   with its siblings at the same level. Top-level family descriptions are
   regenerated against the other families.
9. **Reports**:
   - Markdown survey + JSON under `reports/`.
   - `reports/hierarchy.json` — the full tree, papers carry a `sources`
     array with one entry per contributing channel post.
   - `web/public/data.json` — the SPA's data source.
10. **SPA** (`web/`): a Vite + React + Tailwind app rendering a D3
    circle-packing of the hierarchy, with side panel, search, zoom and a
    "paper-only" filter.

## Layout

```
src/gonzo/
  scrape.py         # paginating web-preview scraper (--channel) -> SQLite
  parse.py          # HTML -> structured records
  stitch.py         # consecutive messages -> logical threads, per channel
  enrich.py         # extract arxiv/github/substack/title/authors
  taxonomy.py       # 29 curated families w/ regex patterns
  classify.py       # rule-based per-thread tagging
  dedup.py          # group threads across channels into papers
  report.py         # rule-based markdown + JSON report
  llm_client.py     # OpenAI wrapper with on-disk SQLite cache
  llm_classify.py   # per-paper LLM classification (gpt-5)
  hierarchy.py      # LLM clustering + distinguishing descriptions
  build_web_data.py # export data.json for the SPA
  db.py             # SQLite schema, in-place v1→v2 migration
data/
  gonzo.db
  cache/llm.sqlite  # response cache (so reruns are free)
reports/
  classification.md
  classification.json
  hierarchy.json
web/                # Vite + React + Tailwind + D3 circle-pack SPA
  src/
    App.jsx
    CirclePack.jsx
    DetailPanel.jsx
  public/data.json
```

## Running

The Python toolchain uses the `pt` conda env on this Mac
(`/Users/Oleg.Bukhvalov/miniconda3/envs/pt/bin/python`); it has `requests`,
`bs4`, `openai`, and `python-dotenv`.

```bash
# Put your key into ./.env (gitignored):
cp .env.example .env  # then edit

# One-shot pipeline (idempotent — uses --resume / --only-missing / LLM cache).
# Scrapes both channels; PODCASTS_SINCE / GONZOML_SINCE override the cutoffs.
./run.sh

# Or step by step:
PY=/Users/Oleg.Bukhvalov/miniconda3/envs/pt/bin/python
PYTHONPATH=src $PY -m gonzo.scrape       --db data/gonzo.db \
                                         --channel gonzo_ML_podcasts \
                                         --since 2024-05-11 --resume
PYTHONPATH=src $PY -m gonzo.scrape       --db data/gonzo.db \
                                         --channel gonzo_ML \
                                         --since 2019-01-01 --resume
PYTHONPATH=src $PY -m gonzo.stitch       --db data/gonzo.db
PYTHONPATH=src $PY -m gonzo.enrich       --db data/gonzo.db
PYTHONPATH=src $PY -m gonzo.classify     --db data/gonzo.db
PYTHONPATH=src $PY -m gonzo.dedup        --db data/gonzo.db
PYTHONPATH=src $PY -m gonzo.report       --db data/gonzo.db --out reports/
PYTHONPATH=src $PY -m gonzo.llm_classify --db data/gonzo.db --only-missing --workers 12
PYTHONPATH=src $PY -m gonzo.hierarchy    --db data/gonzo.db --out reports/hierarchy.json
PYTHONPATH=src $PY -m gonzo.build_web_data \
  --db data/gonzo.db --hierarchy reports/hierarchy.json \
  --out web/public/data.json
```

Existing v1 single-channel databases are upgraded in-place on the next
`db.connect()` call: `messages` / `threads` are rebuilt with a `channel`
column (defaulting to `gonzo_ML_podcasts` for legacy rows), a `papers` table
is added, and `PRAGMA user_version` is bumped to `2`.

Then run the SPA:

```bash
cd web
npm install
npm run dev    # http://localhost:5174
# or:
npm run build  # static bundle in web/dist/
```

## What we have so far

A complete run on 2026-05-12 (UTC), covering **both channels**:

- **8 581 raw Telegram messages** scraped:
  - `@gonzo_ML`              — 5 054 messages (2019-02-21 → 2026-05-12)
  - `@gonzo_ML_podcasts` — 3 527 messages (2024-10-22 → 2026-05-10)
- **1 756 logical threads** stitched (1 500 from `@gonzo_ML`, 256 from
  `@gonzo_ML_podcasts` after multi-message reviews collapse).
- **1 524 deduplicated papers** in the `papers` table, of which
  **208 are cross-channel** (a teaser on `@gonzo_ML` and an extended
  review on `@gonzo_ML_podcasts` share the same canonical arXiv id and are
  merged into one paper exposing both telegram links).
- A 29-family taxonomy + the LLM's own family proposals; gpt-5 classifies
  every paper from its merged thread text, then the same model groups
  papers into **261 sub-clusters across 34 families** with comparative
  "distinguishing" descriptions.

The full report lives in [`reports/classification.md`](reports/classification.md)
(also as JSON in [`reports/classification.json`](reports/classification.json)).

## LLM classification

The LLM pipeline (`llm_classify` + `hierarchy`) currently uses **OpenAI
gpt-5** (see `.env.example`). All requests are SHA-cached in
`data/cache/llm.sqlite`, so re-runs are free; full classification of 1 524
papers takes about 6 min with 12 parallel workers. The hierarchy step then
adds 34 family-vs-others descriptions and 34 family-internal sub-cluster
sets in another ~90 s. Distinguishing descriptions are explicitly
comparative ("Unlike … this sub-cluster …").

## SPA

`web/` is a small Vite + React + Tailwind + D3 app. It renders the
hierarchy as a **circle packing**: families are outer circles, sub-clusters
are mid-level circles, papers are leaves. Areas are proportional to paper
counts. Each paper bubble represents one *deduplicated paper*, and the
right-side detail panel lists all telegram sources for that paper (one entry
per channel — typically one for `@gonzo_ML` and one for `@gonzo_ML_podcasts`
for cross-channel papers, marked with an amber `cross-channel` pill in the
paper-list view).

Controls:

- **scroll wheel / two-finger scroll** — zoom in/out around the cursor.
- **click + drag** — pan.
- **click bubble** — drill into a family / cluster and open its description
  in the side panel.
- **click background** — reset to the full map.
- **paper-only checkbox** (in the header) — filter out posts that aren't
  actually paper reviews. With the box on, the SPA hides:
  (1) the entire `meta` family (channel admin, podcast logistics, industry
  announcements, polls) and
  (2) any other paper that has neither an arXiv URL / canonical arXiv id
  nor a substack-style long-form review.
  Empty sub-clusters and families collapse automatically; the header
  shows `<shown> / <total> papers` while the filter is on.
- **search field** highlights matching titles / one-liners / key concepts
  across the visible tree.

White labels render with a thin black stroke on top of the bubbles and
nudge along the y-axis to resolve same-row collisions; paper labels appear
when zoomed in far enough and wrap onto multiple lines.

### Publishing

`web/` is structured as a GitHub-Pages-ready SPA. The whole repo is meant to
be pushed to GitHub as a single project (Python pipeline at the root, SPA
under `web/`).

- `web/vite.config.js` reads `VITE_BASE` (default
  `/gonzomlpodcastsurvey/`) so the same code can serve from a sub-path on
  GitHub Pages or from `/` for a custom domain.
- `.github/workflows/deploy.yml` (at the **repo root**, where GitHub
  discovers it) runs on every push to `main` that touches `web/**`. It
  scopes `npm ci` / `npm run build` to `web/` via
  `defaults.run.working-directory` and uploads `web/dist/` via
  `actions/deploy-pages`.
- `web/public/data.json` is the prebuilt hierarchy snapshot — commit it
  along with code changes; CI re-deploys automatically.

To publish, push to a new GitHub repo (default name
`gonzomlpodcastsurvey`), enable *Settings → Pages → Build and deployment →
GitHub Actions*, and the next push to `main` will surface a URL like
`https://<owner>.github.io/gonzomlpodcastsurvey/`. See `web/README.md` for
the full publishing recipe.

## Known limitations

- `@gonzo_ML` is a curation / news channel: a sizable fraction of its posts
  are link-shares, polls and channel administration rather than full paper
  reviews. The LLM correctly routes those into the `meta` family; the SPA's
  `paper-only` filter is on by default to hide them.
- Dedup currently relies on canonical arXiv id (primary) and exact
  normalized-title match within ±60 days (fallback). It does **not** catch
  cases where the two channels reference the same paper but neither post
  contains an arXiv URL and the titles diverge stylistically — those
  remain as separate papers.
- The rule-based classifier (still produced as a sanity check) occasionally
  tags a paper into a family on a passing mention. The LLM classifier
  fixes most of these but introduces its own minor noise (e.g. a
  theory-heavy paper on an SSM-vs-Transformer comparison may end up in
  `theory-generalization` rather than `ssm-mamba`).
- For some older posts the title heuristic picks a line that happens to
  look like an author list. The arXiv link is still correct, and the
  one-liner / cluster placement are LLM-driven so they remain useful.

## Notes on the channels

Both channels post long paper-review threads. Because Telegram caps a single
message at ~4096 chars, a single logical review is usually split across
several consecutive messages (sometimes one header image + N body messages,
posted in the same minute). The `stitch` step rebuilds those into a single
thread keyed by the leading message id, scoped per channel.

`@gonzo_ML_podcasts` tends to publish a longer, podcast-driven take on the
same paper that `@gonzo_ML` posted as a shorter teaser — the dedup step
collapses such pairs and the SPA exposes both telegram links per merged
paper.
