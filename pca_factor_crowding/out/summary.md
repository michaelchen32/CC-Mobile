# PCA factor / crowding summary

Panel: 42 names, US calendar 2025-07-10 -> 2026-07-09.

| window | n_obs | assets | PC1 | PC2 | PC3 | AR(top k) | avg corr | N_eff |
|---|---|---|---|---|---|---|---|---|
| 20d | 20 | 42 | 40.5% | 20.1% | 8.1% | 88.4% (k=8) | 0.230 | 4.5 |
| 60d | 60 | 41 | 29.4% | 19.0% | 7.7% | 74.7% (k=8) | 0.211 | 7.2 |

## 60d loadings (sorted by PC1)

```
            PC1    PC2    PC3  comm3              sector
LRCX     +0.913 -0.055 +0.042 +0.839             Semicap
AMAT     +0.865 -0.125 -0.069 +0.769             Semicap
KLAC     +0.849 -0.061 -0.014 +0.725             Semicap
MU       +0.824 +0.023 -0.038 +0.680          Memory/HBM
COHR     +0.813 -0.099 -0.263 +0.741         Optical/Net
AMD      +0.806 +0.114 +0.193 +0.700  Compute/AI-silicon
MRVL     +0.792 -0.027 -0.128 +0.644  Compute/AI-silicon
VRT      +0.775 -0.208 -0.135 +0.662         AI-power/DC
SNDK     +0.745 -0.016 -0.098 +0.565          Memory/HBM
INTC     +0.714 -0.026 +0.075 +0.516  Compute/AI-silicon
CRDO     +0.676 -0.004 +0.013 +0.457  Compute/AI-silicon
TSLA     +0.674 +0.267 +0.131 +0.542            Mega-cap
LITE     +0.660 +0.012 -0.480 +0.666         Optical/Net
QCOM     +0.634 +0.065 +0.064 +0.410  Compute/AI-silicon
BE       +0.624 -0.162 +0.107 +0.427         AI-power/DC
AVGO     +0.623 +0.239 -0.004 +0.446  Compute/AI-silicon
ENPH     +0.614 +0.086 +0.060 +0.388         AI-power/DC
IONQ     +0.594 +0.254 +0.125 +0.433             Quantum
SK Hynix +0.553 -0.047 +0.053 +0.311          Memory/HBM
AAOI     +0.551 +0.144 -0.351 +0.448         Optical/Net
NVDA     +0.514 +0.369 +0.187 +0.436  Compute/AI-silicon
CDNS     +0.462 +0.641 -0.132 +0.642                 EDA
Samsung  +0.458 +0.013 +0.043 +0.211          Memory/HBM
DELL     +0.322 +0.418 -0.206 +0.321            Mega-cap
AS       +0.314 +0.161 +0.671 +0.575            Consumer
PANW     +0.253 +0.626 -0.298 +0.544        Software/Sec
CRWD     +0.227 +0.716 -0.290 +0.648        Software/Sec
GOOG     +0.211 +0.162 +0.566 +0.391            Mega-cap
AMZN     +0.200 +0.373 +0.545 +0.477            Mega-cap
U        +0.101 +0.723 +0.250 +0.595        Software/Sec
LULU     -0.000 +0.565 +0.385 +0.467            Consumer
DDOG     -0.030 +0.661 -0.301 +0.529        Software/Sec
NKE      -0.030 +0.394 +0.759 +0.733            Consumer
UBER     -0.031 +0.376 +0.407 +0.308            Mega-cap
MDB      -0.086 +0.745 -0.206 +0.605        Software/Sec
SHOP     -0.137 +0.688 +0.211 +0.537        Software/Sec
NOW      -0.179 +0.895 -0.153 +0.856        Software/Sec
TEAM     -0.188 +0.763 -0.153 +0.641        Software/Sec
HUBS     -0.299 +0.694 -0.183 +0.605        Software/Sec
ADBE     -0.361 +0.750 -0.154 +0.717        Software/Sec
WDAY     -0.430 +0.778 -0.179 +0.822        Software/Sec
```

## 20d loadings (sorted by PC1)

```
            PC1    PC2    PC3  comm3              sector
LRCX     +0.953 +0.047 -0.090 +0.918             Semicap
MRVL     +0.930 +0.241 +0.039 +0.924  Compute/AI-silicon
KLAC     +0.914 +0.046 -0.187 +0.873             Semicap
VRT      +0.909 -0.159 +0.112 +0.864         AI-power/DC
AMD      +0.908 +0.230 +0.069 +0.882  Compute/AI-silicon
INTC     +0.899 +0.017 -0.023 +0.809  Compute/AI-silicon
AMAT     +0.895 -0.137 -0.149 +0.843             Semicap
SNDK     +0.881 -0.128 +0.092 +0.801          Memory/HBM
COHR     +0.875 -0.050 +0.038 +0.770         Optical/Net
MU       +0.873 -0.062 +0.163 +0.792          Memory/HBM
CRDO     +0.864 -0.037 -0.043 +0.749  Compute/AI-silicon
LITE     +0.781 +0.045 -0.183 +0.645         Optical/Net
QCOM     +0.769 +0.115 +0.358 +0.732  Compute/AI-silicon
SK Hynix +0.760 -0.129 +0.268 +0.666          Memory/HBM
BE       +0.744 +0.038 +0.177 +0.586         AI-power/DC
ENPH     +0.717 +0.372 +0.235 +0.708         AI-power/DC
AVGO     +0.674 +0.263 +0.222 +0.573  Compute/AI-silicon
TSLA     +0.666 +0.517 -0.144 +0.732            Mega-cap
NVDA     +0.634 +0.363 +0.291 +0.618  Compute/AI-silicon
AAOI     +0.630 +0.280 -0.303 +0.567         Optical/Net
Samsung  +0.614 -0.061 +0.524 +0.655          Memory/HBM
IONQ     +0.572 +0.377 -0.509 +0.729             Quantum
DELL     +0.503 +0.229 -0.092 +0.314            Mega-cap
PANW     +0.375 +0.554 -0.457 +0.657        Software/Sec
CRWD     +0.361 +0.640 -0.386 +0.689        Software/Sec
CDNS     +0.315 +0.512 +0.030 +0.362                 EDA
AS       +0.302 +0.412 +0.545 +0.558            Consumer
GOOG     +0.209 +0.532 +0.081 +0.333            Mega-cap
CBRS     +0.164 +0.447 -0.692 +0.706  Compute/AI-silicon
U        -0.014 +0.810 +0.190 +0.692        Software/Sec
DDOG     -0.039 +0.685 -0.253 +0.535        Software/Sec
NKE      -0.069 +0.614 +0.137 +0.401            Consumer
AMZN     -0.095 +0.872 +0.137 +0.788            Mega-cap
MDB      -0.207 +0.768 -0.472 +0.856        Software/Sec
SHOP     -0.229 +0.670 +0.471 +0.722        Software/Sec
UBER     -0.238 +0.474 +0.513 +0.545            Mega-cap
TEAM     -0.398 +0.786 +0.102 +0.786        Software/Sec
LULU     -0.468 +0.483 +0.294 +0.538            Consumer
NOW      -0.543 +0.751 -0.131 +0.875        Software/Sec
HUBS     -0.549 +0.572 +0.264 +0.698        Software/Sec
ADBE     -0.607 +0.437 -0.073 +0.565        Software/Sec
WDAY     -0.730 +0.499 +0.120 +0.796        Software/Sec
```
