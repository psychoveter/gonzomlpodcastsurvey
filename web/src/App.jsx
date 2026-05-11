import React, { useEffect, useMemo, useState } from "react";
import CirclePack from "./CirclePack.jsx";
import DetailPanel from "./DetailPanel.jsx";

export default function App() {
  const [data, setData] = useState(null);
  const [err, setErr] = useState(null);
  const [selection, setSelection] = useState(null);
  const [search, setSearch] = useState("");
  const [jumpId, setJumpId] = useState(null);

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

  const selectedId = selection?.id || null;

  function jumpTo(sel) {
    // Translate a "jumpTo" request from the side panel into a (selection, focus)
    // pair the CirclePack understands.
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

  return (
    <div className="h-screen w-screen flex flex-col bg-zinc-950 text-zinc-200 overflow-hidden">
      <header className="px-4 py-3 border-b border-zinc-900 flex items-baseline gap-4 flex-wrap shrink-0">
        <h1 className="text-zinc-100 text-lg sm:text-xl font-semibold">
          <a
            href={data.channel_url || "https://t.me/gonzo_ML_podcasts"}
            target="_blank"
            rel="noreferrer"
            className="hover:text-cyan-300"
          >
            @{data.channel}
          </a>
          <span className="text-zinc-500"> · architectures map</span>
        </h1>
        <div className="text-xs sm:text-sm text-zinc-500">
          {stats.threads_total} papers in {stats.clusters_total} clusters across{" "}
          {stats.families_total} families ·{" "}
          {(stats.oldest_post || "").slice(0, 10)} —{" "}
          {(stats.newest_post || "").slice(0, 10)} · clustered by{" "}
          <span className="text-zinc-300">{data.generated_with || "LLM"}</span>
        </div>
        <div className="ml-auto flex items-center gap-2">
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
            data={data}
            onSelect={setSelection}
            selectedId={selectedId}
            search={search}
            jumpId={jumpId}
          />
          <div className="pointer-events-none absolute top-2 left-3 text-[11px] text-zinc-500 bg-zinc-950/60 backdrop-blur-sm rounded px-2 py-1 border border-zinc-900">
            scroll = zoom · drag = pan · click bubble = drill in · click background = reset
          </div>
          <Legend families={data.families} onSelect={(f) => jumpTo({ kind: "family", data: f })} />
        </div>
        <aside className="border-t lg:border-t-0 lg:border-l border-zinc-900 bg-zinc-950 p-4 overflow-auto scrollbar-thin">
          <DetailPanel selection={selection} onJumpTo={jumpTo} />
        </aside>
      </main>

      <footer className="px-4 py-2 border-t border-zinc-900 text-xs text-zinc-500 shrink-0">
        {stats.messages_total} raw Telegram messages → {stats.threads_total} logical
        posts ·{" "}
        <a
          className="hover:text-zinc-300"
          href="https://t.me/gonzo_ML_podcasts"
          target="_blank"
          rel="noreferrer"
        >
          source channel
        </a>{" "}
        · classification via OpenAI {data.generated_with} (cached on disk).
      </footer>
    </div>
  );
}

function Legend({ families, onSelect }) {
  const [open, setOpen] = useState(true);
  if (!families) return null;
  const top = families.slice(0, 12);
  return (
    <div className="absolute left-3 bottom-3 max-w-[260px] bg-zinc-900/80 backdrop-blur rounded-md border border-zinc-800 text-xs text-zinc-300 shadow-lg">
      <button
        onClick={() => setOpen(!open)}
        className="w-full px-2 py-1 text-left text-zinc-400 hover:text-zinc-200"
      >
        {open ? "▾" : "▸"} top families
      </button>
      {open && (
        <ul className="px-2 pb-2 space-y-1 max-h-72 overflow-auto scrollbar-thin">
          {top.map((f) => {
            const n = f.clusters.reduce((s, c) => s + c.papers.length, 0);
            return (
              <li key={f.slug}>
                <button
                  onClick={() => onSelect(f)}
                  className="w-full text-left flex items-center gap-2 hover:text-zinc-100"
                >
                  <span
                    className="inline-block w-2.5 h-2.5 rounded-full shrink-0"
                    style={{ background: hueFor(f.slug) }}
                  />
                  <span className="truncate">{f.name}</span>
                  <span className="ml-auto text-zinc-500">{n}</span>
                </button>
              </li>
            );
          })}
        </ul>
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
