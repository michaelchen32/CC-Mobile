"""Construct the screening universe: all US-listed common stocks with a
market capitalisation above a threshold (default $10bn).

Source: the Nasdaq stock screener API
(``https://api.nasdaq.com/api/screener/stocks``), which returns every
NYSE/Nasdaq/AMEX-listed name with a live market-cap figure in a single call.
We filter by market cap, drop non-common-stock artefacts (warrants, units,
rights, preferreds, and known fund/ADR-noise), and normalise ticker symbols to
the form yfinance expects (e.g. ``BRK/B`` -> ``BRK-B``).
"""
from __future__ import annotations

import json
import os
import re

from .data import session

CACHE_DIR = os.path.join(os.path.dirname(__file__), os.pardir, "data_cache")
_SCREENER_URL = "https://api.nasdaq.com/api/screener/stocks"

# Suffix patterns that indicate a non-common-stock security we don't want.
_DROP_NAME_RE = re.compile(
    r"\b(warrant|right|unit|preferred|depositary|debenture|note|"
    r"subordinated|when[- ]issued)\b",
    re.IGNORECASE,
)


def _parse_market_cap(raw: str) -> float:
    """'1,234,000,000' -> 1234000000.0 ; '' / 'N/A' -> 0.0"""
    if not raw:
        return 0.0
    cleaned = raw.replace(",", "").replace("$", "").strip()
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


def _normalize_symbol(sym: str) -> str | None:
    sym = sym.strip().upper()
    if not sym:
        return None
    # Share-class separators: Nasdaq uses '/', yfinance uses '-' (BRK/B->BRK-B).
    sym = sym.replace("/", "-").replace(".", "-")
    # Drop symbols with characters yfinance can't resolve (warrants '.WS', etc.).
    if not re.fullmatch(r"[A-Z][A-Z0-9-]{0,6}", sym):
        return None
    # Warrant/unit/right/preferred suffix tickers.
    if re.search(r"-(W|WS|WT|U|R|RT|P)$", sym):
        return None
    return sym


def fetch_screener_rows() -> list[dict]:
    """Raw rows from the Nasdaq screener (symbol, name, marketCap, ...)."""
    sess = session()
    r = sess.get(
        _SCREENER_URL,
        params={"tableonly": "true", "limit": "10000", "exchange": ""},
        timeout=45,
    )
    r.raise_for_status()
    return r.json()["data"]["table"]["rows"]


def build_universe(min_market_cap: float = 10e9, cache: bool = True) -> list[dict]:
    """Return ``[{symbol, name, market_cap}]`` for names above ``min_market_cap``.

    Sorted by market cap descending. Cached to disk so a re-run of the screen
    on the same day doesn't re-hit the screener API.
    """
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_path = os.path.join(CACHE_DIR, f"universe_{int(min_market_cap/1e9)}bn.json")
    if cache and os.path.exists(cache_path):
        with open(cache_path) as fh:
            return json.load(fh)

    rows = fetch_screener_rows()
    seen: set[str] = set()
    out: list[dict] = []
    for row in rows:
        name = (row.get("name") or "")
        if _DROP_NAME_RE.search(name):
            continue
        mcap = _parse_market_cap(row.get("marketCap", ""))
        if mcap < min_market_cap:
            continue
        sym = _normalize_symbol(row.get("symbol", ""))
        if not sym or sym in seen:
            continue
        seen.add(sym)
        out.append({"symbol": sym, "name": name.strip(), "market_cap": mcap})

    out.sort(key=lambda d: d["market_cap"], reverse=True)
    if cache:
        with open(cache_path, "w") as fh:
            json.dump(out, fh)
    return out


if __name__ == "__main__":
    u = build_universe(cache=False)
    print(f"{len(u)} names >$10bn")
    for d in u[:10]:
        print(f"  {d['symbol']:6s} {d['market_cap']/1e9:8.1f}bn  {d['name'][:40]}")
