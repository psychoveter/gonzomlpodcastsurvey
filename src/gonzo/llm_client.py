"""OpenAI client wrapper with on-disk SQLite cache and concurrent helpers.

- Loads `.env` from project root (./.env).
- Caches each (model, prompt_kind, payload_hash) chat completion to
  `data/cache/llm.sqlite` so reruns are free.
- All public helpers return parsed JSON.
"""
from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Callable, Iterable

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CACHE_PATH = PROJECT_ROOT / "data" / "cache" / "llm.sqlite"


def _load_env() -> None:
    env_path = PROJECT_ROOT / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=str(env_path))


def _hash_payload(payload: Any) -> str:
    blob = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def _cache_conn() -> sqlite3.Connection:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(CACHE_PATH))
    conn.execute(
        "CREATE TABLE IF NOT EXISTS llm_cache ("
        "key TEXT PRIMARY KEY,"
        "model TEXT NOT NULL,"
        "kind TEXT NOT NULL,"
        "request TEXT NOT NULL,"
        "response TEXT NOT NULL,"
        "usage TEXT,"
        "created_at REAL NOT NULL)"
    )
    return conn


class LLM:
    """Thin OpenAI chat-completions wrapper with caching and JSON parsing."""

    def __init__(
        self,
        model: str | None = None,
        reasoning_effort: str | None = None,
        timeout: float = 90.0,
    ):
        _load_env()
        from openai import OpenAI  # imported lazily

        self.model = model or os.environ.get("GONZO_OPENAI_MODEL", "gpt-5")
        self.reasoning_effort = reasoning_effort or os.environ.get(
            "GONZO_OPENAI_REASONING", "minimal"
        )
        self.client = OpenAI(timeout=timeout)

    def _call_chat(self, kind: str, messages: list[dict], **kwargs) -> tuple[str, dict]:
        payload = {
            "model": self.model,
            "messages": messages,
            "reasoning_effort": self.reasoning_effort,
            **kwargs,
        }
        cache_key = _hash_payload({"kind": kind, **payload})
        conn = _cache_conn()
        row = conn.execute(
            "SELECT response, usage FROM llm_cache WHERE key = ?", (cache_key,)
        ).fetchone()
        if row is not None:
            return row[0], json.loads(row[1] or "null") or {}

        # Some older models don't accept reasoning_effort; fall back without it.
        try:
            resp = self.client.chat.completions.create(**payload)
        except Exception as e:
            if "reasoning_effort" in str(e):
                payload.pop("reasoning_effort", None)
                resp = self.client.chat.completions.create(**payload)
            else:
                raise
        text = resp.choices[0].message.content or ""
        usage = (resp.usage.model_dump() if resp.usage else {}) or {}
        with conn:
            conn.execute(
                "INSERT OR REPLACE INTO llm_cache "
                "(key, model, kind, request, response, usage, created_at) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    cache_key,
                    self.model,
                    kind,
                    json.dumps(payload, ensure_ascii=False),
                    text,
                    json.dumps(usage),
                    time.time(),
                ),
            )
        return text, usage

    def json(
        self,
        kind: str,
        system: str,
        user: str,
        *,
        retries: int = 3,
        **kwargs,
    ) -> dict:
        """Run a chat with response_format=json_object, returning parsed dict.

        Re-asks once if the first attempt is unparseable.
        """
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]
        last_err: Exception | None = None
        for attempt in range(retries):
            try:
                text, _ = self._call_chat(
                    kind,
                    messages,
                    response_format={"type": "json_object"},
                    **kwargs,
                )
                try:
                    return json.loads(text)
                except json.JSONDecodeError:
                    # Try to extract the first {...} blob
                    start = text.find("{")
                    end = text.rfind("}")
                    if start != -1 and end > start:
                        return json.loads(text[start : end + 1])
                    raise
            except Exception as e:
                last_err = e
                # exponential backoff for rate limits / transient
                time.sleep(2 * (attempt + 1))
        raise RuntimeError(f"LLM call '{kind}' failed after {retries} retries: {last_err}")


def map_concurrent(
    fn: Callable[[Any], Any],
    items: Iterable[Any],
    *,
    workers: int = 8,
    desc: str = "task",
    log_every: int = 10,
) -> list[Any]:
    items = list(items)
    out: list[Any] = [None] * len(items)
    started = time.time()
    done = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(fn, item): i for i, item in enumerate(items)}
        for fut in as_completed(futs):
            i = futs[fut]
            try:
                out[i] = fut.result()
            except Exception as e:
                out[i] = {"_error": str(e)}
            done += 1
            if done % log_every == 0 or done == len(items):
                elapsed = time.time() - started
                rate = done / max(elapsed, 1e-3)
                eta = (len(items) - done) / max(rate, 1e-3)
                print(
                    f"[{desc}] {done}/{len(items)}  rate={rate:.1f}/s  eta={eta:.0f}s",
                    flush=True,
                )
    return out
