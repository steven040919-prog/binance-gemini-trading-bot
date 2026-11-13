# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T01:16:55Z`
- **Ciclo de ejecucion:** `#283`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado opera de manera generalizada bajo presión bajista con la mayoría de los activos cotizando por debajo de la EMA 200 en temporalidad de 1H. Los activos analizados muestran configuraciones mixtas, destacando GRAMUSDT con una entrada LONG validada bajo el Pilar 1 (Pullback de valor sobre EMA 200), mientras que BTCUSDT y otros pares bajo régimen bajista estricto se encuentran en zonas de vigilancia o gestionando salidas. No hay posiciones abiertas actuales en el portafolio, por lo que se prioriza la ejecución de entradas de alta probabilidad según las reglas de los pilares institucionales.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71000.0 | 74880.782402 | `-5.18%` | `14.01` / `12.37` | `21.26` | `0.16` | `BEARISH_ENGULFING` | 69154.0 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NBISBUSDT` | 130.77 | 140.318771 | `-6.81%` | `25.69` / `24.58` | `37.46` | `0.371` | `NONE` | 124.75458 | `WATCH` | HOLD |
| `BNBUSDT` | 655.48 | 685.514595 | `-4.38%` | `31.55` / `26.0` | `31.73` | `0.337` | `BULLISH_HAMMER` | 638.43752 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0812 | 0.077751 | `+4.44%` | `5.19` / `3.24` | `39.18` | `0.198` | `NONE` | 0.0774648 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOXSBUSDT` | 44.0 | 56.243151 | `-21.77%` | `9.72` / `15.48` | `36.15` | `0.134` | `BEARISH_ENGULFING` | 41.976 | `EXIT_SHORT_STOCH_20` | HOLD |
| `GRAMUSDT` | 1.152 | 1.13782 | `+1.25%` | `16.86` / `14.6` | `41.32` | `0.255` | `BULLISH_ENGULFING` | 1.099008 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `AVAXUSDT` | 8.337 | 8.429726 | `-1.10%` | `32.47` / `27.37` | `41.27` | `0.333` | `BULLISH_HAMMER` | 8.107923 | `WATCH` | HOLD |
| `INITUSDT` | 0.1175 | 0.15771 | `-25.50%` | `32.67` / `29.37` | `39.53` | `0.358` | `NONE` | 0.112095 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001516 | 0.001552 | `-2.32%` | `4.49` / `3.84` | `42.51` | `0.196` | `BULLISH_ENGULFING` | 0.00144626 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRXUSDT` | 0.3156 | 0.31776 | `-0.68%` | `16.4` / `15.82` | `36.59` | `0.246` | `BEARISH_SHOOTING_STAR` | 0.3073944 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2012.57 | 2141.669571 | `-6.03%` | `52.5` / `49.01` | `36.71` | `0.324` | `BULLISH_HAMMER` | 1960.24318 | `WATCH` | HOLD |
| `ZECUSDT` | 959.17 | 1128.752888 | `-15.02%` | `46.05` / `37.37` | `44.29` | `0.406` | `BULLISH_HAMMER` | 915.04818 | `WATCH` | HOLD |
| `SOLUSDT` | 81.59 | 86.78923 | `-5.99%` | `44.09` / `39.42` | `39.46` | `0.355` | `BULLISH_HAMMER` | 79.414518 | `WATCH` | HOLD |
| `NEARUSDT` | 3.442 | 3.672585 | `-6.28%` | `60.74` / `48.6` | `43.44` | `0.535` | `BULLISH_HAMMER` | 3.2858052 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0335 | 1.119315 | `-7.67%` | `59.34` / `55.61` | `42.32` | `0.392` | `BULLISH_HAMMER` | 1.006629 | `WATCH` | HOLD |
| `XAUTUSDT` | 3894.5 | 4006.475334 | `-2.79%` | `36.64` / `31.24` | `39.55` | `0.45` | `NONE` | 3793.243 | `WATCH` | HOLD |
