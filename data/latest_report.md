# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T17:32:31Z`
- **Ciclo de ejecucion:** `#353`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un régimen bajista generalizado en temporalidad de 1H con la mayoría de los activos operando por debajo de la EMA 200. Se evalúan los pilares de la estrategia detectando una oportunidad institucional de tipo SHORT en SOXSBUSDT bajo el Pilar S1 (Rechazo bajista en resistencia de la EMA 200, con RSI en 66.35, Estocástico en 81.64 girando a la baja, BB %B en 0.941 y patrón BEARISH_SHOOTING_STAR). No se registran posiciones abiertas previas para gestión dinámica, por lo que el enfoque se limita a la ejecución del short validado.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68725.4 | 73926.720618 | `-7.04%` | `41.22` / `41.34` | `32.39` | `0.315` | `BULLISH_HAMMER` | 66728.492 | `WATCH` | HOLD |
| `ETHUSDT` | 1932.35 | 2110.328998 | `-8.43%` | `35.08` / `39.26` | `34.8` | `0.308` | `NONE` | 1867.94242 | `WATCH` | HOLD |
| `BNBUSDT` | 632.16 | 677.521489 | `-6.70%` | `34.24` / `40.1` | `35.39` | `0.3` | `NONE` | 615.541072 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0759 | 0.077938 | `-2.62%` | `12.62` / `15.66` | `36.58` | `0.154` | `BEARISH_SHOOTING_STAR` | 0.0724086 | `EXIT_SHORT_STOCH_20` | HOLD |
| `GRAMUSDT` | 1.13 | 1.137551 | `-0.66%` | `29.17` / `28.73` | `39.37` | `0.167` | `BEARISH_SHOOTING_STAR` | 1.07802 | `WATCH` | HOLD |
| `XAUTUSDT` | 3874.22 | 3991.362145 | `-2.93%` | `17.39` / `19.89` | `40.09` | `0.248` | `NONE` | 3773.49028 | `EXIT_SHORT_STOCH_20` | HOLD |
| `MUBUSDT` | 763.02 | 763.303975 | `-0.04%` | `15.78` / `11.97` | `35.33` | `0.056` | `BULLISH_HAMMER` | 727.92108 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 110.71 | 122.938687 | `-9.95%` | `30.33` / `47.98` | `38.84` | `0.268` | `BULLISH_HAMMER` | 106.586558 | `WATCH` | HOLD |
| `PAXGUSDT` | 3875.8 | 3995.283638 | `-2.99%` | `17.72` / `19.22` | `39.84` | `0.258` | `NONE` | 3775.0292 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BARDUSDT` | 0.1503 | 0.108806 | `+38.14%` | `57.36` / `66.57` | `58.13` | `0.594` | `NONE` | 0.1433862 | `WATCH` | HOLD |
| `SOLUSDT` | 80.01 | 85.617987 | `-6.55%` | `43.57` / `52.69` | `43.75` | `0.437` | `BULLISH_ENGULFING` | 76.951754 | `WATCH` | HOLD |
| `ZECUSDT` | 948.41 | 1093.679721 | `-13.28%` | `59.9` / `64.02` | `47.5` | `0.53` | `BULLISH_HAMMER` | 904.78314 | `WATCH` | HOLD |
| `NEARUSDT` | 3.516 | 3.626904 | `-3.06%` | `65.33` / `70.11` | `53.17` | `0.654` | `BULLISH_ENGULFING` | 3.354264 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0231 | 1.10483 | `-7.40%` | `47.7` / `57.76` | `46.44` | `0.464` | `BULLISH_ENGULFING` | 0.9833225 | `WATCH` | HOLD |
| `SOXSBUSDT` | 52.32 | 55.59373 | `-5.89%` | `81.64` / `86.33` | `66.35` | `0.941` | `BEARISH_SHOOTING_STAR` | 54.72672 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `PEPEUSDT` | 4.48e-06 | 5e-06 | `-7.44%` | `23.61` / `29.37` | `45.1` | `0.221` | `NONE` | 4.27e-06 | `WATCH` | HOLD |
