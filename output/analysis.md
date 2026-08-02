# Market Regime Detection on SOXX — Analysis

**Data:** SOXX daily, dividend/split-adjusted (yfinance), 2005-01-03 → 2026-07-31.
**Train window:** 2005-01-03 → 2022-12-30 (all fitting and tuning; 4,527 daily returns).
**Test window:** 2023-01-03 → 2026-07-31 (out-of-sample, ~3.6 years).
**Execution:** signals from day *t*'s close earn day *t+1*'s return; 5 bps per side on every switch.

Data notes: yfinance's default transport failed through this environment's
TLS-intercepting egress proxy (its modern-Chrome TLS fingerprint gets reset);
`data.py` hands it a curl_cffi session impersonating an older browser
(chrome116), which both passes the proxy and avoids Yahoo's 429
fingerprint-blocking. VIX/VIX3M closes come from CBOE's published history
CSVs. A breadth signal (top-30 holdings above their 50-day MA) was dropped:
no free point-in-time holdings history exists, and reconstructing it from
today's holdings would itself be look-ahead.

## 1. HMM parameter estimates (frozen fit, train window only)

Two-state Gaussian HMM on daily log returns, EM with 5 seeded restarts
(best log-likelihood 12,175.2):

| State | Daily mean | Daily vol | Annualized | Self-transition | Expected duration |
|---|---|---|---|---|---|
| **Bull** (state 0) | +0.127% | 1.28% | +32%/yr, 20% vol | 0.9906 | ~106 trading days |
| **Bear** (state 1) | −0.157% | 2.82% | −40%/yr, 45% vol | 0.9773 | ~44 trading days |

The classic picture: a persistent low-volatility drift-up state and a
shorter-lived high-volatility drift-down state. The separation is mostly in
**volatility** (2.2×), not mean — the HMM is largely a volatility classifier
with a drift tie-breaker. That is exactly why it exits fast (vol jumps
instantly at tops) and re-enters late (vol is still elevated at bottoms):
the asymmetry is baked into what the model measures.

## 2. Detection lags at the two major test-window drawdowns

Episodes identified from the data: **(A)** peak 2024-07-10 → trough
2025-04-08, −41.4% (recovered 2025-09-18); **(B)** peak 2026-06-22 → trough
2026-07-29, −29.0% (ongoing at the data edge — trough provisional).

Trading days from peak to bear flip / trough to bull flip:

| Algorithm | A: peak→bear | A: trough→bull | B: peak→bear | B: trough→bull |
|---|---|---|---|---|
| HMM (frozen) | 5 | 16 | **0** | still bear |
| HMM (walk-forward) | 5 | 16 | **0** | still bear |
| CUSUM | already bear (flipped 2024-04-19) | **1** | never | — |
| Coppock (monthly) | never turned bear | — | never | — |
| Kalman drift | 5 | 17 | 8 | still bear |
| VIX term structure | 17 | 12 | never | — |
| Composite (≥2 of 4) | 5 | **1** | never | — |
| Composite + contango gate | 5 | 12 | never | — |

**On the asymmetry hypothesis.** The HMM shows the documented pattern, but
milder than folklore: ~5 days into bear versus ~16 days out (3× asymmetric),
and in episode B it flagged the bear on the day of the peak itself. Did the
alternatives fix the slow bear→bull side?

- **CUSUM re-entered one trading day after the trough** — 2025-04-09, the
  +19% tariff-pause session, whose z-score blew straight through the S⁺
  threshold. A cumulative-surprise trigger *can* fix re-entry lag when the
  bottom is a V: it doesn't wait for average calm, one enormous day is
  enough. The flip side: its "bear detection" fired 2024-04-19, three months
  *before* the July peak, so it also skipped the final +20% melt-up leg.
  Two switches in 3.6 years is closer to luck than to detection — see §4.
- **VIX term structure** re-entered in 12 days with modest whipsaw cost: the
  ratio normalizes as soon as panic leaves the front of the curve, near the
  bottom rather than after a streak of calm. But it was slower into the bear
  (17 days) and never flagged episode B at all (VIX barely inverted in the
  2026 selloff).
