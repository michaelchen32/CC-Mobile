# Breakout-algorithm study

Algorithms: Donchian/Turtle (20), Darvas box, Bollinger squeeze, TTM squeeze, volume-confirmed resistance, 52-week-high momentum.

Two views per signal (entry = signal-bar close, 20 trading-day horizon):

1. **Tradeable outcome** — `true` = +8% target hit before −5% stop; `false` = stop first; `timeout_up/down` = neither. `stop_whipsaw_%` = (false + timeout_down) / signals.
2. **Identification quality** (path-independent) — `confirmed` = price later ran ≥ +8%; `fakeout` = never made ≥ +4% upside or rolled over past −5%; `marginal` = in between. `fakeout_%` is the true false-positive rate for *breakout detection* (a tight stop can whipsaw a real breakout, which inflates view 1's false count).


## GOOG (2025 study)


### GOOG  (2021-04-01 → 2026-05-15)

_signals in study window 2025-01-01 → 2025-12-31:_


| algorithm | entry_date | entry_price | outcome | breakout_class | days_to_resolve | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| donchian_20 | 2025-01-31 | 204.66 | false | fakeout | 3 | -18.0 | 1.5 | -18.5 |
| donchian_20 | 2025-06-10 | 179.61 | false | fakeout | 7 | -0.7 | 1.0 | -9.3 |
| donchian_20 | 2025-07-14 | 182.4 | true | confirmed | 8 | 10.3 | 11.3 | -0.7 |
| donchian_20 | 2025-08-08 | 201.64 | true | confirmed | 17 | 16.0 | 18.1 | -2.3 |
| donchian_20 | 2025-08-28 | 211.89 | true | confirmed | 3 | 16.5 | 21.0 | -2.5 |
| donchian_20 | 2025-09-15 | 251.42 | false | fakeout | 19 | -2.8 | 2.0 | -6.0 |
| donchian_20 | 2025-10-24 | 260.16 | true | confirmed | 4 | 15.0 | 17.8 | 1.7 |
| donchian_20 | 2025-11-24 | 318.04 | false | fakeout | 16 | -0.8 | 3.2 | -6.5 |
| darvas_box | 2025-01-31 | 204.66 | false | fakeout | 3 | -18.0 | 1.5 | -18.5 |
| darvas_box | 2025-06-10 | 179.61 | false | fakeout | 7 | -0.7 | 1.0 | -9.3 |
| darvas_box | 2025-07-14 | 182.4 | true | confirmed | 8 | 10.3 | 11.3 | -0.7 |
| darvas_box | 2025-08-08 | 201.64 | true | confirmed | 17 | 16.0 | 18.1 | -2.3 |
| darvas_box | 2025-08-25 | 208.69 | true | confirmed | 6 | 20.8 | 22.8 | -1.3 |
| darvas_box | 2025-10-20 | 256.67 | true | confirmed | 8 | 11.1 | 14.6 | -4.8 |
| darvas_box | 2025-11-19 | 292.59 | true | confirmed | 3 | 3.7 | 12.2 | -1.3 |
| bollinger_squeeze | 2025-01-31 | 204.66 | false | fakeout | 3 | -18.0 | 1.5 | -18.5 |
| bollinger_squeeze | 2025-07-21 | 190.72 | true | confirmed | 19 | 6.9 | 8.5 | -1.4 |
| bollinger_squeeze | 2025-09-03 | 230.58 | true | confirmed | 8 | 6.3 | 11.2 | -1.9 |
| bollinger_squeeze | 2025-10-20 | 256.67 | true | confirmed | 8 | 11.1 | 14.6 | -4.8 |
| bollinger_squeeze | 2025-11-21 | 299.24 | true | confirmed | 2 | 4.0 | 9.7 | -0.7 |
| ttm_squeeze | 2025-01-23 | 198.67 | false | fakeout | 11 | -9.0 | 4.6 | -9.2 |
| ttm_squeeze | 2025-10-23 | 253.39 | true | confirmed | 4 | 14.3 | 21.0 | 0.9 |
| volume_resistance | 2025-02-04 | 206.76 | false | fakeout | 1 | -15.8 | -6.3 | -19.3 |
| volume_resistance | 2025-07-24 | 192.77 | timeout_up | marginal | 20 | 3.8 | 7.3 | -2.3 |
| volume_resistance | 2025-09-02 | 211.51 | true | confirmed | 1 | 15.0 | 21.2 | 6.2 |
| volume_resistance | 2025-09-19 | 254.89 | false | fakeout | 4 | -0.6 | 0.9 | -7.3 |
| volume_resistance | 2025-10-30 | 281.52 | true | confirmed | 15 | 13.6 | 16.6 | -3.7 |
| volume_resistance | 2025-11-17 | 285.21 | true | confirmed | 5 | 7.8 | 15.1 | -2.3 |
| high_52w_momentum | 2025-01-21 | 198.72 | false | fakeout | 13 | -6.3 | 4.5 | -8.0 |
| high_52w_momentum | 2025-08-25 | 208.69 | true | confirmed | 6 | 20.8 | 22.8 | -1.3 |
| high_52w_momentum | 2025-09-11 | 240.45 | timeout_up | marginal | 20 | 0.6 | 6.6 | -0.9 |
| high_52w_momentum | 2025-10-20 | 256.67 | true | confirmed | 8 | 11.1 | 14.6 | -4.8 |
| high_52w_momentum | 2025-11-05 | 284.36 | true | confirmed | 13 | 11.8 | 15.4 | -4.7 |
| high_52w_momentum | 2025-11-21 | 299.24 | true | confirmed | 2 | 4.0 | 9.7 | -0.7 |


**GOOG (2025 study) — summary across all signals (full history):**


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 20 | 8 | 7 | 3 | 2 | 1.12 | 8 | 7 | 40.0 | 45.0 | 40.0 | 35.0 |
| darvas_box | 27 | 8 | 11 | 6 | 2 | 1.66 | 8 | 13 | 29.6 | 48.1 | 29.6 | 48.1 |
| donchian_20 | 42 | 13 | 20 | 6 | 3 | 1.25 | 13 | 22 | 31.0 | 54.8 | 31.0 | 52.4 |
| high_52w_momentum | 25 | 6 | 10 | 6 | 3 | 1.92 | 7 | 10 | 24.0 | 52.0 | 28.0 | 40.0 |
| ttm_squeeze | 8 | 2 | 5 | 0 | 1 | -2.29 | 2 | 4 | 25.0 | 75.0 | 25.0 | 50.0 |
| volume_resistance | 20 | 6 | 10 | 4 | 0 | 0.8 | 6 | 9 | 30.0 | 50.0 | 30.0 | 45.0 |


## Memory (late-25/early-26 study)


### MU  (2021-04-01 → 2026-05-15)

_signals in study window 2025-09-01 → 2026-05-18:_


| algorithm | entry_date | entry_price | outcome | breakout_class | days_to_resolve | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| donchian_20 | 2025-09-05 | 131.18 | true | confirmed | 3 | 43.1 | 46.1 | -2.3 |
| donchian_20 | 2025-10-01 | 181.89 | true | confirmed | 3 | 24.5 | 27.7 | -1.3 |
| donchian_20 | 2025-10-16 | 202.36 | false | confirmed | 4 | 17.0 | 26.9 | -5.0 |
| donchian_20 | 2025-11-03 | 234.51 | false | confirmed | 1 | 2.0 | 11.0 | -17.9 |
| donchian_20 | 2025-12-10 | 263.49 | false | confirmed | 2 | 30.9 | 31.4 | -15.9 |
| donchian_20 | 2025-12-29 | 294.25 | true | confirmed | 4 | 47.9 | 49.1 | -3.5 |
| donchian_20 | 2026-01-16 | 362.6 | true | confirmed | 2 | 10.2 | 25.6 | -0.4 |
| donchian_20 | 2026-03-16 | 441.61 | false | marginal | 4 | 5.4 | 6.7 | -29.5 |
| donchian_20 | 2026-04-22 | 487.48 | true | confirmed | 3 | 48.7 | 67.9 | -3.2 |
| donchian_20 | 2026-05-08 | 746.81 | true | confirmed | 1 | -3.0 | 9.6 | -5.4 |
| darvas_box | 2025-09-05 | 131.18 | true | confirmed | 3 | 43.1 | 46.1 | -2.3 |
| darvas_box | 2025-10-01 | 181.89 | true | confirmed | 3 | 24.5 | 27.7 | -1.3 |
| darvas_box | 2025-10-16 | 202.36 | false | confirmed | 4 | 17.0 | 26.9 | -5.0 |
| darvas_box | 2025-12-10 | 263.49 | false | confirmed | 2 | 30.9 | 31.4 | -15.9 |
| darvas_box | 2026-03-17 | 461.5 | false | fakeout | 2 | -1.1 | 2.1 | -32.5 |
| darvas_box | 2026-04-22 | 487.48 | true | confirmed | 3 | 48.7 | 67.9 | -3.2 |
| bollinger_squeeze | 2025-09-05 | 131.18 | true | confirmed | 3 | 43.1 | 46.1 | -2.3 |
| bollinger_squeeze | 2026-03-17 | 461.5 | false | fakeout | 2 | -1.1 | 2.1 | -32.5 |
| ttm_squeeze | 2026-03-12 | 405.18 | true | confirmed | 2 | 3.8 | 16.3 | -23.1 |
| volume_resistance | 2025-09-05 | 131.18 | true | confirmed | 3 | 43.1 | 46.1 | -2.3 |
| volume_resistance | 2025-09-23 | 166.17 | false | confirmed | 2 | 21.6 | 29.1 | -7.1 |
| volume_resistance | 2025-11-14 | 246.63 | false | marginal | 2 | -3.8 | 7.3 | -22.0 |
| volume_resistance | 2025-12-19 | 265.7 | true | confirmed | 3 | 46.4 | 48.3 | 0.9 |
| volume_resistance | 2026-01-20 | 364.85 | true | confirmed | 1 | 15.3 | 24.8 | -0.3 |
| volume_resistance | 2026-02-04 | 379.24 | true | confirmed | 5 | 4.7 | 15.6 | -3.5 |
| volume_resistance | 2026-03-18 | 461.54 | false | fakeout | 1 | -0.9 | 0.9 | -32.5 |
| volume_resistance | 2026-05-05 | 640.2 | true | confirmed | 3 | 13.2 | 27.9 | -2.0 |
| high_52w_momentum | 2025-09-05 | 131.18 | true | confirmed | 3 | 43.1 | 46.1 | -2.3 |
| high_52w_momentum | 2025-10-01 | 181.89 | true | confirmed | 3 | 24.5 | 27.7 | -1.3 |
| high_52w_momentum | 2025-10-16 | 202.36 | false | confirmed | 4 | 17.0 | 26.9 | -5.0 |
| high_52w_momentum | 2025-11-03 | 234.51 | false | confirmed | 1 | 2.0 | 11.0 | -17.9 |
| high_52w_momentum | 2025-12-10 | 263.49 | false | confirmed | 2 | 30.9 | 31.4 | -15.9 |
| high_52w_momentum | 2025-12-29 | 294.25 | true | confirmed | 4 | 47.9 | 49.1 | -3.5 |
| high_52w_momentum | 2026-01-16 | 362.6 | true | confirmed | 2 | 10.2 | 25.6 | -0.4 |
| high_52w_momentum | 2026-03-16 | 441.61 | false | marginal | 4 | 5.4 | 6.7 | -29.5 |
| high_52w_momentum | 2026-04-22 | 487.48 | true | confirmed | 3 | 48.7 | 67.9 | -3.2 |
| high_52w_momentum | 2026-05-08 | 746.81 | true | confirmed | 1 | -3.0 | 9.6 | -5.4 |


### WDC  (2021-04-01 → 2026-05-15)

_signals in study window 2025-09-01 → 2026-05-18:_


| algorithm | entry_date | entry_price | outcome | breakout_class | days_to_resolve | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| donchian_20 | 2025-09-15 | 102.26 | true | confirmed | 5 | 16.1 | 34.2 | -2.6 |
| donchian_20 | 2025-09-30 | 119.91 | true | confirmed | 1 | 4.0 | 14.4 | -6.3 |
| donchian_20 | 2025-10-29 | 141.2 | true | confirmed | 2 | 11.6 | 26.2 | -6.3 |
| donchian_20 | 2025-12-10 | 181.86 | false | confirmed | 2 | 10.2 | 21.6 | -9.1 |
| donchian_20 | 2026-01-06 | 219.28 | false | confirmed | 1 | 22.8 | 35.2 | -17.6 |
| donchian_20 | 2026-01-27 | 252.54 | true | confirmed | 1 | 15.2 | 22.7 | -6.0 |
| donchian_20 | 2026-03-17 | 313.81 | false | confirmed | 2 | 16.3 | 16.7 | -20.6 |
| donchian_20 | 2026-04-08 | 338.78 | true | confirmed | 4 | 42.6 | 42.8 | -2.7 |
| donchian_20 | 2026-04-23 | 403.12 | false | confirmed | 3 | 19.6 | 30.3 | -7.2 |
| donchian_20 | 2026-05-11 | 515.83 | false | fakeout | 1 | -6.6 | -1.4 | -9.9 |
| darvas_box | 2025-10-29 | 141.2 | true | confirmed | 2 | 11.6 | 26.2 | -6.3 |
| darvas_box | 2025-12-10 | 181.86 | false | confirmed | 2 | 10.2 | 21.6 | -9.1 |
| darvas_box | 2026-01-06 | 219.28 | false | confirmed | 1 | 22.8 | 35.2 | -17.6 |
| darvas_box | 2026-02-18 | 296.42 | false | marginal | 1 | 2.9 | 7.8 | -19.7 |
| darvas_box | 2026-03-17 | 313.81 | false | confirmed | 2 | 16.3 | 16.7 | -20.6 |
| darvas_box | 2026-04-08 | 338.78 | true | confirmed | 4 | 42.6 | 42.8 | -2.7 |
| bollinger_squeeze | 2025-10-29 | 141.2 | true | confirmed | 2 | 11.6 | 26.2 | -6.3 |
| bollinger_squeeze | 2026-01-06 | 219.28 | false | confirmed | 1 | 22.8 | 35.2 | -17.6 |
| bollinger_squeeze | 2026-03-17 | 313.81 | false | confirmed | 2 | 16.3 | 16.7 | -20.6 |
| ttm_squeeze | 2026-01-06 | 219.28 | false | confirmed | 1 | 22.8 | 35.2 | -17.6 |
| volume_resistance | 2025-09-03 | 85.79 | true | confirmed | 2 | 52.0 | 52.6 | 0.0 |
| volume_resistance | 2025-10-01 | 130.42 | false | confirmed | 4 | 8.3 | 11.6 | -13.8 |
| volume_resistance | 2025-10-29 | 141.2 | true | confirmed | 2 | 11.6 | 26.2 | -6.3 |
| volume_resistance | 2025-12-19 | 180.99 | false | confirmed | 1 | 33.6 | 35.2 | -5.4 |
| volume_resistance | 2026-01-07 | 199.78 | false | confirmed | 1 | 30.2 | 48.3 | -9.6 |
| volume_resistance | 2026-01-28 | 279.57 | false | confirmed | 2 | 0.9 | 10.8 | -15.1 |
| volume_resistance | 2026-03-17 | 313.81 | false | confirmed | 2 | 16.3 | 16.7 | -20.6 |
| volume_resistance | 2026-04-30 | 434.52 | false | confirmed | 1 | 10.9 | 20.9 | -7.0 |
| high_52w_momentum | 2025-09-10 | 94.9 | true | confirmed | 3 | 27.5 | 44.6 | -0.6 |
| high_52w_momentum | 2025-09-29 | 116.59 | true | confirmed | 2 | 8.5 | 17.7 | -3.6 |
| high_52w_momentum | 2025-10-29 | 141.2 | true | confirmed | 2 | 11.6 | 26.2 | -6.3 |
| high_52w_momentum | 2025-12-10 | 181.86 | false | confirmed | 2 | 10.2 | 21.6 | -9.1 |
| high_52w_momentum | 2026-01-02 | 187.61 | true | confirmed | 2 | 44.0 | 52.1 | -3.7 |
| high_52w_momentum | 2026-01-20 | 222.86 | true | confirmed | 1 | 33.0 | 39.0 | 1.4 |
| high_52w_momentum | 2026-02-18 | 296.42 | false | marginal | 1 | 2.9 | 7.8 | -19.7 |
| high_52w_momentum | 2026-03-17 | 313.81 | false | confirmed | 2 | 16.3 | 16.7 | -20.6 |
| high_52w_momentum | 2026-04-08 | 338.78 | true | confirmed | 4 | 42.6 | 42.8 | -2.7 |
| high_52w_momentum | 2026-04-23 | 403.12 | false | confirmed | 3 | 19.6 | 30.3 | -7.2 |
| high_52w_momentum | 2026-05-11 | 515.83 | false | fakeout | 1 | -6.6 | -1.4 | -9.9 |


### STX  (2021-04-01 → 2026-05-15)

_signals in study window 2025-09-01 → 2026-05-18:_


| algorithm | entry_date | entry_price | outcome | breakout_class | days_to_resolve | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| donchian_20 | 2025-09-03 | 175.0 | true | confirmed | 3 | 46.1 | 47.0 | -0.3 |
| donchian_20 | 2025-09-18 | 215.02 | true | confirmed | 7 | 4.7 | 22.6 | -2.5 |
| donchian_20 | 2025-10-29 | 264.46 | false | confirmed | 2 | 2.5 | 12.1 | -13.9 |
| donchian_20 | 2025-12-10 | 297.62 | false | confirmed | 2 | 2.0 | 11.4 | -8.1 |
| donchian_20 | 2026-01-06 | 329.84 | false | confirmed | 1 | 26.7 | 39.0 | -15.8 |
| donchian_20 | 2026-01-26 | 357.67 | true | confirmed | 2 | 10.5 | 28.3 | 0.8 |
| donchian_20 | 2026-03-19 | 433.84 | false | confirmed | 1 | 26.3 | 27.6 | -19.0 |
| donchian_20 | 2026-04-06 | 453.3 | true | confirmed | 2 | 62.9 | 65.2 | -1.8 |
| donchian_20 | 2026-04-21 | 559.9 | true | confirmed | 2 | 42.1 | 50.3 | -1.2 |
| donchian_20 | 2026-05-11 | 834.01 | false | fakeout | 1 | -4.6 | 0.6 | -8.2 |
| darvas_box | 2025-10-29 | 264.46 | false | confirmed | 2 | 2.5 | 12.1 | -13.9 |
| darvas_box | 2025-12-10 | 297.62 | false | confirmed | 2 | 2.0 | 11.4 | -8.1 |
| darvas_box | 2026-01-06 | 329.84 | false | confirmed | 1 | 26.7 | 39.0 | -15.8 |
| darvas_box | 2026-04-07 | 468.72 | true | confirmed | 1 | 64.5 | 69.0 | 4.0 |
| bollinger_squeeze | 2026-01-06 | 329.84 | false | confirmed | 1 | 26.7 | 39.0 | -15.8 |
| bollinger_squeeze | 2026-04-06 | 453.3 | true | confirmed | 2 | 62.9 | 65.2 | -1.8 |
| ttm_squeeze | 2026-01-06 | 329.84 | false | confirmed | 1 | 26.7 | 39.0 | -15.8 |
| volume_resistance | 2025-09-04 | 182.6 | true | confirmed | 5 | 38.9 | 44.4 | -0.5 |
| volume_resistance | 2025-10-01 | 255.72 | false | marginal | 3 | 3.4 | 4.7 | -18.6 |
| volume_resistance | 2025-11-05 | 274.57 | true | confirmed | 5 | -3.7 | 8.0 | -17.1 |
| volume_resistance | 2026-01-26 | 357.67 | true | confirmed | 2 | 10.5 | 28.3 | 0.8 |
| volume_resistance | 2026-04-28 | 579.03 | true | confirmed | 1 | 37.4 | 45.3 | 9.1 |
| high_52w_momentum | 2025-09-03 | 175.0 | true | confirmed | 3 | 46.1 | 47.0 | -0.3 |
| high_52w_momentum | 2025-09-18 | 215.02 | true | confirmed | 7 | 4.7 | 22.6 | -2.5 |
| high_52w_momentum | 2025-10-29 | 264.46 | false | confirmed | 2 | 2.5 | 12.1 | -13.9 |
| high_52w_momentum | 2025-12-10 | 297.62 | false | confirmed | 2 | 2.0 | 11.4 | -8.1 |
| high_52w_momentum | 2026-01-06 | 329.84 | false | confirmed | 1 | 26.7 | 39.0 | -15.8 |
| high_52w_momentum | 2026-01-22 | 345.93 | true | confirmed | 3 | 18.6 | 32.7 | -4.3 |
| high_52w_momentum | 2026-04-09 | 500.77 | true | confirmed | 6 | 53.1 | 58.2 | -1.2 |
| high_52w_momentum | 2026-04-27 | 595.86 | false | confirmed | 1 | 33.5 | 41.2 | -7.2 |


### SNDK  (2025-02-13 → 2026-05-15)

_signals in study window 2025-09-01 → 2026-05-18:_


| algorithm | entry_date | entry_price | outcome | breakout_class | days_to_resolve | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| donchian_20 | 2025-09-15 | 90.09 | true | confirmed | 3 | 49.4 | 52.1 | -0.6 |
| donchian_20 | 2025-10-01 | 121.12 | true | confirmed | 1 | 68.7 | 69.8 | -4.5 |
| donchian_20 | 2025-10-23 | 167.05 | true | confirmed | 1 | 17.3 | 70.5 | -1.5 |
| donchian_20 | 2025-11-07 | 239.48 | true | confirmed | 1 | -5.9 | 18.9 | -23.6 |
| donchian_20 | 2026-01-02 | 275.24 | true | confirmed | 2 | 141.7 | 145.9 | -3.2 |
| donchian_20 | 2026-01-20 | 453.12 | true | confirmed | 1 | 32.5 | 60.0 | -1.0 |
| donchian_20 | 2026-03-16 | 703.63 | true | confirmed | 2 | 34.2 | 37.1 | -20.6 |
| donchian_20 | 2026-04-08 | 780.9 | true | confirmed | 1 | 80.6 | 84.4 | 3.1 |
| donchian_20 | 2026-04-24 | 989.9 | true | confirmed | 1 | 42.2 | 61.6 | -1.0 |
| darvas_box | 2025-10-15 | 144.3 | false | confirmed | 2 | 96.2 | 97.3 | -5.6 |
| darvas_box | 2026-01-06 | 349.63 | false | confirmed | 1 | 67.2 | 107.4 | -11.1 |
| darvas_box | 2026-03-18 | 753.69 | false | confirmed | 1 | 22.0 | 28.0 | -25.9 |
| darvas_box | 2026-04-08 | 780.9 | true | confirmed | 1 | 80.6 | 84.4 | 3.1 |
| bollinger_squeeze | 2026-01-02 | 275.24 | true | confirmed | 2 | 141.7 | 145.9 | -3.2 |
| bollinger_squeeze | 2026-03-16 | 703.63 | true | confirmed | 2 | 34.2 | 37.1 | -20.6 |
| bollinger_squeeze | 2026-04-09 | 851.57 | true | confirmed | 2 | 57.4 | 69.1 | -1.9 |
| ttm_squeeze | 2025-12-23 | 244.9 | true | confirmed | 6 | 93.5 | 108.0 | -3.9 |
| volume_resistance | 2025-09-17 | 93.97 | true | confirmed | 1 | 53.6 | 53.8 | -0.5 |
| volume_resistance | 2026-01-06 | 349.63 | false | confirmed | 1 | 67.2 | 107.4 | -11.1 |
| volume_resistance | 2026-01-22 | 503.44 | false | confirmed | 1 | 29.1 | 44.0 | -9.8 |
| volume_resistance | 2026-05-01 | 1187.0 | true | confirmed | 2 | 18.6 | 34.8 | 1.5 |
| high_52w_momentum | 2026-03-16 | 703.63 | true | confirmed | 2 | 34.2 | 37.1 | -20.6 |
| high_52w_momentum | 2026-04-08 | 780.9 | true | confirmed | 1 | 80.6 | 84.4 | 3.1 |
| high_52w_momentum | 2026-04-24 | 989.9 | true | confirmed | 1 | 42.2 | 61.6 | -1.0 |


**Memory (late-25/early-26 study) — summary across all signals (full history):**


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 71 | 31 | 35 | 5 | 0 | 10.6 | 40 | 17 | 43.7 | 49.3 | 56.3 | 23.9 |
| darvas_box | 52 | 26 | 24 | 2 | 0 | 17.32 | 39 | 6 | 50.0 | 46.2 | 75.0 | 11.5 |
| donchian_20 | 138 | 74 | 60 | 2 | 2 | 10.64 | 90 | 31 | 53.6 | 44.9 | 65.2 | 22.5 |
| high_52w_momentum | 70 | 37 | 31 | 1 | 1 | 14.13 | 50 | 11 | 52.9 | 45.7 | 71.4 | 15.7 |
| ttm_squeeze | 27 | 10 | 16 | 1 | 0 | 3.37 | 13 | 10 | 37.0 | 59.3 | 48.1 | 37.0 |
| volume_resistance | 60 | 29 | 28 | 2 | 1 | 12.74 | 40 | 12 | 48.3 | 48.3 | 66.7 | 20.0 |


## Optics (late-25/early-26 study)


### COHR  (2021-04-01 → 2026-05-15)

_signals in study window 2025-09-01 → 2026-05-18:_


| algorithm | entry_date | entry_price | outcome | breakout_class | days_to_resolve | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| donchian_20 | 2025-09-19 | 109.11 | false | confirmed | 4 | 6.6 | 12.7 | -6.4 |
| donchian_20 | 2025-10-09 | 122.35 | false | confirmed | 1 | 30.2 | 32.8 | -11.6 |
| donchian_20 | 2025-10-24 | 129.34 | true | confirmed | 3 | 7.9 | 30.3 | -4.3 |
| donchian_20 | 2025-11-10 | 166.72 | false | confirmed | 1 | 15.6 | 17.0 | -21.8 |
| donchian_20 | 2025-12-04 | 177.35 | true | confirmed | 3 | 5.1 | 12.9 | -4.1 |
| donchian_20 | 2026-01-27 | 214.0 | true | confirmed | 3 | 25.2 | 29.2 | -18.1 |
| donchian_20 | 2026-02-20 | 248.18 | true | confirmed | 3 | 2.2 | 21.0 | -7.3 |
| donchian_20 | 2026-04-08 | 281.79 | true | confirmed | 2 | 22.3 | 29.5 | -2.2 |
| donchian_20 | 2026-05-11 | 379.69 | false | confirmed | 1 | 0.7 | 8.8 | -8.1 |
| darvas_box | 2025-10-24 | 129.34 | true | confirmed | 3 | 7.9 | 30.3 | -4.3 |
| darvas_box | 2025-12-03 | 170.96 | true | confirmed | 1 | 13.7 | 17.1 | -0.9 |
| darvas_box | 2026-01-21 | 201.46 | false | confirmed | 2 | 15.4 | 22.7 | -13.0 |
| darvas_box | 2026-02-20 | 248.18 | true | confirmed | 3 | 2.2 | 21.0 | -7.3 |
| darvas_box | 2026-04-10 | 307.5 | true | confirmed | 5 | 9.0 | 18.6 | -5.4 |
| darvas_box | 2026-05-11 | 379.69 | false | confirmed | 1 | 0.7 | 8.8 | -8.1 |
| bollinger_squeeze | 2025-10-09 | 122.35 | false | confirmed | 1 | 30.2 | 32.8 | -11.6 |
| bollinger_squeeze | 2025-10-24 | 129.34 | true | confirmed | 3 | 7.9 | 30.3 | -4.3 |
| bollinger_squeeze | 2026-01-27 | 214.0 | true | confirmed | 3 | 25.2 | 29.2 | -18.1 |
| bollinger_squeeze | 2026-02-20 | 248.18 | true | confirmed | 3 | 2.2 | 21.0 | -7.3 |
| bollinger_squeeze | 2026-04-08 | 281.79 | true | confirmed | 2 | 22.3 | 29.5 | -2.2 |
| bollinger_squeeze | 2026-05-11 | 379.69 | false | confirmed | 1 | 0.7 | 8.8 | -8.1 |
| ttm_squeeze | 2025-10-21 | 120.79 | false | confirmed | 1 | 14.4 | 39.6 | -6.5 |
| ttm_squeeze | 2026-01-13 | 190.03 | true | confirmed | 2 | 17.7 | 30.1 | -7.8 |
| ttm_squeeze | 2026-02-25 | 267.9 | false | confirmed | 1 | 1.5 | 12.1 | -14.1 |
| ttm_squeeze | 2026-04-09 | 284.17 | true | confirmed | 1 | 12.3 | 28.4 | -3.0 |
| volume_resistance | 2025-10-24 | 129.34 | true | confirmed | 3 | 7.9 | 30.3 | -4.3 |
| volume_resistance | 2025-11-10 | 166.72 | false | confirmed | 1 | 15.6 | 17.0 | -21.8 |
| volume_resistance | 2025-12-12 | 178.34 | true | confirmed | 6 | 6.6 | 12.2 | -6.1 |
| volume_resistance | 2026-01-21 | 201.46 | false | confirmed | 2 | 15.4 | 22.7 | -13.0 |
| volume_resistance | 2026-02-05 | 209.24 | true | confirmed | 1 | 12.7 | 43.5 | -2.2 |
| volume_resistance | 2026-02-27 | 258.93 | true | confirmed | 1 | -6.0 | 15.9 | -11.1 |
| volume_resistance | 2026-05-06 | 344.67 | false | confirmed | 1 | 11.0 | 19.8 | -10.6 |
| high_52w_momentum | 2025-10-08 | 116.67 | false | confirmed | 4 | 15.4 | 21.2 | -7.3 |
| high_52w_momentum | 2025-10-24 | 129.34 | true | confirmed | 3 | 7.9 | 30.3 | -4.3 |
| high_52w_momentum | 2025-11-10 | 166.72 | false | confirmed | 1 | 15.6 | 17.0 | -21.8 |
| high_52w_momentum | 2025-12-03 | 170.96 | true | confirmed | 1 | 13.7 | 17.1 | -0.9 |
| high_52w_momentum | 2026-01-21 | 201.46 | false | confirmed | 2 | 15.4 | 22.7 | -13.0 |
| high_52w_momentum | 2026-02-09 | 242.46 | false | confirmed | 1 | 7.5 | 23.8 | -15.6 |
| high_52w_momentum | 2026-02-25 | 267.9 | false | confirmed | 1 | 1.5 | 12.1 | -14.1 |
| high_52w_momentum | 2026-04-10 | 307.5 | true | confirmed | 5 | 9.0 | 18.6 | -5.4 |
| high_52w_momentum | 2026-05-11 | 379.69 | false | confirmed | 1 | 0.7 | 8.8 | -8.1 |


### LITE  (2021-04-01 → 2026-05-15)

_signals in study window 2025-09-01 → 2026-05-18:_


| algorithm | entry_date | entry_price | outcome | breakout_class | days_to_resolve | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| donchian_20 | 2025-09-15 | 168.77 | false | marginal | 7 | -4.9 | 5.8 | -14.4 |
| donchian_20 | 2025-10-24 | 179.3 | true | confirmed | 1 | 42.5 | 57.6 | 2.7 |
| donchian_20 | 2025-11-10 | 259.89 | false | confirmed | 3 | 38.6 | 39.5 | -17.1 |
| donchian_20 | 2025-11-26 | 308.28 | false | confirmed | 4 | 26.8 | 30.3 | -6.4 |
| donchian_20 | 2025-12-22 | 389.88 | false | fakeout | 4 | -9.1 | 3.3 | -18.6 |
| donchian_20 | 2026-02-04 | 465.54 | false | confirmed | 1 | 39.8 | 68.4 | -8.7 |
| donchian_20 | 2026-02-20 | 667.77 | true | confirmed | 3 | 5.8 | 17.9 | -17.9 |
| donchian_20 | 2026-03-24 | 801.99 | false | confirmed | 2 | 8.9 | 19.7 | -19.9 |
| donchian_20 | 2026-05-11 | 1053.09 | false | fakeout | 1 | -7.8 | 3.1 | -12.4 |
| darvas_box | 2025-10-24 | 179.3 | true | confirmed | 1 | 42.5 | 57.6 | 2.7 |
| darvas_box | 2025-11-24 | 299.36 | false | confirmed | 1 | 29.4 | 30.7 | -6.8 |
| darvas_box | 2025-12-22 | 389.88 | false | fakeout | 4 | -9.1 | 3.3 | -18.6 |
| darvas_box | 2026-02-02 | 423.42 | true | confirmed | 1 | 64.0 | 85.1 | 0.3 |
| darvas_box | 2026-03-24 | 801.99 | false | confirmed | 2 | 8.9 | 19.7 | -19.9 |
| darvas_box | 2026-05-04 | 976.18 | false | confirmed | 2 | -0.6 | 11.2 | -12.5 |
| bollinger_squeeze | 2025-10-24 | 179.3 | true | confirmed | 1 | 42.5 | 57.6 | 2.7 |
| bollinger_squeeze | 2026-02-02 | 423.42 | true | confirmed | 1 | 64.0 | 85.1 | 0.3 |
| bollinger_squeeze | 2026-05-01 | 949.93 | false | confirmed | 3 | 2.2 | 14.3 | -10.0 |
| ttm_squeeze | 2025-10-27 | 193.8 | true | confirmed | 2 | 54.5 | 54.8 | -5.0 |
| ttm_squeeze | 2026-02-02 | 423.42 | true | confirmed | 1 | 64.0 | 85.1 | 0.3 |
| ttm_squeeze | 2026-05-05 | 994.56 | false | confirmed | 1 | -2.4 | 9.2 | -14.1 |
| volume_resistance | 2025-10-27 | 193.8 | true | confirmed | 2 | 54.5 | 54.8 | -5.0 |
| volume_resistance | 2026-01-05 | 357.05 | false | confirmed | 1 | 21.9 | 30.0 | -11.1 |
| volume_resistance | 2026-02-03 | 435.1 | true | confirmed | 1 | 56.5 | 80.1 | -2.3 |
| volume_resistance | 2026-02-27 | 700.91 | true | confirmed | 1 | 0.3 | 15.4 | -21.8 |
| volume_resistance | 2026-05-11 | 1053.09 | false | fakeout | 1 | -7.8 | 3.1 | -12.4 |
| high_52w_momentum | 2025-09-10 | 164.88 | false | confirmed | 10 | -1.1 | 8.3 | -12.3 |
| high_52w_momentum | 2025-10-24 | 179.3 | true | confirmed | 1 | 42.5 | 57.6 | 2.7 |
| high_52w_momentum | 2025-11-10 | 259.89 | false | confirmed | 3 | 38.6 | 39.5 | -17.1 |
| high_52w_momentum | 2025-11-26 | 308.28 | false | confirmed | 4 | 26.8 | 30.3 | -6.4 |
| high_52w_momentum | 2025-12-22 | 389.88 | false | fakeout | 4 | -9.1 | 3.3 | -18.6 |
| high_52w_momentum | 2026-02-02 | 423.42 | true | confirmed | 1 | 64.0 | 85.1 | 0.3 |
| high_52w_momentum | 2026-02-19 | 635.64 | true | confirmed | 2 | 21.5 | 23.3 | -13.7 |
| high_52w_momentum | 2026-03-24 | 801.99 | false | confirmed | 2 | 8.9 | 19.7 | -19.9 |
| high_52w_momentum | 2026-04-10 | 897.3 | false | confirmed | 1 | 0.7 | 13.8 | -13.0 |
| high_52w_momentum | 2026-04-30 | 902.32 | true | confirmed | 1 | 7.6 | 20.3 | -5.3 |


### FN  (2021-04-01 → 2026-05-15)

_signals in study window 2025-09-01 → 2026-05-18:_


| algorithm | entry_date | entry_price | outcome | breakout_class | days_to_resolve | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| donchian_20 | 2025-09-04 | 362.16 | true | confirmed | 13 | 2.0 | 9.7 | -3.9 |
| donchian_20 | 2025-09-19 | 383.13 | false | confirmed | 4 | 7.0 | 12.8 | -7.5 |
| donchian_20 | 2025-10-15 | 398.34 | true | confirmed | 1 | 12.3 | 25.0 | -3.1 |
| donchian_20 | 2025-11-04 | 459.6 | false | marginal | 3 | -2.7 | 7.7 | -19.3 |
| donchian_20 | 2025-12-08 | 491.03 | true | confirmed | 3 | -4.2 | 8.2 | -13.6 |
| donchian_20 | 2026-02-20 | 546.13 | true | confirmed | 2 | -7.3 | 15.9 | -13.6 |
| donchian_20 | 2026-04-10 | 662.13 | true | confirmed | 7 | -6.2 | 11.0 | -8.2 |
| donchian_20 | 2026-05-14 | 746.47 | false | fakeout | 1 | -3.3 | -1.0 | -7.3 |
| darvas_box | 2025-09-04 | 362.16 | true | confirmed | 13 | 2.0 | 9.7 | -3.9 |
| darvas_box | 2025-09-19 | 383.13 | false | confirmed | 4 | 7.0 | 12.8 | -7.5 |
| darvas_box | 2025-10-15 | 398.34 | true | confirmed | 1 | 12.3 | 25.0 | -3.1 |
| darvas_box | 2025-12-09 | 498.45 | false | fakeout | 3 | -11.1 | 6.6 | -14.8 |
| darvas_box | 2026-02-20 | 546.13 | true | confirmed | 2 | -7.3 | 15.9 | -13.6 |
| darvas_box | 2026-04-10 | 662.13 | true | confirmed | 7 | -6.2 | 11.0 | -8.2 |
| darvas_box | 2026-05-14 | 746.47 | false | fakeout | 1 | -3.3 | -1.0 | -7.3 |
| bollinger_squeeze | 2025-10-15 | 398.34 | true | confirmed | 1 | 12.3 | 25.0 | -3.1 |
| ttm_squeeze | 2025-10-16 | 412.46 | false | confirmed | 4 | -2.4 | 20.7 | -6.4 |
| ttm_squeeze | 2026-02-20 | 546.13 | true | confirmed | 2 | -7.3 | 15.9 | -13.6 |
| volume_resistance | 2025-10-16 | 412.46 | false | confirmed | 4 | -2.4 | 20.7 | -6.4 |
| volume_resistance | 2025-10-31 | 440.57 | true | confirmed | 2 | 2.0 | 13.0 | -15.8 |
| volume_resistance | 2026-04-10 | 662.13 | true | confirmed | 7 | -6.2 | 11.0 | -8.2 |
| volume_resistance | 2026-05-04 | 717.8 | false | marginal | 1 | 0.6 | 4.3 | -15.7 |
| high_52w_momentum | 2025-09-18 | 378.01 | false | confirmed | 5 | 9.1 | 14.3 | -6.2 |
| high_52w_momentum | 2025-10-15 | 398.34 | true | confirmed | 1 | 12.3 | 25.0 | -3.1 |
| high_52w_momentum | 2025-11-04 | 459.6 | false | marginal | 3 | -2.7 | 7.7 | -19.3 |
| high_52w_momentum | 2025-12-08 | 491.03 | true | confirmed | 3 | -4.2 | 8.2 | -13.6 |
| high_52w_momentum | 2026-02-20 | 546.13 | true | confirmed | 2 | -7.3 | 15.9 | -13.6 |
| high_52w_momentum | 2026-04-09 | 618.26 | true | confirmed | 1 | 1.3 | 18.8 | -0.8 |
| high_52w_momentum | 2026-04-24 | 720.19 | false | fakeout | 1 | 0.3 | 4.0 | -16.0 |
| high_52w_momentum | 2026-05-14 | 746.47 | false | fakeout | 1 | -3.3 | -1.0 | -7.3 |


### CIEN  (2021-04-01 → 2026-05-15)

_signals in study window 2025-09-01 → 2026-05-18:_


| algorithm | entry_date | entry_price | outcome | breakout_class | days_to_resolve | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| donchian_20 | 2025-09-04 | 116.92 | true | confirmed | 4 | 30.6 | 31.4 | -2.8 |
| donchian_20 | 2025-09-26 | 141.93 | true | confirmed | 4 | 26.2 | 27.6 | 0.8 |
| donchian_20 | 2025-10-15 | 168.71 | false | confirmed | 5 | 24.2 | 26.9 | -5.4 |
| donchian_20 | 2025-11-05 | 195.81 | true | confirmed | 3 | -0.0 | 9.4 | -14.1 |
| donchian_20 | 2025-12-09 | 214.35 | true | confirmed | 2 | 5.1 | 21.8 | -5.9 |
| donchian_20 | 2026-01-06 | 254.19 | false | confirmed | 2 | -0.3 | 12.5 | -15.0 |
| donchian_20 | 2026-02-03 | 276.52 | false | confirmed | 1 | 24.2 | 32.3 | -13.7 |
| donchian_20 | 2026-02-19 | 318.41 | true | confirmed | 2 | 29.6 | 30.9 | -12.6 |
| donchian_20 | 2026-03-17 | 370.05 | true | confirmed | 1 | 28.6 | 38.8 | -2.3 |
| donchian_20 | 2026-04-02 | 447.76 | false | confirmed | 2 | 19.5 | 22.8 | -5.9 |
| donchian_20 | 2026-05-01 | 535.29 | true | confirmed | 3 | 3.6 | 11.9 | -3.7 |
| darvas_box | 2025-09-04 | 116.92 | true | confirmed | 4 | 30.6 | 31.4 | -2.8 |
| darvas_box | 2025-12-09 | 214.35 | true | confirmed | 2 | 5.1 | 21.8 | -5.9 |
| darvas_box | 2026-01-06 | 254.19 | false | confirmed | 2 | -0.3 | 12.5 | -15.0 |
| darvas_box | 2026-02-02 | 268.49 | false | confirmed | 2 | 24.1 | 36.3 | -11.1 |
| darvas_box | 2026-03-17 | 370.05 | true | confirmed | 1 | 28.6 | 38.8 | -2.3 |
| darvas_box | 2026-04-02 | 447.76 | false | confirmed | 2 | 19.5 | 22.8 | -5.9 |
| darvas_box | 2026-04-23 | 515.85 | false | confirmed | 2 | 7.5 | 16.1 | -10.6 |
| bollinger_squeeze | 2025-09-04 | 116.92 | true | confirmed | 4 | 30.6 | 31.4 | -2.8 |
| bollinger_squeeze | 2025-10-08 | 159.66 | true | confirmed | 5 | 22.6 | 23.4 | -4.0 |
| bollinger_squeeze | 2025-10-29 | 189.27 | false | confirmed | 4 | 5.8 | 13.2 | -11.1 |
| bollinger_squeeze | 2025-12-10 | 221.85 | true | confirmed | 1 | 3.9 | 17.7 | -9.1 |
| bollinger_squeeze | 2026-02-02 | 268.49 | false | confirmed | 2 | 24.1 | 36.3 | -11.1 |
| bollinger_squeeze | 2026-03-18 | 385.26 | true | confirmed | 1 | 28.5 | 33.3 | -6.1 |
| bollinger_squeeze | 2026-05-06 | 576.79 | false | fakeout | 1 | -3.9 | 3.8 | -10.6 |
| ttm_squeeze | 2026-02-03 | 276.52 | false | confirmed | 1 | 24.2 | 32.3 | -13.7 |
| volume_resistance | 2025-09-04 | 116.92 | true | confirmed | 4 | 30.6 | 31.4 | -2.8 |
| volume_resistance | 2025-11-14 | 191.71 | false | confirmed | 4 | 12.8 | 29.4 | -12.3 |
| volume_resistance | 2025-12-11 | 242.37 | false | marginal | 1 | -3.3 | 7.7 | -16.8 |
| volume_resistance | 2026-02-06 | 271.32 | true | confirmed | 1 | 17.4 | 34.9 | -1.7 |
| volume_resistance | 2026-03-05 | 299.3 | true | confirmed | 3 | 49.6 | 51.4 | -4.0 |
| volume_resistance | 2026-03-20 | 383.89 | true | confirmed | 1 | 31.1 | 34.9 | -5.8 |
| volume_resistance | 2026-05-07 | 538.76 | true | confirmed | 2 | 2.9 | 11.2 | 0.0 |
| high_52w_momentum | 2025-09-04 | 116.92 | true | confirmed | 4 | 30.6 | 31.4 | -2.8 |
| high_52w_momentum | 2025-09-19 | 138.37 | true | confirmed | 8 | 23.5 | 27.8 | -3.4 |
| high_52w_momentum | 2025-10-06 | 153.25 | true | confirmed | 5 | 23.7 | 26.9 | -3.8 |
| high_52w_momentum | 2025-10-24 | 179.05 | true | confirmed | 4 | -0.4 | 19.6 | -6.0 |
| high_52w_momentum | 2025-11-10 | 208.74 | false | marginal | 3 | 2.7 | 5.3 | -19.4 |
| high_52w_momentum | 2025-12-08 | 212.93 | true | confirmed | 3 | 21.8 | 22.6 | -5.3 |
| high_52w_momentum | 2026-01-02 | 246.06 | false | confirmed | 1 | 9.1 | 10.2 | -12.2 |
| high_52w_momentum | 2026-02-02 | 268.49 | false | confirmed | 2 | 24.1 | 36.3 | -11.1 |
| high_52w_momentum | 2026-02-18 | 310.96 | true | confirmed | 2 | 23.9 | 29.3 | -10.5 |
| high_52w_momentum | 2026-03-16 | 363.88 | true | confirmed | 2 | 28.4 | 41.1 | -3.7 |
| high_52w_momentum | 2026-04-02 | 447.76 | false | confirmed | 2 | 19.5 | 22.8 | -5.9 |
| high_52w_momentum | 2026-04-23 | 515.85 | false | confirmed | 2 | 7.5 | 16.1 | -10.6 |
| high_52w_momentum | 2026-05-11 | 581.47 | false | fakeout | 1 | -4.6 | 3.0 | -5.9 |


### AAOI  (2021-04-01 → 2026-05-15)

_signals in study window 2025-09-01 → 2026-05-18:_


| algorithm | entry_date | entry_price | outcome | breakout_class | days_to_resolve | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| donchian_20 | 2025-09-10 | 27.72 | false | confirmed | 1 | 16.2 | 24.9 | -10.6 |
| donchian_20 | 2025-10-06 | 33.79 | false | confirmed | 1 | -2.2 | 15.4 | -21.1 |
| donchian_20 | 2025-10-27 | 37.22 | false | fakeout | 1 | -39.6 | 4.8 | -50.3 |
| donchian_20 | 2025-12-09 | 30.38 | true | confirmed | 1 | 8.7 | 38.1 | -11.8 |
| donchian_20 | 2026-01-28 | 45.23 | false | confirmed | 1 | 18.7 | 31.0 | -18.2 |
| donchian_20 | 2026-02-20 | 51.68 | true | confirmed | 2 | 69.4 | 149.5 | -3.3 |
| donchian_20 | 2026-03-10 | 120.49 | false | confirmed | 1 | 10.1 | 11.6 | -34.8 |
| donchian_20 | 2026-04-08 | 132.7 | true | confirmed | 1 | 34.5 | 44.6 | -4.2 |
| donchian_20 | 2026-05-01 | 183.51 | false | confirmed | 1 | 3.7 | 27.3 | -21.8 |
| darvas_box | 2025-10-06 | 33.79 | false | confirmed | 1 | -2.2 | 15.4 | -21.1 |
| darvas_box | 2025-10-27 | 37.22 | false | fakeout | 1 | -39.6 | 4.8 | -50.3 |
| darvas_box | 2025-12-22 | 39.1 | false | marginal | 3 | -2.4 | 7.3 | -19.0 |
| darvas_box | 2026-01-28 | 45.23 | false | confirmed | 1 | 18.7 | 31.0 | -18.2 |
| darvas_box | 2026-02-20 | 51.68 | true | confirmed | 2 | 69.4 | 149.5 | -3.3 |
| darvas_box | 2026-04-08 | 132.7 | true | confirmed | 1 | 34.5 | 44.6 | -4.2 |
| darvas_box | 2026-05-01 | 183.51 | false | confirmed | 1 | 3.7 | 27.3 | -21.8 |
| bollinger_squeeze | 2025-09-10 | 27.72 | false | confirmed | 1 | 16.2 | 24.9 | -10.6 |
| bollinger_squeeze | 2025-10-06 | 33.79 | false | confirmed | 1 | -2.2 | 15.4 | -21.1 |
| bollinger_squeeze | 2025-10-27 | 37.22 | false | fakeout | 1 | -39.6 | 4.8 | -50.3 |
| bollinger_squeeze | 2026-01-28 | 45.23 | false | confirmed | 1 | 18.7 | 31.0 | -18.2 |
| bollinger_squeeze | 2026-04-08 | 132.7 | true | confirmed | 1 | 34.5 | 44.6 | -4.2 |
| bollinger_squeeze | 2026-05-01 | 183.51 | false | confirmed | 1 | 3.7 | 27.3 | -21.8 |
| ttm_squeeze | 2025-09-11 | 26.85 | true | confirmed | 2 | 20.6 | 28.9 | -7.7 |
| ttm_squeeze | 2026-01-28 | 45.23 | false | confirmed | 1 | 18.7 | 31.0 | -18.2 |
| volume_resistance | 2025-10-06 | 33.79 | false | confirmed | 1 | -2.2 | 15.4 | -21.1 |
| volume_resistance | 2025-11-07 | 28.57 | false | fakeout | 1 | -2.6 | -1.8 | -35.2 |
| volume_resistance | 2025-12-23 | 40.64 | false | fakeout | 2 | -12.1 | 2.0 | -22.1 |
| volume_resistance | 2026-01-28 | 45.23 | false | confirmed | 1 | 18.7 | 31.0 | -18.2 |
| volume_resistance | 2026-02-27 | 84.23 | true | confirmed | 1 | 16.6 | 53.1 | 0.4 |
| volume_resistance | 2026-04-10 | 150.6 | false | confirmed | 2 | -1.1 | 27.4 | -11.9 |
| volume_resistance | 2026-05-08 | 148.94 | true | confirmed | 1 | 27.8 | 56.9 | 1.1 |
| high_52w_momentum | 2026-01-28 | 45.23 | false | confirmed | 1 | 18.7 | 31.0 | -18.2 |
| high_52w_momentum | 2026-02-20 | 51.68 | true | confirmed | 2 | 69.4 | 149.5 | -3.3 |
| high_52w_momentum | 2026-03-09 | 110.62 | true | confirmed | 1 | 6.3 | 16.6 | -29.0 |
| high_52w_momentum | 2026-04-08 | 132.7 | true | confirmed | 1 | 34.5 | 44.6 | -4.2 |
| high_52w_momentum | 2026-04-30 | 164.36 | true | confirmed | 1 | 15.8 | 42.2 | -12.6 |


### POET  (2021-04-01 → 2026-05-15)

_signals in study window 2025-09-01 → 2026-05-18:_


| algorithm | entry_date | entry_price | outcome | breakout_class | days_to_resolve | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| donchian_20 | 2025-09-23 | 6.0 | true | confirmed | 1 | 24.2 | 56.8 | -12.0 |
| donchian_20 | 2025-10-08 | 9.22 | false | fakeout | 1 | -34.5 | 2.1 | -37.1 |
| donchian_20 | 2025-12-04 | 6.37 | false | confirmed | 1 | 16.6 | 24.0 | -8.8 |
| donchian_20 | 2025-12-22 | 7.61 | false | confirmed | 1 | -8.8 | 20.1 | -18.7 |
| donchian_20 | 2026-01-14 | 8.09 | true | confirmed | 3 | -30.2 | 13.0 | -36.6 |
| donchian_20 | 2026-03-02 | 6.91 | false | confirmed | 1 | -26.5 | 19.7 | -29.5 |
| donchian_20 | 2026-04-20 | 8.59 | true | confirmed | 1 | 85.9 | 142.3 | -25.8 |
| donchian_20 | 2026-05-14 | 20.57 | false | fakeout | 1 | -22.4 | -1.5 | -22.5 |
| darvas_box | 2025-10-07 | 7.88 | true | confirmed | 1 | -24.5 | 19.4 | -26.4 |
| darvas_box | 2026-04-21 | 10.25 | true | confirmed | 1 | 55.8 | 103.0 | -37.9 |
| darvas_box | 2026-05-14 | 20.57 | false | fakeout | 1 | -22.4 | -1.5 | -22.5 |
| bollinger_squeeze | 2025-09-23 | 6.0 | true | confirmed | 1 | 24.2 | 56.8 | -12.0 |
| bollinger_squeeze | 2026-03-02 | 6.91 | false | confirmed | 1 | -26.5 | 19.7 | -29.5 |
| bollinger_squeeze | 2026-04-13 | 7.3 | false | confirmed | 1 | 90.4 | 112.3 | -12.7 |
| ttm_squeeze | 2025-09-24 | 6.05 | true | confirmed | 1 | 21.8 | 55.5 | -12.7 |
| volume_resistance | 2025-10-07 | 7.88 | true | confirmed | 1 | -24.5 | 19.4 | -26.4 |
| volume_resistance | 2026-04-21 | 10.25 | true | confirmed | 1 | 55.8 | 103.0 | -37.9 |
| volume_resistance | 2026-05-14 | 20.57 | false | fakeout | 1 | -22.4 | -1.5 | -22.5 |
| high_52w_momentum | 2025-10-07 | 7.88 | true | confirmed | 1 | -24.5 | 19.4 | -26.4 |
| high_52w_momentum | 2026-04-21 | 10.25 | true | confirmed | 1 | 55.8 | 103.0 | -37.9 |
| high_52w_momentum | 2026-05-14 | 20.57 | false | fakeout | 1 | -22.4 | -1.5 | -22.5 |


**Optics (late-25/early-26 study) — summary across all signals (full history):**


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 126 | 56 | 64 | 1 | 5 | 7.32 | 84 | 33 | 44.4 | 54.8 | 66.7 | 26.2 |
| darvas_box | 111 | 53 | 54 | 3 | 1 | 6.43 | 76 | 29 | 47.7 | 49.5 | 68.5 | 26.1 |
| donchian_20 | 222 | 99 | 115 | 4 | 4 | 5.57 | 144 | 60 | 44.6 | 53.6 | 64.9 | 27.0 |
| high_52w_momentum | 96 | 46 | 46 | 2 | 2 | 8.07 | 68 | 19 | 47.9 | 50.0 | 70.8 | 19.8 |
| ttm_squeeze | 47 | 21 | 26 | 0 | 0 | 5.19 | 34 | 11 | 44.7 | 55.3 | 72.3 | 23.4 |
| volume_resistance | 124 | 59 | 59 | 4 | 2 | 5.95 | 86 | 26 | 47.6 | 49.2 | 69.4 | 21.0 |


## QQQ/SPY 3-yr false-positive sample


### NVDA  (2021-04-01 → 2026-05-15)

_per-algorithm summary (full 3-yr history):_


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 19 | 8 | 11 | 0 | 0 | 4.93 | 11 | 8 | 42.1 | 57.9 | 57.9 | 42.1 |
| darvas_box | 25 | 9 | 14 | 2 | 0 | 7.61 | 13 | 6 | 36.0 | 56.0 | 52.0 | 24.0 |
| donchian_20 | 45 | 21 | 22 | 2 | 0 | 6.82 | 30 | 10 | 46.7 | 48.9 | 66.7 | 22.2 |
| high_52w_momentum | 25 | 10 | 13 | 2 | 0 | 9.12 | 15 | 5 | 40.0 | 52.0 | 60.0 | 20.0 |
| ttm_squeeze | 2 | 0 | 1 | 1 | 0 | -1.3 | 0 | 0 | 0.0 | 50.0 | 0.0 | 0.0 |
| volume_resistance | 16 | 11 | 5 | 0 | 0 | 7.34 | 12 | 3 | 68.8 | 31.2 | 75.0 | 18.8 |


_worst false positives (fakeouts) — 32 total:_


| algorithm | entry_date | entry_price | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- |
| donchian_20 | 2022-08-04 | 19.18 | -27.5 | 0.1 | -30.9 |
| bollinger_squeeze | 2022-06-02 | 19.56 | -25.9 | -1.3 | -26.5 |
| donchian_20 | 2025-01-06 | 149.38 | -16.5 | 2.5 | -24.4 |
| bollinger_squeeze | 2025-01-06 | 149.38 | -16.5 | 2.5 | -24.4 |
| donchian_20 | 2021-11-19 | 32.92 | -16.0 | 5.0 | -17.7 |
| darvas_box | 2021-11-19 | 32.92 | -16.0 | 5.0 | -17.7 |


### AAPL  (2021-04-01 → 2026-05-15)

_per-algorithm summary (full 3-yr history):_


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 24 | 7 | 6 | 9 | 2 | 3.6 | 7 | 8 | 29.2 | 33.3 | 29.2 | 33.3 |
| darvas_box | 18 | 4 | 3 | 9 | 2 | 2.84 | 5 | 4 | 22.2 | 27.8 | 27.8 | 22.2 |
| donchian_20 | 39 | 12 | 12 | 13 | 2 | 2.16 | 13 | 12 | 30.8 | 35.9 | 33.3 | 30.8 |
| high_52w_momentum | 14 | 3 | 4 | 6 | 1 | 0.69 | 3 | 5 | 21.4 | 35.7 | 21.4 | 35.7 |
| ttm_squeeze | 6 | 2 | 2 | 2 | 0 | 2.4 | 2 | 2 | 33.3 | 33.3 | 33.3 | 33.3 |
| volume_resistance | 9 | 4 | 2 | 2 | 1 | 3.54 | 4 | 2 | 44.4 | 33.3 | 44.4 | 22.2 |


_worst false positives (fakeouts) — 33 total:_


| algorithm | entry_date | entry_price | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- |
| volume_resistance | 2024-12-20 | 252.87 | -12.1 | 2.2 | -13.8 |
| donchian_20 | 2022-08-15 | 170.02 | -11.2 | 1.7 | -11.8 |
| donchian_20 | 2021-09-07 | 152.96 | -9.9 | 0.2 | -11.8 |
| bollinger_squeeze | 2021-09-07 | 152.96 | -9.9 | 0.2 | -11.8 |
| donchian_20 | 2023-07-19 | 192.4 | -9.4 | 1.1 | -9.4 |
| darvas_box | 2023-07-19 | 192.4 | -9.4 | 1.1 | -9.4 |


### MSFT  (2021-04-01 → 2026-05-15)

_per-algorithm summary (full 3-yr history):_


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 21 | 4 | 8 | 6 | 3 | 0.03 | 4 | 8 | 19.0 | 52.4 | 19.0 | 38.1 |
| darvas_box | 17 | 5 | 7 | 4 | 1 | 1.73 | 5 | 6 | 29.4 | 47.1 | 29.4 | 35.3 |
| donchian_20 | 43 | 10 | 14 | 11 | 8 | 0.6 | 10 | 18 | 23.3 | 51.2 | 23.3 | 41.9 |
| high_52w_momentum | 16 | 6 | 3 | 4 | 3 | 1.06 | 6 | 6 | 37.5 | 37.5 | 37.5 | 37.5 |
| ttm_squeeze | 8 | 2 | 4 | 1 | 1 | -2.92 | 2 | 5 | 25.0 | 62.5 | 25.0 | 62.5 |
| volume_resistance | 15 | 3 | 3 | 6 | 3 | 1.24 | 3 | 5 | 20.0 | 40.0 | 20.0 | 33.3 |


_worst false positives (fakeouts) — 48 total:_


| algorithm | entry_date | entry_price | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- |
| ttm_squeeze | 2021-12-27 | 330.59 | -15.8 | 0.5 | -19.4 |
| ttm_squeeze | 2025-10-28 | 539.83 | -11.8 | 0.8 | -14.1 |
| high_52w_momentum | 2025-10-28 | 539.83 | -11.8 | 0.8 | -14.1 |
| donchian_20 | 2025-10-27 | 529.32 | -10.7 | 4.2 | -11.8 |
| bollinger_squeeze | 2025-10-27 | 529.32 | -10.7 | 4.2 | -11.8 |
| donchian_20 | 2023-07-18 | 351.94 | -10.5 | 0.8 | -11.2 |


### AMZN  (2021-04-01 → 2026-05-15)

_per-algorithm summary (full 3-yr history):_


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 26 | 5 | 12 | 8 | 1 | 2.38 | 7 | 10 | 19.2 | 50.0 | 26.9 | 38.5 |
| darvas_box | 20 | 2 | 10 | 6 | 2 | 0.07 | 2 | 8 | 10.0 | 60.0 | 10.0 | 40.0 |
| donchian_20 | 37 | 11 | 17 | 6 | 3 | 1.71 | 12 | 14 | 29.7 | 54.1 | 32.4 | 37.8 |
| high_52w_momentum | 14 | 3 | 6 | 5 | 0 | 1.39 | 3 | 6 | 21.4 | 42.9 | 21.4 | 42.9 |
| ttm_squeeze | 10 | 4 | 5 | 0 | 1 | 7.36 | 5 | 1 | 40.0 | 60.0 | 50.0 | 10.0 |
| volume_resistance | 14 | 4 | 7 | 3 | 0 | -0.68 | 4 | 6 | 28.6 | 50.0 | 28.6 | 42.9 |


_worst false positives (fakeouts) — 45 total:_


| algorithm | entry_date | entry_price | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- |
| donchian_20 | 2023-09-11 | 143.1 | -10.4 | 1.9 | -14.0 |
| bollinger_squeeze | 2023-09-11 | 143.1 | -10.4 | 1.9 | -14.0 |
| high_52w_momentum | 2023-09-11 | 143.1 | -10.4 | 1.9 | -14.0 |
| volume_resistance | 2025-01-27 | 235.42 | -9.6 | 3.0 | -13.3 |
| donchian_20 | 2022-08-03 | 139.52 | -9.1 | 5.1 | -9.2 |
| darvas_box | 2023-09-13 | 144.85 | -9.0 | 0.7 | -15.1 |


### META  (2021-04-01 → 2026-05-15)

_per-algorithm summary (full 3-yr history):_


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 29 | 7 | 17 | 4 | 1 | -0.13 | 7 | 11 | 24.1 | 62.1 | 24.1 | 37.9 |
| darvas_box | 21 | 8 | 9 | 4 | 0 | 2.48 | 8 | 8 | 38.1 | 42.9 | 38.1 | 38.1 |
| donchian_20 | 42 | 15 | 20 | 5 | 2 | 1.81 | 15 | 16 | 35.7 | 52.4 | 35.7 | 38.1 |
| high_52w_momentum | 21 | 8 | 10 | 2 | 1 | 2.09 | 8 | 10 | 38.1 | 52.4 | 38.1 | 47.6 |
| ttm_squeeze | 9 | 4 | 5 | 0 | 0 | 4.73 | 4 | 5 | 44.4 | 55.6 | 44.4 | 55.6 |
| volume_resistance | 15 | 8 | 6 | 1 | 0 | 5.51 | 9 | 4 | 53.3 | 40.0 | 60.0 | 26.7 |


_worst false positives (fakeouts) — 54 total:_


| algorithm | entry_date | entry_price | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- |
| donchian_20 | 2025-02-12 | 722.48 | -18.6 | 2.1 | -19.1 |
| donchian_20 | 2025-10-27 | 749.57 | -18.3 | 1.1 | -22.6 |
| bollinger_squeeze | 2025-10-27 | 749.57 | -18.3 | 1.1 | -22.6 |
| high_52w_momentum | 2025-02-07 | 711.66 | -16.3 | 3.7 | -17.9 |
| donchian_20 | 2022-03-24 | 217.86 | -16.1 | 7.9 | -16.5 |
| darvas_box | 2024-04-05 | 523.79 | -14.3 | 0.8 | -21.4 |


### TSLA  (2021-04-01 → 2026-05-15)

_per-algorithm summary (full 3-yr history):_


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 18 | 9 | 9 | 0 | 0 | 6.54 | 10 | 5 | 50.0 | 50.0 | 55.6 | 27.8 |
| darvas_box | 10 | 7 | 3 | 0 | 0 | 12.41 | 7 | 3 | 70.0 | 30.0 | 70.0 | 30.0 |
| donchian_20 | 35 | 14 | 21 | 0 | 0 | 5.46 | 21 | 11 | 40.0 | 60.0 | 60.0 | 31.4 |
| high_52w_momentum | 5 | 1 | 4 | 0 | 0 | 7.42 | 3 | 2 | 20.0 | 80.0 | 60.0 | 40.0 |
| ttm_squeeze | 7 | 4 | 3 | 0 | 0 | 5.69 | 5 | 1 | 57.1 | 42.9 | 71.4 | 14.3 |
| volume_resistance | 10 | 5 | 5 | 0 | 0 | 14.06 | 8 | 2 | 50.0 | 50.0 | 80.0 | 20.0 |


_worst false positives (fakeouts) — 24 total:_


| algorithm | entry_date | entry_price | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- |
| donchian_20 | 2023-12-27 | 261.44 | -29.9 | 1.4 | -31.1 |
| donchian_20 | 2022-01-03 | 399.93 | -22.4 | 0.7 | -34.0 |
| donchian_20 | 2023-03-31 | 207.46 | -22.0 | -2.3 | -26.6 |
| bollinger_squeeze | 2023-03-31 | 207.46 | -22.0 | -2.3 | -26.6 |
| ttm_squeeze | 2023-12-19 | 257.22 | -17.5 | 3.1 | -19.3 |
| donchian_20 | 2024-09-23 | 250.0 | -12.5 | 5.9 | -14.5 |


### AVGO  (2021-04-01 → 2026-05-15)

_per-algorithm summary (full 3-yr history):_


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 28 | 10 | 11 | 5 | 2 | 4.79 | 12 | 8 | 35.7 | 46.4 | 42.9 | 28.6 |
| darvas_box | 26 | 11 | 12 | 3 | 0 | 5.27 | 14 | 9 | 42.3 | 46.2 | 53.8 | 34.6 |
| donchian_20 | 43 | 18 | 15 | 7 | 3 | 5.02 | 22 | 14 | 41.9 | 41.9 | 51.2 | 32.6 |
| high_52w_momentum | 25 | 10 | 11 | 3 | 1 | 4.44 | 12 | 8 | 40.0 | 48.0 | 48.0 | 32.0 |
| ttm_squeeze | 9 | 2 | 4 | 3 | 0 | 4.41 | 2 | 2 | 22.2 | 44.4 | 22.2 | 22.2 |
| volume_resistance | 17 | 10 | 4 | 2 | 1 | 5.09 | 11 | 3 | 58.8 | 29.4 | 64.7 | 17.6 |


_worst false positives (fakeouts) — 44 total:_


| algorithm | entry_date | entry_price | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- |
| donchian_20 | 2021-12-22 | 60.57 | -18.6 | 3.4 | -18.9 |
| ttm_squeeze | 2022-05-17 | 56.6 | -13.4 | -1.2 | -15.7 |
| volume_resistance | 2025-12-11 | 404.74 | -13.2 | -6.0 | -20.9 |
| donchian_20 | 2025-11-26 | 395.98 | -11.3 | 4.3 | -19.2 |
| darvas_box | 2025-11-26 | 395.98 | -11.3 | 4.3 | -19.2 |
| bollinger_squeeze | 2025-11-26 | 395.98 | -11.3 | 4.3 | -19.2 |


### AMD  (2021-04-01 → 2026-05-15)

_per-algorithm summary (full 3-yr history):_


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 22 | 14 | 8 | 0 | 0 | 8.43 | 18 | 4 | 63.6 | 36.4 | 81.8 | 18.2 |
| darvas_box | 13 | 9 | 4 | 0 | 0 | 12.81 | 11 | 2 | 69.2 | 30.8 | 84.6 | 15.4 |
| donchian_20 | 36 | 18 | 17 | 0 | 1 | 5.16 | 25 | 10 | 50.0 | 50.0 | 69.4 | 27.8 |
| high_52w_momentum | 12 | 4 | 8 | 0 | 0 | 5.28 | 8 | 4 | 33.3 | 66.7 | 66.7 | 33.3 |
| ttm_squeeze | 6 | 4 | 2 | 0 | 0 | 21.52 | 5 | 1 | 66.7 | 33.3 | 83.3 | 16.7 |
| volume_resistance | 18 | 11 | 7 | 0 | 0 | 7.03 | 12 | 4 | 61.1 | 38.9 | 66.7 | 22.2 |


_worst false positives (fakeouts) — 25 total:_


| algorithm | entry_date | entry_price | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- |
| donchian_20 | 2022-06-02 | 108.59 | -32.2 | 0.9 | -33.1 |
| bollinger_squeeze | 2022-06-02 | 108.59 | -32.2 | 0.9 | -33.1 |
| donchian_20 | 2022-03-29 | 123.23 | -31.1 | 2.0 | -31.8 |
| volume_resistance | 2024-07-10 | 183.96 | -30.1 | 1.7 | -33.8 |
| ttm_squeeze | 2024-07-08 | 178.69 | -24.6 | 4.8 | -31.8 |
| donchian_20 | 2025-03-24 | 113.85 | -24.2 | 1.8 | -32.8 |


### NFLX  (2021-04-01 → 2026-05-15)

_per-algorithm summary (full 3-yr history):_


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 23 | 11 | 9 | 2 | 1 | 3.15 | 11 | 8 | 47.8 | 43.5 | 47.8 | 34.8 |
| darvas_box | 27 | 8 | 11 | 4 | 4 | 1.5 | 9 | 10 | 29.6 | 55.6 | 33.3 | 37.0 |
| donchian_20 | 44 | 13 | 20 | 7 | 4 | 0.94 | 13 | 18 | 29.5 | 54.5 | 29.5 | 40.9 |
| high_52w_momentum | 25 | 8 | 8 | 5 | 4 | 1.91 | 8 | 8 | 32.0 | 48.0 | 32.0 | 32.0 |
| ttm_squeeze | 8 | 6 | 2 | 0 | 0 | 8.83 | 6 | 1 | 75.0 | 25.0 | 75.0 | 12.5 |
| volume_resistance | 21 | 12 | 5 | 2 | 2 | 3.52 | 13 | 5 | 57.1 | 33.3 | 61.9 | 23.8 |


_worst false positives (fakeouts) — 50 total:_


| algorithm | entry_date | entry_price | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- |
| volume_resistance | 2026-04-16 | 107.79 | -19.3 | -8.4 | -21.1 |
| donchian_20 | 2023-09-05 | 44.87 | -16.0 | 0.6 | -17.3 |
| donchian_20 | 2026-04-10 | 103.01 | -15.1 | 5.8 | -15.8 |
| donchian_20 | 2021-11-17 | 69.17 | -14.5 | 0.4 | -15.5 |
| darvas_box | 2021-11-17 | 69.17 | -14.5 | 0.4 | -15.5 |
| bollinger_squeeze | 2026-04-09 | 102.05 | -13.5 | 6.8 | -15.0 |


### COST  (2021-04-01 → 2026-05-15)

_per-algorithm summary (full 3-yr history):_


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 17 | 3 | 8 | 5 | 1 | 0.54 | 3 | 10 | 17.6 | 52.9 | 17.6 | 58.8 |
| darvas_box | 24 | 5 | 7 | 10 | 2 | 1.59 | 5 | 10 | 20.8 | 37.5 | 20.8 | 41.7 |
| donchian_20 | 47 | 11 | 9 | 17 | 10 | 1.74 | 11 | 20 | 23.4 | 40.4 | 23.4 | 42.6 |
| high_52w_momentum | 20 | 4 | 8 | 5 | 3 | 0.02 | 4 | 10 | 20.0 | 55.0 | 20.0 | 50.0 |
| ttm_squeeze | 12 | 4 | 0 | 5 | 3 | 4.33 | 4 | 3 | 33.3 | 25.0 | 33.3 | 25.0 |
| volume_resistance | 15 | 3 | 7 | 2 | 3 | -1.61 | 3 | 7 | 20.0 | 66.7 | 20.0 | 46.7 |


_worst false positives (fakeouts) — 60 total:_


| algorithm | entry_date | entry_price | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- |
| donchian_20 | 2022-04-07 | 578.96 | -17.1 | 0.2 | -17.8 |
| volume_resistance | 2022-04-07 | 578.96 | -17.1 | 0.2 | -17.8 |
| donchian_20 | 2025-02-13 | 1069.44 | -16.1 | 0.1 | -18.1 |
| donchian_20 | 2022-11-30 | 516.1 | -15.3 | -3.7 | -16.1 |
| high_52w_momentum | 2025-02-10 | 1054.6 | -12.4 | 1.5 | -13.3 |
| high_52w_momentum | 2022-04-06 | 556.81 | -11.4 | 4.7 | -12.3 |


### INTC  (2021-04-01 → 2026-05-15)

_per-algorithm summary (full 3-yr history):_


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 24 | 7 | 15 | 1 | 1 | 2.41 | 11 | 11 | 29.2 | 66.7 | 45.8 | 45.8 |
| darvas_box | 13 | 6 | 7 | 0 | 0 | 9.28 | 8 | 5 | 46.2 | 53.8 | 61.5 | 38.5 |
| donchian_20 | 33 | 9 | 22 | 1 | 1 | 2.51 | 15 | 15 | 27.3 | 69.7 | 45.5 | 45.5 |
| high_52w_momentum | 11 | 7 | 4 | 0 | 0 | 10.38 | 9 | 2 | 63.6 | 36.4 | 81.8 | 18.2 |
| ttm_squeeze | 10 | 4 | 5 | 0 | 1 | 5.24 | 6 | 3 | 40.0 | 60.0 | 60.0 | 30.0 |
| volume_resistance | 16 | 5 | 11 | 0 | 0 | 2.82 | 8 | 8 | 31.2 | 68.8 | 50.0 | 50.0 |


_worst false positives (fakeouts) — 44 total:_


| algorithm | entry_date | entry_price | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- |
| volume_resistance | 2024-07-17 | 34.24 | -41.8 | 5.3 | -45.0 |
| donchian_20 | 2024-11-06 | 25.05 | -17.0 | 5.5 | -17.5 |
| donchian_20 | 2025-07-10 | 23.82 | -17.0 | 0.0 | -20.4 |
| bollinger_squeeze | 2024-11-06 | 25.05 | -17.0 | 5.5 | -17.5 |
| ttm_squeeze | 2024-11-06 | 25.05 | -17.0 | 5.5 | -17.5 |
| volume_resistance | 2024-11-06 | 25.05 | -17.0 | 5.5 | -17.5 |


### PYPL  (2021-04-01 → 2026-05-15)

_per-algorithm summary (full 3-yr history):_


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 23 | 6 | 15 | 2 | 0 | -2.98 | 8 | 11 | 26.1 | 65.2 | 34.8 | 47.8 |
| darvas_box | 10 | 0 | 9 | 1 | 0 | -4.37 | 0 | 7 | 0.0 | 90.0 | 0.0 | 70.0 |
| donchian_20 | 32 | 10 | 21 | 1 | 0 | -2.89 | 13 | 16 | 31.2 | 65.6 | 40.6 | 50.0 |
| high_52w_momentum | 7 | 1 | 4 | 1 | 1 | -0.66 | 1 | 1 | 14.3 | 71.4 | 14.3 | 14.3 |
| ttm_squeeze | 5 | 4 | 1 | 0 | 0 | 1.38 | 4 | 1 | 80.0 | 20.0 | 80.0 | 20.0 |
| volume_resistance | 6 | 1 | 5 | 0 | 0 | -5.6 | 1 | 4 | 16.7 | 83.3 | 16.7 | 66.7 |


_worst false positives (fakeouts) — 40 total:_


| algorithm | entry_date | entry_price | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- |
| ttm_squeeze | 2023-04-18 | 76.01 | -20.4 | 0.1 | -20.5 |
| donchian_20 | 2023-04-17 | 76.92 | -19.5 | 0.8 | -20.7 |
| bollinger_squeeze | 2023-04-17 | 76.92 | -19.5 | 0.8 | -20.7 |
| bollinger_squeeze | 2022-06-02 | 87.85 | -19.2 | 1.1 | -23.5 |
| donchian_20 | 2023-07-31 | 75.42 | -18.7 | 0.6 | -24.4 |
| donchian_20 | 2022-03-18 | 118.14 | -15.3 | 3.5 | -16.5 |


### SBUX  (2021-04-01 → 2026-05-15)

_per-algorithm summary (full 3-yr history):_


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 21 | 7 | 9 | 1 | 4 | 1.09 | 7 | 12 | 33.3 | 61.9 | 33.3 | 57.1 |
| darvas_box | 13 | 2 | 7 | 2 | 2 | -1.53 | 2 | 10 | 15.4 | 69.2 | 15.4 | 76.9 |
| donchian_20 | 28 | 10 | 14 | 1 | 3 | 0.31 | 10 | 16 | 35.7 | 60.7 | 35.7 | 57.1 |
| high_52w_momentum | 8 | 0 | 5 | 3 | 0 | -5.42 | 0 | 7 | 0.0 | 62.5 | 0.0 | 87.5 |
| ttm_squeeze | 11 | 3 | 6 | 1 | 1 | -0.05 | 4 | 6 | 27.3 | 63.6 | 36.4 | 54.5 |
| volume_resistance | 14 | 2 | 8 | 2 | 2 | -1.73 | 2 | 10 | 14.3 | 71.4 | 14.3 | 71.4 |


_worst false positives (fakeouts) — 61 total:_


| algorithm | entry_date | entry_price | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- |
| volume_resistance | 2025-03-06 | 102.04 | -16.3 | 1.3 | -16.9 |
| donchian_20 | 2025-02-28 | 112.04 | -15.6 | 1.4 | -18.2 |
| ttm_squeeze | 2024-11-22 | 98.63 | -14.7 | 0.8 | -15.8 |
| high_52w_momentum | 2024-11-22 | 98.63 | -14.7 | 0.8 | -15.8 |
| high_52w_momentum | 2025-02-20 | 109.65 | -12.4 | 3.6 | -15.4 |
| bollinger_squeeze | 2023-04-27 | 104.08 | -12.3 | 2.4 | -12.9 |


### PFE  (2021-04-01 → 2026-05-15)

_per-algorithm summary (full 3-yr history):_


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 24 | 5 | 11 | 5 | 3 | 0.37 | 5 | 15 | 20.8 | 58.3 | 20.8 | 62.5 |
| darvas_box | 8 | 2 | 4 | 0 | 2 | -1.9 | 2 | 5 | 25.0 | 75.0 | 25.0 | 62.5 |
| donchian_20 | 32 | 12 | 11 | 2 | 7 | 0.53 | 12 | 18 | 37.5 | 56.2 | 37.5 | 56.2 |
| high_52w_momentum | 3 | 0 | 2 | 1 | 0 | -1.83 | 0 | 2 | 0.0 | 66.7 | 0.0 | 66.7 |
| ttm_squeeze | 9 | 3 | 4 | 1 | 1 | 1.39 | 3 | 6 | 33.3 | 55.6 | 33.3 | 66.7 |
| volume_resistance | 8 | 2 | 5 | 1 | 0 | -0.99 | 2 | 4 | 25.0 | 62.5 | 25.0 | 50.0 |


_worst false positives (fakeouts) — 50 total:_


| algorithm | entry_date | entry_price | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- |
| volume_resistance | 2022-12-16 | 41.81 | -12.5 | 1.5 | -12.5 |
| donchian_20 | 2021-08-17 | 39.38 | -11.2 | 2.9 | -12.3 |
| bollinger_squeeze | 2022-04-07 | 43.79 | -11.1 | 2.1 | -14.6 |
| darvas_box | 2025-10-01 | 25.87 | -10.7 | 1.8 | -11.2 |
| volume_resistance | 2025-10-01 | 25.87 | -10.7 | 1.8 | -11.2 |
| donchian_20 | 2023-06-13 | 33.42 | -10.5 | 0.2 | -12.2 |


### MRNA  (2021-04-01 → 2026-05-15)

_per-algorithm summary (full 3-yr history):_


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 17 | 7 | 10 | 0 | 0 | 7.4 | 12 | 5 | 41.2 | 58.8 | 70.6 | 29.4 |
| darvas_box | 8 | 4 | 4 | 0 | 0 | -0.02 | 5 | 3 | 50.0 | 50.0 | 62.5 | 37.5 |
| donchian_20 | 26 | 13 | 13 | 0 | 0 | 1.8 | 17 | 9 | 50.0 | 50.0 | 65.4 | 34.6 |
| high_52w_momentum | 3 | 2 | 1 | 0 | 0 | -4.4 | 3 | 0 | 66.7 | 33.3 | 100.0 | 0.0 |
| ttm_squeeze | 9 | 3 | 6 | 0 | 0 | -5.89 | 4 | 4 | 33.3 | 66.7 | 44.4 | 44.4 |
| volume_resistance | 12 | 4 | 8 | 0 | 0 | 2.19 | 7 | 5 | 33.3 | 66.7 | 58.3 | 41.7 |


_worst false positives (fakeouts) — 26 total:_


| algorithm | entry_date | entry_price | fwd_return_% | max_favorable_% | max_adverse_% |
| --- | --- | --- | --- | --- | --- |
| donchian_20 | 2021-11-29 | 368.51 | -34.5 | -2.9 | -36.6 |
| donchian_20 | 2021-09-09 | 455.92 | -32.1 | 2.0 | -35.6 |
| bollinger_squeeze | 2021-09-09 | 455.92 | -32.1 | 2.0 | -35.6 |
| ttm_squeeze | 2021-09-09 | 455.92 | -32.1 | 2.0 | -35.6 |
| donchian_20 | 2025-01-07 | 47.53 | -29.3 | 0.4 | -32.8 |
| bollinger_squeeze | 2025-01-07 | 47.53 | -29.3 | 0.4 | -32.8 |


**QQQ/SPY 3-yr false-positive sample — summary across all signals (full history):**


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 336 | 110 | 159 | 48 | 19 | 2.69 | 133 | 134 | 32.7 | 53.0 | 39.6 | 39.9 |
| darvas_box | 253 | 82 | 111 | 45 | 15 | 3.45 | 96 | 96 | 32.4 | 49.8 | 37.9 | 37.9 |
| donchian_20 | 562 | 197 | 248 | 73 | 44 | 2.37 | 239 | 217 | 35.1 | 52.0 | 42.5 | 38.6 |
| high_52w_momentum | 209 | 67 | 91 | 37 | 14 | 2.99 | 83 | 76 | 32.1 | 50.2 | 39.7 | 36.4 |
| ttm_squeeze | 121 | 49 | 50 | 14 | 8 | 3.75 | 56 | 41 | 40.5 | 47.9 | 46.3 | 33.9 |
| volume_resistance | 206 | 85 | 88 | 21 | 12 | 3.16 | 99 | 72 | 41.3 | 48.5 | 48.1 | 35.0 |


## Overall, every name, full history (false-positive view)


| algorithm | signals | true | false | timeout_up | timeout_down | avg_fwd_return_pct | confirmed | fakeout | tradeable_win_% | stop_whipsaw_% | confirmed_% | fakeout_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bollinger_squeeze | 553 | 205 | 265 | 57 | 26 | 4.7 | 265 | 191 | 37.1 | 52.6 | 47.9 | 34.5 |
| darvas_box | 443 | 169 | 200 | 56 | 18 | 5.71 | 219 | 144 | 38.1 | 49.2 | 49.4 | 32.5 |
| donchian_20 | 964 | 383 | 443 | 85 | 53 | 4.24 | 486 | 330 | 39.7 | 51.5 | 50.4 | 34.2 |
| high_52w_momentum | 400 | 156 | 178 | 46 | 20 | 6.09 | 208 | 116 | 39.0 | 49.5 | 52.0 | 29.0 |
| ttm_squeeze | 203 | 82 | 97 | 15 | 9 | 3.8 | 105 | 66 | 40.4 | 52.2 | 51.7 | 32.5 |
| volume_resistance | 410 | 179 | 185 | 31 | 15 | 5.29 | 231 | 119 | 43.7 | 48.8 | 56.3 | 29.0 |
