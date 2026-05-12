"""Group consecutive Telegram messages into logical threads.

A thread is a maximal run of messages (within a single channel) whose pairwise
time gap is <= cutoff (default: 300s). The thread key is
``(channel, first_msg_id)``.
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime

from . import db as dbmod


def iso_to_dt(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def build_threads(conn, cutoff_s: int = 300, *,
                  channels: list[str] | None = None) -> int:
    """Rebuild the ``threads`` table from ``messages``.

    By default rebuilds across all channels present in the DB. When
    ``channels`` is given, only those channels are rebuilt (threads from
    other channels are preserved).
    """
    if channels is None:
        channels = [r[0] for r in conn.execute(
            "SELECT DISTINCT channel FROM messages ORDER BY channel"
        ).fetchall()]

    total = 0
    for channel in channels:
        rows = conn.execute(
            "SELECT id, posted_at, text, has_photo, has_video, has_document "
            "FROM messages WHERE channel = ? ORDER BY id",
            (channel,),
        ).fetchall()
        if not rows:
            continue

        groups: list[list[dict]] = [[]]
        prev_dt: datetime | None = None
        for r in rows:
            dt = iso_to_dt(r["posted_at"])
            if prev_dt is not None and (dt - prev_dt).total_seconds() > cutoff_s:
                groups.append([])
            groups[-1].append(dict(r))
            prev_dt = dt
        groups = [g for g in groups if g]

        # Wipe only this channel's threads; keep enrichment for other channels.
        conn.execute("DELETE FROM threads WHERE channel = ?", (channel,))

        for th in groups:
            first = th[0]
            last = th[-1]
            text = "\n\n".join(m["text"] for m in th if m["text"]).strip()
            if not text:
                # Photos-only threads can't be classified.
                continue
            total += 1
            conn.execute(
                "INSERT OR REPLACE INTO threads "
                "(channel, first_msg_id, last_msg_id, posted_at, text) "
                "VALUES (?, ?, ?, ?, ?)",
                (channel, first["id"], last["id"], first["posted_at"], text),
            )
        conn.commit()
        print(f"[stitch] {channel}: {sum(1 for g in groups)} candidate runs "
              f"-> threads with text", file=sys.stderr)

    return total


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--db", required=True)
    p.add_argument("--cutoff", type=int, default=300, help="seconds")
    p.add_argument(
        "--channel", action="append", default=None,
        help="Limit rebuild to one channel (repeatable). Default: all channels.",
    )
    args = p.parse_args(argv)
    conn = dbmod.connect(args.db)
    n = build_threads(conn, cutoff_s=args.cutoff, channels=args.channel)
    print(f"built {n} threads total with cutoff {args.cutoff}s", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
