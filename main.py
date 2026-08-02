"""End-to-end pipeline: data -> signals -> backtest -> charts -> analysis.

Run:  python main.py                       # canonical study (train 2005-2022,
                                           # test 2023 -> today) into ./output/
      python main.py --train-start 2022-01-01 --train-end 2026-02-28 \
                     --test-start 2026-03-01 --out output_alt   # a scenario

All fitting/tuning uses [train_start, train_end] only; signals are computed
causally from train_start onward; metrics cover test_start -> last bar.
Downloads are cached in ./cache/.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

import algos
import backtest as bt
import charts
import data

COST_BPS = 5.0
SEED = 42


@dataclass
class Config:
    train_start: str
    train_end: pd.Timestamp
    test_start: str
    out: Path


def build_signals(
    soxx: pd.DataFrame,
    vix_pair: pd.DataFrame | None,
    tuning_log: dict,
    cfg: Config,
) -> tuple[dict[str, pd.Series], dict]:
    """Fit/tune every algorithm on the train window; emit causal signals.

    ``soxx`` is already sliced to start at cfg.train_start, so no filter ever
    sees earlier data. Returns the signal dict and chart diagnostics.
    """
    close = soxx["Close"]
    rets = data.log_returns(close)
    train_rets = rets.loc[:cfg.train_end]
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
    cusum_best, cusum_grid = algos.tune_cusum(rets, cfg.train_end, cost_bps=COST_BPS)
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
        "selection": "max net Sharpe on train window, 20-95% time-in-market band",
    }
    cusum_grid.to_csv(cfg.out / "cusum_train_grid.csv", index=False)

    # 3.3 Coppock — monthly vs daily variant chosen on train
    variant, cop_scores = algos.choose_coppock_variant(
        close, rets, cfg.train_end, COST_BPS
    )
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
    kal_best, kal_grid = algos.tune_kalman(rets, cfg.train_end, cost_bps=COST_BPS)
    sig_kalman = algos.kalman_signal(rets, q=kal_best["q"], mult=kal_best["mult"])
    tuning_log["kalman"] = {
        "chosen": {"Q": kal_best["q"], "mult": kal_best["mult"]},
        "train_sharpe_net": kal_best["sharpe"],
        "grid_Q": sorted(kal_grid["q"].unique().tolist()),
        "grid_mult": sorted(kal_grid["mult"].unique().tolist()),
        "selection": "max net Sharpe on train window, 20-95% time-in-market band",
    }
    kal_grid.to_csv(cfg.out / "kalman_train_grid.csv", index=False)

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

    # 6. Walk-forward HMM (annual expanding refits within the allowed data)
    first_test_year = pd.Timestamp(cfg.test_start).year
    signals["hmm_walkforward"] = algos.fit_hmm_walkforward(
        rets, first_test_year=first_test_year, seed=SEED
    )
    tuning_log["hmm_walkforward"] = {
        "scheme": "refit each Dec-31 on all history from train_start; params "
        "through year Y generate signals for year Y+1",
        "first_test_year": first_test_year,
        "n_restarts": 5,
        "seed": SEED,
    }
    return signals, diag


def lookahead_audit(soxx: pd.DataFrame, tuning_log: dict, cfg: Config) -> pd.DataFrame:
    """§4.5: recompute signals on truncated data; values before the cut must
    match the full-sample run exactly. Cut dates span the test window."""
    close = soxx["Close"]
    rets = data.log_returns(close)
    train_rets = rets.loc[:cfg.train_end]
    hmm_params = algos.fit_hmm(train_rets, n_restarts=3, seed=SEED)
    cus = tuning_log["cusum"]["chosen"]
    kal = tuning_log["kalman"]["chosen"]

    full = {
        "hmm": algos.hmm_signal(rets, hmm_params),
        "cusum": algos.cusum_signal(rets, k=cus["k"], h_up=cus["h"], h_down=cus["h"]),
        "kalman": algos.kalman_signal(rets, q=kal["Q"], mult=kal["mult"]),
    }
    test_idx = rets.loc[cfg.test_start:].index
    cut_dates = [
        str(test_idx[int(frac * (len(test_idx) - 1))].date())
        for frac in (0.25, 0.5, 0.75, 0.9)
    ]
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


def parse_args() -> Config:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--train-start", default="2005-01-01",
                   help="first date of data used anywhere (default 2005-01-01)")
    p.add_argument("--train-end", default="2022-12-31",
                   help="last date usable for fitting/tuning (default 2022-12-31)")
    p.add_argument("--test-start", default="2023-01-01",
                   help="first date of the evaluation window (default 2023-01-01)")
    p.add_argument("--out", default="output", help="output directory (default ./output)")
    a = p.parse_args()
    assert pd.Timestamp(a.train_end) < pd.Timestamp(a.test_start), (
        "train-end must precede test-start"
    )
    return Config(
        train_start=a.train_start,
        train_end=pd.Timestamp(a.train_end),
        test_start=a.test_start,
        out=Path(__file__).resolve().parent / a.out,
    )


def main() -> None:
    cfg = parse_args()
    cfg.out.mkdir(exist_ok=True)
    np.random.seed(SEED)
    tuning_log: dict = {}

    # ------------------------------------------------------------------ data
    soxx = data.load_ohlcv("SOXX", start="2005-01-01").loc[cfg.train_start:]
    vix_pair = data.load_vix_pair()
    close = soxx["Close"]
    rets = data.log_returns(close)
    print(f"[data] window used: {rets.index[0].date()} -> {rets.index[-1].date()}; "
          f"train end {rets.loc[:cfg.train_end].index[-1].date()}; "
          f"test {rets.loc[cfg.test_start:].index[0].date()} -> {rets.index[-1].date()}")

    # --------------------------------------------------------------- signals
    signals, diag = build_signals(soxx, vix_pair, tuning_log, cfg)

    # ----------------------------------------------------------------- audit
    audit = lookahead_audit(soxx, tuning_log, cfg)
    audit.to_csv(cfg.out / "lookahead_audit.csv", index=False)

    # -------------------------------------------------------------- backtest
    metrics, streams = bt.evaluate_strategies(rets, signals, cfg.test_start, COST_BPS)
    metrics.to_csv(cfg.out / "metrics.csv", index=False)

    # ---------------------------------------------------- events & detection
    test_close = close.loc[cfg.test_start:]
    episodes = bt.top_drawdown_episodes(test_close, n=2)
    lags = bt.detection_lags(signals, episodes, rets.index)
    lags.to_csv(cfg.out / "detection_lags.csv", index=False)
    whips = {
        name: bt.whipsaw_count(
            sig.reindex(rets.index).ffill().fillna(0), 10, cfg.test_start
        )
        for name, sig in signals.items()
    }

    # ---------------------------------------------------------------- charts
    charts.regime_panels(
        close, signals, cfg.out / "regimes_by_algorithm.png", cfg.test_start
    )
    charts.equity_curves(streams, cfg.out / "equity_curves_net.png", basis="net")
    charts.drawdown_chart(streams, cfg.out / "drawdowns_net.png", basis="net")
    charts.cusum_diagnostic(
        diag["cusum_paths"], signals["cusum"],
        {"k": diag["cusum_best"]["k"], "h": diag["cusum_best"]["h"]},
        cfg.out / "cusum_diagnostic.png", cfg.test_start,
    )
    charts.hmm_prob_chart(close, diag["p_bull"], cfg.out / "hmm_p_bull.png", cfg.test_start)
    charts.transition_timing_chart(
        close, signals, episodes, lags, cfg.out / "transition_timing.png"
    )

    # ------------------------------------------------------------- provenance
    tuning_log["protocol"] = {
        "train_window": f"{cfg.train_start} .. {cfg.train_end.date()}",
        "test_window": f"{cfg.test_start} .. {rets.index[-1].date()}",
        "execution_lag_bars": 1,
        "cost_bps_per_side": COST_BPS,
        "whipsaw_counts_test": whips,
        "episodes": [
            {k: (str(v.date()) if isinstance(v, pd.Timestamp) else v)
             for k, v in ep.items()} for ep in episodes
        ],
    }
    with open(cfg.out / "tuning_log.json", "w") as f:
        json.dump(tuning_log, f, indent=2, default=str)

    # ----------------------------------------------------------------- print
    show = metrics.copy()
    for c in ("ann_return", "ann_vol", "max_drawdown", "hit_rate", "time_in_market"):
        show[c] = (show[c] * 100).round(1)
    for c in ("sharpe", "sortino", "calmar"):
        show[c] = show[c].round(2)
    print("\n=== Test-window metrics (%, ratios) ===")
    print(show.to_string(index=False))
    print(f"\nOutputs written to {cfg.out}/")
    print("Charts:", sorted(p.name for p in cfg.out.glob("*.png")))


if __name__ == "__main__":
    main()
