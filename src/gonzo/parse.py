"""Parse Telegram public-channel preview HTML into structured records."""
from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Iterable
from urllib.parse import urlparse

from bs4 import BeautifulSoup, Tag


def _domain_of(url: str) -> str:
    try:
        return urlparse(url).netloc.lower()
    except Exception:
        return ""


def _text_with_breaks(tag: Tag) -> str:
    # Replace <br> with newlines, then take text
    for br in tag.find_all("br"):
        br.replace_with("\n")
    return tag.get_text("", strip=False)


def parse_page(html: str, *, fetched_at: str | None = None,
               channel: str | None = None) -> list[dict]:
    """Return a list of message dicts ready to insert into messages/links.

    ``channel``, if provided, is included as ``msg["channel"]`` for downstream
    convenience; it does not affect parsing (the channel is also encoded in
    the ``data-post`` attribute of each ``.tgme_widget_message``).
    """
    fetched_at = fetched_at or datetime.now(timezone.utc).isoformat()
    soup = BeautifulSoup(html, "html.parser")
    out: list[dict] = []

    for wrap in soup.select("div.tgme_widget_message_wrap"):
        msg = wrap.select_one("div.tgme_widget_message")
        if not msg:
            continue
        data_post = msg.get("data-post") or ""
        # form: gonzo_ML_podcasts/3548
        m = re.search(r"/(\d+)$", data_post)
        if not m:
            continue
        msg_id = int(m.group(1))

        time_tag = msg.select_one("time[datetime]")
        if not time_tag:
            continue
        posted_at = time_tag["datetime"]

        views_tag = msg.select_one(".tgme_widget_message_views")
        views = views_tag.get_text(strip=True) if views_tag else None

        body_tag = msg.select_one(".tgme_widget_message_text")
        # Some posts have a separate caption text block; tgme exposes it under
        # the same class. If there are multiple, concatenate.
        bodies = msg.select(".tgme_widget_message_text")
        html_parts: list[str] = []
        text_parts: list[str] = []
        links: list[dict] = []
        for b in bodies:
            html_parts.append(b.decode_contents())
            text_parts.append(_text_with_breaks(b))
            for a in b.find_all("a"):
                href = a.get("href")
                if not href:
                    continue
                links.append(
                    {
                        "url": href,
                        "domain": _domain_of(href),
                        "label": a.get_text(strip=True) or None,
                    }
                )
        body_html = "\n\n".join(html_parts) if html_parts else None
        body_text = "\n\n".join(text_parts).strip() if text_parts else None

        has_photo = 1 if msg.select_one(".tgme_widget_message_photo_wrap") else 0
        has_video = 1 if msg.select_one(".tgme_widget_message_video, .tgme_widget_message_video_player") else 0
        has_document = 1 if msg.select_one(".tgme_widget_message_document") else 0
        has_link_preview = 1 if msg.select_one(".tgme_widget_message_link_preview") else 0

        reply = msg.select_one("a.tgme_widget_message_reply")
        reply_to_id = None
        if reply and reply.get("href"):
            mm = re.search(r"/(\d+)(?:\?|$)", reply["href"])
            if mm:
                reply_to_id = int(mm.group(1))

        fwd = msg.select_one(".tgme_widget_message_forwarded_from")
        forwarded_from = fwd.get_text(" ", strip=True) if fwd else None

        # Also surface links from the link-preview block if present
        for lp in msg.select(".tgme_widget_message_link_preview a"):
            href = lp.get("href")
            if not href:
                continue
            links.append(
                {
                    "url": href,
                    "domain": _domain_of(href),
                    "label": lp.get_text(" ", strip=True) or None,
                }
            )

        msg_dict = {
            "id": msg_id,
            "posted_at": posted_at,
            "views": views,
            "html": body_html,
            "text": body_text,
            "has_photo": has_photo,
            "has_video": has_video,
            "has_document": has_document,
            "has_link_preview": has_link_preview,
            "reply_to_id": reply_to_id,
            "forwarded_from": forwarded_from,
            "fetched_at": fetched_at,
        }
        if channel is not None:
            msg_dict["channel"] = channel
        out.append({"msg": msg_dict, "links": links})

    return out


def min_id(records: Iterable[dict]) -> int | None:
    ids = [r["msg"]["id"] for r in records]
    return min(ids) if ids else None
