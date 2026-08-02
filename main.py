"""End-to-end pipeline: data -> signals -> backtest -> charts -> analysis.

Run:  python main.py
Everything lands in ./output/ ; downloads are cached in ./cache/.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

import algos
import backtest as bt
import charts
import data

OUT = Path(__file__).resolve().parent / "output"
TRAIN_END = pd.Timestamp("2022-12-31")
TEST_START = "2023-01-01"
COST_BPS = 5.0
SEED = 42


def build_signals(
    soxx: pd.DataFrame,
    vix_pair: pd.DataFrame | None,
    tuning_log: dict,
) -> tuple[dict[str, pd.Series], dict]:
    """Fit/tune every algorithm on the train window; emit full-sample signals.

    Returns the signal dict and a dict of diagnostics for charts/analysis.
    """
    close = soxx["Close"]
    rets = data.log_returns(close)
    train_rets = rets.loc[:TRAIN_END]
    diag: dict = {}

    # 3.1 HMM — frozen train-window parameters, manual forward filter
    hmm_params = algos.fit_hmm(train_rets, n_restarts=5, seed=SEED)
    p_bull = algos.hmm_filtered_prob(rets, hmm_params)
    sig_hmm = (p_bull > 0.5).astype(int)
    diag["hmm_params"] = hmm_params
    diag["p_bull"] = p_bull
    tuning_log["hmm"] = {
        "fit_window": f"{train_rets.index[0].date()} .. {train_rets.index[-1].date()}",
        "n_restarts": 5,
        "seed": SEED,
        "log_likelihood": hmm_params.log_likelihood,
        "means_daily": hmm_params.means.tolist(),
        "vols_daily": np.sqrt(hmm_params.variances).tolist(),
        "transmat": hmm_params.transmat.tolist(),
        "bull_state": hmm_params.bull_state,
    }

    # 3.2 CUSUM — (k, h) tuned on train net Sharpe
    cusum_best, cusum_grid = algos.tune_cusum(rets, TRAIN_END, cost_bps=COST_BPS)
    sig_cusum, cusum_paths = algos.cusum_signal(
        rets, k=cusum_best["k"], h_up=cusum_best["h"], h_down=cusum_best["h"],
        return_paths=True,
    )
    diag["cusum_paths"] = cusum_paths
    diag["cusum_best"] = cusum_best
    tuning_log["cusum"] = {
        "chosen": {"k": cusum_best["k"], "h": cusum_best["h"]},
        "train_sharpe_net": cusum_best["sharpe"],
        "grid_k": sorted(cusum_grid["k"].unique().tolist()),
        "grid_h": sorted(cusum_grid["h"].unique().tolist()),
        "selection": "max net Sharpe of long/flat strategy on train window",
    }
    cusum_grid.to_csv(OUT / "cusum_train_grid.csv", index=False)

    # 3.3 Coppock — monthly vs daily variant chosen on train
    variant, cop_scores = algos.choose_coppock_variant(close, rets, TRAIN_END, COST_BPS)
    sig_coppock = (
        algos.coppock_signal_monthly(close)
        if variant == "monthly"
        else algos.coppock_signal_daily(close)
    )
    tuning_log["coppock"] = {
        "variant_chosen": variant,
        "train_sharpe_net": {k: float(v) for k, v in cop_scores.items()},
        "entry": "Coppock turns up while below zero, or crosses above zero",
        "exit": "Coppock turns down (rolls over) while below zero",
    }

    # 3.4 Kalman — Q and multiplier tuned on train
    kal_best, kal_grid = algos.tune_kalman(rets, TRAIN_END, cost_bps=COST_BPS)
    sig_kalman = algos.kalman_signal(rets, q=kal_best["q"], mult=kal_best["mult"])
    tuning_log["kalman"] = {
        "chosen": {"Q": kal_best["q"], "mult": kal_best["mult"]},
        "train_sharpe_net": kal_best["sharpe"],
        "grid_Q": sorted(kal_grid["q"].unique().tolist()),
        "grid_mult": sorted(kal_grid["mult"].unique().tolist()),
        "selection": "max net Sharpe of long/flat strategy on train window",
    }
    kal_grid.to_csv(OUT / "kalman_train_grid.csv", index=False)

    signals: dict[str, pd.Series] = {
        "hmm": sig_hmm,
        "cusum": sig_cusum,
        "coppock": sig_coppock.reindex(rets.index).ffill().fillna(0).astype(int),
        "kalman": sig_kalman,
    }

    # 3.5 VIX term structure (skip gracefully if data missing)
    if vix_pair is not None:
        signals["vix_ts"] = algos.vix_signal(vix_pair, rets.index)
        tuning_log["vix_ts"] = {"rule": "VIX3M/VIX > 1.0 (contango)", "tuned": "nothing"}

    # 3.6 Composite of 3.1–3.4 (+ contango-gated variant)
    core = {k: signals[k] for k in ("hmm", "cusum", "coppock", "kalman")}
    signals["composite"] = algos.composite_signal(core, rets.index)
    if "vix_ts" in signals:
        signals["composite_gated"] = (
            (signals["composite"] == 1) & (signals["vix_ts"] == 1)
        ).astype(int)
    tuning_log["composite"] = {
        "rule": "mean(hmm, cusum, coppock, kalman) >= 0.5",
        "gated_variant": "composite AND VIX3M/VIX > 1",
    }

    # 6. Walk-forward HMM (annual expanding refits)
    signals["hmm_walkforward"] = algos.fit_hmm_walkforward(rets, seed=SEED)
    tuning_log["hmm_walkforward"] = {
        "scheme": "refit each Dec-31 on all history; params through year Y "
        "generate signals for year Y+1",
        "n_restarts": 5,
        "seed": SEED,
    }
    return signals, diag


def lookahead_audit(soxx: pd.DataFrame, tuning_log: dict) -> pd.DataFrame:
    """§4.5: recompute signals on truncated data; values before the cut must
    match the full-sample run exactly. Run for several dates x 3 algorithms."""
    close = soxx["Close"]
    rets = data.log_returns(close)
    train_rets = rets.loc[:TRAIN_END]
    hmm_params = algos.fit_hmm(train_rets, n_restarts=3, seed=SEED)
    cus = tuning_log["cusum"]["chosen"]
    kal = tuning_log["kalman"]["chosen"]

    full = {
        "hmm": algos.hmm_signal(rets, hmm_params),
        "cusum": algos.cusum_signal(rets, k=cus["k"], h_up=cus["h"], h_down=cus["h"]),
        "kalman": algos.kalman_signal(rets, q=kal["Q"], mult=kal["mult"]),
    }
    cut_dates = ["2023-06-30", "2024-03-28", "2024-12-31", "2025-08-29"]
    rows = []
    for d in cut_dates:
        trunc_rets = rets.loc[:d]
        trunc = {
            "hmm": algos.hmm_signal(trunc_rets, hmm_params),
            "cusum": algos.cusum_signal(trunc_rets, k=cus["k"], h_up=cus["h"], h_down=cus["h"]),
            "kalman": algos.kalman_signal(trunc_rets, q=kal["Q"], mult=kal["mult"]),
        }
        for name in full:
            a = full[name].loc[:d]
            b = trunc[name]
            identical = bool(a.equals(b))
            rows.append({"algorithm": name, "truncation_date": d,
                         "n_compared": len(b), "identical": identical})
            assert identical, f"LOOK-AHEAD DETECTED: {name} differs before {d}"
    audit = pd.DataFrame(rows)
    print("[audit] look-ahead audit passed for all truncation dates:")
    print(audit.to_string(index=False))
    return audit


def main() -> None:
    OUT.mkdir(exist_ok=True)
    np.random.seed(SEED)
    tuning_log: dict = {}

    # ------------------------------------------------------------------ data
    soxx = data.load_ohlcv("SOXX", start="2005-01-01")
    vix_pair = data.load_vix_pair()
    close = soxx["Close"]
    rets = data.log_returns(close)
    print(f"[data] train: {rets.loc[:TRAIN_END].index[-1].date()} end; "
          f"test: {rets.loc[TEST_START:].index[0].date()} -> {rets.index[-1].date()}")

    # --------------------------------------------------------------- signals
    signals, diag = build_signals(soxx, vix_pair, tuning_log)

    # ----------------------------------------------------------------- audit
    audit = lookahead_audit(soxx, tuning_log)
    audit.to_csv(OUT / "lookahead_audit.csv", index=False)

    # -------------------------------------------------------------- backtest
    metrics, streams = bt.evaluate_strategies(rets, signals, TEST_START, COST_BPS)
    metrics.to_csv(OUT / "metrics.csv", index=False)

    # ---------------------------------------------------- events & detection
    test_close = close.loc[TEST_START:]
    episodes = bt.top_drawdown_episodes(test_close, n=2)
    lags = bt.detection_lags(signals, episodes, rets.index)
    lags.to_csv(OUT / "detection_lags.csv", index=False)
    whips = {
        name: bt.whipsaw_count(sig.reindex(rets.index).ffill().fillna(0), 10, TEST_START)
        for name, sig in signals.items()
    }

    # ---------------------------------------------------------------- charts
    charts.regime_panels(close, signals, OUT / "regimes_by_algorithm.png", TEST_START)
    charts.equity_curves(streams, OUT / "equity_curves_net.png", basis="net")
    charts.drawdown_chart(streams, OUT / "drawdowns_net.png", basis="net")
    charts.cusum_diagnostic(
        diag["cusum_paths"], signals["cusum"],
        {"k": diag["cusum_best"]["k"], "h": diag["cusum_best"]["h"]},
        OUT / "cusum_diagnostic.png", TEST_START,
    )
    charts.hmm_prob_chart(close, diag["p_bull"], OUT / "hmm_p_bull.png", TEST_START)
    charts.transition_timing_chart(
        close, signals, episodes, lags, OUT / "transition_timing.png"
    )

    # ------------------------------------------------------------- provenance
    tuning_log["protocol"] = {
        "train_window": f"2005 start .. {TRAIN_END.date()}",
        "test_window": f"{TEST_START} .. {rets.index[-1].date()}",
        "execution_lag_bars": 1,
        "cost_bps_per_side": COST_BPS,
        "whipsaw_counts_test": whips,
        "episodes": [
            {k: (str(v.date()) if isinstance(v, pd.Timestamp) else v)
             for k, v in ep.items()} for ep in episodes
        ],
    }
    with open(OUT / "tuning_log.json", "w") as f:
        json.dump(tuning_log, f, indent=2, default=str)

    # ----------------------------------------------------------------- print
    show = metrics.copy()
    for c in ("ann_return", "ann_vol", "max_drawdown", "hit_rate", "time_in_market"):
        show[c] = (show[c] * 100).round(1)
    for c in ("sharpe", "sortino", "calmar"):
        show[c] = show[c].round(2)
    print("\n=== Test-window metrics (%, ratios) ===")
    print(show.to_string(index=False))
    print(f"\nOutputs written to {OUT}/")
    print("Charts:", sorted(p.name for p in OUT.glob("*.png")))


if __name__ == "__main__":
    main()
