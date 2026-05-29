# Statistical Factor Analysis & Crowdedness — Daily Returns (20d & 60d)

**Data:** actual Yahoo Finance daily adjusted closes, 30-name basket + 11 factor-proxy ETFs,
123 aligned daily returns through **2026-05-29**. Reproducible in `factor_analysis_daily.py`.
**Factors:** MKT=SPY, Mom=MTUM, Qual=QUAL, LowVol=USMV, Size=IWM, Growth=IWF, Value=IWD,
Semis/AI=SMH, Spec-growth=ARKK, Crypto=IBIT, Duration=TLT.

> Caveat: the 20d window has only 20 observations, so its multi-factor and single-stock betas
> are noisy — the 60d regressions are the more reliable read. Risk-on months push the factor
> ETFs to co-move, which inflates *univariate* correlations; the *multivariate* regression is
> what isolates the true marginal drivers.

---

## 1. What's driving the rise

### Equal-weight basket, multi-factor OLS
| Factor | 20d β (t) | 60d β (t) |
|---|---|---|
| alpha | +1.0%/day (4.7)\* | +1.0%/day (3.0)\* |
| MKT (SPY) | 1.49 (1.5) | **0.10 (0.2)** |
| Semis/AI (SMH) | **0.70 (2.9)\*** | **0.70 (4.7)\*** |
| Spec-growth (ARKK) | 0.23 (1.2) | **0.52 (3.6)\*** |
| Crypto (IBIT) | — | −0.12 (−1.0) |
| Duration (TLT) | — | 0.33 (0.9) |

(\* = |t| ≥ 2. Basket R² = 0.87 (20d), 0.79 (60d).)

**Three statistical conclusions:**
1. **The one robust systematic driver is the AI/semiconductor factor (SMH): β ≈ 0.70, significant in
   both windows** (t = 2.9 and 4.7). This is the engine.
2. **It is NOT simply "high market beta."** Once you control for Semis + Spec-growth, the market (SPY)
   beta collapses to **0.10 (insignificant)** over 60d. The basket isn't riding the index — it's riding
   the *AI-hardware + speculative-growth* complex specifically. Over 60d, ARKK (spec-growth) is the
   second significant factor (β = 0.52, t = 3.6).
3. **Large, highly-significant alpha (~+1%/day) survives the factor model**, and single-stock R² vs the
   market is only ~0.21 — i.e. **~80% of each name's variance is idiosyncratic/theme-specific**, not
   explained by broad factors. Translation: a big slice of the move is single-name catalysts and
   short-squeezes, not a common beta wave.

### Style tilts (univariate correlations + betas)
- **High-beta / anti-low-vol is confirmed:** LowVol (USMV) is the only factor with a **negative**
  correlation at 20d (−0.21) and the weakest at 60d; per-stock market beta is enormous (60d **median
  ≈ 2.9, up to 5.1**; 20d median ≈ 5.1). These are ~3–5× market-sensitivity names.
- **Momentum + Size (small) are the strongest style correlations** (Mom ≈ 0.85–0.90, Size/IWM ≈ 0.84–0.88)
  — the basket behaves like a small/mid-cap momentum sleeve.
- **Crypto is a minor, non-significant driver** (corr 0.39–0.47, β insignificant/negative) — the miners
  rose on their own crypto-beta more than as a basket-wide factor.
- Quality/Value/Growth all correlate ~0.75–0.84, but that's the risk-on month pushing every ETF up
  together — they wash out in the multivariate fit, leaving **Semis + Spec** as the marginal drivers.

---

## 2. Crowdedness (PCA + correlation of the 30-name return matrix)

| Metric | 20d | 60d | Read |
|---|---|---|---|
| Avg pairwise correlation | +0.16 | +0.25 | moderate, positive co-movement |
| **PC1 variance share** | **31%** | **31%** | one common factor ≈ ⅓ of all daily movement |
| PC1+PC2 share | 44% | 45% | two factors ≈ 45% |
| **Effective # independent bets** | **6.7** | **7.3** | of a nominal 30 |

**Punchline:** despite holding 30 names, the participation ratio says you effectively own only
**~7 independent bets** — the basket is far less diversified than its name count suggests. A single
common factor (PC1 = the "AI/risk-on momentum" factor) drives ~31% of daily variance, stable across
both windows.

**A nuance worth flagging:** pairwise correlation is *lower* over 20d (0.16) than 60d (0.25). Over the
last month, big single-name catalysts (e.g. the IonQ federal-funding/squeeze pop, individual earnings)
temporarily *de-correlated* day-to-day moves even as price *levels* all rose together. The stable
PC1 = 31% in both windows shows the systematic core didn't change — only the idiosyncratic tail widened
recently. Structurally this is still **one trade wearing 30 tickers.**

---

## 3. Bottom line
- **Driver:** a significant, stable **AI-hardware factor (SMH β≈0.70)** plus, over the longer window, a
  **speculative-growth factor (ARKK β≈0.52)** — *not* generic market beta (SPY β≈0, insignificant once
  controlled). Expressed at ~3–5× market beta with a small/mid-cap momentum tilt and a negative low-vol
  loading.
- **Idiosyncratic alpha is large** (~+1%/day, ~80% of single-name variance) → single-stock catalysts and
  short-squeezes are a major, factor-unexplained part of the rise.
- **Crowding is real but concentrated, not extreme:** ~7 effective bets, PC1 ≈ 31%. The diversification
  within the basket is largely illusory — these will draw down together, led by the highest-beta,
  most-idiosyncratic (most-shorted) names, if the AI-hardware factor rolls over.
