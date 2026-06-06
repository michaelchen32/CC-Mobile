"""Plot the walk-forward HMM regimes over the S&P 500. -> results/regimes.png"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd

NAMES = ["Bear", "Neutral", "Bull"]
COLORS = {"Bear": "#d62728", "Neutral": "#ff7f0e", "Bull": "#2ca02c"}


def main():
    o = pd.read_csv("results/regimes.csv", parse_dates=["date"])
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(15, 9), sharex=True,
        gridspec_kw={"height_ratios": [3, 1]})

    # price coloured by filtered regime
    reg = o["regime"].astype(int).values
    d = o["date"].values
    p = o["price"].values
    ax1.set_yscale("log")
    for i, name in enumerate(NAMES):
        mask = reg == i
        ax1.scatter(d[mask], p[mask], s=3, color=COLORS[name], label=name)
    ax1.plot(d, p, color="black", lw=0.4, alpha=0.4)
    ax1.set_title("S&P 500 — HMM market regime (walk-forward, causal/filtered, no look-ahead)",
                  fontsize=13, weight="bold")
    ax1.set_ylabel("S&P 500 (log scale)")
    ax1.legend(loc="upper left", markerscale=4, framealpha=0.9)
    ax1.grid(True, which="both", alpha=0.2)

    # regime probability ribbon
    ax2.stackplot(d, o["pBear"], o["pNeutral"], o["pBull"],
                  colors=[COLORS["Bear"], COLORS["Neutral"], COLORS["Bull"]],
                  labels=NAMES)
    ax2.set_ylim(0, 1)
    ax2.set_ylabel("P(regime)")
    ax2.set_xlabel("Date")
    ax2.margins(x=0)
    ax2.xaxis.set_major_locator(mdates.YearLocator(2))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    last = o.iloc[-1]
    ax1.annotate(f"{last['date'].date()}\nclose {last['price']:,.0f}",
                 xy=(last["date"], last["price"]),
                 xytext=(-90, 20), textcoords="offset points",
                 fontsize=9, arrowprops=dict(arrowstyle="->", color="black"))

    fig.tight_layout()
    fig.savefig("results/regimes.png", dpi=130)
    print("wrote results/regimes.png")


if __name__ == "__main__":
    main()
