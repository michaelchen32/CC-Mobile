# Market Regime Detection on SOXX — Analysis

**Test window:** 2023-01-03 → 2026-07-31 (out-of-sample, ~3.6 years).
**Train window:** 2016-08-01 → 2022-12-30 (all parameter fitting and tuning).
**Execution:** signals from day *t*'s close earn day *t+1*'s return; 5 bps per side on every switch.

## 0. Data caveat (read first)

Yahoo Finance was persistently rate-limited from this environment (HTTP 429 on
every endpoint over ~40 minutes of exponential backoff), so prices come from
Nasdaq's free API: split-adjusted daily OHLCV back-adjusted for dividends using
Nasdaq's own dividend history (same convention as Yahoo's adjusted close).
Nasdaq serves at most ~10 years of history, so **SOXX starts 2016-08-01, not
2005-01-01** as the spec requested. The train window is therefore ~6.4 years
(1,610 daily returns) instead of ~18. This matters: 2016–2022 contains two
crash-recoveries (2018Q4, 2020 COVID) and one grinding bear (2022), and the
tuned CUSUM/Kalman parameters lean heavily on that 2022 experience. VIX and
VIX3M come from CBOE's published history CSVs (authoritative source). The
automated look-ahead audit and all protocol rules are unaffected.

## 1. HMM parameter estimates (frozen fit, train window only)

Two-state Gaussian HMM on daily log returns, EM with 5 seeded restarts
(best log-likelihood 4216.05):

| State | Daily mean | Daily vol | Annualized | Self-transition | Expected duration |
|---|---|---|---|---|---|
| **Bull** (state 0) | +0.223% | 1.26% | +56%/yr, 20% vol | 0.9846 | ~65 trading days |
| **Bear** (state 1) | −0.129% | 2.94% | −32%/yr, 47% vol | 0.9765 | ~43 trading days |

The classic picture: a low-volatility drifting-up state and a high-volatility
drifting-down state, both highly persistent. Note the states are separated far
more by **volatility** (2.3×) than by mean — the HMM is largely a volatility
classifier with a drift tie-breaker, which is exactly why it exits fast (vol
spikes instantly at the top) and re-enters late (vol stays elevated at the
bottom).

## 2. Detection lags at the two major test-window drawdowns

Episodes identified from the data: **(A)** peak 2024-07-10 → trough 2025-04-08,
−41.4% (the AI-semis unwind; recovery 2025-09-18); **(B)** peak 2026-06-22 →
trough 2026-07-29, −29.0% (ongoing at the data edge — trough provisional).

Trading days from peak to bear flip / trough to bull flip:

| Algorithm | A: peak→bear | A: trough→bull | B: peak→bear | B: trough→bull |
|---|---|---|---|---|
| HMM (frozen) | **5** | 16 | **0** | still bear |
| HMM (walk-forward) | **5** | 16 | **0** | still bear |
| CUSUM | 185 (at the low) | 262 | never | — |
| Coppock | never turned bear | — | never | — |
| Kalman drift | **1** | 23 | 1 | still bear |
| VIX term structure | 17 | **12** | never | — |
| Composite (≥2 of 4) | 185 | 16 | never | — |
| Composite + contango gate | 17 | 16 | never | — |

**On the asymmetry hypothesis.** The HMM shows exactly the documented pattern,
but milder than folklore suggests: ~5 days into bear, ~16 days out of it
(3× asymmetric), and in episode B it flagged the bear on the very day of the
peak. Did the alternatives fix the slow bear→bull side?

- **VIX term structure is the only signal that re-entered faster** (12 days):
  the VIX3M/VIX ratio normalizes as soon as panic pricing leaves the front of
  the curve, which happens near the bottom rather than after a long streak of
  calm returns. It was, however, slower into the bear (17 days) and never
  flagged episode B at all — VIX barely inverted in the 2026 selloff.
- **Kalman was the fastest into bear** (1 day — a drift filter reacts to the
  first big negative return) but *slower* out (23 days), because the filtered
  drift must climb from deeply negative through the significance threshold.
- **CUSUM and Coppock did not fix anything** — see §4.
- The composite inherits the median voter, so it fixed nothing either; the
  contango-gated variant at least exited with the VIX overlay (17 days).

Conclusion: the bear→bull lag is intrinsic to *return-statistics* detectors
(HMM, Kalman, CUSUM all wait for enough calm/positive returns to accumulate).
The one genuine fix came from switching information source — the options
market's term structure — not from a better filter on the same returns.

## 3. Re-entry speed vs false-positive cost

Whipsaws = bull runs shorter than 10 trading days in the test window:

| Algorithm | Trough→bull (ep. A) | Whipsaws | Switches (test) |
|---|---|---|---|
| VIX term structure | 12 | 8 | 34 |
| HMM (frozen) | 16 | 32 | 90 |
| Composite | 16 | 14 | 37 |
| Kalman | 23 | 52 | 118 |
| CUSUM | 262 | 0 | 3 |

The HMM's fast re-entry is bought with heavy chattering: 90 switches in 3.6
years (a round trip every ~2 weeks on average), 32 of them sub-10-day bull
stints — the filtered probability hugs the 0.5 line in mixed tape. At 5 bps a
side this costs ~1.6 pp of annualized return (26.4% gross → 24.8% net). The
VIX overlay achieves *faster* re-entry with a quarter of the switching. A
hysteresis band (e.g. enter >0.6, exit <0.4) would likely cut HMM whipsaws
substantially, but was not part of the specified design and was not tuned.

## 4. Net-of-cost performance ranking (test window)

