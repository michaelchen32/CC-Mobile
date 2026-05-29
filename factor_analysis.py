#!/usr/bin/env python3
"""
Factor attribution + crowdedness analysis for the 30-name large-cap
20-trading-day momentum basket (May 2026).

NOTE ON METHOD: This is NOT a statistical PCA on a price-return covariance
matrix -- no per-name daily price history feed is available in this
environment. Instead it is a transparent *characteristic-based* factor
decomposition: each name is tagged with theme + style exposures and
crowding inputs (estimates grounded in public market commentary, late
May 2026), then aggregated. Numeric inputs (beta, short interest %,
retail/HF/valuation 1-5 scores) are analyst estimates and are stated
explicitly so the reader can adjust them.
"""

from collections import defaultdict

# ticker: (theme, ret_20d%, mcap_$B, profitable(1/0), beta, short_int_%,
#          retail_options(1-5), hf_crowding(1-5), valuation_stretch(1-5))
D = {
 "RKLB":("Space",        87.8, 85.7, 0, 2.9, 17, 5, 3, 5),
 "ASTS":("Space",        87.7, 51.7, 0, 3.2, 22, 5, 3, 5),
 "UMC": ("AI-Semi",      73.8, 56.9, 1, 1.5,  3, 2, 2, 2),
 "ALAB":("AI-Semi",      72.3, 59.9, 1, 2.6,  8, 3, 4, 5),
 "MU":  ("AI-Semi",      70.3,120.0, 1, 1.7,  4, 3, 5, 3),
 "SNOW":("Cloud-SW",     69.7, 82.9, 0, 1.6,  6, 3, 3, 4),
 "HUT": ("Crypto-Miner", 61.4, 14.0, 0, 3.2, 14, 4, 2, 4),
 "DDOG":("Cloud-SW",     60.3, 80.2, 1, 1.7,  5, 3, 3, 4),
 "ARM": ("AI-Semi",      58.8,358.0, 1, 1.6,  5, 3, 4, 5),
 "STRL":("AI-Infra-Build",58.3,25.9, 1, 1.7,  6, 2, 3, 3),
 "FLEX":("AI-Hardware",  58.0, 53.1, 1, 1.5,  4, 2, 3, 2),
 "SMTC":("AI-Semi",      54.3, 15.5, 1, 2.2,  9, 3, 3, 4),
 "SMCI":("AI-Hardware",  52.5, 24.8, 1, 2.8, 18, 5, 3, 3),
 "GH":  ("HealthTech",   52.1, 17.7, 0, 1.8, 13, 3, 2, 3),
 "AAON":("AI-Infra-Build",52.0,11.7, 1, 1.4,  7, 2, 3, 4),
 "IONQ":("Quantum",      51.8, 26.2, 0, 3.3, 24, 5, 2, 5),
 "DELL":("AI-Hardware",  50.9,206.0, 1, 1.4,  4, 3, 4, 2),
 "FTNT":("Cyber-SW",     50.3, 95.0, 1, 1.4,  4, 2, 3, 3),
 "RIOT":("Crypto-Miner", 50.0, 10.5, 0, 3.3, 20, 5, 2, 4),
 "APLD":("AI-DataCenter",48.0, 14.2, 0, 3.0, 16, 4, 3, 5),
 "DOCN":("Cloud-SW",     47.7, 15.9, 1, 1.8, 11, 3, 2, 3),
 "CRWD":("Cyber-SW",     47.3,170.8, 1, 1.5,  4, 3, 4, 5),
 "CIFR":("Crypto-Miner", 44.3, 10.1, 0, 3.0, 18, 4, 2, 4),
 "QBTS":("Quantum",      43.9, 10.9, 0, 3.4, 21, 5, 2, 5),
 "AMD": ("AI-Semi",      43.7,845.0, 1, 1.9,  3, 5, 5, 4),
 "FSLR":("Solar/Policy", 43.3, 32.6, 1, 2.2,  9, 3, 3, 3),
 "PANW":("Cyber-SW",     42.4,209.0, 1, 1.3,  3, 2, 3, 3),
 "IREN":("Crypto-Miner", 40.3, 22.9, 0, 3.1, 15, 4, 2, 4),
 "F":   ("Auto/Cyclical",40.2, 66.4, 1, 1.3,  6, 3, 2, 2),
 "PL":  ("Space",        39.3, 18.3, 0, 2.6, 12, 3, 3, 4),
}

N = len(D)
TH, RET, MC, PRF, BETA, SI, RTL, HF, VAL = range(9)

# Map themes -> macro super-factor
SUPER = {
 "AI-Semi":"AI-Infrastructure","AI-Hardware":"AI-Infrastructure",
 "AI-Infra-Build":"AI-Infrastructure","AI-DataCenter":"AI-Infrastructure",
 "Cloud-SW":"Cyber/Cloud-SW","Cyber-SW":"Cyber/Cloud-SW",
 "Crypto-Miner":"Crypto/Digital-Asset","Space":"Space",
 "Quantum":"Quantum","HealthTech":"Idiosyncratic",
 "Solar/Policy":"Idiosyncratic","Auto/Cyclical":"Idiosyncratic",
}

def avg(xs): return sum(xs)/len(xs) if xs else 0