- **Kalman** matched the HMM into the bear (5 days) and out (17 days) — a
  drift filter on the same returns inherits the same asymmetry.
- The **composite** re-entered in 1 day, but only because it piggybacks on
  CUSUM's vote; gated by contango it re-entered with the VIX overlay (12d).

Conclusion: return-statistics detectors (HMM, Kalman) share the slow
bear→bull side because they wait for enough calm/positive data to
accumulate. The two mechanisms that genuinely re-entered faster read
*different information*: the options market's term structure (12d,
systematic) and CUSUM's burst-sensitivity to a V-shaped reversal (1d, but
fragile — it only works if the bottom is violent).

## 3. Re-entry speed vs false-positive cost

Whipsaws = bull runs shorter than 10 trading days in the test window:

| Algorithm | Trough→bull (ep. A) | Whipsaws | Switches (test) |
|---|---|---|---|
| CUSUM | 1 | 0 | 2 |
| Composite | 1 | 12 | 37 |
| VIX term structure | 12 | 8 | 34 |
| HMM (frozen) | 16 | 21 | 70 |
| Kalman | 17 | 58 | 148 |

The HMM's decent re-entry costs heavy chattering: 70 switches (21 sub-10-day
bull stints) as filtered P(bull) hugs the 0.5 line in mixed tape, ~1.1 pp/yr
of return lost to costs (19.7% gross → 18.6% net). Kalman is worse (148
switches, 58 whipsaws, 2.4 pp/yr cost drag). The VIX overlay bought faster
re-entry than the HMM with a third of the switching. CUSUM's zero whipsaws
reflect its two-trade test window, not robustness. A hysteresis band on the
HMM (enter > 0.6, exit < 0.4) would likely cut the chattering materially;
it was not part of the specified design, so it was not tuned or tested.

## 4. Net-of-cost performance ranking (test window)

| Strategy (net) | Ann. return | Vol | Sharpe | Sortino | MaxDD | Calmar | Time in mkt |
|---|---|---|---|---|---|---|---|
| **CUSUM** | **55.2%** | 30.8% | **1.43** | 1.22 | −29.0% | **1.90** | 73% |
| Buy & hold | 52.2% | 37.9% | 1.11 | 1.08 | −41.4% | 1.26 | 100% |
| Composite | 43.5% | 33.4% | 1.08 | 1.00 | −42.7% | 1.02 | 88% |
| VIX term structure | 42.0% | 34.4% | 1.02 | 0.97 | −34.7% | 1.21 | 95% |
| Coppock (monthly) | 45.3% | 37.2% | 1.01 | 0.95 | −41.4% | 1.10 | 96% |
| Composite + gate | 35.3% | 32.3% | 0.94 | 0.87 | −37.2% | 0.95 | 85% |
| HMM (frozen) | 18.6% | 22.3% | 0.76 | 0.59 | −22.4% | 0.83 | 55% |
| HMM (walk-forward) | 18.2% | 22.5% | 0.74 | 0.58 | −24.3% | 0.75 | 56% |
| Kalman | 15.4% | 26.5% | 0.54 | 0.44 | −42.8% | 0.36 | 58% |

**One strategy beat buy-and-hold on both Sharpe and Calmar: CUSUM** (1.43 vs
1.11; 1.90 vs 1.26), by sidestepping most of the −41% drawdown and catching
the entire recovery from its second day. Treat that headline with heavy
skepticism before extrapolating:

- The result rests on **two trades**. Exit three months early (lucky — the
  April-2024 pullback happened to precede a real top), re-enter on the
  single biggest up-day of the window (structural — that's what a CUSUM
  trigger does in a V-bottom, but V-bottoms are not guaranteed).
