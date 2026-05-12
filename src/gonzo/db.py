"""SQLite schema and helpers for the gonzo channel scrape.

Multi-channel ready: each message / thread carries a `channel` column and the
natural keys are composite `(channel, id)` / `(channel, first_msg_id)`. A
separate `papers` table groups threads across channels that talk about the
same paper (detected by canonical arXiv id or title fuzz).

A small `PRAGMA user_version`-based migration upgrades existing single-channel
DBs (everything is assumed to be `gonzo_ML_podcasts`) in-place.
"""
from __future__ import annotations

import sqlite3
from pathlib import Path

SCHEMA_VERSION = 2

SCHEMA = """
CREATE TABLE IF NOT EXISTS messages (
    channel         TEXT    NOT NULL,
    id              INTEGER NOT NULL,           -- telegram message id (per channel)
    posted_at       TEXT    NOT NULL,
    views           TEXT,
    html            TEXT,
    text            TEXT,
    has_photo       INTEGER NOT NULL DEFAULT 0,
    has_video       INTEGER NOT NULL DEFAULT 0,
    has_document    INTEGER NOT NULL DEFAULT 0,
    has_link_preview INTEGER NOT NULL DEFAULT 0,
    reply_to_id     INTEGER,
    forwarded_from  TEXT,
    fetched_at      TEXT    NOT NULL,
    PRIMARY KEY (channel, id)
);

CREATE TABLE IF NOT EXISTS links (
    msg_channel     TEXT    NOT NULL,
    msg_id          INTEGER NOT NULL,
    url             TEXT    NOT NULL,
    domain          TEXT    NOT NULL,
    label           TEXT,
    PRIMARY KEY (msg_channel, msg_id, url)
);

CREATE TABLE IF NOT EXISTS threads (
    channel         TEXT    NOT NULL,
    first_msg_id    INTEGER NOT NULL,
    last_msg_id     INTEGER NOT NULL,
    posted_at       TEXT    NOT NULL,
    text            TEXT    NOT NULL,
    arxiv_url       TEXT,
    github_url      TEXT,
    review_url      TEXT,
    title           TEXT,
    authors         TEXT,
    keywords        TEXT,
    arch_family     TEXT,
    arch_tags       TEXT,
    summary         TEXT,
    llm_family      TEXT,
    llm_subfamily   TEXT,
    llm_modalities  TEXT,
    llm_training_phase TEXT,
    llm_key_concepts TEXT,
    llm_one_liner   TEXT,
    llm_notes       TEXT,
    paper_id        INTEGER,
    PRIMARY KEY (channel, first_msg_id)
);

-- One row per *paper*: a group of one-or-more threads (potentially from
-- different channels) that talk about the same underlying paper.
CREATE TABLE IF NOT EXISTS papers (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    canonical_arxiv     TEXT,               -- e.g. "2410.12345" (no version)
    title               TEXT,
    authors             TEXT,
    earliest_posted_at  TEXT,
    latest_posted_at    TEXT,
    arch_family_hint    TEXT,               -- rule-based family from primary thread
    merged_text         TEXT,
    -- LLM-driven classification (set by gonzo.llm_classify)
    llm_family          TEXT,
    llm_subfamily       TEXT,
    llm_modalities      TEXT,
    llm_training_phase  TEXT,
    llm_key_concepts    TEXT,
    llm_one_liner       TEXT,
    llm_notes           TEXT
);

CREATE INDEX IF NOT EXISTS idx_messages_posted_at ON messages(posted_at);
CREATE INDEX IF NOT EXISTS idx_links_domain ON links(domain);
CREATE INDEX IF NOT EXISTS idx_threads_posted_at ON threads(posted_at);
CREATE INDEX IF NOT EXISTS idx_threads_paper_id ON threads(paper_id);
CREATE INDEX IF NOT EXISTS idx_threads_arxiv ON threads(arxiv_url);
CREATE INDEX IF NOT EXISTS idx_papers_arxiv ON papers(canonical_arxiv);
"""


# ----------------------------- migrations -----------------------------------

DEFAULT_LEGACY_CHANNEL = "gonzo_ML_podcasts"


def _table_cols(conn: sqlite3.Connection, table: str) -> set[str]:
    return {row[1] for row in conn.execute(f"PRAGMA table_info({table})").fetchall()}


def _has_table(conn: sqlite3.Connection, table: str) -> bool:
    row = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,)
    ).fetchone()
    return row is not None


