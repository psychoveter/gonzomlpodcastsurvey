"""Paginating scraper for t.me/s/<channel> -> SQLite.

Usage:
    python -m gonzo.scrape --channel gonzo_ML --since 2019-02-21 --db data/gonzo.db
"""
from __future__ import annotations

import argparse
import sys
import time
from datetime import datetime, timezone

import requests

from . import db as dbmod
from .parse import parse_page, min_id

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/17.4 Safari/605.1.15"
)
DEFAULT_CHANNEL = "gonzo_ML_podcasts"


def fetch(channel: str, before: int | None, *, session: requests.Session,
          retries: int = 4) -> str:
    base = f"https://t.me/s/{channel}"
    url = base if before is None else f"{base}?before={before}"
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            resp = session.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
            if resp.status_code == 200:
                return resp.text
            last_err = RuntimeError(f"HTTP {resp.status_code} for {url}")
        except Exception as e:
            last_err = e
        time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"Failed to fetch {url}: {last_err}")


def iso_to_dt(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(timezone.utc)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--db", required=True)
    p.add_argument(
        "--channel", default=DEFAULT_CHANNEL,
        help=f"Telegram channel username (default: {DEFAULT_CHANNEL})",
    )
    p.add_argument(
        "--since",
        required=True,
        help="ISO date (UTC). Stop when the oldest message on a page is older.",
    )
    p.add_argument("--sleep", type=float, default=0.5,
                   help="seconds between page fetches")
    p.add_argument("--max-pages", type=int, default=2000)
    p.add_argument("--resume", action="store_true",
                   help="continue from the smallest id already in DB for this channel")
    args = p.parse_args(argv)

    since = iso_to_dt(args.since)
    conn = dbmod.connect(args.db)
    session = requests.Session()
    channel = args.channel

    before: int | None = None
    if args.resume:
        row = conn.execute(
            "SELECT MIN(id) AS m FROM messages WHERE channel = ?", (channel,)
        ).fetchone()
        if row and row["m"] is not None:
            before = int(row["m"])
            print(f"[resume] channel={channel}  starting before={before}",
                  file=sys.stderr)

    pages = 0
    total_new = 0
    seen_before: set[int] = set()
    while pages < args.max_pages:
        pages += 1
        html = fetch(channel, before, session=session)
        records = parse_page(html, channel=channel)
        if not records:
            print(f"[stop] empty page (channel={channel}, before={before})",
                  file=sys.stderr)
            break
        oldest = min(iso_to_dt(r["msg"]["posted_at"]) for r in records)
        newest = max(iso_to_dt(r["msg"]["posted_at"]) for r in records)
        new_in_page = 0
        with conn:
            for r in records:
                dbmod.insert_message(conn, channel, r["msg"])
                dbmod.insert_links(conn, channel, r["msg"]["id"], r["links"])
                new_in_page += 1
        total_new += new_in_page
        page_min = min_id(records)
        print(
            f"[{channel}] page {pages:>3}  before={before}  "
            f"ids {page_min}..{max(r['msg']['id'] for r in records)}  "
            f"{newest.date()}..{oldest.date()}  "
            f"new={new_in_page}  total={total_new}",
            file=sys.stderr,
        )
        if oldest < since:
            print(f"[stop] reached cutoff {since.date()} "
                  f"(oldest on page {oldest.date()})", file=sys.stderr)
            break
        if page_min is None:
            break
        if before is not None and page_min >= before:
            print(f"[stop] no progress: page_min {page_min} >= before {before}",
                  file=sys.stderr)
            break
        if page_min in seen_before:
            print(f"[stop] loop detected at before={page_min}", file=sys.stderr)
            break
        seen_before.add(page_min)
        before = page_min
        time.sleep(args.sleep)

    print(f"done. channel={channel}  pages={pages}  total_new={total_new}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
