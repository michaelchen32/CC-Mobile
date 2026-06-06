# CC-Mobile — HMM Market-Regime Detector

A Hidden Markov Model that detects S&P 500 market-regime changes from ~30 years
of daily returns, trained **walk-forward with no look-ahead**.

## Method

| Choice | Value |
|---|---|
| Underlying | S&P 500 (`^GSPC`) adjusted close, 1995–2026 (7,800 daily returns) |
| Observation | trailing **5-trading-day window** → `[mean daily log-return, realized vol]` |
| Model | 3-state Gaussian HMM (full covariance), `hmmlearn` |
| States | **Bear** / **Neutral** / **Bull** (relabelled each re-fit by mean return) |

**No future data is used, anywhere:**
- Model re-fit once per calendar year on an **expanding window of strictly past data**.
- Feature standardisation uses **train-slice statistics only**.
- The regime probability for day *t* is the **filtered** posterior
  `P(state_t | obs_1..t)` from the forward algorithm — it never sees `obs_{t+1..T}`
  (no Viterbi/smoothing back-pass). Out-of-sample window: 2000–2026 (6,646 days).

## Reproduce

```bash
pip install numpy pandas scipy hmmlearn matplotlib
python3 src/hmm_regime.py     # trains, evaluates, prints the current read
python3 src/plot_regimes.py   # -> results/regimes.png
```

Data cache: `data/gspc.csv`. Outputs: `results/regimes.csv`, `results/regime_stats.csv`,
`results/regimes.png`.

## What the regimes are

| Regime | Ann. drift | Ann. vol | Character |
|---|---|---|---|
| Bear | −27% | 31% | turbulent sell-off |
| Neutral | −6% | 15% | choppy / transitional |
| Bull | +27% | 7% | calm uptrend |

**Validation** — fully out-of-sample, the model flags every major crisis at ~100%
P(Bear): 2008 GFC, the March-2020 COVID crash, and the 2022 bear market. The states
separate **risk** cleanly (7% vs 31% vol); forward next-day returns are best
*risk-adjusted* in Neutral/Bull and noisiest in Bear.

## The read after Friday's close (2026-06-05)

The S&P 500 sat in a **calm Bull regime (~99.8%)** for two weeks, then **Friday fell
~2.6%** (7,584 → 7,384), flipping the model to **Neutral (99.7%)** — elevated
volatility, slightly negative drift. It is **not** (yet) a Bear/crisis read
(P(Bear) ≈ 0.3%). Regimes are persistent (~93% stay-probability), so the base case
into Monday is *still choppy/Neutral*, with a roughly flat-to-slightly-negative
one-step expected return. In plain terms: **Friday's drop broke the calm uptrend and
put the market on watch — turbulent, not yet a downturn.**

> Research/educational use only. Not investment advice.
