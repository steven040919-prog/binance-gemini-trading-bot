# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T11:41:14Z`
- **Ciclo de ejecucion:** `#316`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global de 1h se encuentra mayoritariamente bajo la EMA 200 en un régimen BEARISH consolidado. Los candidatos evaluados muestran configuraciones mixtas pero sin la confluencia institucional estricta requerida por los Pilares LONG (P1-P4) ni el Pilar SHORT en Futuros USDT-M (S1), dado que no se cumplen simultáneamente los umbrales requeridos de retroceso/sobreventa extrema con patrones de velas confirmados o rechazos limpios en la EMA 200 con estocásticos en sobrecompra. Por lo tanto, el bot adopta una postura defensiva de espera (HOLD), sin posiciones abiertas que requieran ajustes dinámicos de SL/TP en este ciclo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `NBISBUSDT` | 126.42 | 138.390929 | `-8.65%` | `21.44` / `19.05` | `36.54` | `0.32` | `BULLISH_ENGULFING` | 120.927968 | `EXIT_SHORT_STOCH_20` | HOLD |
| `GRAMUSDT` | 1.153 | 1.138631 | `+1.26%` | `57.33` / `50.95` | `45.7` | `0.483` | `BULLISH_ENGULFING` | 1.1053324 | `WATCH` | HOLD |
| `BTCUSDT` | 69305.23 | 74273.318565 | `-6.69%` | `41.4` / `35.5` | `34.42` | `0.32` | `NONE` | 67183.528078 | `WATCH` | **HOLD** (75%) |
| `TIAUSDT` | 0.4187 | 0.428773 | `-2.35%` | `41.92` / `39.33` | `48.77` | `0.386` | `MORNING_STAR` | 0.3994398 | `WATCH` | HOLD |
| `ETHUSDT` | 1961.18 | 2121.456242 | `-7.56%` | `44.09` / `37.24` | `41.19` | `0.388` | `NONE` | 1884.299444 | `WATCH` | HOLD |
| `SOLUSDT` | 80.63 | 86.032664 | `-6.28%` | `63.33` / `55.46` | `47.14` | `0.513` | `NONE` | 77.767132 | `WATCH` | HOLD |
| `ZECUSDT` | 960.21 | 1107.911914 | `-13.33%` | `82.62` / `76.61` | `52.26` | `0.738` | `NONE` | 916.04034 | `EXIT_LONG_STOCH_80` | HOLD |
| `ERAUSDT` | 0.0771 | 0.078014 | `-1.17%` | `5.82` / `18.2` | `35.47` | `0.092` | `BEARISH_SHOOTING_STAR` | 0.0735534 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 639.54 | 680.332972 | `-6.00%` | `45.34` / `37.3` | `39.07` | `0.371` | `BEARISH_SHOOTING_STAR` | 617.268028 | `WATCH` | HOLD |
| `DODOUSDT` | 0.02933 | 0.023571 | `+24.43%` | `68.84` / `54.69` | `68.75` | `0.993` | `BEARISH_SHOOTING_STAR` | 0.02798082 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0216 | 1.109806 | `-7.95%` | `58.1` / `61.59` | `42.65` | `0.372` | `BEARISH_ENGULFING` | 0.99422048 | `WATCH` | HOLD |
| `NEARUSDT` | 3.552 | 3.640856 | `-2.44%` | `83.61` / `81.6` | `59.39` | `0.953` | `MORNING_STAR` | 3.388608 | `EXIT_LONG_STOCH_80` | HOLD |
| `UNIUSDT` | 5.825 | 6.648406 | `-12.39%` | `34.91` / `34.29` | `38.54` | `0.337` | `NONE` | 5.55705 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.5e-06 | 5e-06 | `-7.23%` | `30.86` / `38.84` | `45.38` | `0.489` | `BEARISH_SHOOTING_STAR` | 4.29e-06 | `WATCH` | HOLD |
| `DOGEUSDT` | 0.06527 | 0.069432 | `-5.99%` | `56.1` / `49.41` | `46.93` | `0.488` | `NONE` | 0.06294657 | `WATCH` | HOLD |
| `HYPEUSDT` | 73.7 | 75.401346 | `-2.26%` | `84.18` / `70.7` | `62.4` | `1.02` | `NONE` | 70.3098 | `EXIT_LONG_STOCH_80` | HOLD |
