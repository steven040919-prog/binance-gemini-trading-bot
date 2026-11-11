# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T01:07:36Z`
- **Ciclo de ejecucion:** `#83`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global de criptomonedas se mantiene bajo presión bajista en temporalidad 1h, con la mayoría de los activos cotizando por debajo de la EMA 200 y con un régimen de tendencia primaria BEARISH. Tras evaluar los 4 pilares LONG (P1-P4) y el Pilar SHORT (S1) en Futuros USDT-M, no se cumplen las condiciones de confluencia extrema requeridas (como rechazos exactos en resistencia EMA 200 con estocástico >= 80 o capitulaciones profundas con volumen institucional). Las posiciones abiertas están vacías y los activos candidatos permanecen en zona de vigilancia (WATCH). Se mantiene la disciplina de riesgo y la arquitectura de gestión dinámica para proteger el capital.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1030.47 | 1220.478352 | `-15.57%` | `20.42` / `22.69` | `31.85` | `0.23` | `BEARISH_ENGULFING` | 983.06838 | `WATCH` | HOLD |
| `XRPUSDT` | 1.051 | 1.163443 | `-9.66%` | `39.32` / `41.95` | `35.44` | `0.245` | `BULLISH_HAMMER` | 1.0201924 | `WATCH` | HOLD |
| `UNIUSDT` | 6.691 | 7.015802 | `-4.63%` | `13.84` / `12.98` | `38.81` | `0.263` | `BEARISH_SHOOTING_STAR` | 6.383214 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 181.13 | 194.270201 | `-6.76%` | `41.32` / `40.59` | `33.29` | `0.296` | `BEARISH_ENGULFING` | 173.225738 | `WATCH` | HOLD |
| `AAVEUSDT` | 123.99 | 129.75107 | `-4.44%` | `54.12` / `53.89` | `38.5` | `0.385` | `BULLISH_ENGULFING` | 119.44631 | `WATCH` | HOLD |
| `XAUTUSDT` | 4026.02 | 4035.633131 | `-0.24%` | `32.33` / `28.69` | `35.6` | `0.347` | `NONE` | 3921.34348 | `WATCH` | HOLD |
| `BTCUSDT` | 73451.58 | 75894.497973 | `-3.22%` | `41.0` / `45.04` | `40.92` | `0.287` | `BEARISH_ENGULFING` | 71541.83892 | `WATCH` | **HOLD** (75%) |
| `TRXUSDT` | 0.318 | 0.318983 | `-0.31%` | `14.44` / `14.44` | `46.17` | `0.29` | `BULLISH_ENGULFING` | 0.309732 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2045.68 | 2197.946587 | `-6.93%` | `42.35` / `42.44` | `37.41` | `0.32` | `NONE` | 1989.991456 | `WATCH` | HOLD |
| `INITUSDT` | 0.25514 | 0.164976 | `+54.65%` | `50.36` / `54.95` | `53.43` | `0.485` | `BEARISH_ENGULFING` | 0.24340356 | `WATCH` | HOLD |
| `PAXGUSDT` | 4029.97 | 4041.799912 | `-0.29%` | `32.77` / `28.48` | `36.88` | `0.354` | `BEARISH_ENGULFING` | 3925.19078 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001893 | 0.001543 | `+22.68%` | `61.68` / `53.26` | `62.31` | `0.743` | `BULLISH_ENGULFING` | 0.00180592 | `WATCH` | HOLD |
| `SOLUSDT` | 83.06 | 89.325346 | `-7.01%` | `45.57` / `42.89` | `37.7` | `0.336` | `NONE` | 80.433828 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.39e-06 | 5e-06 | `+6.65%` | `54.9` / `47.93` | `57.66` | `0.744` | `BEARISH_SHOOTING_STAR` | 5.14e-06 | `WATCH` | HOLD |
| `BNBUSDT` | 679.45 | 693.720808 | `-2.06%` | `46.49` / `44.01` | `43.9` | `0.389` | `BULLISH_HAMMER` | 661.7843 | `WATCH` | HOLD |
| `NEARUSDT` | 3.614 | 3.774423 | `-4.25%` | `47.39` / `41.5` | `51.68` | `0.573` | `MORNING_STAR` | 3.447756 | `WATCH` | HOLD |
