# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T06:26:44Z`
- **Ciclo de ejecucion:** `#203`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general se encuentra en un regimen predominantemente bajista con la mayoria de los activos cotizando por debajo de la EMA 200 de 1H con pendientes negativas. Se evaluaron los 16 candidatos frente a la arquitectura de 4 Pilares LONG y el Pilar S1 SHORT. Ningun activo cumple la totalidad de los criterios cuantitativos requeridos (falta de confirmacion en el giro del Estocastico stoch_turning_up, umbrales de RSI/BB %B no alcanzados o ausencia de climax de volumen). No hay posiciones abiertas para ajustar SL/TP. Se permanece en liquidez protegiendo el capital.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 73734.42 | 75445.379194 | `-2.27%` | `16.86` / `21.51` | `45.25` | `0.277` | `BULLISH_ENGULFING` | 71817.32508 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `PEPEUSDT` | 4.56e-06 | 5e-06 | `-8.82%` | `12.16` / `13.38` | `25.31` | `0.235` | `BULLISH_HAMMER` | 4.38e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `ETHUSDT` | 2053.32 | 2165.618075 | `-5.19%` | `21.05` / `23.54` | `44.58` | `0.298` | `BULLISH_ENGULFING` | 1999.93368 | `WATCH` | **HOLD** (0%) |
| `UNIUSDT` | 6.202 | 6.880016 | `-9.85%` | `20.33` / `21.61` | `33.49` | `0.2` | `BEARISH_ENGULFING` | 5.979536 | `WATCH` | HOLD |
| `SOLUSDT` | 83.21 | 87.886164 | `-5.32%` | `23.86` / `26.47` | `43.69` | `0.233` | `BULLISH_ENGULFING` | 81.04654 | `WATCH` | **HOLD** (0%) |
| `XRPUSDT` | 1.0437 | 1.137059 | `-8.21%` | `10.05` / `12.97` | `38.78` | `0.123` | `NONE` | 1.0165638 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.549 | 3.745739 | `-5.25%` | `6.29` / `7.78` | `39.91` | `0.175` | `BULLISH_ENGULFING` | 3.4128202 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.428 | 7.911098 | `-6.11%` | `10.41` / `15.05` | `30.63` | `0.124` | `NONE` | 7.1105056 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 675.99 | 691.448318 | `-2.24%` | `6.47` / `8.98` | `39.8` | `0.121` | `NONE` | 658.41426 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1435 | 0.159215 | `-9.87%` | `6.27` / `8.1` | `29.84` | `0.165` | `BULLISH_HAMMER` | 0.1378506 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1503 | 0.164207 | `-8.47%` | `6.24` / `7.12` | `30.47` | `0.179` | `BEARISH_SHOOTING_STAR` | 0.14513088 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.0672 | 0.070797 | `-5.08%` | `23.41` / `26.37` | `39.39` | `0.197` | `BULLISH_ENGULFING` | 0.0654528 | `WATCH` | HOLD |
| `QNTUSDT` | 166.09 | 189.757896 | `-12.47%` | `13.53` / `13.18` | `28.95` | `0.197` | `BEARISH_ENGULFING` | 158.44986 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `LINKUSDT` | 10.096 | 10.713804 | `-5.77%` | `10.61` / `13.62` | `36.21` | `0.181` | `NONE` | 9.7967728 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3973.18 | 4027.418711 | `-1.35%` | `22.34` / `19.65` | `32.73` | `0.292` | `BULLISH_HAMMER` | 3869.87732 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `INTCBUSDT` | 60.72 | 59.222011 | `+2.53%` | `15.24` / `18.3` | `47.57` | `0.255` | `BULLISH_ENGULFING` | 58.462704 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
