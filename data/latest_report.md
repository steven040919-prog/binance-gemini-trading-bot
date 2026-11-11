# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T01:34:42Z`
- **Ciclo de ejecucion:** `#95`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general opera bajo un régimen bajista con la mayoría de los activos cotizando por debajo de la EMA 200. No se activan nuevos pilares de entrada LONG (P1-P4) debido a la ausencia de confluencias extremas requeridas o divergencias válidas en los candidatos evaluados. Para futuros USDT-M, se vigila el pilar SHORT (S1) en activos cercanos a la resistencia de la EMA 200, manteniendo la gestión de riesgo estricta (HOLD o ADJUST según corresponda en posiciones con ganancia).

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1029.08 | 1220.464521 | `-15.68%` | `20.2` / `22.62` | `31.64` | `0.225` | `BEARISH_ENGULFING` | 981.74232 | `WATCH` | HOLD |
| `UNIUSDT` | 6.748 | 7.016369 | `-3.82%` | `17.3` / `14.13` | `43.62` | `0.345` | `BEARISH_SHOOTING_STAR` | 6.437592 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 4037.36 | 4035.745967 | `+0.04%` | `37.99` / `30.58` | `42.79` | `0.435` | `BULLISH_ENGULFING` | 3932.38864 | `WATCH` | HOLD |
| `CYBERUSDT` | 0.273 | 0.283241 | `-3.62%` | `15.27` / `21.89` | `45.83` | `0.342` | `BEARISH_SHOOTING_STAR` | 0.260442 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73733.58 | 75897.303943 | `-2.85%` | `45.44` / `46.52` | `45.11` | `0.408` | `BEARISH_ENGULFING` | 71816.50692 | `WATCH` | **HOLD** (75%) |
| `TRXUSDT` | 0.318 | 0.318983 | `-0.31%` | `14.44` / `14.44` | `46.17` | `0.29` | `BULLISH_ENGULFING` | 0.309732 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2055.08 | 2198.040119 | `-6.50%` | `45.39` / `43.45` | `40.99` | `0.39` | `BULLISH_ENGULFING` | 1988.926904 | `WATCH` | HOLD |
| `INITUSDT` | 0.24792 | 0.164904 | `+50.34%` | `48.64` / `54.38` | `51.45` | `0.438` | `BEARISH_ENGULFING` | 0.23651568 | `WATCH` | HOLD |
| `PAXGUSDT` | 4040.0 | 4041.899713 | `-0.05%` | `38.1` / `30.25` | `42.9` | `0.432` | `BEARISH_ENGULFING` | 3934.96 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001894 | 0.001543 | `+22.74%` | `59.05` / `52.39` | `62.37` | `0.745` | `NONE` | 0.00180688 | `WATCH` | HOLD |
| `SOLUSDT` | 83.45 | 89.329227 | `-6.58%` | `48.91` / `44.01` | `41.71` | `0.407` | `BULLISH_ENGULFING` | 80.35685 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0552 | 1.163485 | `-9.31%` | `41.93` / `42.82` | `38.53` | `0.303` | `NONE` | 1.01924336 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.46e-06 | 5e-06 | `+8.02%` | `59.48` / `49.46` | `61.45` | `0.939` | `BEARISH_SHOOTING_STAR` | 5.21e-06 | `WATCH` | HOLD |
| `NEARUSDT` | 3.683 | 3.77511 | `-2.44%` | `55.22` / `44.11` | `57.84` | `0.879` | `MORNING_STAR` | 3.513582 | `WATCH` | HOLD |
| `BNBUSDT` | 682.14 | 693.747574 | `-1.67%` | `50.69` / `45.41` | `48.96` | `0.487` | `BULLISH_ENGULFING` | 664.40436 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0012 | 1.001214 | `-0.00%` | `83.33` / `78.83` | `54.62` | `0.639` | `NONE` | 0.9751688 | `EXIT_LONG_STOCH_80` | HOLD |
