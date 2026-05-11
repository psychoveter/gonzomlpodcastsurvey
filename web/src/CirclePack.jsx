import React, { useEffect, useMemo, useRef, useState } from "react";
import { hierarchy, pack } from "d3-hierarchy";
import { interpolateZoom } from "d3-interpolate";

// Brand colours per family slug. Anything not listed gets a hue derived from
// the slug hash, keeping siblings distinguishable while siblings of one family
// share a hue tone.
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

function hashHue(s) {
  let h = 0;
  for (let i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) | 0;
  return Math.abs(h) % 360;
}
function familyColor(slug) {
  if (FAMILY_PALETTE[slug]) return FAMILY_PALETTE[slug];
  return `hsl(${hashHue(slug)} 65% 60%)`;
}
function mix(c, target, t) {
  return `color-mix(in oklab, ${c}, ${target} ${Math.round(t * 100)}%)`;
}
function nodeColor(d) {
  if (d.depth === 0) return "transparent";
  const fam = d.ancestors().find((a) => a.depth === 1);
  const base = familyColor(fam ? fam.data.slug : d.data.slug);
  if (d.depth === 1) return mix(base, "#000", 0.55);
  if (d.depth === 2) return mix(base, "#000", 0.30);
  if (d.depth === 3) return base;
  return base;
}
function nodeStroke(d) {
  if (d.depth === 0) return "rgba(255,255,255,0.04)";
  const fam = d.ancestors().find((a) => a.depth === 1);
  const base = familyColor(fam ? fam.data.slug : d.data.slug);
  return base;
}

function buildRoot(data) {
  return {
    name: "All architectures",
    slug: "__root",
    type: "root",
    children: (data.families || []).map((f) => ({
      ...f,
      type: "family",
      children: (f.clusters || []).map((c) => ({
        ...c,
        type: "cluster",
        familySlug: f.slug,
        familyName: f.name,
        children: (c.papers || []).map((p) => ({
          ...p,
          type: "paper",
          name: p.title || `#${p.id}`,
          familySlug: f.slug,
          familyName: f.name,
          clusterSlug: c.slug,
          clusterName: c.name,
        })),
      })),
    })),
  };
}

function clamp(x, lo, hi) {
  return Math.max(lo, Math.min(hi, x));
}

