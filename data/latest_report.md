# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T19:00:13Z`
- **Ciclo de ejecucion:** `#147`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado presenta un sesgo bajista predominante con la mayoría de los activos cotizando por debajo de la EMA 200. No se han detectado señales de entrada bajo los pilares P1-P4 (Long) ni S1 (Short) en los activos analizados. Los activos con patrones de velas (PEPE, INJ, MUB, SOXSB, SNXXB) se encuentran en zonas de sobrecompra o sobreventa extrema, pero no cumplen con la confluencia técnica requerida para una ejecución institucional. Se mantiene una postura de espera (HOLD) para preservar el capital ante la falta de setups de alta probabilidad.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.89e-06 | 5e-06 | `-3.32%` | `6.09` / `7.5` | `30.29` | `0.169` | `BEARISH_SHOOTING_STAR` | 4.67e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001503 | 0.001556 | `-3.39%` | `4.58` / `8.77` | `35.69` | `0.208` | `NONE` | 0.00143386 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74498.0 | 75603.265878 | `-1.46%` | `80.41` / `71.56` | `58.73` | `1.05` | `NONE` | 72561.052 | `EXIT_LONG_STOCH_80` | **HOLD** (0%) |
| `XAUTUSDT` | 3982.16 | 4033.940508 | `-1.28%` | `1.74` / `3.45` | `21.99` | `-0.029` | `NONE` | 3878.62384 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1589 | 0.165669 | `-4.09%` | `34.06` / `35.24` | `41.63` | `0.231` | `NONE` | 0.15370122 | `WATCH` | HOLD |
| `INJUSDT` | 7.965 | 7.949476 | `+0.20%` | `27.56` / `24.84` | `46.76` | `0.341` | `BEARISH_ENGULFING` | 7.65219 | `WATCH` | HOLD |
| `PAXGUSDT` | 3983.76 | 4039.591314 | `-1.38%` | `0.7` / `3.05` | `21.84` | `-0.038` | `NONE` | 3880.18224 | `EXIT_SHORT_STOCH_20` | HOLD |
| `MUBUSDT` | 825.55 | 752.772577 | `+9.67%` | `96.09` / `97.02` | `81.66` | `0.963` | `BULLISH_ENGULFING` | 788.41905 | `EXIT_LONG_STOCH_80` | HOLD |
| `ETHUSDT` | 2083.57 | 2177.988248 | `-4.34%` | `72.09` / `67.67` | `56.44` | `0.965` | `NONE` | 2029.39718 | `WATCH` | HOLD |
| `ZECUSDT` | 994.32 | 1184.065002 | `-16.02%` | `59.45` / `48.7` | `41.57` | `0.409` | `NONE` | 948.58128 | `WATCH` | HOLD |
| `SOXSBUSDT` | 42.64 | 59.957969 | `-28.88%` | `6.22` / `6.45` | `25.38` | `0.074` | `BULLISH_ENGULFING` | 40.67856 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SNXXBUSDT` | 4.59 | 4.174402 | `+9.96%` | `94.61` / `96.36` | `77.84` | `0.919` | `BEARISH_ENGULFING` | 4.37886 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 85.0 | 88.446823 | `-3.90%` | `81.7` / `81.33` | `57.93` | `0.899` | `NONE` | 82.783 | `EXIT_LONG_STOCH_80` | HOLD |
| `GRAMUSDT` | 1.228 | 1.119181 | `+9.72%` | `75.13` / `66.44` | `65.05` | `0.806` | `BULLISH_HAMMER` | 1.171512 | `WATCH` | HOLD |
| `NEARUSDT` | 3.722 | 3.767371 | `-1.20%` | `66.53` / `74.13` | `54.12` | `0.622` | `NONE` | 3.5653532 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0634 | 1.147154 | `-7.30%` | `46.39` / `58.16` | `48.69` | `0.646` | `NONE` | 1.0357516 | `WATCH` | HOLD |
