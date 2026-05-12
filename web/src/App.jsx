import React, { useEffect, useMemo, useState } from "react";
import CirclePack from "./CirclePack.jsx";
import DetailPanel from "./DetailPanel.jsx";

// A paper is considered "real" iff it points to an actual research artifact:
// a canonical arXiv id, an arXiv URL, or a long-form review (substack/nature/etc.).
function hasPaperLink(p) {
  return Boolean(p.canonical_arxiv || p.arxiv_url || p.review_url);
}

function applyLinkFilter(tree) {
  const families = (tree.families || [])
    .map((f) => {
      const clusters = (f.clusters || [])
        .map((c) => ({
          ...c,
          papers: (c.papers || []).filter(hasPaperLink),
        }))
        .filter((c) => c.papers.length > 0);
      return { ...f, clusters };
    })
    .filter((f) => f.clusters.length > 0);
  return { ...tree, families };
}

function excludeFamilies(tree, excludedSlugs) {
  if (!excludedSlugs || excludedSlugs.size === 0) return tree;
  return {
    ...tree,
    families: (tree.families || []).filter((f) => !excludedSlugs.has(f.slug)),
  };
}

export default function App() {
  const [data, setData] = useState(null);
  const [err, setErr] = useState(null);
  const [selection, setSelection] = useState(null);
  const [search, setSearch] = useState("");
  const [jumpId, setJumpId] = useState(null);
  const [hasLinkFilter, setHasLinkFilter] = useState(true);
  const [excludedFamilies, setExcludedFamilies] = useState(() => new Set());

  useEffect(() => {
    const base = import.meta.env.BASE_URL || "/";
    fetch(`${base}data.json`)
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then((d) => setData(d))
      .catch((e) => setErr(String(e)));
  }, []);

  // tree after the link filter (used for legend counts so each family row
  // shows how many papers would appear if you enable it).
  const linkFiltered = useMemo(() => {
    if (!data) return null;
    return hasLinkFilter ? applyLinkFilter(data) : data;
  }, [data, hasLinkFilter]);

  // tree after BOTH filters: link filter + family-checkbox exclusions.
  const displayData = useMemo(() => {
    if (!linkFiltered) return null;
    return excludeFamilies(linkFiltered, excludedFamilies);
  }, [linkFiltered, excludedFamilies]);

  // Live counts on the visible tree.
  const visibleCounts = useMemo(() => {
    if (!displayData) {
      const s = data?.stats || {};
      return {
        papers: s.papers_total ?? s.threads_total ?? 0,
        clusters: s.clusters_total || 0,
        families: s.families_total || 0,
        crossChannel: s.papers_merged_cross_channel || 0,
      };
    }
    let papers = 0;
    let clusters = 0;
    let crossChannel = 0;
    for (const f of displayData.families) {
      for (const c of f.clusters) {
        clusters += 1;
        for (const p of c.papers) {
          papers += 1;
          const chans = new Set((p.sources || []).map((s) => s.channel));
          if (chans.size > 1) crossChannel += 1;
        }
      }
    }
    return {
      papers,
      clusters,
      families: displayData.families.length,
      crossChannel,
    };
  }, [displayData, data]);

  // Reset any stale selection when the filter changes and the selected
  // paper/cluster/family is no longer present.
  useEffect(() => {
    if (!displayData || !selection) return;
    if (selection.kind === "paper") {
      const stillThere = displayData.families.some((f) =>
        f.clusters.some((c) => c.papers.some((p) => p.id === selection.data.id))
      );
      if (!stillThere) setSelection(null);
    } else if (selection.kind === "cluster") {
      const stillThere = displayData.families.some((f) =>
        f.clusters.some((c) => c.slug === selection.data.slug && f.slug === selection.family?.slug)
      );
      if (!stillThere) setSelection(null);
    } else if (selection.kind === "family") {
      const stillThere = displayData.families.some((f) => f.slug === selection.data.slug);
      if (!stillThere) setSelection(null);
    }
  }, [displayData, selection]);

  const selectedId = selection?.id || null;

  function jumpTo(sel) {
    if (!sel) return setSelection(null);
    if (sel.kind === "family") {
      setSelection({
        kind: "family",
        id: `family:${sel.data.slug}`,
        data: sel.data,
      });
      setJumpId(`family:${sel.data.slug}`);
    } else if (sel.kind === "cluster") {
      setSelection({
        kind: "cluster",
        id: `cluster:${sel.family.slug}::${sel.data.slug}`,
        data: sel.data,
        family: sel.family,
      });
      setJumpId(`cluster:${sel.family.slug}::${sel.data.slug}`);
    }
  }

  function toggleFamily(slug) {
    setExcludedFamilies((prev) => {
      const next = new Set(prev);
      if (next.has(slug)) next.delete(slug);
      else next.add(slug);
      return next;
    });
  }
  function setAllFamilies(action /* 'all' | 'none' */, candidateSlugs) {
    if (action === "all") setExcludedFamilies(new Set());
    else setExcludedFamilies(new Set(candidateSlugs));
  }

  if (err)
    return (
      <div className="flex h-screen items-center justify-center text-zinc-300">
        <div className="rounded-md border border-rose-700/40 bg-rose-950/40 px-4 py-3">
          Failed to load data: {err}
        </div>
      </div>
    );

  if (!data)
    return (
      <div className="flex h-screen items-center justify-center text-zinc-400">
        Loading…
      </div>
    );

  const stats = data.stats || {};
  const channels =
    data.channels ||
    (data.channel ? [data.channel] : ["gonzo_ML", "gonzo_ML_podcasts"]);
  const nPapersTotal = stats.papers_total ?? stats.threads_total ?? 0;
  const nPapersShown = visibleCounts.papers;
  const nClustersShown = visibleCounts.clusters;
  const nFamiliesShown = visibleCounts.families;
  const nMerged = visibleCounts.crossChannel;

  return (
    <div className="h-screen w-screen flex flex-col bg-zinc-950 text-zinc-200 overflow-hidden">
      <header className="px-4 py-3 border-b border-zinc-900 flex items-baseline gap-4 flex-wrap shrink-0">
        <h1 className="text-zinc-100 text-lg sm:text-xl font-semibold">
          {channels.map((c, i) => (
            <React.Fragment key={c}>
              {i > 0 ? <span className="text-zinc-600 mx-1">+</span> : null}
              <a
                href={`https://t.me/${c}`}
                target="_blank"
                rel="noreferrer"
                className="hover:text-cyan-300"
              >
                @{c}
              </a>
            </React.Fragment>
          ))}
          <span className="text-zinc-500"> · map</span>
        </h1>
        <div className="ml-auto">
          <input
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search title / concept…"
            className="rounded bg-zinc-900 border border-zinc-800 px-3 py-1.5 text-sm placeholder-zinc-600 focus:outline-none focus:border-zinc-600 w-64"
          />
        </div>
      </header>

      <main className="flex-1 min-h-0 grid grid-cols-1 lg:grid-cols-[1fr_440px] xl:grid-cols-[1fr_520px]">
        <div className="relative bg-zinc-950 overflow-hidden">
          <CirclePack
            data={displayData}
            onSelect={setSelection}
            selectedId={selectedId}
            search={search}
            jumpId={jumpId}
          />
          <div className="pointer-events-none absolute top-2 left-3 text-[11px] text-zinc-500 bg-zinc-950/60 backdrop-blur-sm rounded px-2 py-1 border border-zinc-900">
            scroll = zoom · drag = pan · click bubble = drill in · click background = reset
          </div>
          <FilterPanel
            families={linkFiltered?.families || []}
            excludedFamilies={excludedFamilies}
            onToggleFamily={toggleFamily}
            onSetAll={setAllFamilies}
            hasLinkFilter={hasLinkFilter}
            onToggleLinkFilter={setHasLinkFilter}
            onSelectFamily={(f) => jumpTo({ kind: "family", data: f })}
          />
        </div>
        <aside className="border-t lg:border-t-0 lg:border-l border-zinc-900 bg-zinc-950 p-4 overflow-auto scrollbar-thin">
          <DetailPanel selection={selection} onJumpTo={jumpTo} />
        </aside>
      </main>

      <footer className="px-4 py-2 border-t border-zinc-900 text-xs text-zinc-500 shrink-0 flex items-baseline gap-4 flex-wrap">
        <div>
          {stats.messages_total} raw Telegram messages → {stats.threads_total}{" "}
          logical posts → {nPapersTotal} deduplicated topics ·{" "}
          {channels.map((c, i) => (
            <React.Fragment key={c}>
              {i > 0 ? " · " : ""}
              <a
                className="hover:text-zinc-300"
                href={`https://t.me/${c}`}
                target="_blank"
                rel="noreferrer"
              >
                @{c}
              </a>
            </React.Fragment>
          ))}{" "}
          · classification via OpenAI {data.generated_with}.
        </div>
        <div className="ml-auto">
          <span className="text-zinc-300">{nPapersShown}</span> posts
          {nMerged ? (
            <>
              {" "}
              <span
                className="text-amber-200"
                title="Posts visible above that are discussed in both channels and merged into one bubble"
              >
                ({nMerged} cross-channel)
              </span>
            </>
          ) : null}{" "}
          in {nClustersShown} clusters across {nFamiliesShown} families ·{" "}
          {(stats.oldest_post || "").slice(0, 10)} —{" "}
          {(stats.newest_post || "").slice(0, 10)}
        </div>
      </footer>
    </div>
  );
}

