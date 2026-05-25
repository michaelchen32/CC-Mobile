# Semiconductor Dispersion — Equity-Only Regime Test

A diagnostic + backtest for the thesis: **the semi sector flatlines overall while
subgroups rotate as funds move between them.**

-----

## Background

A flat sector index that hides internal rotation is, in options language, a
**low realized-correlation / high cross-sectional dispersion** regime. When money
leaves (say) foundry for memory, TSM and MU move in opposite directions — their
individual vols are alive, but they cancel at the index level, so SMH sits still.

The textbook way to trade this is a **dispersion trade**: short index volatility,
long single-name volatility, profiting from the gap between *implied* and *realized*
correlation. But implied correlation is extracted from **option** prices. In an
equity-only world you can’t see it. So this project measures the **realized** side
directly — which is exactly what an equity expression of the trade bets on anyway:

1. **Rolling average pairwise correlation** across constituents — thesis predicts LOW / FALLING.
1. **Cross-sectional return dispersion** — thesis predicts HIGH / RISING.

If both hold, the thesis is playing out and there is something for an equity proxy to harvest.

### Important: this is a *proxy*, not the real dispersion trade

The true trade is a second-moment (variance) bet. Equities only give first-moment
(return) exposure, so the backtest here captures **idiosyncratic return dispersion**,
not the implied-vs-realized **correlation premium**. It leans on the same regime but
is a different P&L source. A good backtest here is **not** evidence the options trade
would work. This is a regime study and a hypothesis — **not investment advice, not a
validated edge.**

-----

## What the script does

**Part 1 — Diagnostic (the test).** Pulls daily adjusted closes for ~25 liquid semis
plus an index ETF (SMH), computes the two series above, and prints a **regime report**:
current readings, their percentile rank over the full sample, the 60-day correlation
trend, and a verdict (FAVORABLE only when correlation is in a low percentile *and*
dispersion is elevated).

**Part 2 — Beta-neutral dispersion proxy (the tradeable expression).** Monthly, goes
long the top-quintile names by idiosyncratic vol (equal weight) and shorts the index
sized to zero out the basket’s beta. Reports annualized return, vol, Sharpe, max
drawdown, realized beta (should be ≈ 0), turnover, and the correlation of strategy
returns to the dispersion series (should be positive — confirms it harvests dispersion).

-----

## Run it

```bash
pip install -r requirements.txt

python semis_dispersion.py                 # live data, full report + chart
python semis_dispersion.py --json          # machine-readable output
python semis_dispersion.py --synthetic     # NO network: validate the pipeline
python semis_dispersion.py --start 2015-01-01 --top-quantile 0.25 --no-plot
```

Flags: `--index`, `--universe` (comma-separated), `--start`, `--end`,
`--beta-window`, `--top-quantile`, `--synthetic`, `--json`, `--no-plot`, `--outfile`.

### Verify first with `--synthetic`

`--synthetic` builds a known two-regime dataset (high correlation, then a rotation
regime) with no network. Use it to confirm everything runs. **Expected:** correlation
reads high in the first half and collapses in the second, dispersion rises, realized
beta ≈ 0. The backtest **Sharpe will be negative/meaningless in synthetic mode** — the
synthetic names are pure noise with no return premium, so this validates the plumbing
and the diagnostic, *not* profitability. Then switch to live data.

-----

## Reading the output

- **`verdict`** is the headline: is the regime supportive *right now*?
- **`corr_percentile` low + `corr_60d_change` negative** = thesis actively playing out.
- **`realized_beta_to_index` ≈ 0** confirms the hedge worked; far from 0 means the
  beta estimate is stale (try a shorter `--beta-window`).
- **`strat_dispersion_corr` positive** confirms the basket is loading on dispersion.
- The most valuable single number on the first live run is the **correlation
  percentile** — if it isn’t low, the thesis hasn’t started and there’s nothing to harvest yet.

-----

## Caveats (read before trusting any Sharpe)

- Equity proxy ≠ the options dispersion trade (see above).
- **No transaction costs, no borrow/shorting costs.** Both flatter results.
- **Survivorship bias:** today’s constituent list is applied to the whole history.
- Lookback windows are not tuned; treat them as starting points, not optimized values.

-----

## Natural next steps

- Add a **dispersion-timing overlay**: only deploy the basket when correlation is in a
  low percentile, flat otherwise.
- Add a **transaction-cost model** (per-side bps + borrow) and re-check Sharpe.
- Break the universe into **subgroups** (memory / foundry / EDA / WFE / analog / compute)
  to see *which* groups are decoupling, not just that decoupling is happening.
