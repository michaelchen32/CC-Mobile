# Factor Analysis & Crowdedness — 30-Name Large-Cap 20-Day Momentum Basket (May 2026)

**What this is:** a characteristic-based factor decomposition of the top-30 basket, not a
PCA on a return covariance matrix (no per-name price-history feed is available here). Each
name is tagged with theme + style exposures and crowding inputs; numbers are analyst
estimates, stated explicitly in `factor_analysis.py` so they can be adjusted. Grounded in
late-May 2026 market commentary (Goldman flow notes, short-interest screens, HF positioning).

> **Important stats caveat:** the *within-basket* cross-sectional correlations are weak
> (range restriction — every name already won, so the spread carries little signal). The
> real factor story is what these 30 share **versus the market**, not the rank order inside
> the basket. Only valuation-stretch shows a meaningful within-basket tilt (+0.20).

---

## 1. What's driving the rise

### A. The dominant driver is THEME, not a classic style factor
| Super-factor | # of 30 | % basket | Avg 20d ret |
|---|---|---|---|
| AI-Infrastructure | 12 | 40% | +57.7% |
| Cyber/Cloud Software | 6 | 20% | +52.9% |
| Crypto / Digital-Asset miners | 4 | 13% | +49.0% |
| Space | 3 | 10% | +71.6% |
| Quantum | 2 | 7% | +47.8% |
| Idiosyncratic (GH, FSLR, F) | 3 | 10% | +45.2% |

**~90% of the basket is four narratives: AI-infrastructure + the three "frontier-tech"
complexes (Space, Quantum, Crypto-miner).** This is a *thematic* rally — the "hardware golden
age" AI-capex trade plus frontier speculation — far more than a broad value/quality/size rotation.
Space and Quantum posted the highest average moves (+72%, +48%) but on the fewest, most
speculative names.

### B. The style signature: Momentum × High-Beta × Low-Quality × Mid-Cap
| Style factor | Prevalence | Read |
|---|---|---|
| Momentum | 30/30 (100%) | tautological — basket is defined by it |
| High beta (β ≥ 2.0) | 14/30 (47%); **basket avg β ≈ 2.2** | ~2× market sensitivity — a leveraged risk-on bet |
| Low quality (unprofitable / pre-profit) | 12/30 (40%) | classic late-cycle "junk rally" tell |
| Size (mid-cap < $50B) | 15/30 (50%) | equal-weight tilts small; cap-weight is mega (AMD/ARM/PANW) |
| Long-duration growth | most of basket | rate-sensitive; a dovish/falling-yield backdrop is a tailwind |

This is the textbook **risk-on, high-beta, anti-quality** factor cocktail — the profile that
leads in liquidity-driven, sentiment-fueled advances and that also reverses hardest.

### C. The mechanical driver: a short squeeze
- Basket **average short interest ≈ 10.4% of float — roughly 3.5× the ~3% median S&P 500 name.**
- 30% of names sit above 15% short interest; Quantum (avg ~22.5%) and Space (~17%) are the most-shorted clusters.
- This is corroborated externally: IonQ's run was explicitly tied to federal funding + a looming
  squeeze; Bloomberg flagged a space-stock squeeze (RKLB/LUNR); Goldman attributed a multi-billion
  move to algo/HF short-covering. **A meaningful slice of these gains is shorts being forced to cover,
  not fresh fundamental conviction.**

### D. Macro backdrop
Record hedge-fund semiconductor long weight (~10%, highest ever), risk-on positioning, and a
rate/liquidity tailwind for long-duration growth — with the same desks buying puts on NVDA/AMD/AVGO,
i.e. hedging an overheat.

---

## 2. Crowdedness — two very different kinds

Crowding here splits cleanly into **long-crowding** (HF + retail + valuation → unwind risk) and
**short-crowding** (short interest → squeeze fuel). The dangerous names score high on *both*.

### Cluster crowding map
| Cluster | Avg long-crowd (0-100) | Avg short interest | Crowding type |
|---|---|---|---|
| Quantum | 80 | 22.5% | **Both** — max reflexivity |
| Space | 80 | 17.0% | **Both** — squeeze + retail |
| Crypto-miner | 68 | 16.8% | **Both** — crypto-beta + squeeze |
| AI-Infrastructure | 67 | 7.2% | Mostly **crowded longs** (HF) |
| Cyber/Cloud SW | 62 | 5.5% | Moderate long; HFs trimming SW |
| Idiosyncratic | 53 | 9.3% | Low / stock-specific |

### The "squeeze cocktail" — unprofitable + SI ≥ 15% + heavy retail/options (8 names)
**ASTS, IONQ, QBTS, RKLB, RIOT, APLD, CIFR, IREN.** These are the most reflexive, most fragile
names — they rose on a self-reinforcing loop of retail call-buying and short-covering, and they
are the first to gap down when flows reverse.

### Two crowding archetypes to separate
1. **Crowded LONGS, low short interest (positioning risk, not squeeze):** AMD (long-crowd 93),
   ARM, CRWD, MU, DELL, PANW. These are consensus institutional holdings — record HF semi weight.
   Risk is a *de-grossing / unwind*, not a squeeze. Note the HF put-hedging on AMD/NVDA/AVGO.
2. **Crowded BOTH ways (reflexive squeeze):** the 8 cocktail names above. Risk is violent in
   *both* directions.

A nuance on software: SNOW/DDOG/DOCN rallied even as Goldman reports HFs are **dumping software**
to fund semis — so their move looks more like short-covering + retail catch-up than fresh
institutional crowding.

---

## 3. Bottom line

- **Why it rose:** ~90% theme (AI-infra + frontier tech), expressed through a high-beta (≈2.2×),
  low-quality (40% unprofitable), mid-cap-tilted momentum factor — and amplified mechanically by
  a short squeeze (SI ≈ 3.5× the market).
- **Crowding:** high and concentrated. The basket is **the momentum factor itself**, which is among
  the most crowded trades on the Street. Within it, two failure modes: a *positioning unwind* in the
  crowded-long mega semis (AMD/ARM/MU/CRWD), and a *squeeze reversal* in the 8 cocktail names
  (quantum/space/crypto).
- **Fragility:** because exposures are highly correlated (one theme, high beta, low quality, shared
  squeeze fuel), intra-basket diversification is largely illusory — these names will tend to fall
  together as hard as they rose. Falling yields / sustained AI-capex = continuation; any liquidity,
  rate, or AI-capex-doubt shock = sharp, correlated drawdown led by the lowest-quality, most-shorted names.
