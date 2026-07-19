"""Price-data access layer.

Why this is written the way it is
---------------------------------
Recent yfinance (>=1.5) drives its HTTP through **curl_cffi** with a browser-
impersonated TLS fingerprint. In an environment whose outbound HTTPS is
re-terminated by an intercepting proxy, that impersonated handshake is reset by
the proxy ("Recv failure: Connection reset by peer"), so *every* request dies
before it reaches Yahoo. Naked ``curl`` to the chart endpoint fails differently:
it returns HTTP 429 because it carries no cookie/crumb.

The fix used here is to hand yfinance a **plain ``requests.Session``**. That
session honours the environment's ``HTTPS_PROXY`` and ``REQUESTS_CA_BUNDLE``,
performs yfinance's normal cookie + crumb handshake, and does *not* use the
impersonated TLS that the proxy rejects. This is the piece that makes data
retrieval work here where the default path 429s / resets.

Everything is cached per-ticker on disk so re-runs are cheap.
"""
from __future__ import annotations

import os
import time

import pandas as pd
import requests
import yfinance as yf

CACHE_DIR = os.path.join(os.path.dirname(__file__), os.pardir, "data_cache")

_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

_SESSION: requests.Session | None = None


def session() -> requests.Session:
    """A shared, proxy-aware, browser-UA requests session (NOT curl_cffi)."""
    global _SESSION
    if _SESSION is None:
        s = requests.Session()
        s.headers.update({"User-Agent": _UA, "Accept": "application/json, text/plain, */*"})
        _SESSION = s
    return _SESSION


def _cache_path(ticker: str, start: str, end: str) -> str:
    safe = ticker.replace("/", "_").replace("^", "_")
    return os.path.join(CACHE_DIR, f"{safe}_{start}_{end}.csv")


def download_batch(
    tickers: list[str],
    start: str,
    end: str,
    batch_size: int = 50,
    pause: float = 0.4,
    progress_cb=None,
) -> dict[str, pd.DataFrame]:
    """Download OHLCV for many tickers, filling a per-ticker CSV cache.

    Returns ``{ticker: DataFrame}`` for everything that resolved. Failed /
    delisted names are skipped silently. Uses yfinance's threaded multi-ticker
    download over a plain requests session, in modest batches with a short pause
    between them to stay well under any rate ceiling.
    """
    os.makedirs(CACHE_DIR, exist_ok=True)
    out: dict[str, pd.DataFrame] = {}
    missing: list[str] = []

    # Serve from cache first.
    for t in tickers:
        p = _cache_path(t, start, end)
        if os.path.exists(p):
            try:
                df = pd.read_csv(p, index_col=0, parse_dates=True)
                if not df.empty:
                    out[t] = df
                    continue
            except Exception:  # noqa: BLE001 - corrupt cache -> refetch
                pass
        missing.append(t)

    sess = session()
    done = len(out)
    total = len(tickers)
    if progress_cb:
        progress_cb(done, total, "cache")

    for i in range(0, len(missing), batch_size):
        chunk = missing[i : i + batch_size]
        raw = None
        for attempt in range(3):
            try:
                raw = yf.download(
                    chunk,
                    start=start,
                    end=end,
                    auto_adjust=True,
                    group_by="ticker",
                    threads=True,
                    progress=False,
                    session=sess,
                )
                break
            except Exception:  # noqa: BLE001 - retry whole-batch provider errors
                time.sleep(2 ** attempt)
        if raw is None or len(raw) == 0:
            done += len(chunk)
            if progress_cb:
                progress_cb(done, total, "batch-fail")
            time.sleep(pause)
            continue

        multi = isinstance(raw.columns, pd.MultiIndex)
        for t in chunk:
            try:
                sub = raw[t] if multi else raw
                df = sub[["Open", "High", "Low", "Close", "Volume"]].dropna()
                if df.empty:
                    continue
                df.to_csv(_cache_path(t, start, end))
                out[t] = df
            except Exception:  # noqa: BLE001 - skip individual bad ticker
                continue
        done += len(chunk)
        if progress_cb:
            progress_cb(done, total, "batch")
        time.sleep(pause)

    return out
