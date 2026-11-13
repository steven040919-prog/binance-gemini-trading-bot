# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T00:57:54Z`
- **Ciclo de ejecucion:** `#281`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen mayoritariamente bajista (BEARISH) con la mayoría de los activos cotizando por debajo de la EMA 200 en temporalidad 1H. Destaca la oportunidad alcista en ERAUSDT que cumple con los criterios institucionales del Pilar 1 (Pullback de valor sobre EMA 200 en tendencia alcista firme), activando una orden de compra (BUY). No hay posiciones abiertas actuales para aplicar gestión dinámica, y el resto de activos se mantienen en observación (WATCH) o cierre de cortos.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71182.35 | 74936.114064 | `-5.01%` | `12.77` / `10.94` | `22.86` | `0.172` | `BULLISH_HAMMER` | 69331.6089 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 657.05 | 685.988663 | `-4.22%` | `26.14` / `21.67` | `34.07` | `0.366` | `BULLISH_ENGULFING` | 639.9667 | `WATCH` | HOLD |
| `NBISBUSDT` | 130.38 | 140.511918 | `-7.21%` | `24.38` / `23.52` | `36.65` | `0.346` | `BULLISH_ENGULFING` | 124.38252 | `WATCH` | HOLD |
| `ERAUSDT` | 0.081 | 0.077749 | `+4.18%` | `3.34` / `2.49` | `38.69` | `0.155` | `BULLISH_ENGULFING` | 0.077274 | `P1_EMA200_PULLBACK` | **BUY** (88%) |
| `XAUTUSDT` | 3883.14 | 4007.985775 | `-3.11%` | `29.83` / `26.7` | `32.84` | `0.349` | `NONE` | 3782.17836 | `WATCH` | HOLD |
| `INITUSDT` | 0.11714 | 0.158497 | `-26.09%` | `30.93` / `25.22` | `39.19` | `0.328` | `NONE` | 0.11175156 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.15 | 1.138192 | `+1.04%` | `14.15` / `13.18` | `40.72` | `0.23` | `BEARISH_SHOOTING_STAR` | 1.0971 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOXSBUSDT` | 44.33 | 56.313739 | `-21.28%` | `15.73` / `21.49` | `37.31` | `0.149` | `NONE` | 42.29082 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AVAXUSDT` | 8.346 | 8.436789 | `-1.08%` | `28.66` / `23.97` | `41.81` | `0.33` | `MORNING_STAR` | 8.099388 | `WATCH` | HOLD |
| `PAXGUSDT` | 3885.25 | 4012.381872 | `-3.17%` | `30.35` / `26.79` | `32.3` | `0.346` | `BULLISH_HAMMER` | 3784.2335 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3157 | 0.317814 | `-0.67%` | `19.74` / `16.11` | `36.78` | `0.273` | `BULLISH_HAMMER` | 0.3074918 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2013.45 | 2143.476978 | `-6.07%` | `47.56` / `47.36` | `36.7` | `0.316` | `BULLISH_ENGULFING` | 1961.1003 | `WATCH` | HOLD |
| `ZECUSDT` | 964.19 | 1130.830699 | `-14.74%` | `38.42` / `30.85` | `46.57` | `0.47` | `MORNING_STAR` | 919.83726 | `WATCH` | HOLD |
| `SOLUSDT` | 81.59 | 86.876191 | `-6.08%` | `39.32` / `35.04` | `39.32` | `0.336` | `BULLISH_HAMMER` | 79.349246 | `WATCH` | HOLD |
| `NEARUSDT` | 3.442 | 3.68477 | `-6.59%` | `48.18` / `41.73` | `43.38` | `0.504` | `BULLISH_HAMMER` | 3.283668 | `WATCH` | HOLD |
| `XRPUSDT` | 1.036 | 1.120544 | `-7.54%` | `55.44` / `52.14` | `44.54` | `0.464` | `MORNING_STAR` | 1.007108 | `WATCH` | HOLD |
