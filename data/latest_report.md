# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T21:04:54Z`
- **Ciclo de ejecucion:** `#155`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se mantiene predominantemente bajista por debajo de la EMA 200 en la temporalidad de 1H. No se cumplen las condiciones estrictas de los pilares LONG (P1-P4) ni del pilar SHORT (S1) para abrir nuevas posiciones en este momento. Dado que no hay posiciones abiertas en el portafolio (open_positions_count = 0), el bot opera en modo de espera (HOLD), preservando el capital mientras busca activamente setups institucionales de alta probabilidad en los próximos ciclos de vela.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.75e-06 | 5e-06 | `-5.98%` | `3.57` / `3.59` | `24.08` | `0.118` | `BEARISH_SHOOTING_STAR` | 4.54e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001499 | 0.001553 | `-3.51%` | `5.95` / `4.43` | `35.33` | `0.253` | `NONE` | 0.00143005 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOXSBUSDT` | 45.61 | 59.505212 | `-23.35%` | `37.87` / `26.48` | `39.47` | `0.378` | `BULLISH_HAMMER` | 43.51194 | `WATCH` | HOLD |
| `BTCUSDT` | 74612.01 | 75584.159108 | `-1.29%` | `84.31` / `81.13` | `59.35` | `0.929` | `BULLISH_ENGULFING` | 72672.09774 | `EXIT_LONG_STOCH_80` | **HOLD** (75%) |
| `ENAUSDT` | 0.1506 | 0.160561 | `-6.20%` | `19.23` / `24.81` | `43.38` | `0.094` | `BEARISH_SHOOTING_STAR` | 0.14465188 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3978.18 | 4032.413621 | `-1.34%` | `2.76` / `2.43` | `20.9` | `0.118` | `NONE` | 3874.74732 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.864 | 7.949323 | `-1.07%` | `16.33` / `21.34` | `41.8` | `0.252` | `NONE` | 7.5937792 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1578 | 0.165478 | `-4.64%` | `15.63` / `21.58` | `39.2` | `0.182` | `BEARISH_ENGULFING` | 0.1533394 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PAXGUSDT` | 3980.54 | 4037.921427 | `-1.42%` | `2.88` / `2.26` | `20.97` | `0.119` | `NONE` | 3877.04596 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 998.42 | 1177.809728 | `-15.23%` | `61.06` / `59.92` | `43.05` | `0.524` | `NONE` | 952.49268 | `WATCH` | HOLD |
| `ETHUSDT` | 2078.0 | 2175.778372 | `-4.49%` | `59.16` / `62.93` | `53.12` | `0.738` | `NONE` | 2023.972 | `WATCH` | HOLD |
| `MUBUSDT` | 813.11 | 754.540649 | `+7.76%` | `80.89` / `86.69` | `70.86` | `0.762` | `NONE` | 784.857188 | `EXIT_LONG_STOCH_80` | HOLD |
| `SNXXBUSDT` | 4.42 | 4.183369 | `+5.66%` | `76.44` / `83.74` | `65.8` | `0.715` | `NONE` | 4.21668 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 84.93 | 88.338521 | `-3.86%` | `72.86` / `75.35` | `56.57` | `0.772` | `BULLISH_ENGULFING` | 82.72182 | `WATCH` | HOLD |
| `NEARUSDT` | 3.707 | 3.766312 | `-1.57%` | `59.39` / `62.34` | `52.47` | `0.537` | `BEARISH_ENGULFING` | 3.547134 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0656 | 1.1449 | `-6.93%` | `41.57` / `40.54` | `50.67` | `0.712` | `BULLISH_ENGULFING` | 1.03509296 | `WATCH` | HOLD |
