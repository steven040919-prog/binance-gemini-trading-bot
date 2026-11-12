# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T06:45:37Z`
- **Ciclo de ejecucion:** `#205`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen netamente bajista en temporalidad 1H, con todos los activos analizados cotizando por debajo de la EMA 200 y con pendientes negativas pronunciadas. Ninguno de los activos cumple con las condiciones estrictas de los Pilares LONG (P1-P4), ya que la estructura general es bajista y las confirmaciones de giro alcista con estocástico y divergencias no se encuentran completas o alineadas para toma de posiciones en spot. Tampoco se activan operaciones SHORT bajo el pilar S1, ya que los precios actuales se encuentran alejados de la resistencia de la EMA 200 sin el rechazo necesario en sobrecompra. Por lo tanto, no se abren nuevas posiciones y se mantiene la postura defensiva.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 73572.53 | 75443.768348 | `-2.48%` | `12.81` / `20.16` | `41.66` | `0.167` | `BEARISH_SHOOTING_STAR` | 71659.64422 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `PEPEUSDT` | 4.53e-06 | 5e-06 | `-9.41%` | `10.2` / `12.73` | `24.0` | `0.198` | `BULLISH_HAMMER` | 4.35e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2045.23 | 2165.537578 | `-5.56%` | `17.08` / `22.22` | `39.83` | `0.159` | `BEARISH_SHOOTING_STAR` | 1992.05402 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 82.79 | 87.881985 | `-5.79%` | `20.04` / `25.2` | `38.96` | `0.117` | `BEARISH_SHOOTING_STAR` | 80.63746 | `WATCH` | HOLD |
| `UNIUSDT` | 6.143 | 6.879429 | `-10.70%` | `16.95` / `20.48` | `30.86` | `0.12` | `BEARISH_ENGULFING` | 5.9308238 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0409 | 1.137031 | `-8.45%` | `7.89` / `12.25` | `35.87` | `0.059` | `NONE` | 1.0138366 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.514 | 3.745391 | `-6.18%` | `3.23` / `6.76` | `35.41` | `0.093` | `BEARISH_SHOOTING_STAR` | 3.4037688 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.431 | 7.911128 | `-6.07%` | `10.54` / `15.09` | `30.86` | `0.127` | `NONE` | 7.1104012 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1421 | 0.159201 | `-10.74%` | `4.27` / `7.43` | `25.61` | `0.094` | `NONE` | 0.13718228 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 674.06 | 691.429114 | `-2.51%` | `2.3` / `7.59` | `35.28` | `0.022` | `BEARISH_SHOOTING_STAR` | 656.53444 | `EXIT_SHORT_STOCH_20` | HOLD |
| `HYPEUSDT` | 71.17 | 76.868482 | `-7.41%` | `25.18` / `33.63` | `36.88` | `0.052` | `NONE` | 69.31958 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1497 | 0.164201 | `-8.83%` | `5.03` / `6.71` | `29.39` | `0.15` | `BEARISH_SHOOTING_STAR` | 0.14501918 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 164.57 | 189.742772 | `-13.27%` | `10.92` / `12.31` | `26.13` | `0.142` | `BEARISH_ENGULFING` | 157.975942 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06689 | 0.070794 | `-5.51%` | `20.17` / `25.29` | `34.58` | `0.102` | `BEARISH_SHOOTING_STAR` | 0.06515086 | `WATCH` | HOLD |
| `LINKUSDT` | 10.038 | 10.713227 | `-6.30%` | `7.23` / `12.49` | `30.41` | `0.104` | `BEARISH_SHOOTING_STAR` | 9.777012 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3965.52 | 4027.342492 | `-1.54%` | `15.09` / `17.24` | `29.64` | `0.205` | `BULLISH_HAMMER` | 3862.41648 | `EXIT_SHORT_STOCH_20` | HOLD |
