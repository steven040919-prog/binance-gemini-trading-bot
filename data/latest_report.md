# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T02:15:25Z`
- **Ciclo de ejecucion:** `#289`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado muestra una dominancia clara de tendencia bajista, con la mayoria de los pares principales (BTC, ETH, SOL, BNB) cotizando significativamente por debajo de sus EMA 200 de 1H. Se ha identificado una oportunidad compradora valida en ERAUSDT impulsada por el Pilar 1 (P1_EMA200_PULLBACK), confirmada por el patron Morning Star, giro alcista del Estocastico en zona extrema y mejora del histograma MACD. El resto de pares se mantiene en estado de observacion (HOLD) al no cumplir los criterios estrictos de confluencia cuantitativa.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 70632.67 | 74833.971882 | `-5.61%` | `10.44` / `11.94` | `18.44` | `0.106` | `NONE` | 68796.22058 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `ETHUSDT` | 1998.44 | 2140.159519 | `-6.62%` | `45.76` / `48.1` | `29.64` | `0.127` | `BEARISH_ENGULFING` | 1946.48056 | `WATCH` | **HOLD** (90%) |
| `SOLUSDT` | 80.84 | 86.715195 | `-6.78%` | `32.5` / `37.13` | `31.79` | `0.124` | `NONE` | 78.73816 | `WATCH` | **HOLD** (88%) |
| `NBISBUSDT` | 130.0 | 140.237211 | `-7.30%` | `36.8` / `29.12` | `36.84` | `0.371` | `BEARISH_ENGULFING` | 124.02 | `WATCH` | **HOLD** (93%) |
| `BNBUSDT` | 651.36 | 685.115938 | `-4.93%` | `23.48` / `25.87` | `26.75` | `0.225` | `NONE` | 634.42464 | `WATCH` | **HOLD** (85%) |
| `XRPUSDT` | 1.0251 | 1.118355 | `-8.34%` | `47.37` / `53.21` | `35.84` | `0.154` | `NONE` | 0.9984474 | `WATCH` | **HOLD** (89%) |
| `UNIUSDT` | 5.994 | 6.729427 | `-10.93%` | `52.84` / `52.54` | `34.15` | `0.196` | `BULLISH_HAMMER` | 5.813162 | `WATCH` | **HOLD** (86%) |
| `GRAMUSDT` | 1.148 | 1.137921 | `+0.89%` | `18.8` / `16.67` | `40.41` | `0.249` | `BEARISH_SHOOTING_STAR` | 1.095192 | `EXIT_SHORT_STOCH_20` | **HOLD** (87%) |
| `ERAUSDT` | 0.0829 | 0.077789 | `+6.57%` | `12.29` / `7.65` | `42.87` | `0.279` | `MORNING_STAR` | 0.0790866 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `ENAUSDT` | 0.1394 | 0.15518 | `-10.17%` | `63.55` / `64.31` | `33.71` | `0.274` | `BULLISH_HAMMER` | 0.13462284 | `WATCH` | HOLD |
| `AVAXUSDT` | 8.301 | 8.428883 | `-1.52%` | `41.83` / `36.01` | `39.96` | `0.27` | `BULLISH_ENGULFING` | 8.0833974 | `WATCH` | **HOLD** (88%) |
| `SOXSBUSDT` | 44.33 | 56.138194 | `-21.03%` | `9.39` / `11.32` | `39.23` | `0.217` | `BEARISH_ENGULFING` | 42.29082 | `EXIT_SHORT_STOCH_20` | **HOLD** (92%) |
| `ONEUSDT` | 0.001525 | 0.001551 | `-1.70%` | `8.0` / `6.11` | `43.59` | `0.211` | `BULLISH_HAMMER` | 0.00145485 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `WLDUSDT` | 0.2988 | 0.327057 | `-8.64%` | `43.22` / `46.53` | `37.52` | `0.129` | `BULLISH_HAMMER` | 0.2894348 | `WATCH` | **HOLD** (89%) |
| `TRXUSDT` | 0.3154 | 0.317848 | `-0.77%` | `7.51` / `12.96` | `33.88` | `0.176` | `BEARISH_SHOOTING_STAR` | 0.3071996 | `EXIT_SHORT_STOCH_20` | **HOLD** (91%) |
| `ZECUSDT` | 953.0 | 1126.620626 | `-15.41%` | `45.18` / `42.88` | `41.64` | `0.327` | `NONE` | 909.162 | `WATCH` | **HOLD** (90%) |
