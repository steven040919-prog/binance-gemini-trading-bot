# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T20:26:57Z`
- **Ciclo de ejecucion:** `#261`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado cripto mantiene un sesgo bajista generalizado en temporalidad de 1H con la mayoria de los activos cotizando por debajo de la EMA 200 y en zonas de sobreventa segun RSI y Estocastico. No se cumplen de forma limpia los criterios estrictos de los Pilares Long (P1-P4) debido a la debilidad macro y la pendiente negativa de las medias moviles principales. Sin embargo, en Binance Futuros USDT-M se identifica oportunidad bajista en SOLUSDT bajo el pilar M15_SCALPER_PULLBACK_SHORT. Para el resto de activos evaluados como BTCUSDT y BNBUSDT, nos mantenemos en vigilancia o gestionando cierres por salida de sobreventa.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71551.3 | 75084.474579 | `-4.71%` | `16.58` / `19.61` | `23.22` | `0.135` | `BULLISH_HAMMER` | 69690.9662 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 950.32 | 1136.385531 | `-16.37%` | `27.65` / `21.84` | `37.52` | `0.154` | `MORNING_STAR` | 906.60528 | `WATCH` | HOLD |
| `SOLUSDT` | 81.52 | 87.099467 | `-6.41%` | `37.06` / `37.22` | `35.65` | `0.213` | `BEARISH_ENGULFING` | 83.63952 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (78%) |
| `NEARUSDT` | 3.429 | 3.699888 | `-7.32%` | `42.82` / `37.12` | `37.8` | `0.335` | `BULLISH_HAMMER` | 3.2860726 | `WATCH` | HOLD |
| `UNIUSDT` | 6.024 | 6.776577 | `-11.11%` | `33.18` / `29.3` | `32.3` | `0.239` | `NONE` | 5.809328 | `WATCH` | HOLD |
| `BNBUSDT` | 654.48 | 687.465229 | `-4.80%` | `19.5` / `20.44` | `25.83` | `0.207` | `BULLISH_HAMMER` | 637.46352 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1394 | 0.156521 | `-10.94%` | `42.41` / `36.86` | `29.55` | `0.266` | `BULLISH_HAMMER` | 0.13416708 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.126 | 1.138052 | `-1.06%` | `3.95` / `20.84` | `35.11` | `-0.025` | `NONE` | 1.074204 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3881.6 | 4012.917735 | `-3.27%` | `24.93` / `22.03` | `28.32` | `0.243` | `BULLISH_HAMMER` | 3780.6784 | `WATCH` | HOLD |
| `AAVEUSDT` | 113.6 | 126.171334 | `-9.96%` | `36.69` / `34.37` | `32.26` | `0.308` | `NONE` | 110.22816 | `WATCH` | HOLD |
| `QNTUSDT` | 161.79 | 186.334485 | `-13.17%` | `26.14` / `24.18` | `30.43` | `0.132` | `BULLISH_HAMMER` | 155.69988 | `WATCH` | HOLD |
| `AVAXUSDT` | 8.346 | 8.44233 | `-1.14%` | `22.78` / `22.13` | `40.62` | `0.24` | `BEARISH_ENGULFING` | 8.0733424 | `WATCH` | HOLD |
| `ERAUSDT` | 0.082 | 0.077724 | `+5.50%` | `7.02` / `10.96` | `38.83` | `0.001` | `BEARISH_SHOOTING_STAR` | 0.078228 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.432 | 7.84465 | `-5.26%` | `47.04` / `37.2` | `42.12` | `0.44` | `NONE` | 7.090128 | `WATCH` | HOLD |
| `WLDUSDT` | 0.2992 | 0.328987 | `-9.05%` | `43.61` / `42.61` | `36.45` | `0.118` | `NONE` | 0.28986336 | `WATCH` | HOLD |
| `PAXGUSDT` | 3885.98 | 4017.615601 | `-3.28%` | `26.15` / `22.87` | `28.72` | `0.252` | `BULLISH_HAMMER` | 3784.94452 | `WATCH` | HOLD |
