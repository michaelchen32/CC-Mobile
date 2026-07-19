"""Breakout detection — a high-recall OR-union of 8 loose detectors.

Methodology mirrors the project's recall system: the design goal is to minimise
*missed* breakouts (a missed multibagger costs more than a false alarm), so any
single detector firing counts as a signal. ``n_detectors`` (how many fired) is
the confluence/strength gauge, and a ``trend`` tag is attached for context only
(it never suppresses a signal).

This is a clean-room reimplementation — the indicator maths and the detector
definitions are written here directly, not imported from any prior code.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

# ----------------------------------------------------------------------------
# Indicators
# ----------------------------------------------------------------------------


def sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n).mean()


def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def true_range(df: pd.DataFrame) -> pd.Series:
    prev_close = df["Close"].shift(1)
    hl = df["High"] - df["Low"]
    hc = (df["High"] - prev_close).abs()
    lc = (df["Low"] - prev_close).abs()
    return pd.concat([hl, hc, lc], axis=1).max(axis=1)


def atr(df: pd.DataFrame, n: int = 20) -> pd.Series:
    return true_range(df).rolling(n).mean()


# ----------------------------------------------------------------------------
# Squeeze (TTM): Bollinger Bands inside Keltner Channels = coiled.
# ----------------------------------------------------------------------------


def _squeeze_on(df: pd.DataFrame, n: int = 20, bb_k: float = 2.0, kc_k: float = 1.5) -> pd.Series:
    close = df["Close"]
    mid = sma(close, n)
    sd = close.rolling(n).std()
    bb_up, bb_lo = mid + bb_k * sd, mid - bb_k * sd
    kc_mid = ema(close, n)
    rng = atr(df, n)
    kc_up, kc_lo = kc_mid + kc_k * rng, kc_mid - kc_k * rng
    return (bb_lo > kc_lo) & (bb_up < kc_up)


# ----------------------------------------------------------------------------
# Detectors — each returns True/False for the LATEST bar of ``df``.
# "prior N-day high" excludes the current bar (uses .shift(1)).
# ----------------------------------------------------------------------------

MIN_BARS = 210  # need SMA200 + a little warmup


def _detect(df: pd.DataFrame) -> dict:
    close = df["Close"]
    high = df["High"]
    low = df["Low"]
    vol = df["Volume"]
    open_ = df["Open"]

    c = close.iloc[-1]
    fired: list[str] = []

    def prior_high(win: int) -> float:
        # highest high of the `win` bars ending just before today
        return float(high.shift(1).iloc[-win:].max())

    # 1. fast_donchian — close > prior 10-day high (early base break)
    if c > prior_high(10):
        fired.append("fast_donchian")

    # 2. donchian_20 — close > prior 20-day high
    if c > prior_high(20):
        fired.append("donchian_20")

    # 3. six_month_high — close >= prior 126-day high
    if c >= prior_high(126):
        fired.append("six_month_high")

    # 4. volume_thrust — >=5% up day AND >=2x 20d avg vol AND close in top 30% of range
    day_ret = c / close.iloc[-2] - 1.0
    avg_vol = float(vol.iloc[-21:-1].mean())
    rng = high.iloc[-1] - low.iloc[-1]
    close_pos = (c - low.iloc[-1]) / rng if rng > 0 else 0.0
    if day_ret >= 0.05 and avg_vol > 0 and vol.iloc[-1] >= 2 * avg_vol and close_pos >= 0.70:
        fired.append("volume_thrust")

    # 5. gap_go — gap up >=2.5% and holds the open (close >= open)
    if open_.iloc[-1] >= close.iloc[-2] * 1.025 and c >= open_.iloc[-1]:
        fired.append("gap_go")

    # 6. range_expansion — true range >=2x ATR(20) while pushing the 10-day high
    tr = true_range(df).iloc[-1]
    atr20_prior = float(atr(df, 20).iloc[-2])
    if atr20_prior > 0 and tr >= 2 * atr20_prior and c > prior_high(10):
        fired.append("range_expansion")

    # 7. squeeze_release — TTM squeeze released within last ~6 bars, positive momentum
    sq = _squeeze_on(df)
    released = (not bool(sq.iloc[-1])) and bool(sq.iloc[-7:-1].any())
    momentum_up = c > close.iloc[-5]
    if released and momentum_up:
        fired.append("squeeze_release")

    # 8. trend_continuation — uptrend (c>SMA50>SMA150), new 5-day high right after a >=3% dip
    sma50 = float(sma(close, 50).iloc[-1])
    sma150 = float(sma(close, 150).iloc[-1])
    win = close.iloc[-6:-1]
    dip = (win.max() - win.min()) / win.max() if len(win) and win.max() > 0 else 0.0
    if c > sma50 > sma150 and c > prior_high(5) and dip >= 0.03:
        fired.append("trend_continuation")

    # ---- trend tag (context only) ----
    sma50_series = sma(close, 50)
    sma200 = float(sma(close, 200).iloc[-1])
    sma50_now = float(sma50_series.iloc[-1])
    sma50_rising = sma50_now > float(sma50_series.iloc[-6])
    if c > sma50_now and sma50_rising:
        trend = "up"
    elif c > sma200:
        trend = "weak"
    else:
        trend = "down"

    return {
        "close": round(float(c), 2),
        "n_detectors": len(fired),
        "detectors": fired,
        "trend": trend,
        "day_ret": round(float(day_ret) * 100, 2),
    }


def todays_signal(df: pd.DataFrame) -> dict | None:
    """Evaluate the latest bar. Returns a signal dict if >=1 detector fired,
    else None. Returns None when there isn't enough history."""
    if df is None or len(df) < MIN_BARS:
        return None
    df = df[["Open", "High", "Low", "Close", "Volume"]].dropna()
    if len(df) < MIN_BARS:
        return None
    try:
        sig = _detect(df)
    except Exception:  # noqa: BLE001 - a single bad frame shouldn't kill the screen
        return None
    if sig["n_detectors"] == 0:
        return None
    return sig
