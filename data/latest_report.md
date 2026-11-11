# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T20:02:22Z`
- **Ciclo de ejecucion:** `#151`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> Evaluación general del mercado en temporalidad 1H con sesgo mayoritariamente bajista (por debajo de la EMA 200). No se cumplen de forma estricta los requisitos de los Pilares Long (P1-P4) ni del Pilar Short (S1) debido a la ausencia de confluencia simultánea perfecta en sobreventa/sobrecompra extrema con los patrones de vela y pendientes requeridas. El portafolio no posee posiciones abiertas actualmente (open_positions_count = 0), por lo que se mantiene en estado de vigilancia (WATCH) preservando el capital en USDT libre (14.0 USDT).

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.8e-06 | 5e-06 | `-5.09%` | `3.01` / `4.46` | `26.11` | `0.139` | `NONE` | 4.58e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001508 | 0.001554 | `-2.99%` | `5.22` / `4.22` | `36.43` | `0.265` | `BULLISH_HAMMER` | 0.00143863 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74474.0 | 75590.866498 | `-1.48%` | `76.54` / `78.15` | `57.87` | `0.916` | `BULLISH_HAMMER` | 72537.676 | `WATCH` | **HOLD** (50%) |
| `XAUTUSDT` | 3979.35 | 4032.963322 | `-1.33%` | `2.3` / `1.83` | `21.25` | `0.08` | `NONE` | 3875.8869 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.92 | 7.952294 | `-0.41%` | `25.59` / `25.96` | `44.74` | `0.301` | `BEARISH_ENGULFING` | 7.59364 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1591 | 0.16554 | `-3.89%` | `26.51` / `29.15` | `42.36` | `0.286` | `BULLISH_HAMMER` | 0.15349976 | `WATCH` | HOLD |
| `PAXGUSDT` | 3981.79 | 4038.517637 | `-1.40%` | `2.24` / `1.39` | `21.33` | `0.081` | `BULLISH_HAMMER` | 3878.26346 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2081.24 | 2177.141613 | `-4.40%` | `61.75` / `67.06` | `55.01` | `0.839` | `NONE` | 2027.12776 | `WATCH` | HOLD |
| `MUBUSDT` | 818.54 | 754.064065 | `+8.55%` | `89.96` / `92.71` | `75.2` | `0.831` | `NONE` | 793.77088 | `EXIT_LONG_STOCH_80` | HOLD |
| `ZECUSDT` | 1003.99 | 1180.875096 | `-14.98%` | `60.77` / `60.0` | `44.7` | `0.587` | `BULLISH_HAMMER` | 957.80646 | `WATCH` | HOLD |
| `SOXSBUSDT` | 44.1 | 59.635227 | `-26.05%` | `21.57` / `14.3` | `33.13` | `0.23` | `MORNING_STAR` | 42.0714 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SNXXBUSDT` | 4.55 | 4.183333 | `+8.76%` | `89.38` / `91.75` | `75.02` | `0.819` | `BULLISH_HAMMER` | 4.3407 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 84.99 | 88.392435 | `-3.85%` | `74.63` / `78.11` | `57.5` | `0.821` | `BULLISH_HAMMER` | 82.78026 | `WATCH` | HOLD |
| `NEARUSDT` | 3.726 | 3.770228 | `-1.17%` | `63.36` / `68.58` | `54.5` | `0.622` | `BULLISH_HAMMER` | 3.554604 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.206 | 1.119383 | `+7.74%` | `64.83` / `66.91` | `58.65` | `0.657` | `BEARISH_ENGULFING` | 1.150524 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0867 | 0.074371 | `+16.58%` | `47.39` / `43.16` | `59.49` | `0.71` | `BEARISH_SHOOTING_STAR` | 0.0827118 | `WATCH` | HOLD |
