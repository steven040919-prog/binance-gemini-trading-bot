# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-10T23:39:29Z`
- **Ciclo de ejecucion:** `#47`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra predominantemente bajo régimen bajista (mayoría de activos cotizando por debajo de la EMA 200 con pendientes negativas). No se activan nuevos Pilares LONG (P1-P4) ni el Pilar SHORT (S1) debido a que no se cumplen con exactitud los filtros requeridos de rechazo en resistencia o confluencias extremas de osciladores en este ciclo horario. Las posiciones abiertas activas se mantienen en modo WATCH o gestión estandar, priorizando la preservación del capital con 0 posiciones abiertas y 14.0 USDT de liquidez disponible.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1045.9 | 1223.583729 | `-14.52%` | `26.08` / `26.46` | `34.39` | `0.237` | `BEARISH_ENGULFING` | 997.7886 | `WATCH` | HOLD |
| `UNIUSDT` | 6.674 | 7.015053 | `-4.86%` | `13.68` / `15.49` | `36.99` | `0.186` | `BEARISH_ENGULFING` | 6.366996 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1608 | 0.166353 | `-3.34%` | `36.91` / `30.56` | `38.57` | `0.339` | `MORNING_STAR` | 0.1534032 | `WATCH` | HOLD |
| `QNTUSDT` | 181.1 | 194.460802 | `-6.87%` | `37.77` / `37.87` | `33.11` | `0.258` | `BULLISH_HAMMER` | 172.86466 | `WATCH` | HOLD |
| `AAVEUSDT` | 123.83 | 129.63636 | `-4.48%` | `53.96` / `48.89` | `35.83` | `0.319` | `BEARISH_SHOOTING_STAR` | 119.21744 | `WATCH` | HOLD |
| `XAUTUSDT` | 4028.14 | 4035.478195 | `-0.18%` | `23.49` / `19.13` | `35.58` | `0.324` | `BULLISH_HAMMER` | 3923.40836 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73750.88 | 75927.786927 | `-2.87%` | `48.62` / `46.77` | `44.45` | `0.374` | `BEARISH_ENGULFING` | 71833.35712 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3177 | 0.319092 | `-0.44%` | `13.33` / `14.07` | `42.0` | `0.195` | `NONE` | 0.3094398 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2052.2 | 2200.505985 | `-6.74%` | `42.55` / `41.99` | `39.17` | `0.33` | `BULLISH_HAMMER` | 1986.95016 | `WATCH` | HOLD |
| `INITUSDT` | 0.26859 | 0.16313 | `+64.65%` | `58.58` / `64.26` | `57.59` | `0.6` | `BULLISH_HAMMER` | 0.25623486 | `WATCH` | HOLD |
| `PAXGUSDT` | 4031.17 | 4041.781046 | `-0.26%` | `23.05` / `18.93` | `35.53` | `0.324` | `BULLISH_ENGULFING` | 3926.35958 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001832 | 0.001537 | `+19.19%` | `47.27` / `50.77` | `58.3` | `0.635` | `NONE` | 0.00174773 | `WATCH` | HOLD |
| `SOLUSDT` | 83.27 | 89.431438 | `-6.89%` | `40.13` / `38.39` | `38.93` | `0.335` | `BEARISH_ENGULFING` | 80.27844 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0574 | 1.165378 | `-9.27%` | `45.01` / `43.68` | `38.35` | `0.285` | `BEARISH_ENGULFING` | 1.0198354 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.32e-06 | 5e-06 | `+5.71%` | `35.95` / `32.03` | `54.18` | `0.562` | `MORNING_STAR` | 5.08e-06 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.142 | 1.104048 | `+3.44%` | `80.65` / `78.59` | `67.18` | `0.971` | `NONE` | 1.089468 | `EXIT_LONG_STOCH_80` | HOLD |
