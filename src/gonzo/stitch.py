"""Group consecutive Telegram messages into logical threads.

A thread is a maximal run of messages whose pairwise time gap is <= cutoff
(default: 300s). The thread id is the id of the leading (smallest-id) message.
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime

from . import db as dbmod


def iso_to_dt(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def build_threads(conn, cutoff_s: int = 300) -> int:
    rows = conn.execute(
        "SELECT id, posted_at, text, has_photo, has_video, has_document "
        "FROM messages ORDER BY id"
    ).fetchall()
    if not rows:
        return 0

    threads: list[list[dict]] = [[]]
    prev_dt: datetime | None = None
    for r in rows:
        dt = iso_to_dt(r["posted_at"])
        if prev_dt is not None and (dt - prev_dt).total_seconds() > cutoff_s:
            threads.append([])
        threads[-1].append(dict(r))
        prev_dt = dt
    threads = [t for t in threads if t]

    # Wipe and rebuild threads table
    conn.execute("DELETE FROM threads")
    n = 0
    for th in threads:
        first = th[0]
        last = th[-1]
        text = "\n\n".join(m["text"] for m in th if m["text"]).strip()
        if not text:
            # Threads with only photos (no body) are not useful for classification
            continue
        n += 1
        conn.execute(
            "INSERT OR REPLACE INTO threads "
            "(id, first_msg_id, last_msg_id, posted_at, text) "
            "VALUES (?, ?, ?, ?, ?)",
            (first["id"], first["id"], last["id"], first["posted_at"], text),
        )
    conn.commit()
    return n


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--db", required=True)
    p.add_argument("--cutoff", type=int, default=300, help="seconds")
    args = p.parse_args(argv)
    conn = dbmod.connect(args.db)
    n = build_threads(conn, cutoff_s=args.cutoff)
    print(f"built {n} threads with cutoff {args.cutoff}s", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
