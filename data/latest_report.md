# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T12:19:17Z`
- **Ciclo de ejecucion:** `#320`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen predominantemente bajista con la mayoría de los activos cotizando por debajo de sus respectivas EMA 200. No se cumplen las condiciones exactas de los pilares LONG (P1-P4) debido a que no hay pullbacks limpios sobre soporte con sobreventa extrema combinada en estocástico y RSI, y tampoco se activan operaciones SHORT bajo el pilar S1 ya que ningún activo en tendencia bajista está testeando actualmente la resistencia de la EMA 200 con sobrecompra en el estocástico. El portafolio actual se mantiene sin posiciones abiertas.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `GRAMUSDT` | 1.155 | 1.137744 | `+1.52%` | `58.33` / `55.21` | `46.57` | `0.568` | `BULLISH_ENGULFING` | 1.108198 | `WATCH` | HOLD |
| `BTCUSDT` | 69421.43 | 74199.353682 | `-6.44%` | `44.64` / `40.72` | `36.1` | `0.36` | `BULLISH_ENGULFING` | 67616.47282 | `WATCH` | **HOLD** (75%) |
| `ETHUSDT` | 1961.52 | 2119.114889 | `-7.44%` | `48.97` / `42.93` | `41.41` | `0.405` | `NONE` | 1894.39352 | `WATCH` | HOLD |
| `TIAUSDT` | 0.412 | 0.428276 | `-3.80%` | `37.74` / `38.81` | `44.48` | `0.235` | `NONE` | 0.393048 | `WATCH` | HOLD |
| `SOLUSDT` | 80.73 | 85.890426 | `-6.01%` | `69.49` / `62.78` | `48.1` | `0.543` | `BEARISH_SHOOTING_STAR` | 78.150918 | `WATCH` | HOLD |
| `NBISBUSDT` | 127.18 | 138.139055 | `-7.93%` | `35.22` / `26.13` | `38.99` | `0.417` | `MORNING_STAR` | 121.382652 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0761 | 0.077975 | `-2.41%` | `5.46` / `10.13` | `34.27` | `0.018` | `NONE` | 0.0725994 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 967.22 | 1102.425001 | `-12.26%` | `85.64` / `80.88` | `54.57` | `0.827` | `NONE` | 922.72788 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 640.01 | 679.642694 | `-5.83%` | `47.48` / `43.42` | `39.89` | `0.399` | `BEARISH_SHOOTING_STAR` | 623.36974 | `WATCH` | HOLD |
| `DODOUSDT` | 0.02922 | 0.023629 | `+23.66%` | `70.85` / `64.24` | `68.32` | `0.92` | `BEARISH_SHOOTING_STAR` | 0.02787588 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0248 | 1.108355 | `-7.54%` | `56.5` / `59.45` | `45.37` | `0.453` | `BULLISH_HAMMER` | 0.9943544 | `WATCH` | HOLD |
| `UNIUSDT` | 5.804 | 6.636053 | `-12.54%` | `36.64` / `34.77` | `36.86` | `0.319` | `BEARISH_SHOOTING_STAR` | 5.5592168 | `WATCH` | HOLD |
| `NEARUSDT` | 3.53 | 3.636208 | `-2.92%` | `86.63` / `83.29` | `56.59` | `0.831` | `MORNING_STAR` | 3.36762 | `EXIT_LONG_STOCH_80` | HOLD |
| `PEPEUSDT` | 4.53e-06 | 5e-06 | `-6.54%` | `33.33` / `33.77` | `49.24` | `0.574` | `MORNING_STAR` | 4.32e-06 | `WATCH` | HOLD |
| `HYPEUSDT` | 74.02 | 75.313716 | `-1.72%` | `92.95` / `83.48` | `64.01` | `1.005` | `BEARISH_SHOOTING_STAR` | 70.61508 | `EXIT_LONG_STOCH_80` | HOLD |
| `DOGEUSDT` | 0.06544 | 0.069322 | `-5.60%` | `62.33` / `56.1` | `48.86` | `0.534` | `NONE` | 0.06323253 | `WATCH` | HOLD |