export default function CirclePack({ data, onSelect, selectedId, search, jumpId }) {
  const svgRef = useRef(null);
  const [size, setSize] = useState({ w: 900, h: 900 });

  // Responsive resize
  useEffect(() => {
    const el = svgRef.current?.parentElement;
    if (!el) return;
    const ro = new ResizeObserver(([entry]) => {
      const { width, height } = entry.contentRect;
      const s = Math.min(width, height);
      setSize({ w: width, h: Math.max(s, 600) });
    });
    ro.observe(el);
    return () => ro.disconnect();
  }, []);

  // Build d3 hierarchy + pack
  const root = useMemo(() => {
    const tree = buildRoot(data);
    const hr = hierarchy(tree)
      .sum((d) => (d.type === "paper" ? 1 : 0))
      .sort((a, b) => b.value - a.value);
    pack()
      .size([size.w, size.h])
      .padding((d) => (d.depth === 0 ? 6 : d.depth === 1 ? 4 : 2))(hr);
    return hr;
  }, [data, size]);

  // ----- ids -----
  const idOf = (d) => {
    if (d.depth === 0) return "__root";
    if (d.data.type === "paper") return `paper:${d.data.id}`;
    if (d.data.type === "cluster") return `cluster:${d.parent?.data.slug}::${d.data.slug}`;
    if (d.data.type === "family") return `family:${d.data.slug}`;
    return "?";
  };

  // ----- focus state (click-driven) + animation -----
  const [focusId, setFocusId] = useState("__root");
  // bump on every click so re-clicking the same focus re-animates after wheel-zoom
  const focusGenRef = useRef(0);
  const [, forceRender] = useState(0);

  useEffect(() => {
    if (jumpId) {
      setFocusId(jumpId);
      focusGenRef.current += 1;
      forceRender((n) => n + 1);
    }
  }, [jumpId]);

  const focus = useMemo(
    () => root.descendants().find((d) => idOf(d) === focusId) || root,
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [root, focusId]
  );

  // ----- view: [x, y, viewRadius] ; viewRef is the always-current value -----
  const viewRef = useRef(null);
  const [view, setView] = useState(null);
  const rafRef = useRef(0);

  // Initialize view on first mount / root rebuild
  useEffect(() => {
    if (!viewRef.current) {
      const init = [root.x, root.y, root.r * 2 + 32];
      viewRef.current = init;
      setView(init);
    }
  }, [root]);

  // Animate to focus whenever focusId changes (re-running the effect via focusGen)
  useEffect(() => {
    if (!viewRef.current) return;
    const target = [focus.x, focus.y, focus.r * 2 + 32];
    const interp = interpolateZoom(viewRef.current, target);
    const duration = Math.min(1200, interp.duration);
    const t0 = performance.now();
    cancelAnimationFrame(rafRef.current);
    const step = (now) => {
      const t = Math.min(1, (now - t0) / duration);
      const v = interp(t);
      viewRef.current = v;
      setView(v);
      if (t < 1) rafRef.current = requestAnimationFrame(step);
    };
    rafRef.current = requestAnimationFrame(step);
    return () => cancelAnimationFrame(rafRef.current);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [focusId, focusGenRef.current]);

  // ----- wheel zoom + drag pan via native listeners -----
  const wheelHandlerRef = useRef(null);
  wheelHandlerRef.current = (e) => {
    e.preventDefault();
    const svg = svgRef.current;
    if (!svg || !viewRef.current) return;
    cancelAnimationFrame(rafRef.current);
    const rect = svg.getBoundingClientRect();
    // Map clientX/Y -> internal viewBox coordinates (viewBox is 0..size.w x 0..size.h)
    const cx = ((e.clientX - rect.left) / rect.width) * size.w;
    const cy = ((e.clientY - rect.top) / rect.height) * size.h;

    const [vx, vy, vr] = viewRef.current;
    const kCur = size.w / vr;
    const txCur = size.w / 2 - vx * kCur;
    const tyCur = size.h / 2 - vy * kCur;
    const dataX = (cx - txCur) / kCur;
    const dataY = (cy - tyCur) / kCur;

    // Wheel direction: ctrlKey/pinch-zoom is finer; trackpad two-finger
    // scroll on macOS sets deltaMode==0 with deltaY in px.
    const intensity = e.ctrlKey ? 0.0035 : 0.0015;
    const factor = Math.exp(e.deltaY * intensity);
    const minR = Math.max(20, root.r * 0.02);
    const maxR = root.r * 6;
    const newR = clamp(vr * factor, minR, maxR);
    const newK = size.w / newR;
    const newX = dataX - (cx - size.w / 2) / newK;
    const newY = dataY - (cy - size.h / 2) / newK;
    const newView = [newX, newY, newR];
    viewRef.current = newView;
    setView(newView);
  };

  const dragStateRef = useRef(null);
  const mouseDownRef = useRef(null);
  const draggedRef = useRef(false);
  const mouseDownHandlerRef = useRef(null);
  const mouseMoveHandlerRef = useRef(null);
  const mouseUpHandlerRef = useRef(null);

  mouseDownHandlerRef.current = (e) => {
    if (e.button !== 0) return;
    const svg = svgRef.current;
    if (!svg || !viewRef.current) return;
    const rect = svg.getBoundingClientRect();
    mouseDownRef.current = { x: e.clientX, y: e.clientY };
    dragStateRef.current = {
      startView: viewRef.current.slice(),
      startCx: e.clientX,
      startCy: e.clientY,
      rectW: rect.width,
      rectH: rect.height,
    };
    draggedRef.current = false;
  };
  mouseMoveHandlerRef.current = (e) => {
    const s = dragStateRef.current;
    if (!s) return;
    const dx = e.clientX - s.startCx;
    const dy = e.clientY - s.startCy;
    if (!draggedRef.current && Math.hypot(dx, dy) < 4) return;
    draggedRef.current = true;
    cancelAnimationFrame(rafRef.current);
    const [vx, vy, vr] = s.startView;
    const kCur = size.w / vr;
    // Convert pixel delta to data coords
    const ddx = -(dx / s.rectW) * size.w / kCur;
    const ddy = -(dy / s.rectH) * size.h / kCur;
    const newView = [vx + ddx, vy + ddy, vr];
    viewRef.current = newView;
    setView(newView);
  };
  mouseUpHandlerRef.current = () => {
    dragStateRef.current = null;
    mouseDownRef.current = null;
    // draggedRef cleared by click handler after one click cycle
    setTimeout(() => { draggedRef.current = false; }, 0);
  };

  useEffect(() => {
    const svg = svgRef.current;
    if (!svg) return;
    const wh = (e) => wheelHandlerRef.current && wheelHandlerRef.current(e);
    const md = (e) => mouseDownHandlerRef.current && mouseDownHandlerRef.current(e);
    const mm = (e) => mouseMoveHandlerRef.current && mouseMoveHandlerRef.current(e);
    const mu = (e) => mouseUpHandlerRef.current && mouseUpHandlerRef.current(e);
    svg.addEventListener("wheel", wh, { passive: false });
    svg.addEventListener("mousedown", md);
    window.addEventListener("mousemove", mm);
    window.addEventListener("mouseup", mu);
    return () => {
      svg.removeEventListener("wheel", wh);
      svg.removeEventListener("mousedown", md);
      window.removeEventListener("mousemove", mm);
      window.removeEventListener("mouseup", mu);
    };
  }, []);

  // ----- compute current transform -----
  const v = view || [root.x, root.y, root.r * 2 + 32];
  const k = size.w / v[2];
  const tx = size.w / 2 - v[0] * k;
  const ty = size.h / 2 - v[1] * k;

  // ----- search highlight -----
  const lowerSearch = (search || "").trim().toLowerCase();
  const matches = useMemo(() => {
    if (!lowerSearch) return null;
    const out = new Set();
    root.descendants().forEach((d) => {
      const t = d.data;
      const blob = [
        t.title,
        t.name,
        t.one_liner,
        t.subfamily_raw,
        t.distinguishing,
        t.familyName,
        t.clusterName,
        ...(t.key_concepts || []),
      ]
        .filter(Boolean)
        .join(" ")
        .toLowerCase();
      if (blob.includes(lowerSearch)) {
        out.add(idOf(d));
        d.ancestors().forEach((a) => out.add(idOf(a)));
      }
    });
    return out;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [lowerSearch, root]);

  const nodes = useMemo(
    () => root.descendants().filter((d) => d.depth <= 3),
    [root]
  );

  // ----- selection from clicks -----
  function handleNodeClick(d, e) {
    e.stopPropagation();
    if (draggedRef.current) return; // ignore clicks that ended a drag
    if (d.depth === 0) {
      setFocusId("__root");
      focusGenRef.current += 1;
      forceRender((n) => n + 1);
      onSelect && onSelect(null);
      return;
    }
    if (d.data.type === "paper") {
      onSelect &&
        onSelect({
          kind: "paper",
          id: idOf(d),
          data: d.data,
          family: d.parent?.parent?.data,
          cluster: d.parent?.data,
        });
    } else if (d.data.type === "cluster") {
      setFocusId(idOf(d));
      focusGenRef.current += 1;
      forceRender((n) => n + 1);
      onSelect &&
        onSelect({
          kind: "cluster",
          id: idOf(d),
          data: d.data,
          family: d.parent?.data,
        });
    } else if (d.data.type === "family") {
      setFocusId(idOf(d));
      focusGenRef.current += 1;
      forceRender((n) => n + 1);
      onSelect && onSelect({ kind: "family", id: idOf(d), data: d.data });
    }
  }

  function handleBgClick() {
    if (draggedRef.current) return;
    setFocusId("__root");
    focusGenRef.current += 1;
    forceRender((n) => n + 1);
    onSelect && onSelect(null);
  }

  // ----- label placement helpers -----
  function approxWidth(text, fontSize) {
    return text.length * fontSize * 0.55;
  }

  function wrapText(text, maxCharsPerLine, maxLines) {
    if (!text) return [];
    const words = text.split(/\s+/).filter(Boolean);
    const lines = [];
    let cur = "";
    for (let i = 0; i < words.length; i++) {
      const w = words[i];
      const trial = cur ? cur + " " + w : w;
      // also break if a single word is too long: split it
      if (trial.length <= maxCharsPerLine) {
        cur = trial;
      } else {
        if (cur) lines.push(cur);
        cur = w;
        if (lines.length === maxLines - 1) {
          // last line: cram remaining text, truncate with ellipsis
          const rest = words.slice(i).join(" ");
          lines.push(
            rest.length > maxCharsPerLine
              ? rest.slice(0, Math.max(1, maxCharsPerLine - 1)) + "…"
              : rest
          );
          return lines;
        }
      }
      if (lines.length >= maxLines) return lines;
    }
    if (cur && lines.length < maxLines) lines.push(cur);
    return lines;
  }

  function labelFor(d) {
    const id = idOf(d);
    const dim = matches && !matches.has(id);
    const rPx = d.r * k;
    if (d.depth === 1) {
      // Family label: top edge of family circle.
      if (rPx < 36) return null;
      const fontSize = Math.min(d.r * 0.16, 16 / k);
      const text = truncate(d.data.name, 36);
      return {
        d,
        id,
        x: d.x,
        y: d.y - d.r + fontSize * 1.1,
        text,
        fontSize,
        weight: 600,
        opacity: dim ? 0.25 : 1,
        width: approxWidth(text, fontSize),
        height: fontSize,
        type: "family",
        priority: 3,
      };
    }
    if (d.depth === 2) {
      // Cluster label: by default centered on the cluster. Once we're zoomed in
      // enough that the cluster fills most of the panel, the label moves to the
      // top inside edge to avoid covering the inner paper bubbles.
      if (rPx < 22) return null;
      const fontSize = clamp(d.r * 0.22, 10 / k, 15 / k);
      const text = truncate(d.data.name, 30);
      const zoomedIn = rPx > 220;
      const y = zoomedIn ? d.y - d.r + fontSize * 1.1 : d.y;
      return {
        d,
        id,
        x: d.x,
        y,
        text,
        fontSize,
        weight: 600,
        opacity: dim ? 0.25 : 1,
        width: approxWidth(text, fontSize),
        height: fontSize,
        type: "cluster",
        zoomedIn,
        priority: 2,
      };
    }
    if (d.depth === 3) {
      // Paper label: only when zoomed in enough that a paper bubble has decent
      // screen size. Wrap the title across multiple lines.
      if (rPx < 28) return null;
      const fontSize = clamp(d.r * 0.18, 9 / k, 11 / k);
      // available width inside the circle (with a margin)
      const innerW = 2 * d.r * 0.82;
      const innerH = 2 * d.r * 0.82;
      const maxCharsPerLine = Math.max(6, Math.floor(innerW / (fontSize * 0.55)));
      const maxLines = clamp(Math.floor(innerH / (fontSize * 1.15)), 1, 4);
      const title = d.data.title || d.data.name || "";
      const lines = wrapText(title, maxCharsPerLine, maxLines);
      if (!lines.length) return null;
      const w = Math.max(...lines.map((l) => approxWidth(l, fontSize)));
      return {
        d,
        id,
        x: d.x,
        y: d.y,
        lines,
        fontSize,
        weight: 500,
        opacity: dim ? 0.25 : 1,
        width: w,
        height: fontSize * 1.15 * lines.length,
        type: "paper",
        priority: 1,
      };
    }
    return null;
  }

  // Build visible labels.
  const labels = useMemo(() => {
    const out = [];
    for (const d of nodes) {
      const lbl = labelFor(d);
      if (lbl) out.push(lbl);
    }
    // Original y, used to cap drift after collision resolution.
    out.forEach((l) => {
      l.origY = l.y;
    });
    // ----- collision avoidance: nudge overlapping labels apart on y axis -----
    // We iterate a few passes. Higher-priority labels (family > cluster > paper)
    // resist movement more.
    const padding = 1.5 / k;
    for (let iter = 0; iter < 8; iter++) {
      let moved = false;
      for (let i = 0; i < out.length; i++) {
        for (let j = i + 1; j < out.length; j++) {
          const a = out[i];
          const b = out[j];
          const dx = Math.abs(a.x - b.x);
          const dy = Math.abs(a.y - b.y);
          const minX = a.width / 2 + b.width / 2 + padding;
          const minY = a.height / 2 + b.height / 2 + padding;
          if (dx < minX && dy < minY) {
            const overlap = minY - dy;
            const dir = a.y <= b.y ? -1 : 1;
            // Distribute the push inversely to priority — higher-priority
            // labels move less.
            const aw = 1 / a.priority;
            const bw = 1 / b.priority;
            const total = aw + bw;
            a.y += (dir * overlap * aw) / total;
            b.y -= (dir * overlap * bw) / total;
            moved = true;
          }
        }
      }
      if (!moved) break;
    }
    // Cap drift to keep labels near their owner node.
    out.forEach((l) => {
      const maxDrift = (l.type === "paper" ? 0.25 : l.type === "cluster" ? 0.55 : 0.4) * l.d.r;
      const drift = l.y - l.origY;
      if (Math.abs(drift) > maxDrift) {
        l.y = l.origY + Math.sign(drift) * maxDrift;
      }
    });
    return out;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [nodes, k, matches]);

  return (
    <svg
      ref={svgRef}
      viewBox={`0 0 ${size.w} ${size.h}`}
      width="100%"
      height="100%"
      style={{
        display: "block",
        cursor: dragStateRef.current ? "grabbing" : "grab",
        maxHeight: "100vh",
        userSelect: "none",
      }}
      onClick={handleBgClick}
    >
      <g transform={`translate(${tx},${ty}) scale(${k})`}>
        {/* Pass 1: all circles with click handlers */}
        {nodes.map((d) => {
          const id = idOf(d);
          const isSelected = selectedId === id;
          const dim = matches && !matches.has(id);
          const fill = nodeColor(d);
          const stroke = nodeStroke(d);
          const opacity = dim
            ? 0.1
            : d.depth === 0
            ? 0.0
            : d.depth === 1
            ? 0.35
            : d.depth === 2
            ? 0.55
            : 0.95;
          const strokeOpacity = dim
            ? 0.25
            : isSelected
            ? 1
            : d.depth === 1
            ? 0.85
            : 0.6;
          const strokeWidth = isSelected ? 4 : d.depth === 1 ? 1.2 : 0.8;
          return (
            <g
              key={`c:${id}`}
              transform={`translate(${d.x},${d.y})`}
              onClick={(e) => handleNodeClick(d, e)}
              style={{ cursor: "pointer" }}
            >
              <circle
                r={d.r}
                fill={fill}
                fillOpacity={opacity}
                stroke={stroke}
                strokeOpacity={strokeOpacity}
                strokeWidth={strokeWidth / k}
              />
              <title>
                {d.depth === 1
                  ? `${d.data.name} — ${d.value} papers`
                  : d.depth === 2
                  ? `${d.data.familyName} / ${d.data.name} — ${d.value} papers`
                  : d.depth === 3
                  ? `${d.data.familyName} / ${d.data.clusterName}\n${
                      d.data.title || ""
                    }\n${d.data.one_liner || ""}`
                  : "All architectures"}
              </title>
            </g>
          );
        })}

        {/* Pass 2: labels above all circles. No backgrounds — just white text
            with a thin black stroke for legibility, plus collision-resolved y. */}
        {labels.map((lbl) => {
          const stroke = lbl.type === "family" ? 0.9 / k : 0.6 / k;
          if (lbl.lines) {
            // multi-line (papers)
            const n = lbl.lines.length;
            return (
              <text
                key={`l:${lbl.id}`}
                x={lbl.x}
                y={lbl.y}
                textAnchor="middle"
                style={{
                  pointerEvents: "none",
                  opacity: lbl.opacity,
                  fontSize: lbl.fontSize,
                  fontWeight: lbl.weight,
                  fill: "#fafafa",
                  paintOrder: "stroke",
                  stroke: "rgba(0,0,0,0.85)",
                  strokeWidth: stroke,
                }}
              >
                {lbl.lines.map((line, i) => (
                  <tspan
                    key={i}
                    x={lbl.x}
                    dy={
                      i === 0
                        ? -((n - 1) * lbl.fontSize * 1.15) / 2 + lbl.fontSize * 0.35
                        : lbl.fontSize * 1.15
                    }
                  >
                    {line}
                  </tspan>
                ))}
              </text>
            );
          }
          return (
            <text
              key={`l:${lbl.id}`}
              x={lbl.x}
              y={lbl.y}
              textAnchor="middle"
              dy="0.35em"
              style={{
                pointerEvents: "none",
                opacity: lbl.opacity,
                fontSize: lbl.fontSize,
                fontWeight: lbl.weight,
                fill: "#fafafa",
                paintOrder: "stroke",
                stroke: "rgba(0,0,0,0.85)",
                strokeWidth: stroke,
              }}
            >
              {lbl.text}
            </text>
          );
        })}
      </g>
    </svg>
  );
}

function truncate(s, n) {
  if (!s) return "";
  return s.length > n ? s.slice(0, n - 1) + "…" : s;
}
