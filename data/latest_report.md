# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T04:41:03Z`
- **Ciclo de ejecucion:** `#192`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un regimen claramente bajista (BEARISH) con la gran mayoria de los activos cotizando por debajo de la EMA 200 y con pendientes negativas pronunciadas. Se evaluan los pilares de tendencia bajista y scalping en 15m (como PEPEUSDT bajo M15_SCALPER_PULLBACK_SHORT), manteniendo la cautela y preparandose para buscar entradas SHORT o gestionar posiciones segun los criterios de los pilares definidos. No hay posiciones abiertas actuales en el portfolio, por lo que no se requiere ajuste dinamico de SL/TP en este ciclo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.56e-06 | 5e-06 | `-9.09%` | `14.81` / `14.61` | `25.34` | `0.181` | `NONE` | 4.77e-06 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (78%) |
| `BTCUSDT` | 73695.45 | 75493.328768 | `-2.38%` | `26.53` / `29.17` | `43.77` | `0.213` | `BEARISH_ENGULFING` | 71779.3683 | `WATCH` | HOLD |
| `ETHUSDT` | 2049.6 | 2167.966368 | `-5.46%` | `27.19` / `28.94` | `41.75` | `0.191` | `NONE` | 1996.3104 | `WATCH` | HOLD |
| `UNIUSDT` | 6.253 | 6.896056 | `-9.32%` | `23.25` / `17.41` | `36.11` | `0.223` | `BULLISH_HAMMER` | 5.965362 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001434 | 0.001547 | `-7.31%` | `4.87` / `6.05` | `29.34` | `0.059` | `NONE` | 0.00136804 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.542 | 3.751596 | `-5.59%` | `9.59` / `16.18` | `37.95` | `0.093` | `BULLISH_HAMMER` | 3.4101552 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 82.96 | 87.997647 | `-5.72%` | `28.96` / `30.9` | `40.43` | `0.104` | `BULLISH_HAMMER` | 80.80304 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0449 | 1.138783 | `-8.24%` | `17.67` / `22.7` | `38.22` | `0.023` | `BEARISH_ENGULFING` | 1.0177326 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.536 | 7.923186 | `-4.89%` | `19.67` / `17.0` | `32.83` | `0.154` | `BULLISH_HAMMER` | 7.189344 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1504 | 0.164489 | `-8.57%` | `8.15` / `8.54` | `29.88` | `0.111` | `BEARISH_ENGULFING` | 0.14479696 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1437 | 0.159633 | `-9.98%` | `10.72` / `14.53` | `28.93` | `0.087` | `BEARISH_ENGULFING` | 0.13785436 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 677.0 | 691.673407 | `-2.12%` | `15.05` / `19.63` | `39.64` | `0.064` | `NONE` | 659.398 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06718 | 0.07087 | `-5.21%` | `30.51` / `31.73` | `37.5` | `0.109` | `NONE` | 0.06543332 | `WATCH` | HOLD |
| `QNTUSDT` | 165.45 | 190.203519 | `-13.01%` | `11.76` / `9.72` | `26.62` | `0.098` | `BEARISH_SHOOTING_STAR` | 157.8393 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LINKUSDT` | 10.104 | 10.725708 | `-5.80%` | `18.12` / `20.61` | `33.37` | `0.096` | `BEARISH_ENGULFING` | 9.8203168 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 118.44 | 128.268783 | `-7.66%` | `12.09` / `11.82` | `29.86` | `0.073` | `BEARISH_SHOOTING_STAR` | 114.66212 | `EXIT_SHORT_STOCH_20` | HOLD |