| Strategy (net) | Ann. return | Vol | Sharpe | Sortino | MaxDD | Calmar | Time in mkt |
|---|---|---|---|---|---|---|---|
| Buy & hold | 53.0% | 37.9% | 1.12 | 1.09 | −41.4% | 1.28 | 100% |
| VIX term structure | 42.7% | 34.4% | 1.03 | 0.99 | −34.7% | 1.23 | 95% |
| Coppock | 40.9% | 37.4% | 0.92 | 0.88 | −41.4% | 0.99 | 97% |
| HMM (walk-forward) | 25.5% | 23.6% | 0.96 | 0.75 | −28.5% | 0.90 | 59% |
| HMM (frozen) | 24.8% | 22.2% | 1.00 | 0.78 | −17.9% | **1.39** | 53% |
| Composite + gate | 25.0% | 32.4% | 0.69 | 0.62 | −34.2% | 0.73 | 83% |
| Composite | 22.3% | 33.8% | 0.59 | 0.53 | −40.3% | 0.55 | 86% |
| Kalman | 12.1% | 20.0% | 0.57 | 0.37 | −23.5% | 0.52 | 32% |
| CUSUM | 2.3% | 30.0% | 0.08 | 0.05 | −43.3% | 0.05 | 59% |

**Honest read: nothing beat buy-and-hold on Sharpe.** SOXX compounded at 53%
a year over this window; a long/flat overlay can only subtract exposure from
that. The one clean win is the frozen-parameter **HMM on Calmar (1.39 vs
1.28)** — it more than halved the max drawdown (−17.9% vs −41.4%) while
keeping a Sharpe of 1.00, which is the risk-management story these models are
actually for. Every other strategy lost on both measures.

Specific post-mortems:

- **CUSUM is the disaster case, and instructively so.** Train-window tuning
  chose k=0.5, h=6 (grid in `cusum_train_grid.csv`; train Sharpe 0.75 — beat
  looser settings because going flat early and staying flat was rewarded in
  2018/2020/2022). Out of sample that drift term k=0.5 makes the bull-side
  accumulator S⁺ = Σ(z−0.5) nearly unreachable: it triggered bear essentially
  **at the April-2025 low** (185 days after the peak), then needed **262
  trading days** to re-arm, sitting flat through the entire +130% recovery,
  and was long again just in time for the −29% June-2026 drawdown. Sold the
  low, bought the next high. A textbook overfit-to-train outcome.
- **Coppock** (daily variant chosen on train, Sharpe 0.45 vs 0.37 monthly)
  is too slow for state detection at this horizon: with ~10-month lookbacks it
  simply never left the bull state after mid-2023 and delivered buy-and-hold
  with a small lag drag. Its two whipsaws happened at the choppy 2023 start.
- **Kalman** exited superbly (1 day after both peaks) but its tuned threshold
  (Q=1e-5, mult=0.5; note the spec's mult=1.0 baseline puts the bar at
  ~0.7%/day drift, which is never met — the tuned grid had to extend below it,
  and a 20% minimum time-in-market floor was imposed to reject degenerate
  always-flat optima) still keeps it out of the market two-thirds of the
  time. In a 53%/yr tape that's fatal for returns.
- **Walk-forward vs frozen HMM:** annual expanding refits changed little
  (Sharpe 0.96 vs 1.00) and actually *worsened* drawdown (−28.5% vs −17.9%):
  the 2023-refit parameters, diluted by more calm data, held P(bull) higher
  through the early-2025 top. With ~6 years of training data the frozen
  parameters were already stable; refitting is not where the edge is.
- **Flat-leg yield is ignored.** Cash earned ~4–5% (T-bills) over 2023–2026.
  The HMM was flat 47% of the time — crediting ~4.5% on the flat leg would add
  roughly +2 pp/yr to its net return (and similar for Kalman/CUSUM), narrowing
  but not closing the return gap to buy-and-hold. Sharpe comparisons vs a
  rf=0 benchmark are likewise slightly unkind to the flat-heavy strategies.

## 5. Caveats

- **Single asset, single test window.** One instrument, ~3.6 years, and one
  and a half bear episodes out of sample. Every ranking above could reshuffle
  on another asset or window; treat the detection-lag table (which is about
  mechanics, not luck) as the more transferable result.
- **Short train sample (data-source limitation).** 6.4 years of training data
  instead of the intended 18. CUSUM's and Kalman's tuned parameters are
  clearly fragile (CUSUM's train Sharpe of 0.75 collapsed to 0.08 out of
  sample); the HMM, with only ~6 effective parameters, traveled much better
  than the tuned-threshold methods — small-parameter models degrade more
  gracefully.
- **The 2026 episode is unfinished.** Its "trough" is the last data point's
  neighborhood; re-entry lags for episode B are unknowable yet, and B&H's
  final-leg drawdown is still open.
- **Costs are stylized.** 5 bps/side is reasonable for SOXX today, but ignores
  slippage clustering exactly when regime signals fire (gaps, high-vol opens).
  High-switching strategies (HMM, Kalman) are hurt more in reality than here.
- **Threshold 0.5 on P(bull)** and the equal-weight composite rule were fixed
  by spec, not tuned — but the CUSUM/Kalman/Coppock variant choices were
  tuned on train, and with grids this small the winner's-curse risk is real.

## 6. Bottom line

The known HMM asymmetry is confirmed but modest here (5 days into bear vs ~16
out), and it is the *best* overall regime detector in the suite — fastest
useful exits, acceptable re-entry, and the only strategy to beat buy-and-hold
on any headline metric (Calmar, via a max drawdown less than half the
market's). Of the alternatives, only the VIX term structure improved re-entry
speed (12 days, with far fewer whipsaws), because it reads a different market
rather than filtering the same returns harder. CUSUM and Coppock, as tuned on
this train window, failed at the task. If the goal is faster bear→bull
recovery detection, combine the HMM's exit with an options-market re-entry
trigger rather than searching for a better filter on price alone.
