# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T14:23:39Z`
- **Ciclo de ejecucion:** `#333`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de temporalidad 1h se encuentra mayoritariamente bajo régimen bajista, por debajo de la EMA 200. Se evalúan oportunidades basadas en los pilares institucionales. ERAUSDT cumple con el Pilar 1 (P1_EMA200_PULLBACK) mostrando una entrada LONG válida con envolvente alcista y estocástico girando al alza. ZECUSDT e HYPEUSDT activan el Pilar S1 (S1_EMA200_RESISTANCE_REJECT) para cortos en Binance Futuros USDT-M debido al rechazo bajista en la resistencia de la EMA 200 con patrones de estrella fugaz.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.0788 | 0.077912 | `+1.14%` | `27.59` / `19.03` | `40.7` | `0.275` | `BULLISH_ENGULFING` | 0.0751752 | `P1_EMA200_PULLBACK` | **BUY** (88%) |
| `GRAMUSDT` | 1.133 | 1.137333 | `-0.38%` | `44.94` / `52.44` | `39.99` | `0.091` | `BEARISH_ENGULFING` | 1.080882 | `WATCH` | HOLD |
| `BTCUSDT` | 69265.62 | 74098.231617 | `-6.52%` | `45.99` / `44.66` | `36.38` | `0.367` | `BULLISH_ENGULFING` | 67464.71388 | `WATCH` | HOLD |
| `ETHUSDT` | 1963.73 | 2115.67633 | `-7.18%` | `54.3` / `51.83` | `42.85` | `0.45` | `BEARISH_SHOOTING_STAR` | 1900.624004 | `WATCH` | HOLD |
| `NEARUSDT` | 3.575 | 3.632195 | `-1.57%` | `84.86` / `86.81` | `60.28` | `0.875` | `BULLISH_ENGULFING` | 3.41055 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 81.36 | 85.769761 | `-5.14%` | `76.15` / `73.11` | `53.69` | `0.697` | `NONE` | 78.496 | `WATCH` | HOLD |
| `DODOUSDT` | 0.02826 | 0.023744 | `+19.02%` | `64.57` / `69.71` | `58.25` | `0.595` | `NONE` | 0.02696004 | `WATCH` | HOLD |
| `ZECUSDT` | 964.0 | 1097.827032 | `-12.19%` | `79.95` / `83.19` | `53.28` | `0.734` | `BEARISH_SHOOTING_STAR` | 1008.344 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `BNBUSDT` | 641.61 | 678.760958 | `-5.47%` | `54.89` / `51.59` | `42.73` | `0.463` | `BEARISH_SHOOTING_STAR` | 624.371292 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0312 | 1.107432 | `-6.88%` | `65.69` / `59.55` | `51.17` | `0.621` | `BULLISH_ENGULFING` | 0.99054496 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.56e-06 | 5e-06 | `-5.94%` | `49.38` / `41.98` | `52.75` | `0.707` | `BEARISH_SHOOTING_STAR` | 4.35e-06 | `WATCH` | HOLD |
| `HYPEUSDT` | 74.38 | 75.245475 | `-1.15%` | `84.09` / `89.17` | `65.91` | `0.944` | `BEARISH_SHOOTING_STAR` | 77.492144 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (82%) |
| `INJUSDT` | 8.193 | 7.78311 | `+5.27%` | `91.87` / `92.98` | `76.38` | `1.115` | `NONE` | 7.816122 | `EXIT_LONG_STOCH_80` | HOLD |
| `SUIUSDT` | 0.8208 | 0.835935 | `-1.81%` | `87.14` / `87.21` | `63.71` | `0.925` | `NONE` | 0.7830432 | `EXIT_LONG_STOCH_80` | HOLD |
| `UNIUSDT` | 5.921 | 6.613328 | `-10.47%` | `56.33` / `47.44` | `47.98` | `0.551` | `NONE` | 5.648634 | `WATCH` | HOLD |
| `DOGEUSDT` | 0.0661 | 0.069235 | `-4.53%` | `77.22` / `69.43` | `55.8` | `0.701` | `BULLISH_HAMMER` | 0.06353428 | `WATCH` | HOLD |
