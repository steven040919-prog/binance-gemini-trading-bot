# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-10T08:06:01Z`
- **Ciclo de ejecucion:** `#14`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra operando mayoritariamente bajo la EMA 200 en temporalidad 1h con sesgo bajista generalizado. No se cumplen de forma estricta los requisitos de los Pilares LONG (P1-P4) ni del Pilar SHORT (S1) debido a la ausencia de confluencia exacta entre la distancia a la EMA 200, los niveles extremos del oscilador estocástico y las velas de confirmación para apertura inmediata. El portafolio no registra posiciones abiertas con ganancias que requieran ajuste dinámico (ADJUST). Se mantiene la disciplina de gestión de riesgo en modo HOLD para preservar el capital.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1149.9 | 1243.714116 | `-7.54%` | `17.24` / `16.25` | `33.04` | `0.248` | `BEARISH_ENGULFING` | 1111.47296 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 86.04 | 90.350366 | `-4.77%` | `35.82` / `33.62` | `41.72` | `0.24` | `BEARISH_SHOOTING_STAR` | 83.80296 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1673 | 0.167366 | `-0.04%` | `4.41` / `7.59` | `34.99` | `0.054` | `BULLISH_HAMMER` | 0.16261712 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 126.98 | 130.143286 | `-2.43%` | `20.16` / `16.59` | `34.49` | `0.113` | `BEARISH_SHOOTING_STAR` | 122.037876 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74838.0 | 76272.081377 | `-1.88%` | `37.77` / `35.39` | `48.43` | `0.4` | `BULLISH_ENGULFING` | 72892.212 | `WATCH` | **HOLD** (75%) |
| `QNTUSDT` | 191.37 | 196.391815 | `-2.56%` | `19.57` / `16.4` | `36.13` | `0.177` | `BEARISH_SHOOTING_STAR` | 185.749504 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BCHUSDT` | 238.5 | 260.190918 | `-8.34%` | `40.5` / `40.47` | `42.87` | `0.315` | `BEARISH_SHOOTING_STAR` | 232.299 | `WATCH` | HOLD |
| `ETHUSDT` | 2115.85 | 2222.132315 | `-4.78%` | `23.93` / `29.73` | `39.15` | `0.143` | `BEARISH_SHOOTING_STAR` | 2060.8379 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.34e-06 | 5e-06 | `+6.47%` | `91.05` / `82.81` | `66.56` | `0.901` | `NONE` | 5.09e-06 | `EXIT_LONG_STOCH_80` | HOLD |
| `AVAXUSDT` | 8.467 | 8.384671 | `+0.98%` | `4.81` / `9.81` | `48.94` | `0.166` | `BEARISH_SHOOTING_STAR` | 8.246858 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0936 | 1.18172 | `-7.46%` | `51.64` / `53.7` | `43.24` | `0.288` | `BEARISH_ENGULFING` | 1.0651664 | `WATCH` | HOLD |
| `NEARUSDT` | 3.632 | 3.804001 | `-4.52%` | `73.33` / `69.4` | `52.91` | `0.606` | `BEARISH_SHOOTING_STAR` | 3.5209264 | `WATCH` | HOLD |
| `NVDABUSDT` | 182.2 | 190.520933 | `-4.37%` | `88.3` / `80.86` | `58.61` | `0.926` | `NONE` | 176.5726 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 690.39 | 695.887677 | `-0.79%` | `70.04` / `71.63` | `52.61` | `0.648` | `NONE` | 672.43986 | `WATCH` | HOLD |
| `UNIUSDT` | 7.036 | 7.043937 | `-0.11%` | `71.34` / `67.6` | `55.65` | `0.66` | `BEARISH_SHOOTING_STAR` | 6.803136 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0013 | 1.001285 | `+0.00%` | `72.22` / `78.52` | `56.55` | `0.874` | `BEARISH_ENGULFING` | 0.9752662 | `WATCH` | HOLD |
