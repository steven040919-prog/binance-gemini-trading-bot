# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T12:57:25Z`
- **Ciclo de ejecucion:** `#324`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra mayoritariamente bajo la EMA 200 en temporalidad 1h con un régimen bajista generalizado. No se cumplen los requisitos estrictos de los Pilares Long (P1-P4) debido a la tendencia macro y falta de confirmación simultánea en osciladores. Tampoco hay posiciones abiertas en este ciclo para ajustes dinámicos de SL/TP, por lo que el bot mantiene una postura defensiva en observación (HOLD).

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `GRAMUSDT` | 1.157 | 1.137764 | `+1.69%` | `60.0` / `55.76` | `47.38` | `0.594` | `BULLISH_ENGULFING` | 1.1079098 | `WATCH` | HOLD |
| `BTCUSDT` | 69248.3 | 74197.630996 | `-6.67%` | `43.19` / `40.23` | `33.95` | `0.329` | `BEARISH_SHOOTING_STAR` | 67447.8442 | `WATCH` | **HOLD** (75%) |
| `PAXGUSDT` | 3875.7 | 4001.920602 | `-3.15%` | `14.97` / `24.86` | `33.34` | `0.214` | `BULLISH_HAMMER` | 3774.9318 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 1960.21 | 2119.101854 | `-7.50%` | `48.62` / `42.81` | `40.81` | `0.397` | `BEARISH_SHOOTING_STAR` | 1894.032918 | `WATCH` | HOLD |
| `TIAUSDT` | 0.4133 | 0.428289 | `-3.50%` | `38.69` / `39.13` | `45.28` | `0.262` | `NONE` | 0.3942882 | `WATCH` | HOLD |
| `SOLUSDT` | 80.72 | 85.890327 | `-6.02%` | `69.4` / `62.75` | `48.0` | `0.541` | `BEARISH_SHOOTING_STAR` | 78.135008 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0771 | 0.077985 | `-1.14%` | `10.04` / `11.66` | `35.8` | `0.091` | `BULLISH_HAMMER` | 0.0735534 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 965.62 | 1102.40908 | `-12.41%` | `85.08` / `80.69` | `54.08` | `0.807` | `NONE` | 921.20148 | `EXIT_LONG_STOCH_80` | HOLD |
| `DODOUSDT` | 0.02953 | 0.023632 | `+24.96%` | `73.45` / `65.11` | `69.72` | `0.994` | `BEARISH_SHOOTING_STAR` | 0.02817162 | `WATCH` | HOLD |
| `BNBUSDT` | 640.73 | 679.649859 | `-5.73%` | `48.14` / `43.64` | `40.9` | `0.414` | `BEARISH_SHOOTING_STAR` | 623.35394 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0203 | 1.10831 | `-7.94%` | `53.27` / `58.37` | `41.76` | `0.342` | `BULLISH_HAMMER` | 0.9937722 | `WATCH` | HOLD |
| `NEARUSDT` | 3.533 | 3.636238 | `-2.84%` | `86.96` / `83.4` | `56.95` | `0.84` | `MORNING_STAR` | 3.370482 | `EXIT_LONG_STOCH_80` | HOLD |
| `PEPEUSDT` | 4.53e-06 | 5e-06 | `-6.54%` | `33.33` / `33.77` | `49.24` | `0.574` | `NONE` | 4.32e-06 | `WATCH` | HOLD |
| `UNIUSDT` | 5.815 | 6.636162 | `-12.37%` | `37.43` / `35.04` | `37.57` | `0.338` | `BEARISH_SHOOTING_STAR` | 5.556497 | `WATCH` | HOLD |
| `HYPEUSDT` | 74.06 | 75.314114 | `-1.67%` | `93.25` / `83.58` | `64.21` | `1.013` | `BEARISH_SHOOTING_STAR` | 70.65324 | `EXIT_LONG_STOCH_80` | HOLD |
| `XAUTUSDT` | 3876.53 | 3997.698077 | `-3.03%` | `19.79` / `29.56` | `35.51` | `0.276` | `BULLISH_HAMMER` | 3775.74022 | `EXIT_SHORT_STOCH_20` | HOLD |