def _migrate(conn: sqlite3.Connection) -> None:
    v = conn.execute("PRAGMA user_version").fetchone()[0]
    if v >= SCHEMA_VERSION:
        return
    legacy = DEFAULT_LEGACY_CHANNEL

    # --- messages ---
    if _has_table(conn, "messages") and "channel" not in _table_cols(conn, "messages"):
        # Pre-v2: PK was `id` alone, single channel.
        conn.execute("ALTER TABLE messages RENAME TO _messages_v1")
        conn.executescript(
            """
            CREATE TABLE messages (
                channel         TEXT    NOT NULL,
                id              INTEGER NOT NULL,
                posted_at       TEXT    NOT NULL,
                views           TEXT,
                html            TEXT,
                text            TEXT,
                has_photo       INTEGER NOT NULL DEFAULT 0,
                has_video       INTEGER NOT NULL DEFAULT 0,
                has_document    INTEGER NOT NULL DEFAULT 0,
                has_link_preview INTEGER NOT NULL DEFAULT 0,
                reply_to_id     INTEGER,
                forwarded_from  TEXT,
                fetched_at      TEXT    NOT NULL,
                PRIMARY KEY (channel, id)
            );
            """
        )
        conn.execute(
            """
            INSERT INTO messages
              (channel, id, posted_at, views, html, text, has_photo, has_video,
               has_document, has_link_preview, reply_to_id, forwarded_from, fetched_at)
            SELECT ?, id, posted_at, views, html, text, has_photo, has_video,
                   has_document, has_link_preview, reply_to_id, forwarded_from, fetched_at
            FROM _messages_v1
            """,
            (legacy,),
        )
        conn.execute("DROP TABLE _messages_v1")

    # --- links ---
    if _has_table(conn, "links") and "msg_channel" not in _table_cols(conn, "links"):
        conn.execute("ALTER TABLE links RENAME TO _links_v1")
        conn.executescript(
            """
            CREATE TABLE links (
                msg_channel     TEXT    NOT NULL,
                msg_id          INTEGER NOT NULL,
                url             TEXT    NOT NULL,
                domain          TEXT    NOT NULL,
                label           TEXT,
                PRIMARY KEY (msg_channel, msg_id, url)
            );
            """
        )
        conn.execute(
            "INSERT INTO links (msg_channel, msg_id, url, domain, label) "
            "SELECT ?, msg_id, url, domain, label FROM _links_v1",
            (legacy,),
        )
        conn.execute("DROP TABLE _links_v1")

    # --- threads ---
    if _has_table(conn, "threads") and "channel" not in _table_cols(conn, "threads"):
        old_cols = _table_cols(conn, "threads")
        conn.execute("ALTER TABLE threads RENAME TO _threads_v1")
        conn.executescript(
            """
            CREATE TABLE threads (
                channel         TEXT    NOT NULL,
                first_msg_id    INTEGER NOT NULL,
                last_msg_id     INTEGER NOT NULL,
                posted_at       TEXT    NOT NULL,
                text            TEXT    NOT NULL,
                arxiv_url       TEXT,
                github_url      TEXT,
                review_url      TEXT,
                title           TEXT,
                authors         TEXT,
                keywords        TEXT,
                arch_family     TEXT,
                arch_tags       TEXT,
                summary         TEXT,
                llm_family      TEXT,
                llm_subfamily   TEXT,
                llm_modalities  TEXT,
                llm_training_phase TEXT,
                llm_key_concepts TEXT,
                llm_one_liner   TEXT,
                llm_notes       TEXT,
                paper_id        INTEGER,
                PRIMARY KEY (channel, first_msg_id)
            );
            """
        )
        carry_cols = [
            "first_msg_id", "last_msg_id", "posted_at", "text", "arxiv_url",
            "github_url", "review_url", "title", "authors", "keywords",
            "arch_family", "arch_tags", "summary",
            "llm_family", "llm_subfamily", "llm_modalities", "llm_training_phase",
            "llm_key_concepts", "llm_one_liner", "llm_notes",
        ]
        carry_present = [c for c in carry_cols if c in old_cols]
        select_cols = ", ".join(carry_present)
        insert_cols = "channel, " + select_cols
        conn.execute(
            f"INSERT INTO threads ({insert_cols}) "
            f"SELECT ?, {select_cols} FROM _threads_v1",
            (legacy,),
        )
        conn.execute("DROP TABLE _threads_v1")

    # Ensure remaining structures exist (papers table + indices) per fresh SCHEMA.
    conn.executescript(SCHEMA)
    conn.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
    conn.commit()


# ----------------------------- public API -----------------------------------

def connect(db_path: str | Path) -> sqlite3.Connection:
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    # Upgrade existing single-channel DBs in place. For a fresh DB this is a
    # no-op (no tables to migrate); the SCHEMA below then creates everything.
    _migrate(conn)
    # SCHEMA uses IF NOT EXISTS, so this safely fills in any missing tables
    # (e.g. ``papers`` on a freshly-migrated DB) and the post-migration indices.
    conn.executescript(SCHEMA)
    conn.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
    conn.commit()
    return conn


def insert_message(conn: sqlite3.Connection, channel: str, msg: dict) -> None:
    conn.execute(
        """
        INSERT OR REPLACE INTO messages
          (channel, id, posted_at, views, html, text, has_photo, has_video,
           has_document, has_link_preview, reply_to_id, forwarded_from, fetched_at)
        VALUES (:channel, :id, :posted_at, :views, :html, :text, :has_photo, :has_video,
                :has_document, :has_link_preview, :reply_to_id, :forwarded_from, :fetched_at)
        """,
        {**msg, "channel": channel},
    )


def insert_links(conn: sqlite3.Connection, channel: str, msg_id: int,
                 links: list[dict]) -> None:
    if not links:
        return
    conn.executemany(
        "INSERT OR IGNORE INTO links (msg_channel, msg_id, url, domain, label) "
        "VALUES (?,?,?,?,?)",
        [(channel, msg_id, l["url"], l["domain"], l.get("label")) for l in links],
    )


def upsert_thread(conn: sqlite3.Connection, thread: dict) -> None:
    cols = (
        "channel, first_msg_id, last_msg_id, posted_at, text, arxiv_url, github_url, "
        "review_url, title, authors, keywords, arch_family, arch_tags, summary"
    )
    placeholders = (
        ":channel, :first_msg_id, :last_msg_id, :posted_at, :text, :arxiv_url, "
        ":github_url, :review_url, :title, :authors, :keywords, "
        ":arch_family, :arch_tags, :summary"
    )
    conn.execute(
        f"INSERT OR REPLACE INTO threads ({cols}) VALUES ({placeholders})",
        thread,
    )
