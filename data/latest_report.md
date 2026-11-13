# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T02:05:14Z`
- **Ciclo de ejecucion:** `#288`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un régimen general bajista (la gran mayoría de los activos cotizan por debajo de su EMA 200 con pendientes negativas). Se evaluaron los 4 pilares LONG y el pilar SHORT (S1). El activo ERAUSDT cumple con las condiciones del Pilar 1 (Pullback de valor sobre EMA 200 con patrón MORNING_STAR), por lo que se emite orden de compra (BUY). No hay posiciones abiertas actuales para ajustar SL/TP, manteniendo el resto de candidatos bajo observación.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 70868.19 | 74836.315364 | `-5.30%` | `11.31` / `12.23` | `20.18` | `0.16` | `NONE` | 69025.61706 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 951.98 | 1126.610477 | `-15.50%` | `44.59` / `42.68` | `41.23` | `0.311` | `NONE` | 908.18892 | `WATCH` | HOLD |
| `SOLUSDT` | 81.15 | 86.71828 | `-6.42%` | `37.79` / `38.89` | `34.61` | `0.225` | `NONE` | 79.0401 | `WATCH` | HOLD |
| `NBISBUSDT` | 131.14 | 140.248554 | `-6.49%` | `38.78` / `29.78` | `38.42` | `0.396` | `NONE` | 125.10756 | `WATCH` | HOLD |
| `BNBUSDT` | 653.48 | 685.137033 | `-4.62%` | `29.96` / `28.03` | `29.16` | `0.293` | `NONE` | 636.48952 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.149 | 1.137931 | `+0.97%` | `18.99` / `16.73` | `40.63` | `0.253` | `BEARISH_SHOOTING_STAR` | 1.096146 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ERAUSDT` | 0.083 | 0.07779 | `+6.70%` | `12.44` / `7.7` | `43.09` | `0.283` | `MORNING_STAR` | 0.079182 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `SOXSBUSDT` | 43.66 | 56.131527 | `-22.22%` | `6.32` / `10.3` | `34.88` | `0.132` | `BEARISH_ENGULFING` | 41.65164 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AVAXUSDT` | 8.344 | 8.429311 | `-1.01%` | `49.62` / `38.6` | `43.01` | `0.36` | `BULLISH_ENGULFING` | 8.1061072 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3154 | 0.317848 | `-0.77%` | `7.51` / `12.96` | `33.88` | `0.176` | `BEARISH_SHOOTING_STAR` | 0.3071996 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2009.09 | 2140.265489 | `-6.13%` | `53.77` / `50.77` | `34.51` | `0.288` | `BEARISH_ENGULFING` | 1956.85366 | `WATCH` | HOLD |
| `NEARUSDT` | 3.441 | 3.669805 | `-6.23%` | `76.25` / `62.43` | `43.67` | `0.55` | `NONE` | 3.2920284 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0286 | 1.11839 | `-8.03%` | `51.6` / `54.62` | `38.32` | `0.256` | `NONE` | 1.0018564 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.62e-06 | 5e-06 | `-5.64%` | `96.72` / `93.16` | `56.69` | `0.997` | `BULLISH_HAMMER` | 4.41e-06 | `EXIT_LONG_STOCH_80` | HOLD |
| `XAUTUSDT` | 3907.2 | 4005.388045 | `-2.45%` | `50.72` / `40.34` | `45.76` | `0.571` | `NONE` | 3805.6128 | `WATCH` | HOLD |
| `UNIUSDT` | 6.036 | 6.729844 | `-10.31%` | `60.25` / `55.01` | `37.51` | `0.366` | `BULLISH_HAMMER` | 5.8576856 | `WATCH` | HOLD |