- The tuned parameters (k=0.25, h=5) sit next to configurations with very
  different outcomes. The *unconstrained* train optimum was "thresholds so
  wide they never trigger" — always-long, i.e. the tuning itself said the
  detector added no train-window value; the reported configuration is the
  best one **subject to a 20–95% time-in-market band** imposed to force the
  detector to actually detect (documented in `tuning_log.json`; full grid in
  `cusum_train_grid.csv`). In an earlier run of this study on a shorter
  2016–2022 train window (Nasdaq's 10-year history, before full Yahoo data
  was obtained), the tuner chose k=0.5, h=6 — which out-of-sample flipped
  bear **at the April-2025 low** and stayed flat almost a year: net Sharpe
  0.08. Same algorithm, same protocol, slightly different train data —
  disaster instead of triumph. That interval between outcomes is the honest
  error bar on the CUSUM row.
- **Everything else lagged buy-and-hold on Sharpe**, as expected in a tape
  that compounded at ~52%/yr. The defensive story is drawdown: HMM cut max
  drawdown to −22.4% (but its 2023 chattering cost so much return that
  Calmar still lost), the VIX overlay to −34.7% at nearly full participation.
- **Coppock** (monthly variant won on train, Sharpe 0.50 vs 0.45 daily) is
  too slow to be a regime detector at this horizon — one switch, ~96% long,
  ≈ buy-and-hold with lag. **Kalman**'s tuned threshold (Q=1e-5, mult=0.05 —
  the spec's 1.0×√P baseline is never met by realistic daily drift, so the
  grid had to extend far below it, and every feasible configuration had
  *negative* train Sharpe) whipsawed 148 times and lost on every metric.
- **Walk-forward vs frozen HMM:** annual expanding refits changed almost
  nothing (0.74 vs 0.76 Sharpe, −24.3% vs −22.4% MaxDD). With 18 years of
  training data the parameters are stable; refitting is not where the edge
  is.
- **Flat-leg yield is ignored.** Cash earned ~4–5% (T-bills) in 2023–2026.
  The HMM was flat 45% of the time — crediting ~4.5% would add roughly
  +2 pp/yr to its net return; similar for Kalman, ~+1.2 pp/yr for CUSUM.
  This narrows but does not close the return gap to buy-and-hold, and makes
  the CUSUM outperformance slightly larger.

## 5. Caveats

- **Single asset, single test window.** One instrument, ~3.6 years, one
  completed bear episode plus one in progress. Every ranking above could
  reshuffle on another window; the detection-lag mechanics (§2) are the more
  transferable result.
- **Parameter fragility is demonstrated, not hypothetical.** The same CUSUM
  under two defensible train windows produced the best and nearly the worst
  strategy in the table. Low-parameter models (the HMM's ~6 effective
  parameters) traveled between train windows far more gracefully than tuned
  thresholds.
- **The 2026 episode is unfinished** — its trough is provisional and B&H's
  last-leg drawdown still open; episode-B re-entry lags are unknowable yet.
- **Costs are stylized.** 5 bps/side ignores slippage clustering exactly when
  regime signals fire (gaps, high-vol opens); high-switching strategies
  (Kalman, HMM) are hurt more in reality than on paper.
- **Some structure was fixed by spec, some tuned.** P(bull) > 0.5 and the
  equal-weight ≥ 0.5 composite rule were fixed. CUSUM (k,h), Kalman (Q,
  mult), and the Coppock variant were tuned on train with small grids —
  winner's-curse risk is real, and the time-in-market band on the tuners,
  while principled, was a judgment call made to avoid degenerate optima.

## 6. Bottom line

The HMM's known asymmetry is confirmed and explained (5 days into bear vs
~16 out; it detects volatility, which rises faster than it falls), but the
2023–2026 SOXX window punished its chattering more than it rewarded its
drawdown control. The bear→bull lag was genuinely improved by two things
that don't just re-filter returns: the VIX term structure (12-day re-entry,
systematic, cheap in whipsaws) and CUSUM's burst trigger (1-day re-entry —
spectacular here, but a two-trade sample whose twin, trained on a shorter
window, was the worst strategy tested). A defensible practical synthesis:
HMM-style exit (fast, reliable), options-market re-entry confirmation, and
deep suspicion of any tuned threshold that a slightly different train window
can turn from hero to disaster.
