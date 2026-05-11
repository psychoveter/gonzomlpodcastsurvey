"""SQLite schema and helpers for the gonzo channel scrape."""
from __future__ import annotations

import sqlite3
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS messages (
    id              INTEGER PRIMARY KEY,         -- Telegram message id
    posted_at       TEXT    NOT NULL,            -- ISO8601 UTC
    views           TEXT,                        -- raw views label (e.g. "2.3K")
    html            TEXT,                        -- inner HTML of the body
    text            TEXT,                        -- plain-text body
    has_photo       INTEGER NOT NULL DEFAULT 0,
    has_video       INTEGER NOT NULL DEFAULT 0,
    has_document    INTEGER NOT NULL DEFAULT 0,
    has_link_preview INTEGER NOT NULL DEFAULT 0,
    reply_to_id     INTEGER,                     -- when message replies to another
    forwarded_from  TEXT,
    fetched_at      TEXT NOT NULL                -- ISO8601 UTC when we scraped
);

CREATE TABLE IF NOT EXISTS links (
    msg_id          INTEGER NOT NULL,
    url             TEXT    NOT NULL,
    domain          TEXT    NOT NULL,
    label           TEXT,                        -- text of <a> tag if any
    PRIMARY KEY (msg_id, url),
    FOREIGN KEY (msg_id) REFERENCES messages(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS threads (
    id              INTEGER PRIMARY KEY,         -- id of the leading message
    first_msg_id    INTEGER NOT NULL,
    last_msg_id     INTEGER NOT NULL,
    posted_at       TEXT    NOT NULL,            -- of the leading message
    text            TEXT    NOT NULL,            -- concatenated plain text
    arxiv_url       TEXT,
    github_url      TEXT,
    review_url      TEXT,                        -- substack/arxiviq
    title           TEXT,
    authors         TEXT,
    keywords        TEXT,                        -- comma-separated
    arch_family     TEXT,                        -- top-level family from taxonomy
    arch_tags       TEXT,                        -- comma-separated finer-grained tags
    summary         TEXT
);

CREATE INDEX IF NOT EXISTS idx_messages_posted_at ON messages(posted_at);
CREATE INDEX IF NOT EXISTS idx_links_domain ON links(domain);
CREATE INDEX IF NOT EXISTS idx_threads_posted_at ON threads(posted_at);
"""


def connect(db_path: str | Path) -> sqlite3.Connection:
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn


def insert_message(conn: sqlite3.Connection, msg: dict) -> None:
    conn.execute(
        """
        INSERT OR REPLACE INTO messages
          (id, posted_at, views, html, text, has_photo, has_video,
           has_document, has_link_preview, reply_to_id, forwarded_from, fetched_at)
        VALUES (:id, :posted_at, :views, :html, :text, :has_photo, :has_video,
                :has_document, :has_link_preview, :reply_to_id, :forwarded_from, :fetched_at)
        """,
        msg,
    )


def insert_links(conn: sqlite3.Connection, msg_id: int, links: list[dict]) -> None:
    if not links:
        return
    conn.executemany(
        "INSERT OR IGNORE INTO links (msg_id, url, domain, label) VALUES (?,?,?,?)",
        [(msg_id, l["url"], l["domain"], l.get("label")) for l in links],
    )


def upsert_thread(conn: sqlite3.Connection, thread: dict) -> None:
    cols = (
        "id, first_msg_id, last_msg_id, posted_at, text, arxiv_url, github_url, "
        "review_url, title, authors, keywords, arch_family, arch_tags, summary"
    )
    placeholders = ":id, :first_msg_id, :last_msg_id, :posted_at, :text, :arxiv_url, "\
                   ":github_url, :review_url, :title, :authors, :keywords, "\
                   ":arch_family, :arch_tags, :summary"
    conn.execute(
        f"INSERT OR REPLACE INTO threads ({cols}) VALUES ({placeholders})",
        thread,
    )
