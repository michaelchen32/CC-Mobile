"""Screen orchestrator: build the >$10bn universe, fetch OHLCV, run the
breakout detectors on the latest bar, enrich the resulting signals with
sector/industry, and rank them.
"""
from __future__ import annotations

import sys
import time
from datetime import date, datetime, timedelta

import pandas as pd
import yfinance as yf

from .data import download_batch, session
from .detectors import todays_signal
from .universe import build_universe

LOOKBACK_DAYS = 560  # ~385 trading days: enough for the 252d high + 50d slope


def _progress(done: int, total: int, tag: str) -> None:
    pct = 100 * done / total if total else 100
    sys.stderr.write(f"\r  fetch {done}/{total} ({pct:4.0f}%) [{tag}]      ")
    sys.stderr.flush()


def enrich_sector(symbols: list[str], pause: float = 0.15) -> dict[str, dict]:
    """Best-effort sector/industry/revenue-growth for the signal names only.

    Uses Ticker.get_info() over the shared requests session. Failures degrade to
    'Unknown' rather than aborting the screen.
    """
    sess = session()
    out: dict[str, dict] = {}
    for i, sym in enumerate(symbols):
        info = {}
        try:
            info = yf.Ticker(sym, session=sess).get_info() or {}
        except Exception:  # noqa: BLE001
            info = {}
        out[sym] = {
            "sector": info.get("sector") or "Unknown",
            "industry": info.get("industry") or "",
            "rev_growth": info.get("revenueGrowth"),
        }
        sys.stderr.write(f"\r  sector {i+1}/{len(symbols)}      ")
        sys.stderr.flush()
        time.sleep(pause)
    sys.stderr.write("\n")
    return out


def run_screen(asof: str | None = None, min_market_cap: float = 10e9) -> dict:
    """Run the full screen. ``asof`` = trading day to evaluate (YYYY-MM-DD);
    defaults to today. Returns a result dict with the ranked signals."""
    if asof is None:
        asof = date.today().isoformat()
    asof_d = datetime.strptime(asof, "%Y-%m-%d").date()
    end = (asof_d + timedelta(days=1)).isoformat()  # yfinance end is exclusive
    start = (asof_d - timedelta(days=LOOKBACK_DAYS)).isoformat()

    universe = build_universe(min_market_cap=min_market_cap)
    mcap = {d["symbol"]: d["market_cap"] for d in universe}
    names = {d["symbol"]: d["name"] for d in universe}
    symbols = [d["symbol"] for d in universe]
    sys.stderr.write(f"Universe: {len(symbols)} names >${min_market_cap/1e9:.0f}bn\n")

    data = download_batch(symbols, start, end, batch_size=50, progress_cb=_progress)
    sys.stderr.write(f"\n  resolved OHLCV for {len(data)}/{len(symbols)} names\n")

    signals: list[dict] = []
    last_bar_dates: dict[str, str] = {}
    for sym in symbols:
        df = data.get(sym)
        if df is None or df.empty:
            continue
        # Only evaluate names whose latest bar is the requested session.
        last_bar = df.index[-1].date().isoformat()
        last_bar_dates[sym] = last_bar
        sig = todays_signal(df)
        if sig is None:
            continue
        sig.update(
            symbol=sym,
            name=names.get(sym, ""),
            market_cap=mcap.get(sym, 0.0),
            last_bar=last_bar,
        )
        signals.append(sig)

    # Enrich only the signal names with sector data.
    sig_syms = [s["symbol"] for s in signals]
    sys.stderr.write(f"Signals: {len(sig_syms)}; enriching sectors...\n")
    sectors = enrich_sector(sig_syms)
    for s in signals:
        meta = sectors.get(s["symbol"], {})
        s["sector"] = meta.get("sector", "Unknown")
        s["industry"] = meta.get("industry", "")
        s["rev_growth"] = meta.get("rev_growth")

    # Rank: confluence first, then day move.
    signals.sort(key=lambda s: (s["n_detectors"], s["day_ret"]), reverse=True)

    # Most-common last bar across the universe = the effective session screened.
    from collections import Counter
    session_bar = Counter(last_bar_dates.values()).most_common(1)
    session_date = session_bar[0][0] if session_bar else asof

    return {
        "asof": asof,
        "session_date": session_date,
        "universe_size": len(symbols),
        "resolved": len(data),
        "signals": signals,
        "min_market_cap": min_market_cap,
    }


def signals_dataframe(result: dict) -> pd.DataFrame:
    rows = []
    for s in result["signals"]:
        rows.append({
            "symbol": s["symbol"],
            "name": s["name"],
            "sector": s.get("sector", "Unknown"),
            "market_cap_bn": round(s["market_cap"] / 1e9, 1),
            "close": s["close"],
            "day_ret_pct": s["day_ret"],
            "n_detectors": s["n_detectors"],
            "detectors": ";".join(s["detectors"]),
            "trend": s["trend"],
            "rev_growth": s.get("rev_growth"),
        })
    return pd.DataFrame(rows)
