# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T12:28:41Z`
- **Ciclo de ejecucion:** `#321`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general opera bajo presión bajista con la mayoría de activos cotizando por debajo de la EMA 200 en temporalidad de 1H. No se cumplen los requisitos estrictos de los Pilares Long (P1-P4) ni del Pilar Short (S1) al carecer de las confluencias exactas de sobreventa/sobrecompra extrema o patrones de giro confirmados con suficiente volumen. Tampoco existen posiciones abiertas que requieran ajustes de gestión dinámica. Por lo tanto, se adopta una postura conservadora de espera (HOLD).

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `GRAMUSDT` | 1.159 | 1.137784 | `+1.86%` | `61.67` / `56.32` | `48.17` | `0.619` | `BULLISH_ENGULFING` | 1.1078526 | `WATCH` | HOLD |
| `BTCUSDT` | 69287.19 | 74198.017961 | `-6.62%` | `43.51` / `40.34` | `34.26` | `0.336` | `BEARISH_SHOOTING_STAR` | 67485.72306 | `WATCH` | **HOLD** (75%) |
| `TIAUSDT` | 0.412 | 0.428276 | `-3.80%` | `37.74` / `38.81` | `44.48` | `0.235` | `NONE` | 0.393048 | `WATCH` | HOLD |
| `ETHUSDT` | 1959.27 | 2119.092501 | `-7.54%` | `48.37` / `42.73` | `40.37` | `0.391` | `BEARISH_SHOOTING_STAR` | 1894.055666 | `WATCH` | HOLD |
| `SOLUSDT` | 80.72 | 85.890327 | `-6.02%` | `69.4` / `62.75` | `48.0` | `0.541` | `BEARISH_SHOOTING_STAR` | 78.135008 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0764 | 0.077978 | `-2.02%` | `7.36` / `10.77` | `34.71` | `0.039` | `NONE` | 0.0728856 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DODOUSDT` | 0.02946 | 0.023631 | `+24.66%` | `72.86` / `64.91` | `69.41` | `0.978` | `BEARISH_SHOOTING_STAR` | 0.02810484 | `WATCH` | HOLD |
| `ZECUSDT` | 964.32 | 1102.396145 | `-12.53%` | `84.63` / `80.54` | `53.67` | `0.79` | `BEARISH_SHOOTING_STAR` | 919.96128 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 640.41 | 679.646674 | `-5.77%` | `47.85` / `43.55` | `40.46` | `0.407` | `BEARISH_SHOOTING_STAR` | 623.489062 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0237 | 1.108344 | `-7.64%` | `55.71` / `59.18` | `44.32` | `0.425` | `BULLISH_HAMMER` | 0.99417386 | `WATCH` | HOLD |
| `NEARUSDT` | 3.533 | 3.636238 | `-2.84%` | `86.96` / `83.4` | `56.95` | `0.84` | `MORNING_STAR` | 3.370482 | `EXIT_LONG_STOCH_80` | HOLD |
| `PEPEUSDT` | 4.56e-06 | 5e-06 | `-5.92%` | `37.04` / `35.01` | `52.59` | `0.7` | `MORNING_STAR` | 4.35e-06 | `WATCH` | HOLD |
| `UNIUSDT` | 5.797 | 6.635983 | `-12.64%` | `36.14` / `34.61` | `36.42` | `0.307` | `BEARISH_SHOOTING_STAR` | 5.558308 | `WATCH` | HOLD |
| `HYPEUSDT` | 74.01 | 75.313616 | `-1.73%` | `92.88` / `83.46` | `63.96` | `1.003` | `BEARISH_SHOOTING_STAR` | 70.60554 | `EXIT_LONG_STOCH_80` | HOLD |
| `NBISBUSDT` | 126.77 | 138.134976 | `-8.23%` | `33.33` / `25.5` | `38.19` | `0.366` | `MORNING_STAR` | 121.369024 | `WATCH` | HOLD |
| `XAUTUSDT` | 3884.65 | 3997.778873 | `-2.83%` | `26.25` / `31.71` | `39.06` | `0.436` | `BULLISH_HAMMER` | 3783.6491 | `WATCH` | HOLD |
