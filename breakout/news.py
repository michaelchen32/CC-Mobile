"""Pull recent news headlines for tickers via yfinance.

For each ticker, returns up to 10 recent stories with title, summary, source,
publish date. We then filter to stories published within the last N days.
"""
from __future__ import annotations

import time
from datetime import datetime, timedelta, timezone

import yfinance as yf


def fetch_news(ticker: str, days: int = 14, max_items: int = 6) -> list[dict]:
    """Return at most `max_items` recent stories within the last `days`."""
    try:
        t = yf.Ticker(ticker)
        raw = t.news or []
    except Exception:
        return []
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    out = []
    for item in raw:
        c = item.get("content") or item
        pub_str = c.get("pubDate") or c.get("displayTime") or ""
        try:
            pub = datetime.fromisoformat(pub_str.replace("Z", "+00:00"))
        except Exception:
            continue
        if pub < cutoff:
            continue
        out.append({
            "title": c.get("title", "").strip(),
            "summary": (c.get("summary") or c.get("description") or "").strip(),
            "source": ((c.get("provider") or {}).get("displayName") or "").strip(),
            "pub": pub.date().isoformat(),
        })
        if len(out) >= max_items:
            break
    return out


def format_news_block(news: list[dict]) -> str:
    if not news:
        return "_no recent headlines found via yfinance_"
    lines = []
    for n in news:
        title = n["title"]
        src = f" — {n['source']}" if n["source"] else ""
        lines.append(f"- **{n['pub']}**: {title}{src}")
    return "\n".join(lines)


if __name__ == "__main__":
    import sys
    for tk in sys.argv[1:]:
        items = fetch_news(tk, days=14)
        print(f"\n=== {tk} ({len(items)} stories) ===")
        print(format_news_block(items))
        time.sleep(0.3)
