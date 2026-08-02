# SOXX Market Regime Detection & Backtest

Regime-detection suite (bull/bear) on the iShares Semiconductor ETF (SOXX),
converted to daily long/flat strategies and backtested out of sample on
2023-01-01 → today with a strict no-look-ahead protocol.

## Run

```bash
pip install -r requirements.txt
python main.py        # full pipeline: data -> signals -> backtest -> charts
pytest tests/         # CUSUM correctness, look-ahead audits, execution lag

# alternative windows (all fitting/tuning stays inside [train-start, train-end]):
python main.py --train-start 2022-01-01 --train-end 2026-02-28 \
               --test-start 2026-03-01 --out output_test2026
```

All outputs land in `./output/` (metrics.csv, detection_lags.csv,
lookahead_audit.csv, tuning_log.json, six PNG charts, and `analysis.md` —
the written findings). Downloads are cached in `./cache/` (parquet); the
committed cache makes the run reproducible without network access — delete it
to force a re-download.

## Layout

- `data.py` — data acquisition + validation. SOXX daily adjusted OHLCV via
  yfinance (`auto_adjust=True`), full 2005 → today history. Behind a
  TLS-intercepting egress proxy, yfinance's default curl_cffi transport
  (modern-Chrome TLS fingerprint with ECH/post-quantum extensions) gets its
  handshake reset, and non-browser fingerprints get 429'd by Yahoo — so the
  loader hands yfinance a curl_cffi session impersonating an older browser
  (`chrome116` first), which passes both. Falls back to Nasdaq's API
  (split-adjusted, ~10y cap, dividends back-adjusted locally) if Yahoo
  fails entirely. VIX/VIX3M from CBOE's history CSVs.
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

Default windows: train = history through 2022-12-31 (all fitting/tuning),
test = 2023-01-01 → today. Randomness (HMM restarts) is seeded.

`output_test2026/` holds a requested scenario run — train 2022-01 →
2026-02, test 2026-03 → today — with its own `analysis.md`.
