# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T21:36:13Z`
- **Ciclo de ejecucion:** `#157`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado opera mayoritariamente bajo la EMA 200 en temporalidad de 1H con sesgo bajista (Regimen BEARISH). No se cumplen de forma estricta los requisitos de los Pilares LONG (P1-P4) ni del Pilar SHORT (S1) en los candidatos evaluados actualmente, ya que falta confluencia simultanea de volumen institucional o divergencias validas en resistencia. Las posiciones abiertas estan vacias, por lo que se prioriza la conservacion de capital manteniendo el estado de espera (HOLD).

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.68e-06 | 5e-06 | `-7.35%` | `3.5` / `3.57` | `21.62` | `0.047` | `NONE` | 4.46e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001491 | 0.001553 | `-4.02%` | `4.55` / `3.96` | `34.64` | `0.235` | `NONE` | 0.00142241 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.834 | 7.949025 | `-1.45%` | `14.3` / `20.66` | `40.39` | `0.215` | `NONE` | 7.557478 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74662.01 | 75584.65662 | `-1.22%` | `84.84` / `81.31` | `60.44` | `0.958` | `BULLISH_ENGULFING` | 72720.79774 | `EXIT_LONG_STOCH_80` | **HOLD** (75%) |
| `XAUTUSDT` | 3978.78 | 4032.419591 | `-1.33%` | `3.04` / `2.52` | `21.07` | `0.123` | `NONE` | 3875.33172 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1502 | 0.160557 | `-6.45%` | `17.52` / `24.24` | `42.07` | `0.027` | `NONE` | 0.14451376 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1572 | 0.165472 | `-5.00%` | `16.48` / `21.86` | `37.83` | `0.126` | `BEARISH_ENGULFING` | 0.1523984 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PAXGUSDT` | 3981.32 | 4037.929188 | `-1.40%` | `3.23` / `2.38` | `21.19` | `0.125` | `NONE` | 3877.80568 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 996.43 | 1177.789927 | `-15.40%` | `60.02` / `59.57` | `42.53` | `0.494` | `NONE` | 950.59422 | `WATCH` | HOLD |
| `ETHUSDT` | 2081.11 | 2175.809318 | `-4.35%` | `60.91` / `63.52` | `54.81` | `0.801` | `BULLISH_HAMMER` | 2027.00114 | `WATCH` | HOLD |
| `MUBUSDT` | 816.55 | 754.574877 | `+8.21%` | `82.58` / `87.25` | `71.96` | `0.791` | `NONE` | 784.43012 | `M15_SCALPER_PULLBACK_LONG` | HOLD |
| `SOXSBUSDT` | 45.21 | 59.501232 | `-24.02%` | `36.33` / `25.96` | `37.98` | `0.341` | `NONE` | 43.13034 | `WATCH` | HOLD |
| `SNXXBUSDT` | 4.48 | 4.183966 | `+7.08%` | `78.85` / `84.54` | `67.53` | `0.756` | `NONE` | 4.27392 | `M15_SCALPER_PULLBACK_LONG` | HOLD |
| `SOLUSDT` | 84.85 | 88.337725 | `-3.95%` | `71.96` / `75.05` | `55.67` | `0.75` | `BULLISH_ENGULFING` | 82.6439 | `WATCH` | HOLD |
| `NEARUSDT` | 3.7 | 3.766242 | `-1.76%` | `58.47` / `62.04` | `51.69` | `0.509` | `BEARISH_ENGULFING` | 3.54592 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0655 | 1.144899 | `-6.94%` | `41.46` / `40.51` | `50.59` | `0.708` | `BULLISH_ENGULFING` | 1.0346686 | `WATCH` | HOLD |
