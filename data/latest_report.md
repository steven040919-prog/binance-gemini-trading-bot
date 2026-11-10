# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-10T23:22:46Z`
- **Ciclo de ejecucion:** `#41`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de criptomonedas opera predominantemente bajo un régimen bajista en temporalidad 1H, con la gran mayoría de los activos cotizando por debajo de sus respectivas EMA 200 y con pendientes negativas. No se activan nuevos pilares LONG (P1-P4) debido a la ausencia de condiciones de tendencia alcista o rebotes limpios sobre soportes clave. Tampoco se cumplen las estrictas confluencias del Pilar S1 Short en los activos evaluados (falta de testeo directo y rechazo en resistencia EMA 200 con estocástico en sobrecompra). Por lo tanto, se mantiene el estado de observación (HOLD) con 0 posiciones abiertas y 14.0 USDT de capital libre.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1044.46 | 1223.5694 | `-14.64%` | `25.85` / `26.38` | `33.97` | `0.232` | `BEARISH_ENGULFING` | 996.41484 | `WATCH` | HOLD |
| `UNIUSDT` | 6.666 | 7.014973 | `-4.97%` | `13.19` / `15.33` | `36.28` | `0.175` | `BEARISH_ENGULFING` | 6.359364 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 123.85 | 129.636559 | `-4.46%` | `54.08` / `48.93` | `35.92` | `0.322` | `BEARISH_SHOOTING_STAR` | 119.2168 | `WATCH` | HOLD |
| `QNTUSDT` | 181.22 | 194.461996 | `-6.81%` | `38.07` / `37.97` | `33.34` | `0.265` | `BULLISH_HAMMER` | 172.88388 | `WATCH` | HOLD |
| `XAUTUSDT` | 4026.78 | 4035.464663 | `-0.22%` | `22.83` / `18.91` | `34.65` | `0.315` | `BULLISH_HAMMER` | 3922.08372 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73728.23 | 75927.561554 | `-2.90%` | `48.26` / `46.65` | `44.1` | `0.365` | `BEARISH_ENGULFING` | 71811.29602 | `WATCH` | **HOLD** (70%) |
| `TRXUSDT` | 0.318 | 0.319095 | `-0.34%` | `16.67` / `15.19` | `45.52` | `0.294` | `BULLISH_HAMMER` | 0.309732 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2051.55 | 2200.499517 | `-6.77%` | `42.34` / `41.92` | `38.89` | `0.325` | `BULLISH_HAMMER` | 1986.96784 | `WATCH` | HOLD |
| `PAXGUSDT` | 4029.29 | 4041.762339 | `-0.31%` | `22.16` / `18.64` | `34.24` | `0.311` | `BULLISH_ENGULFING` | 3924.52846 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.00185 | 0.001537 | `+20.34%` | `48.65` / `51.23` | `59.87` | `0.662` | `NONE` | 0.0017649 | `WATCH` | HOLD |
| `SOLUSDT` | 83.08 | 89.429547 | `-7.10%` | `38.68` / `37.91` | `36.84` | `0.304` | `BEARISH_ENGULFING` | 80.300376 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0549 | 1.165353 | `-9.48%` | `43.6` / `43.21` | `37.24` | `0.253` | `BEARISH_ENGULFING` | 1.0199079 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.32e-06 | 5e-06 | `+5.71%` | `35.95` / `32.03` | `54.18` | `0.562` | `MORNING_STAR` | 5.08e-06 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.146 | 1.104087 | `+3.80%` | `82.17` / `79.1` | `68.07` | `1.009` | `NONE` | 1.093284 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 677.68 | 693.961748 | `-2.35%` | `36.57` / `33.62` | `40.26` | `0.299` | `BEARISH_SHOOTING_STAR` | 660.06032 | `WATCH` | HOLD |
| `NEARUSDT` | 3.567 | 3.77323 | `-5.47%` | `34.24` / `34.35` | `47.27` | `0.342` | `BEARISH_ENGULFING` | 3.402918 | `WATCH` | HOLD |