function FilterPanel({
  families,
  excludedFamilies,
  onToggleFamily,
  onSetAll,
  hasLinkFilter,
  onToggleLinkFilter,
  onSelectFamily,
}) {
  const [open, setOpen] = useState(true);
  const allSlugs = families.map((f) => f.slug);
  const nFamiliesShown = families.filter((f) => !excludedFamilies.has(f.slug)).length;

  return (
    <div className="absolute left-3 bottom-3 max-w-[300px] bg-zinc-900/85 backdrop-blur rounded-md border border-zinc-800 text-xs text-zinc-300 shadow-lg">
      <button
        onClick={() => setOpen(!open)}
        className="w-full px-2 py-1 text-left text-zinc-400 hover:text-zinc-200 flex items-center gap-2"
      >
        <span>{open ? "▾" : "▸"}</span>
        <span>filters</span>
        <span className="ml-auto text-zinc-500">
          {nFamiliesShown}/{families.length}
        </span>
      </button>
      {open && (
        <div className="px-2 pb-2 space-y-2">
          <label
            className="flex items-center gap-1.5 text-zinc-300 cursor-pointer select-none"
            title="Hide posts that don't reference a research artifact (no arXiv id, arXiv URL, or substack-style long-form review). Posts in any family are filtered the same way."
          >
            <input
              type="checkbox"
              checked={hasLinkFilter}
              onChange={(e) => onToggleLinkFilter(e.target.checked)}
              className="accent-cyan-500"
            />
            has arxiv or substack link
          </label>
          <div className="flex items-baseline gap-2 text-[10px] uppercase tracking-wider text-zinc-500 pt-1 border-t border-zinc-800">
            <span>families</span>
            <button
              onClick={() => onSetAll("all", allSlugs)}
              className="hover:text-zinc-200 normal-case tracking-normal"
            >
              all
            </button>
            <span className="text-zinc-700">·</span>
            <button
              onClick={() => onSetAll("none", allSlugs)}
              className="hover:text-zinc-200 normal-case tracking-normal"
            >
              none
            </button>
          </div>
          <ul className="space-y-0.5 max-h-72 overflow-auto scrollbar-thin pr-1">
            {families.map((f) => {
              const n = f.clusters.reduce((s, c) => s + c.papers.length, 0);
              const checked = !excludedFamilies.has(f.slug);
              return (
                <li key={f.slug} className="flex items-center gap-1.5">
                  <input
                    type="checkbox"
                    checked={checked}
                    onChange={() => onToggleFamily(f.slug)}
                    className="accent-cyan-500"
                    aria-label={`Toggle family ${f.name}`}
                  />
                  <span
                    className="inline-block w-2.5 h-2.5 rounded-full shrink-0"
                    style={{ background: hueFor(f.slug) }}
                  />
                  <button
                    onClick={() => onSelectFamily(f)}
                    disabled={!checked}
                    className={`flex-1 text-left truncate ${
                      checked ? "hover:text-zinc-100" : "text-zinc-600"
                    }`}
                    title={f.name}
                  >
                    {f.name}
                  </button>
                  <span className="ml-auto text-zinc-500 tabular-nums">{n}</span>
                </li>
              );
            })}
          </ul>
        </div>
      )}
    </div>
  );
}

