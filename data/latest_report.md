# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T12:38:04Z`
- **Ciclo de ejecucion:** `#322`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un régimen bajista generalizado, cotizando mayoritariamente por debajo de la EMA 200 en temporalidad de 1H. Los activos evaluados muestran señales mixtas de rebote técnico pero sin la confluencia institucional completa requerida por los pilares LONG (P1-P4). No se registran posiciones abiertas para aplicar gestión dinámica, por lo que el sistema permanece en modo de observación (WATCH) manteniendo la disciplina de riesgo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `GRAMUSDT` | 1.156 | 1.137754 | `+1.60%` | `59.17` / `55.49` | `46.98` | `0.581` | `BULLISH_ENGULFING` | 1.1079384 | `WATCH` | **HOLD** (50%) |
| `BTCUSDT` | 69235.02 | 74197.498856 | `-6.69%` | `43.07` / `40.19` | `33.84` | `0.327` | `BEARISH_SHOOTING_STAR` | 67434.90948 | `WATCH` | HOLD |
| `TIAUSDT` | 0.4129 | 0.428285 | `-3.59%` | `38.4` / `39.03` | `45.03` | `0.253` | `NONE` | 0.3939066 | `WATCH` | HOLD |
| `ETHUSDT` | 1958.06 | 2119.080461 | `-7.60%` | `48.05` / `42.62` | `39.98` | `0.384` | `BEARISH_SHOOTING_STAR` | 1894.084948 | `WATCH` | HOLD |
| `SOLUSDT` | 80.71 | 85.890227 | `-6.03%` | `69.32` / `62.72` | `47.9` | `0.539` | `BEARISH_SHOOTING_STAR` | 78.135244 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0764 | 0.077978 | `-2.02%` | `7.36` / `10.77` | `34.71` | `0.039` | `NONE` | 0.0728856 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DODOUSDT` | 0.02922 | 0.023629 | `+23.66%` | `70.85` / `64.24` | `68.32` | `0.92` | `BEARISH_SHOOTING_STAR` | 0.02787588 | `WATCH` | HOLD |
| `ZECUSDT` | 969.54 | 1102.448085 | `-12.06%` | `86.44` / `81.15` | `55.26` | `0.856` | `NONE` | 924.94116 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 640.44 | 679.646973 | `-5.77%` | `47.88` / `43.56` | `40.5` | `0.408` | `BEARISH_SHOOTING_STAR` | 623.36032 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0204 | 1.108311 | `-7.93%` | `53.34` / `58.39` | `41.83` | `0.344` | `BULLISH_HAMMER` | 0.99383896 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.57e-06 | 5e-06 | `-5.72%` | `38.27` / `35.42` | `53.61` | `0.74` | `MORNING_STAR` | 4.36e-06 | `WATCH` | HOLD |
| `NEARUSDT` | 3.545 | 3.636357 | `-2.51%` | `88.27` / `83.84` | `58.41` | `0.876` | `MORNING_STAR` | 3.38193 | `EXIT_LONG_STOCH_80` | HOLD |
| `HYPEUSDT` | 74.3 | 75.316502 | `-1.35%` | `95.01` / `84.17` | `65.37` | `1.058` | `NONE` | 70.8822 | `EXIT_LONG_STOCH_80` | HOLD |
| `UNIUSDT` | 5.816 | 6.636172 | `-12.36%` | `37.5` / `35.06` | `37.64` | `0.34` | `BEARISH_SHOOTING_STAR` | 5.557624 | `WATCH` | HOLD |
| `XAUTUSDT` | 3880.88 | 3997.74136 | `-2.92%` | `23.25` / `30.71` | `37.21` | `0.361` | `BULLISH_HAMMER` | 3779.97712 | `WATCH` | HOLD |
| `DOGEUSDT` | 0.06542 | 0.069322 | `-5.63%` | `62.15` / `56.04` | `48.63` | `0.529` | `BEARISH_SHOOTING_STAR` | 0.06321992 | `WATCH` | HOLD |
