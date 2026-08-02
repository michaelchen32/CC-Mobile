"""Regime-detection algorithms.

Every public function returns a daily 0/1 bull-state ``pd.Series`` (int) whose
value at date t uses information up to and including t's close ONLY.

Causality conventions used throughout:
- EWMA statistics are computed with pandas ``ewm`` (past-only by construction)
  and additionally lagged one day (``shift(1)``) wherever a statistic is used
  to normalize the same day's return.
- The HMM applies the forward (filtered) recursion with parameters frozen on
  the training window; no smoothing, no Viterbi.
- Monthly indicators only take effect on the month-end trading day whose close
  completes the month.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd
from hmmlearn.hmm import GaussianHMM

TRAIN_END = pd.Timestamp("2022-12-31")


# --------------------------------------------------------------------------
# 3.1  Two-state Gaussian HMM with a manual forward filter
# --------------------------------------------------------------------------
@dataclass
class HMMParams:
    means: np.ndarray        # (2,)
    variances: np.ndarray    # (2,)
    transmat: np.ndarray     # (2, 2)
    startprob: np.ndarray    # (2,)
    bull_state: int
    log_likelihood: float
    n_restarts: int


def fit_hmm(train_returns: pd.Series, n_restarts: int = 5, seed: int = 42) -> HMMParams:
    """Fit a 2-state Gaussian HMM by EM on training-window returns only.

    Runs ``n_restarts`` seeded EM restarts and keeps the best likelihood.
    """
    import logging

    logging.getLogger("hmmlearn").setLevel(logging.ERROR)  # EM tol chatter
    X = train_returns.to_numpy().reshape(-1, 1)
    best: GaussianHMM | None = None
    best_ll = -np.inf
    for i in range(n_restarts):
        model = GaussianHMM(
            n_components=2,
            covariance_type="diag",
            n_iter=500,
            tol=1e-6,
            random_state=seed + i,
            init_params="stmc",
        )
        model.fit(X)
        ll = model.score(X)
        if ll > best_ll:
            best_ll, best = ll, model
    assert best is not None
    means = best.means_.ravel()
    variances = best.covars_.ravel()
    return HMMParams(
        means=means,
        variances=variances,
        transmat=best.transmat_,
        startprob=best.startprob_,
        bull_state=int(np.argmax(means)),
        log_likelihood=float(best_ll),
        n_restarts=n_restarts,
    )


def hmm_filtered_prob(returns: pd.Series, params: HMMParams) -> pd.Series:
    """Filtered P(bull_t | r_1..t) via the forward algorithm, frozen params.

    Implemented manually so causality is explicit: the recursion is
    predict (p @ A) then update (Gaussian likelihood of today's return),
    normalized each step. Nothing after t ever enters the value at t.
    """
    r = returns.to_numpy()
    mu, var = params.means, params.variances
    A = params.transmat
    norm_const = 1.0 / np.sqrt(2.0 * np.pi * var)

    def emission(x: float) -> np.ndarray:
        return norm_const * np.exp(-0.5 * (x - mu) ** 2 / var)

    p = params.startprob.copy()
    out = np.empty(len(r))
    for t in range(len(r)):
        pred = p @ A if t > 0 else p
        post = pred * emission(r[t])
        s = post.sum()
        if s <= 0 or not np.isfinite(s):  # numerical guard on outliers
            post = pred
            s = post.sum()
        p = post / s
        out[t] = p[params.bull_state]
    return pd.Series(out, index=returns.index, name="p_bull")


def hmm_signal(returns: pd.Series, params: HMMParams) -> pd.Series:
    """Bull when filtered P(bull) > 0.5."""
    return (hmm_filtered_prob(returns, params) > 0.5).astype(int)


def fit_hmm_walkforward(
    returns: pd.Series,
    first_test_year: int = 2023,
    n_restarts: int = 5,
    seed: int = 42,
) -> pd.Series:
    """Walk-forward HMM: refit annually on an expanding window.

    Parameters fitted on data through Dec-31 of year Y generate filtered
    probabilities for calendar year Y+1 (the filter itself is run over all
    history up to each day of Y+1 so state carries in, but the *parameters*
    only ever come from data before the year being signalled).
    """
    last_year = int(returns.index[-1].year)
    sig = pd.Series(0, index=returns.index, dtype=int)
    for year in range(first_test_year, last_year + 1):
        fit_end = pd.Timestamp(f"{year - 1}-12-31")
        params = fit_hmm(returns.loc[:fit_end], n_restarts=n_restarts, seed=seed)
        upto = returns.loc[: pd.Timestamp(f"{year}-12-31")]
        prob = hmm_filtered_prob(upto, params)
        year_mask = prob.index.year == year
        sig.loc[prob.index[year_mask]] = (prob[year_mask] > 0.5).astype(int)
    # Before the first test year, reuse the first fit (train-period signal
    # is only used for display, never for evaluation).
    first_params = fit_hmm(
        returns.loc[: pd.Timestamp(f"{first_test_year - 1}-12-31")],
        n_restarts=n_restarts,
        seed=seed,
    )
    prob0 = hmm_filtered_prob(
        returns.loc[: pd.Timestamp(f"{first_test_year - 1}-12-31")], first_params
    )
    sig.loc[prob0.index] = (prob0 > 0.5).astype(int)
    return sig


# --------------------------------------------------------------------------
# 3.2  Two-sided CUSUM on vol-normalized returns
# --------------------------------------------------------------------------
def ewma_vol_lagged(returns: pd.Series, halflife: float = 20.0) -> pd.Series:
    """EWMA volatility through t-1 (lagged), for normalizing the return at t."""
    return returns.ewm(halflife=halflife, min_periods=20).std().shift(1)


def cusum_signal(
    returns: pd.Series,
    k: float = 0.25,
    h_up: float = 6.0,
    h_down: float = 6.0,
    halflife: float = 20.0,
    initial_bull: int = 1,
    return_paths: bool = False,
) -> pd.Series | tuple[pd.Series, pd.DataFrame]:
    """Two-sided CUSUM (Page 1954) state machine on vol-normalized returns.

    S+_t = max(0, S+_{t-1} + z_t - k); S-_t = min(0, S-_{t-1} + z_t + k).
    Bull-on when S+ > h_up (S+ resets), bull-off when S- < -h_down (S- resets).
    """
    vol = ewma_vol_lagged(returns, halflife)
    z = (returns / vol).replace([np.inf, -np.inf], np.nan)

    s_pos = 0.0
    s_neg = 0.0
    state = initial_bull
    states = np.empty(len(z), dtype=int)
    pos_path = np.full(len(z), np.nan)
    neg_path = np.full(len(z), np.nan)
    zv = z.to_numpy()
    for t in range(len(zv)):
        if np.isfinite(zv[t]):
            s_pos = max(0.0, s_pos + zv[t] - k)
            s_neg = min(0.0, s_neg + zv[t] + k)
            # record pre-reset values so threshold crossings are visible in
            # the diagnostic plot; the reset applies from the next bar on
            pos_path[t] = s_pos
            neg_path[t] = s_neg
            if s_pos > h_up:
                state = 1
                s_pos = 0.0
            if s_neg < -h_down:
                state = 0
                s_neg = 0.0
        else:
            pos_path[t] = s_pos
            neg_path[t] = s_neg
        states[t] = state
    sig = pd.Series(states, index=returns.index, name="cusum")
    if return_paths:
        paths = pd.DataFrame({"S_pos": pos_path, "S_neg": neg_path}, index=returns.index)
        return sig, paths
    return sig


def tune_cusum(
    returns: pd.Series,
    train_end: pd.Timestamp = TRAIN_END,
    k_grid: tuple[float, ...] = (0.1, 0.25, 0.5, 0.75, 1.0),
    h_grid: tuple[float, ...] = (3.0, 4.0, 5.0, 6.0, 8.0, 10.0),
    cost_bps: float = 5.0,
    min_time_in_market: float = 0.2,
    max_time_in_market: float = 0.95,
) -> tuple[dict[str, float], pd.DataFrame]:
    """Grid-search (k, h) on the TRAIN window only, maximizing net Sharpe.

    Symmetric thresholds (h_up = h_down = h). Returns best params and the
    full grid of train Sharpes for reporting. Configurations outside the
    [min, max] time-in-market band are rejected as degenerate: below the
    floor the strategy never participates; above the cap the detector never
    triggers and is indistinguishable from buy-and-hold.
    """
    from backtest import strategy_log_returns, sharpe

    train_r = returns.loc[:train_end]
    rows = []
    best = {"k": 0.25, "h": 6.0, "sharpe": -np.inf}
    for k in k_grid:
        for h in h_grid:
            sig = cusum_signal(train_r, k=k, h_up=h, h_down=h)
            res = strategy_log_returns(train_r, sig, cost_bps=cost_bps)
            s = sharpe(res["net"])
            tim = float((res["position"] > 0).mean())
            rows.append({"k": k, "h": h, "train_sharpe_net": s, "train_time_in_mkt": tim})
            if min_time_in_market <= tim <= max_time_in_market and s > best["sharpe"]:
                best = {"k": k, "h": h, "sharpe": s}
    return best, pd.DataFrame(rows)


# --------------------------------------------------------------------------
# 3.3  Coppock curve
# --------------------------------------------------------------------------
def _wma(x: pd.Series, n: int) -> pd.Series:
    """Linearly weighted MA, heaviest weight on the most recent observation."""
    w = np.arange(1, n + 1, dtype=float)
    return x.rolling(n).apply(lambda v: np.dot(v, w) / w.sum(), raw=True)


def coppock_series(close: pd.Series, roc_long: int, roc_short: int, wma_n: int) -> pd.Series:
    """Coppock = WMA_n( ROC(long) + ROC(short) ), all past-only rolling ops."""
    roc = close.pct_change(roc_long) * 100 + close.pct_change(roc_short) * 100
    return _wma(roc, wma_n)


def coppock_state_from_curve(cop: pd.Series) -> pd.Series:
    """0/1 state from a Coppock curve.

    Entry: Coppock turns up (first rise) while below zero, or crosses above
    zero. Exit: Coppock turns down while below zero (rolls over under the
    zero line). While above zero the state stays bull; the sign of the slope
    above zero is ignored (classic Coppock is a buy indicator — the
    documented exit rule is the sub-zero rollover).
    """
    rising = cop.diff() > 0
    state = 0
    out = np.zeros(len(cop), dtype=int)
    vals = cop.to_numpy()
    ris = rising.to_numpy()
    for t in range(len(vals)):
        if not np.isfinite(vals[t]):
            out[t] = state
            continue
        if vals[t] > 0:
            state = 1
        elif ris[t]:
            state = 1
        else:  # below zero and not rising
            state = 0
        out[t] = state
    return pd.Series(out, index=cop.index, name="coppock")


def coppock_signal_monthly(close: pd.Series) -> pd.Series:
    """Classic monthly Coppock (ROC 14m + ROC 11m, 10m WMA), mapped to daily.

    The monthly value is stamped on the month's last trading day (the close
    that completes the month) and forward-filled — so a change of state is
    only visible from that month-end close onward. Strictly causal.
    """
    monthly = close.groupby(pd.Grouper(freq="ME")).last()
    month_end_dates = close.groupby(pd.Grouper(freq="ME")).apply(lambda s: s.index[-1])
    cop = coppock_series(monthly, 14, 11, 10)
    state_m = coppock_state_from_curve(cop)
    state_m.index = pd.DatetimeIndex(month_end_dates.to_numpy())
    daily = state_m.reindex(close.index).ffill().fillna(0).astype(int)
    return daily


def coppock_signal_daily(close: pd.Series) -> pd.Series:
    """Daily-frequency Coppock variant: same lookbacks in days (x21)."""
    cop = coppock_series(close, 14 * 21, 11 * 21, 10 * 21)
    return coppock_state_from_curve(cop).fillna(0).astype(int)


def choose_coppock_variant(
    close: pd.Series,
    returns: pd.Series,
    train_end: pd.Timestamp = TRAIN_END,
    cost_bps: float = 5.0,
) -> tuple[str, dict[str, float]]:
    """Pick monthly vs daily variant by net Sharpe on the TRAIN window only."""
    from backtest import strategy_log_returns, sharpe

    train_r = returns.loc[:train_end]
    scores = {}
    for name, fn in (("monthly", coppock_signal_monthly), ("daily", coppock_signal_daily)):
        sig = fn(close.loc[:train_end])
        net = strategy_log_returns(train_r, sig.reindex(train_r.index).ffill().fillna(0))["net"]
        scores[name] = sharpe(net)
    winner = max(scores, key=scores.get)  # type: ignore[arg-type]
    return winner, scores


# --------------------------------------------------------------------------
# 3.4  Adaptive Kalman local-level filter
# --------------------------------------------------------------------------
def kalman_drift(
    returns: pd.Series,
    q: float,
    halflife: float = 20.0,
) -> pd.DataFrame:
    """Local-level Kalman filter: r_t = mu_t + eps_t, mu_t = mu_{t-1} + eta_t.

    Observation variance R_t is the lagged EWMA variance of returns
    (adaptive); state noise Q is constant. Returns filtered mu_t and its
    posterior variance P_t, both using data through t only.
    """
    var = returns.ewm(halflife=halflife, min_periods=20).var().shift(1)
    r = returns.to_numpy()
    R = var.to_numpy()
    n = len(r)
    mu = np.full(n, np.nan)
    P = np.full(n, np.nan)
    mu_t = 0.0
    # diffuse-ish start: prior variance = typical daily return variance
    P_t = np.nanmedian(R[np.isfinite(R)][:250]) if np.isfinite(R).any() else 1e-4
    for t in range(n):
        if not np.isfinite(R[t]):
            continue
        P_pred = P_t + q
        K = P_pred / (P_pred + R[t])
        mu_t = mu_t + K * (r[t] - mu_t)
        P_t = (1.0 - K) * P_pred
        mu[t] = mu_t
        P[t] = P_t
    return pd.DataFrame({"mu": mu, "P": P}, index=returns.index)


def kalman_signal(returns: pd.Series, q: float, mult: float = 1.0) -> pd.Series:
    """Bull when filtered drift is significantly positive: mu_t > mult*sqrt(P_t)."""
    kf = kalman_drift(returns, q)
    sig = (kf["mu"] > mult * np.sqrt(kf["P"])).astype(int)
    return sig


def tune_kalman(
    returns: pd.Series,
    train_end: pd.Timestamp = TRAIN_END,
    q_grid: tuple[float, ...] = (1e-5, 3e-5, 1e-4, 3e-4, 1e-3),
    mult_grid: tuple[float, ...] = (0.05, 0.1, 0.25, 0.5, 1.0, 2.0),
    cost_bps: float = 5.0,
    min_time_in_market: float = 0.2,
    max_time_in_market: float = 0.95,
) -> tuple[dict[str, float], pd.DataFrame]:
    """Grid-search Q and the significance multiplier on the TRAIN window only.

    The multiplier grid extends well below the spec's 1.0 baseline: with the
    spec's Q range and realistic SOXX vol, sqrt(P_t) sits around 0.5-2% per
    day — an order of magnitude above any plausible daily drift — so
    mu > 1.0*sqrt(P) is almost never true and the strategy degenerates to
    always-flat. Configurations below the in-market floor are rejected.
    """
    from backtest import strategy_log_returns, sharpe

    train_r = returns.loc[:train_end]
    rows = []
    best = {"q": 1e-4, "mult": 1.0, "sharpe": -np.inf}
    for q in q_grid:
        for m in mult_grid:
            sig = kalman_signal(train_r, q=q, mult=m)
            res = strategy_log_returns(train_r, sig, cost_bps=cost_bps)
            s = sharpe(res["net"])
            tim = float((res["position"] > 0).mean())
            rows.append({"q": q, "mult": m, "train_sharpe_net": s, "train_time_in_mkt": tim})
            if min_time_in_market <= tim <= max_time_in_market and s > best["sharpe"]:
                best = {"q": q, "mult": m, "sharpe": s}
    return best, pd.DataFrame(rows)


# --------------------------------------------------------------------------
# 3.5  VIX term-structure overlay
# --------------------------------------------------------------------------
def vix_signal(vix_pair: pd.DataFrame, index: pd.DatetimeIndex) -> pd.Series:
    """Bull-friendly when VIX3M/VIX > 1 (contango), aligned to trading days.

    Reindexed with ffill so a missing VIX print reuses the latest known
    ratio (never a future one).
    """
    ratio = (vix_pair["VIX3M"] / vix_pair["VIX"]).reindex(index).ffill()
    return (ratio > 1.0).astype(int)


# --------------------------------------------------------------------------
# 3.6  Composite
# --------------------------------------------------------------------------
def composite_signal(signals: dict[str, pd.Series], index: pd.DatetimeIndex) -> pd.Series:
    """Equal-weight vote of the component 0/1 signals; bull when mean >= 0.5."""
    aligned = pd.DataFrame(
        {k: s.reindex(index).ffill().fillna(0) for k, s in signals.items()}
    )
    return (aligned.mean(axis=1) >= 0.5).astype(int)