print("="*70)
print("1.  THEME / SUPER-FACTOR DECOMPOSITION  (what bucket is the rally?)")
print("="*70)
buckets = defaultdict(list)
for t,v in D.items(): buckets[SUPER[v[TH]]].append((t,v))
print(f"{'Super-factor':<22}{'#':>3}{'%basket':>8}{'avgRet':>8}{'avgMcap$B':>10}")
for sf in sorted(buckets, key=lambda s:-len(buckets[s])):
    rows=buckets[sf]
    print(f"{sf:<22}{len(rows):>3}{100*len(rows)/N:>7.0f}%"
          f"{avg([v[RET] for _,v in rows]):>8.1f}{avg([v[MC] for _,v in rows]):>10.0f}")
print(f"\n  -> AI-Infrastructure + the three 'frontier-tech' buckets "
      "(Space/Quantum/Crypto) make up the bulk of the basket.")

print("\n"+"="*70)
print("2.  STYLE-FACTOR PREVALENCE  (what style signature?)")
print("="*70)
unprofit=[t for t,v in D.items() if v[PRF]==0]
highbeta=[t for t,v in D.items() if v[BETA]>=2.0]
highsi  =[t for t,v in D.items() if v[SI]>=15]
midcap  =[t for t,v in D.items() if v[MC]<50]
def pct(lst): return 100*len(lst)/N
print(f"  Unprofitable / pre-profit (LOW QUALITY):  {len(unprofit):>2}/{N}  ({pct(unprofit):.0f}%)")
print(f"  High beta (>=2.0):                         {len(highbeta):>2}/{N}  ({pct(highbeta):.0f}%)")
print(f"  High short interest (>=15% float):         {len(highsi):>2}/{N}  ({pct(highsi):.0f}%)")
print(f"  Mid-cap (<$50B) vs mega:                    {len(midcap):>2}/{N}  ({pct(midcap):.0f}%)")
print(f"  Momentum: 30/30 (100%) -- basket is defined by it (circular)")
print(f"\n  basket avg beta            : {avg([v[BETA] for v in D.values()]):.2f}")
print(f"  basket avg short interest  : {avg([v[SI] for v in D.values()]):.1f}% of float")
print(f"  cap-wtd is mega (AMD/ARM/PANW/DELL/CRWD) but EQ-wtd tilts mid-cap")

# correlation of return vs each factor (rough driver signal)
def corr(a,b):
    ma,mb=avg(a),avg(b); na=[x-ma for x in a]; nb=[x-mb for x in b]
    num=sum(x*y for x,y in zip(na,nb)); den=(sum(x*x for x in na)*sum(y*y for y in nb))**.5
    return num/den if den else 0
rets=[v[RET] for v in D.values()]
print("\n  Cross-sectional corr of 20d return vs factor (sign = tilt that paid):")
for name,idx in [("beta",BETA),("short-int%",SI),("retail/options",RTL),
                 ("(-)profitability",PRF),("valuation-stretch",VAL),("(-)log mcap",MC)]:
    xs=[v[idx] for v in D.values()]
    c=corr(rets,xs)
    if name.startswith("(-)"): c=-c
    print(f"     {name:<20}{c:+.2f}")

print("\n"+"="*70)
print("3.  CROWDEDNESS SCORECARD")
print("="*70)
print("  LONG-crowding  = mean(retail, hf, valuation) scaled 0-100")
print("  SHORT-crowding = short interest %% (squeeze fuel)")
print("  SQUEEZE COCKTAIL = unprofitable & SI>=15%% & retail>=4\n")
rows=[]
for t,v in D.items():
    longc=100*avg([v[RTL],v[HF],v[VAL]])/5
    shortc=v[SI]
    cocktail = (v[PRF]==0 and v[SI]>=15 and v[RTL]>=4)
    rows.append((t,v[TH],longc,shortc,cocktail))
rows.sort(key=lambda r:-(r[2]+r[3]*2))
print(f"{'Tkr':<6}{'Theme':<16}{'LongCrowd':>10}{'ShortInt%':>10}  Squeeze")
for t,th,lc,sc,ck in rows:
    print(f"{t:<6}{th:<16}{lc:>9.0f}{sc:>10.0f}  {'<<< YES' if ck else ''}")

cocktails=[r[0] for r in rows if r[4]]
print(f"\n  SQUEEZE-COCKTAIL names ({len(cocktails)}): {', '.join(cocktails)}")
print(f"  basket avg LONG-crowd : {avg([r[2] for r in rows]):.0f}/100")
print(f"  basket avg SHORT-int  : {avg([r[3] for r in rows]):.1f}% of float "
      f"(vs ~3% median S&P 500 -> ~{avg([r[3] for r in rows])/3:.1f}x market)")

print("\n"+"="*70)
print("4.  CLUSTER CROWDING SUMMARY")
print("="*70)
print(f"{'Cluster':<22}{'avgLongCrowd':>14}{'avgShortInt%':>14}")
for sf in sorted(buckets, key=lambda s:-len(buckets[s])):
    rows2=buckets[sf]
    lc=avg([100*avg([v[RTL],v[HF],v[VAL]])/5 for _,v in rows2])
    sc=avg([v[SI] for _,v in rows2])
    print(f"{sf:<22}{lc:>13.0f}{sc:>14.1f}")
