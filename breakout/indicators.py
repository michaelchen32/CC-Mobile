"""Shared technical-indicator helpers used by the breakout algorithms."""
from __future__ import annotations

import numpy as np
import pandas as pd


def sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def true_range(df: pd.DataFrame) -> pd.Series:
    prev_close = df["Close"].shift(1)
    a = df["High"] - df["Low"]
    b = (df["High"] - prev_close).abs()
    c = (df["Low"] - prev_close).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    return true_range(df).rolling(n, min_periods=n).mean()


def rolling_slope(s: pd.Series, n: int) -> pd.Series:
    """Least-squares slope of the last n points, normalised by price level."""
    x = np.arange(n, dtype=float)
    x = x - x.mean()
    denom = (x ** 2).sum()

    def _slope(window: np.ndarray) -> float:
        y = window - window.mean()
        return float((x * y).sum() / denom)

    return s.rolling(n, min_periods=n).apply(_slope, raw=True) / s
