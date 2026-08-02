# SOXX Market Regime Detection & Backtest

Regime-detection suite (bull/bear) on the iShares Semiconductor ETF (SOXX),
converted to daily long/flat strategies and backtested out of sample on
2023-01-01 → today with a strict no-look-ahead protocol.

## Run

```bash
pip install -r requirements.txt
python main.py        # full pipeline: data -> signals -> backtest -> charts
pytest tests/         # CUSUM correctness, look-ahead audits, execution lag
```

All outputs land in `./output/` (metrics.csv, detection_lags.csv,
lookahead_audit.csv, tuning_log.json, six PNG charts, and `analysis.md` —
the written findings). Downloads are cached in `./cache/` (parquet); the
committed cache makes the run reproducible without network access — delete it
to force a re-download.

## Layout

- `data.py` — data acquisition + validation. SOXX daily adjusted OHLCV from
  the Yahoo chart API via plain `requests` (yfinance's curl_cffi transport
  cannot TLS-handshake through this environment's egress proxy), with an
  automatic fallback to Nasdaq's API (split-adjusted prices, dividend
  back-adjusted locally). VIX/VIX3M from CBOE's history CSVs.
  **Note:** Yahoo was hard rate-limited (429) when this repo was built, so the
  committed cache is the Nasdaq set: 2016-08-01 → today (Nasdaq caps history
  at ~10y). The spec's 2005 start was unavailable; see `output/analysis.md` §0.
- `algos.py` — the detectors, each emitting a causal daily 0/1 bull state:
  two-state Gaussian HMM (frozen train params, manual forward filter — never
  smoothed/Viterbi), two-sided CUSUM on vol-normalized returns, Coppock curve
  (monthly + daily variants), adaptive Kalman local-level drift filter, VIX
  term-structure overlay, equal-weight composite (+ contango-gated variant),
  and an annual walk-forward HMM.
- `backtest.py` — 1-bar execution lag, 5 bps/side costs, gross & net metrics,
  drawdown-episode detection, detection-lag and whipsaw analysis.
- `charts.py` — regime shading panels, equity curves, drawdowns, CUSUM
  diagnostic, HMM filtered P(bull), transition-timing exhibit.
- `main.py` — runs everything end to end and prints the metrics table.
- `tests/` — unit tests incl. the §4.5 look-ahead audit (truncated-data
  recompute must match the full-sample run exactly).

Train window: history through 2022-12-31 (all fitting/tuning). Test window:
2023-01-01 → today. Randomness (HMM restarts) is seeded.
