# PCA factor / crowding summary

Panel: 42 names, US calendar 2025-06-13 -> 2026-06-12.

| window | n_obs | assets | PC1 | PC2 | PC3 | AR(top k) | avg corr | N_eff |
|---|---|---|---|---|---|---|---|---|
| 20d | 20 | 42 | 30.9% | 22.0% | 11.0% | 86.4% (k=8) | 0.248 | 5.9 |
| 60d | 60 | 41 | 27.0% | 19.0% | 6.6% | 71.7% (k=8) | 0.218 | 8.0 |

## 60d loadings (sorted by PC1)

```
            PC1    PC2    PC3  comm3              sector
LRCX     +0.868 -0.242 +0.064 +0.817             Semicap
AMAT     +0.835 -0.254 -0.048 +0.763             Semicap
MU       +0.766 -0.059 -0.071 +0.595          Memory/HBM
AMD      +0.761 -0.104 +0.128 +0.606  Compute/AI-silicon
COHR     +0.741 -0.299 -0.395 +0.794         Optical/Net
VRT      +0.740 -0.309 -0.159 +0.668         AI-power/DC
SNDK     +0.706 -0.006 -0.056 +0.501          Memory/HBM
AVGO     +0.687 +0.112 -0.092 +0.492  Compute/AI-silicon
TSLA     +0.685 +0.056 +0.167 +0.500            Mega-cap
INTC     +0.677 -0.144 +0.006 +0.479  Compute/AI-silicon
MRVL     +0.674 -0.212 -0.255 +0.564  Compute/AI-silicon
IONQ     +0.645 +0.127 +0.003 +0.432             Quantum
NVDA     +0.639 +0.217 +0.230 +0.508  Compute/AI-silicon
BE       +0.605 -0.278 -0.015 +0.444         AI-power/DC
LITE     +0.592 -0.173 -0.571 +0.706         Optical/Net
AS       +0.582 -0.013 +0.507 +0.596            Consumer
CRDO     +0.579 +0.012 -0.081 +0.342  Compute/AI-silicon
CDNS     +0.559 +0.599 -0.098 +0.681                 EDA
ENPH     +0.557 -0.070 -0.128 +0.331         AI-power/DC
AMZN     +0.547 -0.028 +0.405 +0.464            Mega-cap
QCOM     +0.540 -0.020 -0.122 +0.307  Compute/AI-silicon
LULU     +0.495 +0.322 +0.380 +0.493            Consumer
AAOI     +0.495 -0.123 -0.480 +0.491         Optical/Net
GOOG     +0.442 +0.053 +0.445 +0.395            Mega-cap
DELL     +0.403 +0.350 -0.210 +0.328            Mega-cap
SK Hynix +0.372 -0.094 +0.137 +0.166          Memory/HBM
UBER     +0.349 +0.361 +0.470 +0.474            Mega-cap
KLAC     +0.291 +0.031 +0.259 +0.153             Semicap
Samsung  +0.277 -0.030 +0.080 +0.084          Memory/HBM
CRWD     +0.267 +0.748 -0.222 +0.680        Software/Sec
U        +0.265 +0.484 +0.227 +0.357        Software/Sec
PANW     +0.245 +0.702 -0.218 +0.600        Software/Sec
SHOP     +0.190 +0.679 +0.278 +0.575        Software/Sec
MDB      +0.127 +0.764 -0.170 +0.629        Software/Sec
NKE      +0.106 +0.183 +0.521 +0.316            Consumer
DDOG     +0.101 +0.733 -0.162 +0.574        Software/Sec
NOW      +0.050 +0.909 -0.104 +0.840        Software/Sec
TEAM     +0.004 +0.801 -0.093 +0.650        Software/Sec
HUBS     -0.094 +0.791 -0.061 +0.638        Software/Sec
ADBE     -0.109 +0.839 -0.092 +0.725        Software/Sec
WDAY     -0.176 +0.865 -0.140 +0.800        Software/Sec
```

## 20d loadings (sorted by PC1)

```
            PC1    PC2    PC3  comm3              sector
LRCX     +0.893 -0.341 +0.047 +0.916             Semicap
AMD      +0.857 -0.194 +0.136 +0.790  Compute/AI-silicon
AMAT     +0.849 -0.284 -0.093 +0.811             Semicap
MU       +0.819 -0.056 +0.022 +0.675          Memory/HBM
TSLA     +0.809 -0.412 +0.074 +0.830            Mega-cap
IONQ     +0.763 -0.116 -0.219 +0.644             Quantum
VRT      +0.748 -0.070 -0.329 +0.673         AI-power/DC
MRVL     +0.716 -0.242 -0.418 +0.746  Compute/AI-silicon
CDNS     +0.715 +0.359 -0.190 +0.675                 EDA
SNDK     +0.711 -0.066 +0.084 +0.517          Memory/HBM
ENPH     +0.710 -0.218 -0.078 +0.557         AI-power/DC
NVDA     +0.708 +0.299 +0.084 +0.598  Compute/AI-silicon
BE       +0.691 -0.371 +0.072 +0.620         AI-power/DC
INTC     +0.690 -0.420 +0.147 +0.675  Compute/AI-silicon
AVGO     +0.684 +0.103 -0.164 +0.505  Compute/AI-silicon
LULU     +0.678 +0.165 +0.451 +0.691            Consumer
COHR     +0.635 -0.383 -0.543 +0.845         Optical/Net
QCOM     +0.629 -0.178 -0.036 +0.429  Compute/AI-silicon
CRDO     +0.559 -0.162 -0.004 +0.339  Compute/AI-silicon
CRWD     +0.537 +0.652 -0.063 +0.717        Software/Sec
LITE     +0.524 -0.168 -0.659 +0.737         Optical/Net
AS       +0.503 -0.070 +0.516 +0.523            Consumer
AMZN     +0.483 -0.082 +0.550 +0.542            Mega-cap
DELL     +0.445 +0.632 -0.155 +0.621            Mega-cap
AAOI     +0.436 +0.033 -0.611 +0.564         Optical/Net
SK Hynix +0.433 -0.003 +0.483 +0.420          Memory/HBM
SHOP     +0.428 +0.685 +0.362 +0.784        Software/Sec
PANW     +0.416 +0.695 -0.179 +0.688        Software/Sec
U        +0.358 +0.590 +0.337 +0.589        Software/Sec
KLAC     +0.332 +0.066 +0.368 +0.250             Semicap
DDOG     +0.332 +0.800 -0.255 +0.816        Software/Sec
NKE      +0.331 +0.122 +0.795 +0.757            Consumer
Samsung  +0.309 +0.183 +0.148 +0.151          Memory/HBM
MDB      +0.226 +0.759 -0.250 +0.690        Software/Sec
UBER     +0.222 +0.577 +0.344 +0.499            Mega-cap
NOW      +0.154 +0.894 -0.130 +0.841        Software/Sec
GOOG     +0.124 +0.030 +0.734 +0.555            Mega-cap
CBRS     +0.088 -0.349 -0.306 +0.223  Compute/AI-silicon
TEAM     +0.046 +0.899 -0.023 +0.811        Software/Sec
HUBS     +0.032 +0.929 -0.162 +0.890        Software/Sec
WDAY     -0.066 +0.893 -0.169 +0.830        Software/Sec
ADBE     -0.150 +0.876 -0.105 +0.801        Software/Sec
```
