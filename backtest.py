"""Backtest engine: execution-lag accounting, costs, and performance metrics.

Hard no-look-ahead rules enforced here:
- ``strategy_log_returns`` shifts the signal by one bar BEFORE multiplying
  with returns: a signal computed from day t's close earns day t+1's return
  at the earliest.
- Transaction costs (default 5 bps per side) are charged on every unit of
  position change, on the day the new position takes effect.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

TRADING_DAYS = 252


def strategy_log_returns(
    asset_log_returns: pd.Series,
    signal: pd.Series,
    cost_bps: float = 5.0,
    lag: int = 1,
) -> pd.DataFrame:
    """Long/flat daily log returns for a 0/1 signal, gross and net of costs.

    ``position_t = signal_{t-lag}`` (execution lag, default one bar).
    Cost per side = ``cost_bps``; a 0->1 or 1->0 flip is one side.
    """
    sig = signal.reindex(asset_log_returns.index).ffill().fillna(0)
    position = sig.shift(lag).fillna(0)
    gross = position * asset_log_returns
    turnover = position.diff().abs().fillna(position.abs())
    cost = turnover * (-np.log(1.0 - cost_bps / 1e4))
    net = gross - cost
    return pd.DataFrame(
        {"position": position, "gross": gross, "net": net, "turnover": turnover}
    )


def sharpe(log_ret: pd.Series) -> float:
    """Annualized Sharpe on daily log returns (rf = 0)."""
    r = log_ret.dropna()
    if len(r) < 2 or r.std() == 0:
        return 0.0
    return float(r.mean() / r.std() * np.sqrt(TRADING_DAYS))


def sortino(log_ret: pd.Series) -> float:
    r = log_ret.dropna()
    downside = r[r < 0]
    if len(r) < 2 or len(downside) == 0 or downside.std() == 0:
        return 0.0
    dd = np.sqrt((downside**2).mean())
    return float(r.mean() / dd * np.sqrt(TRADING_DAYS))


def max_drawdown(log_ret: pd.Series) -> float:
    """Max drawdown (negative fraction) of the compounded equity curve."""
    equity = np.exp(log_ret.cumsum())
    peak = equity.cummax()
    return float((equity / peak - 1.0).min())


def drawdown_curve(log_ret: pd.Series) -> pd.Series:
    equity = np.exp(log_ret.cumsum())
    return equity / equity.cummax() - 1.0


def annualized_return(log_ret: pd.Series) -> float:
    """Geometric annualized return."""
    r = log_ret.dropna()
    if len(r) == 0:
        return 0.0
    return float(np.exp(r.mean() * TRADING_DAYS) - 1.0)


def annualized_vol(log_ret: pd.Series) -> float:
    return float(log_ret.dropna().std() * np.sqrt(TRADING_DAYS))


def perf_metrics(log_ret: pd.Series, position: pd.Series | None = None) -> dict[str, float]:
    """Full metric block for one return stream."""
    ar = annualized_return(log_ret)
    mdd = max_drawdown(log_ret)
    out = {
        "ann_return": ar,
        "ann_vol": annualized_vol(log_ret),
        "sharpe": sharpe(log_ret),
        "sortino": sortino(log_ret),
        "max_drawdown": mdd,
        "calmar": ar / abs(mdd) if mdd < 0 else np.nan,
    }
    if position is not None:
        pos = position.reindex(log_ret.index).fillna(0)
        in_mkt = pos > 0
        active = log_ret[in_mkt]
        out["hit_rate"] = float((active > 0).mean()) if len(active) else np.nan
        out["time_in_market"] = float(in_mkt.mean())
        out["n_switches"] = int(pos.diff().abs().sum())
    else:
        out["hit_rate"] = float((log_ret > 0).mean())
        out["time_in_market"] = 1.0
        out["n_switches"] = 0
    return out


def evaluate_strategies(
    asset_log_returns: pd.Series,
    signals: dict[str, pd.Series],
    test_start: str = "2023-01-01",
    cost_bps: float = 5.0,
) -> tuple[pd.DataFrame, dict[str, pd.DataFrame]]:
    """Metrics table (gross & net) over the test window + per-strategy streams.

    The signal history BEFORE test_start is used only to seed the position on
    the first test day (state carries in causally); returns are evaluated
    strictly inside the test window.
    """
    rows = []
    streams: dict[str, pd.DataFrame] = {}

    test_r = asset_log_returns.loc[test_start:]
    bh = perf_metrics(test_r)
    rows.append({"strategy": "buy_and_hold", "basis": "gross", **bh})
    rows.append({"strategy": "buy_and_hold", "basis": "net", **bh})
    streams["buy_and_hold"] = pd.DataFrame(
        {"position": 1.0, "gross": test_r, "net": test_r, "turnover": 0.0}
    )

    for name, sig in signals.items():
        full = strategy_log_returns(asset_log_returns, sig, cost_bps=cost_bps)
        test = full.loc[test_start:]
        streams[name] = test
        rows.append(
            {"strategy": name, "basis": "gross", **perf_metrics(test["gross"], test["position"])}
        )
        rows.append(
            {"strategy": name, "basis": "net", **perf_metrics(test["net"], test["position"])}
        )
    return pd.DataFrame(rows), streams


# --------------------------------------------------------------------------
# Event analysis: drawdown episodes, detection lags, whipsaws
# --------------------------------------------------------------------------
def top_drawdown_episodes(close: pd.Series, n: int = 2) -> list[dict]:
    """The n deepest peak-to-trough episodes in ``close`` (non-overlapping).

    Each episode: peak date, trough date, depth, and the recovery date (first
    date the prior peak is regained, if any).
    """
    dd = close / close.cummax() - 1.0
    episodes = []
    used = pd.Series(False, index=close.index)
    remaining = dd.copy()
    for _ in range(n * 3):  # search a few extra in case of overlap
        if remaining[~used].empty:
            break
        trough_date = remaining[~used].idxmin()
        depth = float(remaining.loc[trough_date])
        if depth >= -0.02:
            break
        pre = close.loc[:trough_date]
        peak_date = pre[pre == pre.cummax().loc[trough_date]].index[-1]
        peak_val = float(close.loc[peak_date])
        post = close.loc[trough_date:]
        rec = post[post >= peak_val]
        rec_date = rec.index[0] if len(rec) else None
        span_end = rec_date if rec_date is not None else close.index[-1]
        overlap = used.loc[peak_date:span_end].any()
        if not overlap:
            episodes.append(
                {
                    "peak": peak_date,
                    "trough": trough_date,
                    "depth": depth,
                    "recovery": rec_date,
                }
            )
        used.loc[peak_date:span_end] = True
        if len(episodes) >= n:
            break
    episodes.sort(key=lambda e: e["depth"])
    return episodes[:n]


def detection_lags(
    signals: dict[str, pd.Series],
    episodes: list[dict],
    index: pd.DatetimeIndex,
) -> pd.DataFrame:
    """Days from peak to each algo's bear flip, and trough to bull flip.

    Lags are in trading days. ``None`` if the algo never flipped within the
    episode window (peak -> next episode's peak or end of data).
    """
    rows = []
    for ep in episodes:
        peak, trough = ep["peak"], ep["trough"]
        end = ep["recovery"] if ep["recovery"] is not None else index[-1]
        for name, sig in signals.items():
            s = sig.reindex(index).ffill().fillna(0)
            after_peak = s.loc[peak:end]
            bear_dates = after_peak[after_peak == 0].index
            bear_date = bear_dates[0] if len(bear_dates) else None
            bear_lag = (
                int(index.get_loc(bear_date) - index.get_loc(peak))
                if bear_date is not None
                else None
            )
            note = ""
            if s.loc[:peak].iloc[-1] == 0:
                note = "already bear at peak"
            elif bear_date is None or bear_date > trough:
                note = "never bear before trough"
            # Re-entry lag is only meaningful if the algo was bear at the
            # trough; otherwise it simply rode the drawdown fully invested.
            if s.loc[trough] == 0:
                after_trough = s.loc[trough:]
                bull_dates = after_trough[after_trough == 1].index
                bull_date = bull_dates[0] if len(bull_dates) else None
                bull_lag = (
                    int(index.get_loc(bull_date) - index.get_loc(trough))
                    if bull_date is not None
                    else None
                )
            else:
                bull_date, bull_lag = None, None
                note = (note + "; " if note else "") + "already bull at trough"
            rows.append(
                {
                    "episode_peak": peak.date(),
                    "episode_trough": trough.date(),
                    "depth": ep["depth"],
                    "algorithm": name,
                    "bear_flip_date": bear_date.date() if bear_date is not None else None,
                    "days_peak_to_bear": bear_lag,
                    "bull_flip_date": bull_date.date() if bull_date is not None else None,
                    "days_trough_to_bull": bull_lag,
                    "note": note,
                }
            )
    return pd.DataFrame(rows)


def whipsaw_count(signal: pd.Series, min_days: int = 10, start: str | None = None) -> int:
    """Number of bull runs shorter than ``min_days`` trading days."""
    s = signal.copy()
    if start is not None:
        s = s.loc[start:]
    runs = (s != s.shift()).cumsum()
    lengths = s.groupby(runs).agg(["first", "size"])
    return int(((lengths["first"] == 1) & (lengths["size"] < min_days)).sum())
