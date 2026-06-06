"""
Hidden Markov Model market-regime detector (walk-forward, no look-ahead).

Pipeline
--------
1. Load ~30 years of S&P 500 (^GSPC) daily closes (data/gspc.csv).
2. Build one observation per trading day from a TRAILING 5-trading-day window
   (the "observation window"):
       f1 = mean daily log-return over the window   (trend)
       f2 = std  daily log-return over the window    (risk / realized vol)
   The window only looks backward, so observation at day t uses data <= t.
3. Walk-forward:
       * expanding training window, model re-fit once per calendar year,
         using ONLY data strictly before the re-fit date,
       * feature standardisation uses ONLY the training slice (no leakage),
       * the regime probability reported for each day t is the FILTERED
         posterior  P(state_t | obs_1..t)  produced by the forward algorithm
         -- it never peeks at obs_{t+1..T} (no future data).
4. States are relabelled every re-fit by their mean-return parameter so the
   labels Bear / Neutral / Bull stay consistent across re-fits.
5. Evaluate: realised NEXT-day return conditioned on the (causal) filtered
   regime -- a genuine out-of-sample test of predictive value.
6. Report the regime as of the most recent close ("after Friday's close")
   and the model's one-step-ahead outlook.

Run:  python3 src/hmm_regime.py
"""

import warnings
import numpy as np
import pandas as pd
from scipy.stats import multivariate_normal
from hmmlearn.hmm import GaussianHMM

warnings.filterwarnings("ignore")

WINDOW = 5            # observation window, trading days
N_STATES = 3          # Bear / Neutral / Bull
BURN_IN_YEARS = 5     # initial training before any prediction is made
SEED = 7
TRADING_DAYS = 252

REGIME_NAMES = {0: "Bear", 1: "Neutral", 2: "Bull"}


# --------------------------------------------------------------------------- #
# Data & features
# --------------------------------------------------------------------------- #
def load_data(path="data/gspc.csv"):
    df = pd.read_csv(path, parse_dates=["date"]).sort_values("date").reset_index(drop=True)
    px = df["adjclose"].where(df["adjclose"].notna(), df["close"]).astype(float)
    df["price"] = px
    df["ret"] = np.log(df["price"]).diff()
    return df.dropna(subset=["ret"]).reset_index(drop=True)


def build_features(df, window=WINDOW):
    """One observation per day from the trailing `window` daily returns."""
    r = df["ret"]
    f1 = r.rolling(window).mean()                 # average daily return
    f2 = r.rolling(window).std(ddof=0)            # realized volatility
    feat = pd.DataFrame({"date": df["date"], "price": df["price"], "ret": df["ret"],
                         "f1": f1, "f2": f2}).dropna().reset_index(drop=True)
    return feat


# --------------------------------------------------------------------------- #
# HMM helpers
# --------------------------------------------------------------------------- #
def fit_hmm(X, seed=SEED):
    """Fit a Gaussian HMM, trying a few seeds, keep the best log-likelihood."""
    best, best_ll = None, -np.inf
    for s in range(seed, seed + 6):
        m = GaussianHMM(n_components=N_STATES, covariance_type="full",
                        n_iter=300, tol=1e-4, random_state=s,
                        init_params="stmc")
        try:
            m.fit(X)
            ll = m.score(X)
        except Exception:
            continue
        if np.isfinite(ll) and ll > best_ll:
            best, best_ll = m, ll
    return best


def label_map(model, scaler_mean, scaler_std):
    """Order states by mean daily return -> 0 Bear, 1 Neutral, 2 Bull."""
    # means_ are in standardized space; f1 (index 0) un-standardized for ranking
    mean_ret = model.means_[:, 0] * scaler_std[0] + scaler_mean[0]
    order = np.argsort(mean_ret)            # ascending: bear..bull
    return {state: rank for rank, state in enumerate(order)}, mean_ret


def emission_loglik(model, X):
    """Per-sample, per-state Gaussian log-likelihood (version-robust)."""
    n, k = X.shape[0], model.n_components
    ll = np.empty((n, k))
    for j in range(k):
        ll[:, j] = multivariate_normal.logpdf(
            X, mean=model.means_[j], cov=model.covars_[j], allow_singular=True)
    return ll


def forward_filter(model, X):
    """
    Causal forward algorithm in log-space.
    Returns filtered posteriors gamma_t = P(state_t | obs_1..t) for every t.
    Uses obs up to and including t only -- no future information.
    """
    log_e = emission_loglik(model, X)
    log_pi = np.log(model.startprob_ + 1e-300)
    log_A = np.log(model.transmat_ + 1e-300)
    n, k = log_e.shape
    log_alpha = np.empty((n, k))
    log_alpha[0] = log_pi + log_e[0]
    log_alpha[0] -= _logsumexp(log_alpha[0])           # normalise (filtered)
    for t in range(1, n):
        prev = log_alpha[t - 1][:, None] + log_A        # (k_prev, k_next)
        log_alpha[t] = _logsumexp(prev, axis=0) + log_e[t]
        log_alpha[t] -= _logsumexp(log_alpha[t])
    return np.exp(log_alpha)


