"""Chart GOOG factor-model residuals over time (market-factor model, through Fri)."""
import numpy as np, pandas as pd, yfinance as yf, statsmodels.api as sm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

END = pd.Timestamp("2026-05-15"); START = END - pd.DateOffset(years=5)
dl = yf.download(["GOOG", "^GSPC", "^IRX"], start=START - pd.Timedelta(days=10),
                 end=END + pd.Timedelta(days=1), progress=False,
                 auto_adjust=True)["Close"]
g = dl["GOOG"].pct_change().dropna() * 100
m = dl["^GSPC"].pct_change().dropna() * 100
rf = (dl["^IRX"] / 100 / 252).reindex(m.index).ffill()
B = pd.DataFrame({"GOOG": g, "MKT": m, "RF": rf}).loc[START:END].dropna()
B["y"] = B["GOOG"] - B["RF"]; B["x"] = B["MKT"] - B["RF"]
fit = sm.OLS(B["y"], sm.add_constant(B["x"])).fit()
e = fit.resid
sd = e.std()
cum = e.cumsum()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 9), sharex=True,
                               gridspec_kw={"height_ratios": [1.15, 1]})

# --- daily residuals ---
ax1.bar(e.index, e.values, width=1.0,
        color=np.where(e >= 0, "#2e7d32", "#c62828"), alpha=0.65)
for k, ls in [(2, "--"), (3, ":")]:
    ax1.axhline(k * sd, color="grey", ls=ls, lw=0.9)
    ax1.axhline(-k * sd, color="grey", ls=ls, lw=0.9,
                label=f"±{k}σ ({k*sd:.1f}%)")
ax1.axhline(0, color="black", lw=0.6)
ax1.set_title("GOOG idiosyncratic daily return (market-factor model residual)  "
              f"|  daily σ={sd:.2f}%, ann. idio vol={sd*np.sqrt(252):.1f}%",
              fontsize=12, weight="bold")
ax1.set_ylabel("residual (%)"); ax1.legend(loc="lower left", fontsize=9)
ax1.margins(x=0.01)

# --- cumulative residual ---
ax2.plot(cum.index, cum.values, color="#1565c0", lw=1.4)
ax2.fill_between(cum.index, cum.values, 0,
                 where=cum.values >= 0, color="#1565c0", alpha=0.12)
ax2.fill_between(cum.index, cum.values, 0,
                 where=cum.values < 0, color="#c62828", alpha=0.12)
ax2.axhline(0, color="black", lw=0.6)
ax2.scatter([cum.index[-1]], [cum.values[-1]], color="#d84315", zorder=5)
ax2.annotate(f"Fri {cum.index[-1].date()}\ncum={cum.values[-1]:+.1f}%",
             (cum.index[-1], cum.values[-1]),
             textcoords="offset points", xytext=(-70, 10),
             fontsize=9, color="#d84315", weight="bold")
ax2.set_title("Cumulative idiosyncratic return (residual run-up / drawdown)",
              fontsize=12, weight="bold")
ax2.set_ylabel("cumulative residual (%)")
ax2.xaxis.set_major_locator(mdates.YearLocator())
ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax2.margins(x=0.01)

fig.tight_layout()
fig.savefig("/home/user/CC-Mobile/goog_residuals.png", dpi=130)
print("saved goog_residuals.png  |  obs:", len(e),
      "| range:", e.index[0].date(), "->", e.index[-1].date())
