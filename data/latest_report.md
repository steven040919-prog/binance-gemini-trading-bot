# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T01:07:24Z`
- **Ciclo de ejecucion:** `#282`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un regimen bajista generalizado con la mayoria de los activos cotizando por debajo de sus respectivas EMA 200 en temporalidad 1H. GRAMUSDT activa el Pilar 1 LONG (P1_EMA200_PULLBACK) al cumplir con los criterios de retroceso sobre la EMA 200, estocastico girando al alza y patron envolvente alcista. No hay posiciones abiertas actuales para gestion dinamica.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 70921.82 | 74880.004491 | `-5.29%` | `12.95` / `12.02` | `20.63` | `0.141` | `BEARISH_ENGULFING` | 69077.85268 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 81.37 | 86.787041 | `-6.24%` | `40.95` / `38.37` | `36.88` | `0.277` | `BULLISH_HAMMER` | 79.25438 | `WATCH` | HOLD |
| `BNBUSDT` | 655.15 | 685.511311 | `-4.43%` | `30.83` / `25.76` | `31.29` | `0.327` | `BULLISH_HAMMER` | 638.1161 | `WATCH` | HOLD |
| `NBISBUSDT` | 130.21 | 140.313199 | `-7.20%` | `25.28` / `24.44` | `36.45` | `0.359` | `NONE` | 124.22034 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0811 | 0.07775 | `+4.31%` | `5.03` / `3.18` | `38.95` | `0.194` | `NONE` | 0.0773694 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3886.49 | 4006.395633 | `-2.99%` | `33.78` / `30.29` | `34.93` | `0.391` | `NONE` | 3785.44126 | `WATCH` | HOLD |
| `SOXSBUSDT` | 44.84 | 56.251509 | `-20.29%` | `13.57` / `16.77` | `40.66` | `0.245` | `NONE` | 42.77736 | `EXIT_SHORT_STOCH_20` | HOLD |
| `GRAMUSDT` | 1.154 | 1.13784 | `+1.42%` | `17.25` / `14.73` | `41.92` | `0.265` | `BULLISH_ENGULFING` | 1.100916 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `AVAXUSDT` | 8.321 | 8.429567 | `-1.29%` | `30.47` / `26.7` | `39.85` | `0.301` | `BULLISH_HAMMER` | 8.104654 | `WATCH` | HOLD |
| `INITUSDT` | 0.11822 | 0.157717 | `-25.04%` | `33.59` / `29.68` | `40.21` | `0.379` | `NONE` | 0.11278188 | `WATCH` | HOLD |
| `PAXGUSDT` | 3889.53 | 4010.911942 | `-3.03%` | `34.54` / `30.67` | `35.06` | `0.396` | `NONE` | 3788.40222 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001519 | 0.001552 | `-2.12%` | `4.94` / `3.99` | `42.88` | `0.207` | `BULLISH_ENGULFING` | 0.00144913 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRXUSDT` | 0.3156 | 0.31776 | `-0.68%` | `16.4` / `15.82` | `36.59` | `0.246` | `BEARISH_SHOOTING_STAR` | 0.3073944 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2006.96 | 2141.61375 | `-6.29%` | `48.49` / `47.67` | `33.42` | `0.239` | `NONE` | 1954.77904 | `WATCH` | HOLD |
| `ZECUSDT` | 956.24 | 1128.723733 | `-15.28%` | `44.35` / `36.8` | `43.06` | `0.361` | `BULLISH_HAMMER` | 912.25296 | `WATCH` | HOLD |
| `NEARUSDT` | 3.429 | 3.672456 | `-6.63%` | `57.5` / `47.52` | `41.26` | `0.453` | `BULLISH_HAMMER` | 3.2861874 | `WATCH` | HOLD |
