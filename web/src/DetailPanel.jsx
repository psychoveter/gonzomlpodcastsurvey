import React from "react";

function channelLabel(channel) {
  // Short label for compact links.
  return channel === "gonzo_ML_podcasts" ? "podcast" : channel;
}

function SourceLinks({ sources, className = "" }) {
  if (!sources || sources.length === 0) return null;
  return (
    <span className={`inline-flex flex-wrap gap-x-2 gap-y-1 ${className}`}>
      {sources.map((s) => (
        <a
          key={`${s.channel}#${s.msg_id}`}
          href={s.url}
          target="_blank"
          rel="noreferrer"
          title={`@${s.channel} · ${(s.posted_at || "").slice(0, 10)}`}
          className="text-zinc-400 hover:text-cyan-300 hover:underline"
        >
          tg:{channelLabel(s.channel)}
        </a>
      ))}
    </span>
  );
}

function PaperCard({ p }) {
  const sources = p.sources || [];
  const primaryUrl = sources[0]?.url || p.url;
  return (
    <div className="rounded-lg border border-zinc-800 bg-zinc-900/60 p-3 hover:bg-zinc-900 transition-colors">
      <div className="flex items-baseline gap-2 flex-wrap text-xs text-zinc-400">
        <span>{(p.posted_at || "").slice(0, 10)}</span>
        {sources.length > 1 ? (
          <span
            className="rounded bg-amber-900/40 border border-amber-700/40 text-amber-200 px-1.5 py-0.5 text-[10px] uppercase tracking-wider"
            title="Discussed in both channels"
          >
            cross-channel
          </span>
        ) : null}
        {p.training_phase ? (
          <span className="rounded bg-zinc-800 px-1.5 py-0.5 text-[10px] uppercase tracking-wider">
            {p.training_phase}
          </span>
        ) : null}
        {(p.modalities || []).map((m) => (
          <span
            key={m}
            className="rounded bg-zinc-800 px-1.5 py-0.5 text-[10px] uppercase tracking-wider text-zinc-300"
          >
            {m}
          </span>
        ))}
      </div>
      <a
        href={primaryUrl}
        target="_blank"
        rel="noreferrer"
        className="block mt-1 font-medium text-zinc-100 hover:text-cyan-300 leading-snug"
      >
        {p.title || `#${p.id}`}
      </a>
      {p.one_liner ? (
        <div className="mt-1 text-sm text-zinc-300 leading-snug">{p.one_liner}</div>
      ) : null}
      <div className="mt-2 flex flex-wrap gap-x-3 gap-y-1 text-xs">
        {p.arxiv_url ? (
          <a href={p.arxiv_url} target="_blank" rel="noreferrer" className="text-amber-300 hover:underline">
            arXiv
          </a>
        ) : null}
        {p.github_url ? (
          <a href={p.github_url} target="_blank" rel="noreferrer" className="text-emerald-300 hover:underline">
            code
          </a>
        ) : null}
        {p.review_url ? (
          <a href={p.review_url} target="_blank" rel="noreferrer" className="text-violet-300 hover:underline">
            review
          </a>
        ) : null}
        <SourceLinks sources={sources} />
      </div>
      {p.key_concepts && p.key_concepts.length > 0 ? (
        <div className="mt-2 flex flex-wrap gap-1">
          {p.key_concepts.slice(0, 8).map((k) => (
            <span
              key={k}
              className="rounded-full bg-zinc-800 px-2 py-0.5 text-[11px] text-zinc-300"
            >
              {k}
            </span>
          ))}
        </div>
      ) : null}
    </div>
  );
}

