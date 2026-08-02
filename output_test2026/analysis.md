# Scenario: train 2022-01 → 2026-02, test 2026-03 → 2026-07-31

Variant of the main study (see `output/analysis.md`) with the windows the
follow-up request specified: **train 2022-01-04 → 2026-02-27** (1,043 daily
returns — includes the 2022 bear, the 2023–24 bull, and the full 2024-07 →
2025-04 crash/recovery) and **test 2026-03-02 → 2026-07-31** (105 trading
days). Protocol unchanged: strictly causal signals, 1-bar execution lag,
5 bps/side, all tuning on the train window only; the look-ahead audit passes
at four truncation dates inside the new test window.

**Small-sample warning up front:** five months is one market episode, not a
backtest sample. The window is a vertical AI-semis melt-up (SOXX +80% from
early March to the 2026-06-22 peak) followed by a −29% five-week break. All
annualized figures below extrapolate 105 days and should be read as episode
descriptions, not expected returns.

## What the test window contained

Episodes found from the data: **(A)** peak 2026-06-22 → trough 2026-07-29,
−29.0%, unrecovered at the data edge; **(B)** a two-day −12.3% air-pocket
2026-06-03 → 2026-06-05, recovered by 2026-06-15.

## HMM parameters (fit 2022-01 → 2026-02)

| State | Daily mean | Daily vol | Self-transition | Expected duration |
|---|---|---|---|---|
| Bull | +0.205% | 1.85% | 0.9896 | ~96 trading days |
| Bear | −0.272% | 3.25% | 0.9719 | ~36 trading days |

Same structure as the long-history fit, but the bull state's volatility is
half again higher (1.85% vs 1.28% daily) — 2022–2026 was a high-vol era —
and that matters below.

## Results (net of costs, test window)

| Strategy (net) | Ann. return | Sharpe | MaxDD | Calmar | Time in mkt | Switches |
|---|---|---|---|---|---|---|
| Buy & hold | 135.9% | 1.48 | −29.0% | 4.68 | 100% | 0 |
| CUSUM (k=0.5, h=4) | 135.9% | 1.48 | −29.0% | 4.68 | 100% | 0 |
| Coppock (daily) | 135.9% | 1.48 | −29.0% | 4.68 | 100% | 0 |
| Composite | 135.9% | 1.48 | −29.0% | 4.68 | 100% | 0 |
| Kalman (Q=1e-5, m=0.5) | 57.6% | 1.20 | −23.5% | 2.45 | 42% | 10 |
| VIX term structure | 59.9% | 0.85 | −29.0% | 2.07 | 91% | 12 |
| Composite + gate | 59.9% | 0.85 | −29.0% | 2.07 | 91% | 12 |
| HMM (frozen) | 7.7% | 0.31 | −17.2% | 0.45 | 29% | 7 |
| HMM (walk-forward, fit → 2025-12) | −3.4% | −0.15 | −18.8% | −0.18 | 27% | 9 |

## Findings

1. **Nothing beat buy-and-hold; three strategies matched it by doing
   nothing.** CUSUM, Coppock, and the composite never left the bull state in
   the whole test window — zero switches, so their rows are identical to
   B&H. CUSUM's tuned thresholds (chosen on a train window that includes the
   2024–25 crash) never fired even during the −29% July decline, because the
   selloff was spiky: every multi-day plunge was punctuated by rebound days
   that reset the S⁻ accumulator, and the elevated EWMA vol (denominator of
   z) shrank the crash days' z-scores. The detector that was the star of the
   main study (re-entry one day after the 2025 trough) contributed nothing
   here — further evidence that its value is concentrated in rare, violent
   V-bottoms.

2. **The HMM's failure mode is fully exposed: a melt-up at bear-grade
   volatility reads as a bear.** The March–June rally ran at realized vols
   near or above the *bear* state's 3.25%, so filtered P(bull) stayed low
   through most of the biggest up-move in the sample — the HMM was in the
   market only 29% of the time and captured almost none of the rally (7.7%
   annualized vs 135.9%). Its drawdown control still worked (−17.2% vs
   −29%, and it was already bear at the June peak — 0-day detection), but in
   this window the insurance premium consumed nearly the whole return. The
   HMM is a volatility classifier: when volatility and direction decouple,
   it misfires.

3. **Bear detection at the June top was again instantaneous for the
   return-statistics models** (HMM 0 days — already bear; Kalman 1 day;
   walk-forward 0 days), while CUSUM, Coppock, and the VIX overlay never
   flagged it at all (VIX term structure barely inverted). Re-entry can't be
   scored — the drawdown is unrecovered at the data edge, and the fast
   models were still bear on 2026-07-31.

4. **Kalman was the best genuinely active strategy** (Sharpe 1.20, Calmar
   2.45): its tuned threshold (mult=0.5, vs 0.05 on the long-history train)
   kept it long through more of the rally than the HMM, and it exited one
   day after the June peak. Still 78 pp of annualized return behind
   buy-and-hold.

5. **Walk-forward HMM was worse than frozen** (−3.4% vs +7.7%): the
   scheme's annual refit only sees data through 2025-12-31, surrendering the
   Jan–Feb 2026 observations the frozen fit was allowed, and its slightly
   different parameters kept it flat through even more of the rally — a
   clean illustration that refit cadence is itself a risk parameter.

6. **Tuning instability, third data point.** Across the three train windows
   now tested, CUSUM's chosen parameters were (0.5, 6), (0.25, 5), and
   (0.5, 4), producing respectively the worst strategy in the table, the
   best, and a no-op. Kalman's multiplier moved 0.05 → 0.5 between the two
   most recent windows. The HMM's two parametrizations tell one consistent
   story; the threshold detectors tell three different ones.

## Caveats

Beyond the main study's caveats (single asset, stylized costs, ignored cash
yield — worth ~2 pp annualized here to the flat-heavy HMM rows): the test
window is 105 trading days containing one unfinished drawdown; hit rates,
Sharpes, and especially Calmar ratios at this horizon are episode
anecdotes. The train window (4.1 years) is also the shortest of the three
configurations studied, and it overlaps the 2022 bear that the canonical
study used as test-era-adjacent training data.
