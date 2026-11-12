# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T22:32:27Z`
- **Ciclo de ejecucion:** `#271`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> Evaluación general del mercado en temporalidad 1H con sesgo bajista (bearish) predominante debajo de la EMA 200. No se cumplen los requisitos estrictos de los Pilares Long (P1-P4) debido a la debilidad macro y la falta de capitulaciones o divergencias alcistas claras en soportes mayores. Sin embargo, se identifican oportunidades de entrada bajista en Futuros USDT-M mediante el Pilar S1 o el Scalper M15 (como NBISBUSDT) y señales de salida en activos con sobreventa extrema (Estocástico < 20). No hay posiciones abiertas actuales para ajustar (ADJUST).

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71496.49 | 75029.172188 | `-4.71%` | `10.1` / `12.57` | `25.1` | `0.194` | `BULLISH_HAMMER` | 69637.58126 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `ZECUSDT` | 940.68 | 1134.593034 | `-17.09%` | `22.55` / `27.34` | `34.2` | `0.096` | `NONE` | 897.40872 | `WATCH` | HOLD |
| `SOLUSDT` | 81.44 | 87.033183 | `-6.43%` | `30.37` / `32.6` | `35.99` | `0.25` | `NONE` | 79.32256 | `WATCH` | HOLD |
| `NEARUSDT` | 3.39 | 3.693557 | `-8.22%` | `36.54` / `40.45` | `33.61` | `0.214` | `BEARISH_ENGULFING` | 3.271842 | `WATCH` | HOLD |
| `UNIUSDT` | 5.999 | 6.764883 | `-11.32%` | `30.05` / `33.06` | `30.53` | `0.212` | `NONE` | 5.817028 | `WATCH` | HOLD |
| `BNBUSDT` | 653.55 | 686.845809 | `-4.85%` | `16.82` / `18.58` | `24.94` | `0.233` | `BEARISH_SHOOTING_STAR` | 636.5577 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NBISBUSDT` | 128.9 | 140.736056 | `-8.41%` | `22.46` / `21.47` | `33.73` | `0.276` | `BEARISH_SHOOTING_STAR` | 134.8294 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (82%) |
| `XAUTUSDT` | 3876.42 | 4009.697198 | `-3.32%` | `22.72` / `22.44` | `28.71` | `0.268` | `BEARISH_SHOOTING_STAR` | 3775.63308 | `WATCH` | HOLD |
| `AAVEUSDT` | 113.76 | 125.897282 | `-9.64%` | `48.93` / `44.84` | `34.85` | `0.356` | `BEARISH_SHOOTING_STAR` | 110.247744 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.14 | 1.138313 | `+0.15%` | `12.98` / `10.35` | `37.38` | `0.125` | `BEARISH_SHOOTING_STAR` | 1.08756 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ERAUSDT` | 0.0813 | 0.077774 | `+4.53%` | `3.23` / `5.38` | `38.14` | `0.079` | `NONE` | 0.0775602 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AVAXUSDT` | 8.331 | 8.44173 | `-1.31%` | `20.11` / `20.74` | `39.77` | `0.264` | `BEARISH_ENGULFING` | 8.0883926 | `WATCH` | HOLD |
| `QNTUSDT` | 163.61 | 185.966457 | `-12.02%` | `38.65` / `31.36` | `39.5` | `0.445` | `BULLISH_ENGULFING` | 157.188862 | `WATCH` | HOLD |
| `SOXSBUSDT` | 45.45 | 56.534311 | `-19.61%` | `28.38` / `29.89` | `41.48` | `0.226` | `BEARISH_SHOOTING_STAR` | 43.3593 | `WATCH` | HOLD |
| `PAXGUSDT` | 3879.03 | 4014.238195 | `-3.37%` | `22.62` / `22.78` | `28.38` | `0.267` | `NONE` | 3778.17522 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3158 | 0.317828 | `-0.64%` | `16.18` / `18.15` | `37.92` | `0.267` | `BULLISH_ENGULFING` | 0.3075892 | `EXIT_SHORT_STOCH_20` | HOLD |
