# US Large-Cap Breakout Screen

A breakout-detection screen over **all US-listed stocks with market cap >$10bn**
(~885 names). Clean-room implementation: universe construction, data access,
breakout detection, and a ranked narrative brief.

> Educational analysis only — **not investment advice**.

## Quick start

```bash
pip install -r requirements.txt
python run_screen.py 2026-07-17      # explicit trading session (latest close)
python run_screen.py                 # today
```

Outputs land in `results/`:
- `screen_<date>.csv` — ranked signal table
- `breakout_brief_<date>.md` — narrative brief (sector-grouped, conviction tiers)

## How it works

```
screener/
  data.py        # OHLCV via yfinance over a plain requests.Session (see below)
  universe.py    # Nasdaq screener API -> filter market cap >$10bn
  detectors.py   # 8-detector high-recall breakout union + trend tag
  screen.py      # orchestrator: universe -> fetch -> detect -> enrich -> rank
run_screen.py    # entry point + brief writer
```

### Data access (the important bit)

Modern **yfinance (>=1.5) uses `curl_cffi` with a browser-impersonated TLS
fingerprint by default.** Behind an intercepting HTTPS proxy that re-terminates
TLS, that impersonated handshake gets reset (`curl (35) Recv failure: Connection
reset by peer`), so every request dies. Naked `curl` to the Yahoo chart endpoint
fails differently — HTTP 429, because it sends no cookie/crumb.

**The fix:** hand yfinance a plain `requests.Session`. It is proxy-aware, trusts
the environment CA bundle, performs yfinance's normal cookie+crumb handshake, and
avoids the impersonated TLS the proxy rejects. See `screener/data.py`.

### Universe

Pulled live from the Nasdaq stock screener API (every NYSE/Nasdaq/AMEX name with
a market-cap figure), filtered to >$10bn, with warrants/units/rights/preferreds
dropped and symbols normalised for yfinance (`BRK/B` → `BRK-B`).

### Detectors (high-recall OR-union)

Any single detector firing = a signal; `n_detectors` measures confluence. The
`trend` tag (`up`/`weak`/`down`) is context only and never suppresses a signal.

| Detector | Rule |
|---|---|
| `fast_donchian` | close > prior 10-day high |
| `donchian_20` | close > prior 20-day high |
| `six_month_high` | close ≥ prior 126-day high |
| `volume_thrust` | ≥5% up day AND ≥2× 20-day avg vol AND close in top 30% of range |
| `gap_go` | gap up ≥2.5% and holds the open |
| `range_expansion` | true range ≥2× ATR(20) while pushing the 10-day high |
| `squeeze_release` | TTM squeeze (BB inside Keltner) releases with positive momentum |
| `trend_continuation` | uptrend (c>SMA50>SMA150), new 5-day high right after a ≥3% dip |

**Interpretation:** multi-detector (`n_det≥4`) breakouts with `trend=up` are the
high-quality signals; single-detector `gap_go`-only fires are the fragile,
high-false-alarm cohort.

## Caveats

- Prices are auto-adjusted OHLCV from Yahoo Finance; occasional bad ticks happen.
- Sector/revenue-growth enrichment is best-effort via `Ticker.get_info()` and
  degrades to `Unknown` on failure.
- High recall means high false-alarm rate by design — a signal is a research
  starting point, not a recommendation.