export default function DetailPanel({ selection, onJumpTo }) {
  if (!selection) {
    return (
      <div className="text-zinc-400 text-sm leading-relaxed">
        <h2 className="text-zinc-100 text-base font-semibold">How to read this map</h2>
        <ul className="mt-2 list-disc pl-5 space-y-1">
          <li>Each big bubble is an <span className="text-zinc-200">architecture family</span>.</li>
          <li>Inside it are <span className="text-zinc-200">sub-clusters</span> proposed by gpt-5 from the actual paper bodies.</li>
          <li>Inner dots are <span className="text-zinc-200">individual papers</span>; click one to open its summary and links.</li>
          <li>Click a family or cluster to zoom in. Click the background to zoom out.</li>
          <li>Use the search field to highlight matching papers/clusters.</li>
          <li>Papers tagged <span className="text-amber-200">cross-channel</span> are discussed in both channels (teaser on <span className="text-zinc-200">@gonzo_ML</span> + extended review on <span className="text-zinc-200">@gonzo_ML_podcasts</span>) and are merged into a single bubble.</li>
        </ul>
        <p className="mt-3 text-xs text-zinc-500">
          Areas are proportional to paper count. Hover any node for a tooltip.
        </p>
      </div>
    );
  }

  if (selection.kind === "paper") {
    const p = selection.data;
    const sources = p.sources || [];
    const primaryUrl = sources[0]?.url || p.url;
    return (
      <div>
        <div className="text-xs uppercase tracking-wider text-zinc-500">
          <button
            onClick={() => onJumpTo({ kind: "family", data: selection.family })}
            className="hover:text-zinc-200"
          >
            {selection.family?.name}
          </button>
          <span className="mx-1 text-zinc-700">/</span>
          <button
            onClick={() => onJumpTo({ kind: "cluster", data: selection.cluster, family: selection.family })}
            className="hover:text-zinc-200"
          >
            {selection.cluster?.name}
          </button>
        </div>
        <h2 className="mt-1 text-lg font-semibold text-zinc-100 leading-snug">
          <a href={primaryUrl} target="_blank" rel="noreferrer" className="hover:text-cyan-300">
            {p.title || `#${p.id}`}
          </a>
        </h2>
        {p.one_liner ? (
          <p className="mt-2 text-sm text-zinc-300 leading-relaxed">{p.one_liner}</p>
        ) : null}
        <div className="mt-3 flex flex-wrap gap-x-3 gap-y-1 text-sm">
          {p.arxiv_url ? (
            <a href={p.arxiv_url} target="_blank" rel="noreferrer" className="text-amber-300 hover:underline">
              arXiv
            </a>
          ) : null}
          {p.github_url ? (
            <a href={p.github_url} target="_blank" rel="noreferrer" className="text-emerald-300 hover:underline">
              code
            </a>
          ) : null}
          {p.review_url ? (
            <a href={p.review_url} target="_blank" rel="noreferrer" className="text-violet-300 hover:underline">
              long-form review
            </a>
          ) : null}
        </div>
        {sources.length > 0 ? (
          <div className="mt-3">
            <div className="text-[10px] uppercase tracking-wider text-zinc-500 mb-1">
              telegram source{sources.length > 1 ? "s" : ""}
              {sources.length > 1 ? (
                <span className="ml-2 normal-case tracking-normal text-amber-200">
                  (cross-channel: teaser + extended review)
                </span>
              ) : null}
            </div>
            <ul className="space-y-0.5 text-sm">
              {sources.map((s) => (
                <li key={`${s.channel}#${s.msg_id}`}>
                  <a
                    href={s.url}
                    target="_blank"
                    rel="noreferrer"
                    className="text-cyan-300 hover:underline"
                  >
                    @{s.channel}
                  </a>
                  <span className="text-zinc-500 ml-2 text-xs">
                    {(s.posted_at || "").slice(0, 10)}
                    {" · #"}{s.msg_id}
                  </span>
                </li>
              ))}
            </ul>
          </div>
        ) : null}
        <div className="mt-3 flex flex-wrap gap-1">
          {p.training_phase ? (
            <span className="rounded bg-zinc-800 px-2 py-0.5 text-xs text-zinc-300 uppercase tracking-wider">
              {p.training_phase}
            </span>
          ) : null}
          {(p.modalities || []).map((m) => (
            <span
              key={m}
              className="rounded bg-zinc-800 px-2 py-0.5 text-xs text-zinc-300 uppercase tracking-wider"
            >
              {m}
            </span>
          ))}
        </div>
        {p.key_concepts && p.key_concepts.length > 0 ? (
          <div className="mt-3 flex flex-wrap gap-1.5">
            {p.key_concepts.map((k) => (
              <span
                key={k}
                className="rounded-full bg-zinc-800/80 px-2.5 py-0.5 text-xs text-zinc-200"
              >
                {k}
              </span>
            ))}
          </div>
        ) : null}
        {p.summary ? (
          <div className="mt-4 text-sm text-zinc-300 leading-relaxed whitespace-pre-line">
            <div className="text-[10px] uppercase tracking-wider text-zinc-500 mb-1">
              channel summary
            </div>
            {p.summary}
          </div>
        ) : null}
      </div>
    );
  }

  if (selection.kind === "cluster") {
    const c = selection.data;
    return (
      <div>
        <div className="text-xs uppercase tracking-wider text-zinc-500">
          <button
            onClick={() => onJumpTo({ kind: "family", data: selection.family })}
            className="hover:text-zinc-200"
          >
            {selection.family?.name}
          </button>
          <span className="mx-1 text-zinc-700">/</span>
          <span>sub-cluster</span>
        </div>
        <h2 className="mt-1 text-lg font-semibold text-zinc-100">{c.name}</h2>
        <p className="mt-2 text-sm text-zinc-300 leading-relaxed">{c.distinguishing}</p>
        <div className="mt-4 text-[10px] uppercase tracking-wider text-zinc-500">
          {c.papers.length} paper{c.papers.length === 1 ? "" : "s"}
        </div>
        <div className="mt-2 space-y-2 scrollbar-thin">
          {c.papers
            .slice()
            .sort((a, b) => (b.posted_at || "").localeCompare(a.posted_at || ""))
            .map((p) => (
              <PaperCard key={p.id} p={p} />
            ))}
        </div>
      </div>
    );
  }

  if (selection.kind === "family") {
    const f = selection.data;
    return (
      <div>
        <div className="text-xs uppercase tracking-wider text-zinc-500">family</div>
        <h2 className="mt-1 text-lg font-semibold text-zinc-100">{f.name}</h2>
        <p className="mt-2 text-sm text-zinc-300 leading-relaxed">{f.distinguishing || f.curated_description}</p>
        <div className="mt-4 text-[10px] uppercase tracking-wider text-zinc-500">
          {f.clusters.length} sub-cluster{f.clusters.length === 1 ? "" : "s"} ·{" "}
          {f.clusters.reduce((s, c) => s + c.papers.length, 0)} papers
        </div>
        <div className="mt-2 space-y-2">
          {f.clusters
            .slice()
            .sort((a, b) => b.papers.length - a.papers.length)
            .map((c) => (
              <button
                key={c.slug}
                onClick={() => onJumpTo({ kind: "cluster", data: c, family: f })}
                className="block w-full text-left rounded-lg border border-zinc-800 bg-zinc-900/60 px-3 py-2 hover:bg-zinc-900 transition-colors"
              >
                <div className="flex items-baseline gap-2">
                  <span className="font-medium text-zinc-100">{c.name}</span>
                  <span className="text-xs text-zinc-500">{c.papers.length}</span>
                </div>
                <div className="mt-1 text-xs text-zinc-400 line-clamp-3">{c.distinguishing}</div>
              </button>
            ))}
        </div>
      </div>
    );
  }

  return null;
}
