# PCA factor / crowding summary

Panel: 35 names, US calendar 2025-05-29 -> 2026-05-29.

| window | n_obs | assets | PC1 | PC2 | PC3 | AR(top k) | avg corr | N_eff |
|---|---|---|---|---|---|---|---|---|
| 20d | 20 | 34 | 32.3% | 13.7% | 10.2% | 80.2% (k=7) | 0.168 | 6.5 |
| 60d | 60 | 34 | 31.5% | 11.8% | 6.5% | 69.0% (k=7) | 0.219 | 7.5 |

## 60d loadings (sorted by PC1)

```
            PC1    PC2    PC3  comm3              sector
LRCX     +0.907 -0.059 -0.049 +0.829             Semicap
AMAT     +0.887 -0.100 -0.007 +0.797             Semicap
KLAC     +0.835 -0.046 -0.007 +0.700             Semicap
COHR     +0.813 -0.229 +0.108 +0.724         Optical/Net
VRT      +0.756 -0.288 +0.016 +0.655         AI-power/DC
AMD      +0.736 +0.086 -0.076 +0.555  Compute/AI-silicon
MU       +0.718 +0.006 +0.305 +0.608          Memory/HBM
SNDK     +0.705 +0.019 +0.129 +0.515          Memory/HBM
INTC     +0.683 +0.074 +0.102 +0.482  Compute/AI-silicon
AS       +0.659 +0.078 -0.333 +0.552            Consumer
LITE     +0.659 -0.213 +0.269 +0.552         Optical/Net
BE       +0.658 -0.197 -0.062 +0.476         AI-power/DC
AVGO     +0.623 +0.268 -0.065 +0.465  Compute/AI-silicon
NVDA     +0.607 +0.233 -0.026 +0.424  Compute/AI-silicon
AMZN     +0.593 +0.150 -0.272 +0.448            Mega-cap
GOOG     +0.577 +0.201 -0.226 +0.425            Mega-cap
AAOI     +0.575 -0.223 +0.173 +0.410         Optical/Net
TSLA     +0.566 +0.390 -0.025 +0.474            Mega-cap
IONQ     +0.533 +0.279 -0.185 +0.396             Quantum
CRDO     +0.527 +0.150 +0.024 +0.301  Compute/AI-silicon
MRVL     +0.498 -0.101 -0.218 +0.306  Compute/AI-silicon
QCOM     +0.406 +0.295 +0.037 +0.253  Compute/AI-silicon
ENPH     +0.397 +0.074 +0.037 +0.164         AI-power/DC
LULU     +0.370 +0.399 -0.168 +0.324            Consumer
DELL     +0.293 +0.253 +0.184 +0.184            Mega-cap
UBER     +0.278 +0.337 -0.293 +0.276            Mega-cap
SK Hynix +0.277 -0.080 +0.673 +0.536          Memory/HBM
Samsung  +0.204 -0.084 +0.649 +0.470          Memory/HBM
NKE      +0.087 +0.280 -0.577 +0.419            Consumer
PANW     -0.003 +0.765 +0.291 +0.671        Software/Sec
CRWD     -0.068 +0.793 +0.332 +0.745        Software/Sec
DDOG     -0.132 +0.736 +0.261 +0.627        Software/Sec
TEAM     -0.184 +0.667 +0.049 +0.481        Software/Sec
WDAY     -0.391 +0.733 -0.082 +0.696        Software/Sec
```

## 20d loadings (sorted by PC1)

```
            PC1    PC2    PC3  comm3              sector
LRCX     +0.891 +0.333 -0.028 +0.905             Semicap
AMAT     +0.857 +0.201 +0.215 +0.820             Semicap
COHR     +0.810 -0.518 -0.042 +0.926         Optical/Net
IONQ     +0.807 -0.188 -0.165 +0.714             Quantum
KLAC     +0.774 +0.436 +0.208 +0.832             Semicap
MRVL     +0.754 +0.109 +0.242 +0.640  Compute/AI-silicon
MU       +0.741 +0.005 +0.268 +0.621          Memory/HBM
BE       +0.739 -0.385 -0.046 +0.698         AI-power/DC
AMD      +0.738 +0.532 -0.022 +0.828  Compute/AI-silicon
INTC     +0.716 +0.202 +0.314 +0.652  Compute/AI-silicon
VRT      +0.681 -0.438 -0.098 +0.665         AI-power/DC
TSLA     +0.630 -0.070 +0.240 +0.460            Mega-cap
CRDO     +0.607 -0.170 +0.137 +0.416  Compute/AI-silicon
AVGO     +0.545 +0.302 +0.329 +0.496  Compute/AI-silicon
SNDK     +0.512 -0.034 +0.334 +0.375          Memory/HBM
AAOI     +0.502 -0.679 -0.132 +0.730         Optical/Net
LITE     +0.501 -0.796 +0.124 +0.899         Optical/Net
SK Hynix +0.492 -0.274 -0.196 +0.356          Memory/HBM
Samsung  +0.436 +0.023 -0.309 +0.286          Memory/HBM
QCOM     +0.431 +0.120 +0.562 +0.516  Compute/AI-silicon
NVDA     +0.430 +0.179 -0.082 +0.224  Compute/AI-silicon
ENPH     +0.430 -0.075 +0.027 +0.191         AI-power/DC
AMZN     +0.414 +0.135 -0.182 +0.222            Mega-cap
AS       +0.402 +0.691 -0.295 +0.726            Consumer
GOOG     +0.393 +0.389 -0.119 +0.320            Mega-cap
DELL     +0.244 +0.433 +0.374 +0.387            Mega-cap
UBER     +0.219 +0.242 -0.602 +0.469            Mega-cap
LULU     +0.064 +0.703 -0.272 +0.572            Consumer
NKE      +0.003 +0.726 -0.258 +0.594            Consumer
PANW     -0.109 -0.014 +0.671 +0.462        Software/Sec
CRWD     -0.287 +0.135 +0.769 +0.692        Software/Sec
TEAM     -0.376 +0.032 +0.236 +0.198        Software/Sec
DDOG     -0.422 -0.016 +0.532 +0.461        Software/Sec
WDAY     -0.735 +0.215 +0.415 +0.758        Software/Sec
```