def _logsumexp(a, axis=None):
    m = np.max(a, axis=axis, keepdims=True)
    out = m + np.log(np.sum(np.exp(a - m), axis=axis, keepdims=True))
    return np.squeeze(out, axis=axis) if axis is not None else out.reshape(())


# --------------------------------------------------------------------------- #
# Walk-forward driver
# --------------------------------------------------------------------------- #
def walk_forward(feat):
    feat = feat.copy()
    years = feat["date"].dt.year
    first_year = int(years.iloc[0])
    refit_years = sorted(y for y in years.unique() if y >= first_year + BURN_IN_YEARS)

    cols = [f"p{REGIME_NAMES[i]}" for i in range(N_STATES)]
    filt = pd.DataFrame(index=feat.index, columns=cols, dtype=float)
    feat["regime"] = np.nan
    last_model = last_sm = last_ss = last_lab = last_meanret = None

    for yi, ry in enumerate(refit_years):
        train = feat[feat["date"].dt.year < ry]                 # strictly past
        Xtr = train[["f1", "f2"]].values
        sm, ss = Xtr.mean(0), Xtr.std(0) + 1e-12               # train-only scaler
        model = fit_hmm((Xtr - sm) / ss)
        if model is None:
            continue
        lab, mean_ret = label_map(model, sm, ss)

        # filter over the full available prefix [start .. end of this segment]
        seg_end = feat.index[years == ry].max()
        prefix = feat.loc[:seg_end]
        Xpref = (prefix[["f1", "f2"]].values - sm) / ss
        gamma = forward_filter(model, Xpref)                    # causal

        # remap raw-state columns -> Bear/Neutral/Bull and record this year's days
        remap = np.empty(N_STATES, dtype=int)
        for raw, rank in lab.items():
            remap[rank] = raw
        gamma_named = gamma[:, remap]                           # cols = bear,neu,bull
        seg_mask = (prefix["date"].dt.year == ry).values
        seg_idx = prefix.index[seg_mask]
        filt.loc[seg_idx, cols] = gamma_named[seg_mask]
        feat.loc[seg_idx, "regime"] = np.argmax(gamma_named[seg_mask], axis=1)

        last_model, last_sm, last_ss, last_lab, last_meanret = model, sm, ss, lab, mean_ret

    out = pd.concat([feat, filt], axis=1)
    out = out.dropna(subset=cols).reset_index(drop=True)
    bundle = dict(model=last_model, sm=last_sm, ss=last_ss, lab=last_lab,
                  mean_ret=last_meanret)
    return out, bundle


# --------------------------------------------------------------------------- #
# Evaluation & reporting
# --------------------------------------------------------------------------- #
def evaluate(out):
    out = out.copy()
    out["next_ret"] = out["ret"].shift(-1)            # realised next-day (future)
    ev = out.dropna(subset=["next_ret"])
    rows = []
    for i in range(N_STATES):
        sub = ev[ev["regime"] == i]["next_ret"]
        if len(sub) == 0:
            continue
        rows.append(dict(
            regime=REGIME_NAMES[i], days=len(sub),
            share=len(sub) / len(ev),
            ann_ret=sub.mean() * TRADING_DAYS,
            ann_vol=sub.std() * np.sqrt(TRADING_DAYS),
            daily_mean_bps=sub.mean() * 1e4,
            hit_rate=(sub > 0).mean(),
            sharpe=(sub.mean() / (sub.std() + 1e-12)) * np.sqrt(TRADING_DAYS),
        ))
    return pd.DataFrame(rows)


def regime_profile(out):
    """Annualised trailing drift/vol that defines each regime (transparency)."""
    rows = []
    for i in range(N_STATES):
        s = out[out["regime"] == i]
        rows.append(dict(regime=REGIME_NAMES[i], days=len(s),
                         ann_drift=s["f1"].mean() * TRADING_DAYS,
                         ann_vol=s["f2"].mean() * np.sqrt(TRADING_DAYS)))
    return pd.DataFrame(rows)


def crisis_check(out, dates):
    rows = []
    for d in dates:
        sub = out[out["date"] <= d]
        if len(sub):
            r = sub.iloc[-1]
            rows.append((d, REGIME_NAMES[int(r["regime"])], r["pBear"]))
    return rows