// Mirror palette in CirclePack.jsx; kept simple here.
const FAMILY_PALETTE = {
  "agents": "#22d3ee",
  "reasoning-ttc": "#a78bfa",
  "rlhf-postraining": "#f472b6",
  "theory-generalization": "#94a3b8",
  "world-models": "#34d399",
  "hybrid-arch": "#f59e0b",
  "interp-mech": "#fb7185",
  "optimizers-training": "#facc15",
  "jepa-ssl": "#60a5fa",
  "diffusion": "#fb923c",
  "ssm-mamba": "#4ade80",
  "moe": "#f87171",
  "meta": "#71717a",
  "llm-pretrain": "#a3e635",
  "safety-alignment": "#fda4af",
  "continual-memory": "#67e8f9",
  "kv-attention-eff": "#c4b5fd",
  "quant-pruning-distill": "#fbbf24",
  "long-context": "#5eead4",
  "rag-retrieval": "#e879f9",
  "vlm": "#38bdf8",
  "robotics-vla": "#fcd34d",
  "speech-audio": "#bef264",
  "scaling-laws": "#fca5a5",
  "data-curation": "#fde047",
  "bio-genomics": "#86efac",
  "math-formal": "#93c5fd",
  "omni-multimodal": "#d8b4fe",
  "autoregressive-gen": "#fdba74",
  "rl-general": "#a7f3d0",
  "evaluation": "#e0e0e0",
};

function hueFor(slug) {
  if (FAMILY_PALETTE[slug]) return FAMILY_PALETTE[slug];
  let h = 0;
  for (let i = 0; i < slug.length; i++) h = (h * 31 + slug.charCodeAt(i)) | 0;
  return `hsl(${Math.abs(h) % 360} 65% 60%)`;
}
