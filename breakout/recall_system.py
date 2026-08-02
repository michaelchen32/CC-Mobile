"""High-recall breakout detection.

Design goal: minimise *missed* breakouts. A missed multi-bagger costs far
more than a false alarm, so this inverts the precision-first design — it
is an OR-union of many loose / early triggers rather than an AND-chain of
confirmation gates. Each detector is intentionally permissive; together
they aim to flag essentially every real launch, accepting more noise.

Detectors (any one => a signal):
  fast_donchian   close above the prior 10-day high (early base break)
  donchian_20     close above the prior 20-day high (classic)
  six_month_high  close at a new 126-day high (momentum, looser than 52w)
  volume_thrust   >=5% up day, >=2x avg volume, close in top 30% of range
  gap_go          gap up >=2.5% and holds the open (news-driven launches)
  range_expansion true range >=2x ATR while pushing the 10-day high
                  (catches explosive moves that skip a tidy base)
  squeeze_release TTM squeeze (BB inside KC) fires with positive momentum
  trend_continuation  in an uptrend, new 5-day high right after a >=3% dip
                  (re-entry legs inside an ongoing parabola)

A soft `trend` tag (up / weak / down) is attached for context but does
NOT suppress signals — suppression would reintroduce missed detections.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .indicators import atr, ema, sma

DETECTORS = [
    "fast_donchian",
    "donchian_20",
    "six_month_high",
    "volume_thrust",
    "gap_go",
    "range_expansion",
    "squeeze_release",
    "trend_continuation",
]


def detect(df: pd.DataFrame) -> pd.DataFrame:
    c, h, l, o, v = (
        df["Close"], df["High"], df["Low"], df["Open"], df["Volume"]
    )
    out = pd.DataFrame(index=df.index)

    out["fast_donchian"] = c > h.rolling(10, min_periods=10).max().shift(1)
    out["donchian_20"] = c > h.rolling(20, min_periods=20).max().shift(1)
    out["six_month_high"] = c >= c.rolling(126, min_periods=126).max().shift(1)

    avg_v = v.rolling(20, min_periods=20).mean()
    rng = (h - l).replace(0, np.nan)
    close_pos = (c - l) / rng
    out["volume_thrust"] = (
        (c.pct_change() >= 0.05) & (v >= 2 * avg_v) & (close_pos >= 0.70)
    )

    out["gap_go"] = (o >= c.shift(1) * 1.025) & (c >= o * 0.998)

    a = atr(df, 20)
    tr = pd.concat(
        [h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1
    ).max(axis=1)
    out["range_expansion"] = (tr >= 2 * a) & (
        c > h.rolling(10, min_periods=10).max().shift(1) * 0.995
    )

    n = 20
    mid = sma(c, n)
    sd = c.rolling(n, min_periods=n).std()
    bb_u, bb_l = mid + 2 * sd, mid - 2 * sd
    kc_mid, kc_rng = ema(c, n), atr(df, n)
    kc_u, kc_l = kc_mid + 1.5 * kc_rng, kc_mid - 1.5 * kc_rng
    sqz_on = (bb_u < kc_u) & (bb_l > kc_l)
    released = (~sqz_on) & sqz_on.shift(1).fillna(False)
    out["squeeze_release"] = released & (c > mid)

    sma50, sma150 = sma(c, 50), sma(c, 150)
    uptrend = (c > sma50) & (sma50 > sma150)
    new_5d_high = c >= c.rolling(5, min_periods=5).max()
    dipped = (c.rolling(4, min_periods=4).min() / c) <= 0.97
    out["trend_continuation"] = uptrend & new_5d_high & dipped

    out = out.fillna(False)
    out["n_detectors"] = out[DETECTORS].sum(axis=1).astype(int)
    out["signal"] = out["n_detectors"] > 0

    sma50_rising = sma50 > sma50.shift(10)
    sma200 = sma(c, 200)
    trend = np.where(
        (c > sma50) & sma50_rising, "up",
        np.where(c > sma200, "weak", "down"),
    )
    out["trend"] = trend
    return out


def signal_dates(df: pd.DataFrame, cooldown: int = 3) -> list[pd.Timestamp]:
    """De-duplicated signal bars (small cooldown — we *want* to re-fire on
    fast successive breakouts so continuation legs are not missed)."""
    d = detect(df)
    fired = list(d.index[d["signal"]])
    pos = {ts: i for i, ts in enumerate(df.index)}
    kept, last = [], -(10**9)
    for ts in fired:
        if pos[ts] - last > cooldown:
            kept.append(ts)
            last = pos[ts]
    return kept


def todays_signal(df: pd.DataFrame) -> dict | None:
    """Signal status for the most recent bar in df."""
    d = detect(df)
    last = d.iloc[-1]
    if not bool(last["signal"]):
        return None
    fired = [name for name in DETECTORS if bool(last[name])]
    return {
        "date": df.index[-1].date().isoformat(),
        "close": round(float(df["Close"].iloc[-1]), 2),
        "n_detectors": int(last["n_detectors"]),
        "detectors": "+".join(fired),
        "trend": str(last["trend"]),
    }
