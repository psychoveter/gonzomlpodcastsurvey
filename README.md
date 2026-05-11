# gonzo — Classification of architectures from `@gonzo_ML_podcasts`

Scrape the public Telegram channel
[`gonzo_ML_podcasts`](https://t.me/gonzo_ML_podcasts), build a local database
of posts from the last 2 years, and classify the architectures and techniques
discussed there.

## Pipeline

1. **Scrape** posts via the public web preview `t.me/s/gonzo_ML_podcasts`
   (no Telegram API credentials required).
2. **Persist** raw posts into SQLite at `data/gonzo.db`.
3. **Stitch** multi-message threads into logical "posts" (one paper / topic
   per thread).
4. **Enrich**: extract arXiv / GitHub / Substack links, titles, authors,
   keywords from each thread.
5. **Rule-based classify** threads into a 29-family architecture taxonomy
   (`taxonomy.py`) — fast, deterministic, useful as a sanity check.
6. **LLM classify** (`llm_classify.py`): for each thread, gpt-5 emits
   `{family, subfamily, modalities, training_phase, key_concepts, one_liner}`
   in a single JSON object; all calls are cached in
   `data/cache/llm.sqlite`.
7. **Hierarchical clustering** (`hierarchy.py`): inside each family the LLM
   merges raw `subfamily` labels into 3–8 coherent sub-clusters and writes a
   2–4 sentence *distinguishing* description that contrasts each cluster
   with its siblings at the same level. The top-level family description is
   regenerated the same way against the other families.
8. **Reports**:
   - Markdown survey + JSON under `reports/`.
   - `reports/hierarchy.json` — the full tree.
   - `web/public/data.json` — the SPA's data source.
9. **SPA** (`web/`): a Vite + React + Tailwind app rendering a D3
   circle-packing of the hierarchy, with side panel + search + zoom.

## Layout

```
src/gonzo/
  scrape.py         # paginating web-preview scraper -> SQLite
  parse.py          # HTML -> structured records
  stitch.py         # consecutive messages -> logical threads
  enrich.py         # extract arxiv/github/substack/title/authors
  taxonomy.py       # 29 curated families w/ regex patterns
  classify.py       # rule-based per-thread tagging
  report.py         # rule-based markdown + JSON report
  llm_client.py     # OpenAI wrapper with on-disk SQLite cache
  llm_classify.py   # per-thread LLM classification (gpt-5)
  hierarchy.py      # LLM clustering + distinguishing descriptions
  build_web_data.py # export data.json for the SPA
  db.py             # SQLite schema and helpers
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

# One-shot pipeline (idempotent — uses --resume / --only-missing / LLM cache):
./run.sh

# Or step by step:
PY=/Users/Oleg.Bukhvalov/miniconda3/envs/pt/bin/python
PYTHONPATH=src $PY -m gonzo.scrape       --db data/gonzo.db --since 2024-05-11
PYTHONPATH=src $PY -m gonzo.stitch       --db data/gonzo.db
PYTHONPATH=src $PY -m gonzo.enrich       --db data/gonzo.db
PYTHONPATH=src $PY -m gonzo.classify     --db data/gonzo.db
PYTHONPATH=src $PY -m gonzo.report       --db data/gonzo.db --out reports/
PYTHONPATH=src $PY -m gonzo.llm_classify --db data/gonzo.db --only-missing --workers 10
PYTHONPATH=src $PY -m gonzo.hierarchy    --db data/gonzo.db --out reports/hierarchy.json
PYTHONPATH=src $PY -m gonzo.build_web_data \
  --db data/gonzo.db --hierarchy reports/hierarchy.json \
  --out web/public/data.json
```

Then run the SPA:

```bash
cd web
npm install
npm run dev    # http://localhost:5174
# or:
npm run build  # static bundle in web/dist/
```

## What we have so far

A complete run on 2026-05-11 (UTC) produced:

- **3527 messages** scraped from the channel
  (`2024-10-22` → `2026-05-10`); the channel didn't exist 2 years ago, so this
  is its full history.
- **328 logical threads** (paper-review posts), stitched from the raw
  messages using a 5-minute proximity rule.
- **310 / 328 (94%)** threads link to arXiv, **166 / 328 (50%)** to GitHub,
  **266 / 328 (81%)** to a long-form review on Substack.
- A 29-family architecture taxonomy classifying every thread, with the top
  families being:
  - Reasoning & test-time compute (47)
  - LLM post-training / RLHF-DPO-GRPO (40)
  - Optimizers & training dynamics (26)
  - Agentic systems (24)
  - LLM pretraining (21)
  - MoE (19), world models (18), JEPA/SSL (17), SSM/Mamba (17),
    mechanistic interpretability (13), diffusion (11), KV/attention systems
    (9), RAG (7), continual learning / memory (7), and more.

The full report lives in [`reports/classification.md`](reports/classification.md)
(also as JSON in [`reports/classification.json`](reports/classification.json)).

## LLM classification

The LLM pipeline (`llm_classify` + `hierarchy`) currently uses **OpenAI
gpt-5** (see `.env.example`). All requests are SHA-cached in
`data/cache/llm.sqlite`, so re-runs are free; full classification of 328
threads takes about 100 s with 10 parallel workers. After classification, the
LLM produces 163 sub-clusters across 31 families, each with a 2–4 sentence
"distinguishing" description that contrasts it with sibling clusters at the
same level — the descriptions are explicitly comparative ("Unlike … this
sub-cluster …").

## SPA

`web/` is a small Vite + React + Tailwind + D3 app. It renders the
hierarchy as a **circle packing**: families are outer circles, sub-clusters
are mid-level circles, papers are leaves. Areas are proportional to paper
counts.

Controls:

- **scroll wheel / two-finger scroll** — zoom in/out around the cursor.
- **click + drag** — pan.
- **click bubble** — drill into a family / cluster and open its description
  in the side panel.
- **click background** — reset to the full map.

A legend acts as a quick family picker, and a search field highlights
matching titles / one-liners / key concepts across the whole tree. Family
labels stagger top/bottom and cluster labels radiate outwards across three
vertical lanes with semi-transparent pill backgrounds, so adjacent labels
stay legible without colliding on the same horizontal line.

### Publishing

`web/` is structured as a standalone, GitHub-Pages-ready SPA:

- `web/vite.config.js` reads `VITE_BASE` (default
  `/gonzo-ml-podcasts-map/`) so the same code can serve from a sub-path on
  GitHub Pages or from `/` for a custom domain.
- `web/.github/workflows/deploy.yml` builds on every push to `main` and
  publishes `dist/` via `actions/deploy-pages`.
- `web/public/data.json` is the prebuilt hierarchy snapshot — commit it
  along with code changes; CI re-deploys automatically.

To publish, push `web/` to a new GitHub repo (default name
`gonzo-ml-podcasts-map`), enable *Settings → Pages → Build and deployment →
GitHub Actions*, and the next push to `main` will surface a URL like
`https://<owner>.github.io/gonzo-ml-podcasts-map/`. See `web/README.md` for
the full publishing recipe.

## Known limitations

- The rule-based classifier (still produced as a sanity check) occasionally
  tags a paper into a family on a passing mention. The LLM classifier
  fixes most of these but introduces its own minor noise (e.g. a
  theory-heavy paper on an SSM-vs-Transformer comparison may end up in
  `theory-generalization` rather than `ssm-mamba`).
- For three older posts the title heuristic picks the title line that
  happens to look like an author list. The arXiv link is still correct.
- Niche posts (GNN over-squashing, Forward-Forward CNNs, classical
  billiards as a Turing machine, etc.) end up in a `misc` cluster inside
  whichever family the LLM chose for them.

## Notes on the channel

The channel posts long paper-review threads. Because Telegram caps a single
message at ~4096 chars, a single logical review is usually split across
several consecutive messages (one header image + N body messages, posted in
the same minute). The `stitch` step rebuilds those into a single thread keyed
by the leading message id.