def current_outlook(out, bundle):
    last = out.iloc[-1]
    probs = np.array([last[f"p{REGIME_NAMES[i]}"] for i in range(N_STATES)])
    model, lab, sm, ss = bundle["model"], bundle["lab"], bundle["sm"], bundle["ss"]
    mean_ret = bundle["mean_ret"]

    # transition matrix in NAMED (bear/neu/bull) order
    remap = np.empty(N_STATES, dtype=int)
    for raw, rank in lab.items():
        remap[rank] = raw
    A_named = model.transmat_[np.ix_(remap, remap)]
    mean_ret_named = mean_ret[remap]                       # daily mean return / state

    next_state = probs @ A_named                           # P(regime tomorrow)
    exp_next_day = float(probs @ A_named @ mean_ret_named)  # 1-step-ahead E[ret]
    return dict(last_date=last["date"], last_price=last["price"], probs=probs,
                A=A_named, next_state=next_state, exp_next_day=exp_next_day,
                mean_ret_named=mean_ret_named)


def main():
    df = load_data()
    feat = build_features(df)
    out, bundle = walk_forward(feat)

    out.to_csv("results/regimes.csv", index=False)
    ev = evaluate(out)
    ev.to_csv("results/regime_stats.csv", index=False)
    info = current_outlook(out, bundle)

    span = f"{out['date'].iloc[0].date()} .. {out['date'].iloc[-1].date()}"
    print("=" * 70)
    print("HMM MARKET-REGIME DETECTOR  (walk-forward, causal/filtered)")
    print("=" * 70)
    print(f"Underlying      : S&P 500 (^GSPC) adjusted close")
    print(f"Full history    : {df['date'].iloc[0].date()} .. {df['date'].iloc[-1].date()} "
          f"({len(df)} daily returns)")
    print(f"Observation     : trailing {WINDOW}-day [mean ret, realized vol]")
    print(f"States          : {N_STATES} (Bear / Neutral / Bull)")
    print(f"Out-of-sample   : {span}  ({len(out)} days, refit yearly)")
    print()
    prof = regime_profile(out)
    print("REGIME DEFINITIONS  (annualised trailing 5-day window stats)")
    print("-" * 70)
    with pd.option_context("display.float_format", lambda v: f"{v:,.3f}"):
        print(prof.to_string(index=False))
    print("   -> Bear = turbulent sell-off, Bull = calm uptrend, Neutral = choppy")
    print()
    print("OUT-OF-SAMPLE NEXT-DAY RETURN BY FILTERED REGIME")
    print("-" * 70)
    with pd.option_context("display.float_format", lambda v: f"{v:,.3f}"):
        print(ev.to_string(index=False))
    print()
    print("CRISIS VALIDATION  (regime flagged on/after key dates)")
    print("-" * 70)
    for d, name, pbear in crisis_check(out, ["2008-10-10", "2020-03-16", "2022-06-13"]):
        print(f"   {d}: {name:8s} (P(Bear)={pbear:.2f})")
    print()
    print("RECENT REGIME PATH (last 10 trading days)")
    print("-" * 70)
    tail = out[["date", "price", "pBear", "pNeutral", "pBull"]].tail(10).copy()
    tail["regime"] = [REGIME_NAMES[int(r)] for r in out["regime"].tail(10)]
    tail["date"] = tail["date"].dt.date
    with pd.option_context("display.float_format", lambda v: f"{v:,.3f}"):
        print(tail.to_string(index=False))
    print()

    nm = REGIME_NAMES
    print("=" * 70)
    print(f"WHAT THE MARKET SAYS AFTER THE {info['last_date'].strftime('%A %Y-%m-%d').upper()} CLOSE")
    print("=" * 70)
    print(f"S&P 500 close   : {info['last_price']:,.2f}")
    print("Filtered regime probability (uses data up to & incl. this close):")
    for i in range(N_STATES):
        bar = "#" * int(round(info["probs"][i] * 40))
        print(f"   {nm[i]:8s} {info['probs'][i]*100:5.1f}%  {bar}")
    dom = int(np.argmax(info["probs"]))
    print(f"\nDominant regime : {nm[dom]}  ({info['probs'][dom]*100:.1f}%)")
    print("\nProbability of each regime NEXT trading day (Mon):")
    for i in range(N_STATES):
        print(f"   {nm[i]:8s} {info['next_state'][i]*100:5.1f}%")
    print(f"\nRegime persistence P(stay) : "
          + ", ".join(f"{nm[i]}={info['A'][i,i]*100:.0f}%" for i in range(N_STATES)))
    print(f"\nModel 1-step-ahead expected return:")
    print(f"   next day  : {info['exp_next_day']*1e4:+.1f} bps")
    print(f"   annualized: {info['exp_next_day']*TRADING_DAYS*100:+.1f}%")
    print("=" * 70)
    return out, ev, info, bundle


if __name__ == "__main__":
    main()
