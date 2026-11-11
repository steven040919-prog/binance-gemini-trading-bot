# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T23:57:02Z`
- **Ciclo de ejecucion:** `#166`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado mantiene un sesgo general bajista con la mayoría de los activos cotizando por debajo de la EMA 200 en temporalidad de 1 hora. No se activan nuevos pilares de entrada LONG (P1-P4) ni cortos en S1 debido a la falta de confluencia completa en los osciladores y patrones de velas exigidos por el motor cuantitativo. La cartera permanece en estado de observación (HOLD) con gestión de liquidez en USD.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.54e-06 | 5e-06 | `-9.94%` | `3.72` / `3.46` | `17.58` | `-0.004` | `NONE` | 4.33e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 971.07 | 1174.306573 | `-17.31%` | `33.03` / `44.8` | `36.42` | `0.134` | `BEARISH_SHOOTING_STAR` | 926.40078 | `WATCH` | HOLD |
| `UNIUSDT` | 6.253 | 6.922995 | `-9.68%` | `19.86` / `38.3` | `28.73` | `-0.094` | `NONE` | 5.9993956 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.602 | 3.759823 | `-4.20%` | `27.87` / `40.46` | `42.39` | `0.177` | `BULLISH_HAMMER` | 3.436308 | `WATCH` | HOLD |
| `INJUSDT` | 7.526 | 7.950083 | `-5.33%` | `9.55` / `11.79` | `28.98` | `-0.102` | `NONE` | 7.179804 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1521 | 0.165211 | `-7.94%` | `7.92` / `10.83` | `28.56` | `-0.19` | `NONE` | 0.14569818 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1461 | 0.160354 | `-8.89%` | `11.4` / `11.92` | `31.93` | `-0.117` | `BULLISH_HAMMER` | 0.1393794 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3975.13 | 4031.170055 | `-1.39%` | `5.91` / `5.34` | `21.31` | `0.163` | `BEARISH_SHOOTING_STAR` | 3871.77662 | `EXIT_SHORT_STOCH_20` | HOLD |
| `OPGUSDT` | 0.1349 | 0.125787 | `+7.24%` | `12.35` / `22.24` | `47.73` | `0.396` | `BEARISH_SHOOTING_STAR` | 0.1286946 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74095.95 | 75556.795478 | `-1.93%` | `52.91` / `66.21` | `49.96` | `0.539` | `BULLISH_HAMMER` | 72169.4553 | `WATCH` | **HOLD** (50%) |
| `PAXGUSDT` | 3977.66 | 4036.763162 | `-1.46%` | `5.31` / `4.84` | `21.08` | `0.166` | `BEARISH_SHOOTING_STAR` | 3874.24084 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2060.89 | 2173.502067 | `-5.18%` | `34.42` / `44.28` | `45.52` | `0.362` | `BULLISH_HAMMER` | 2001.207048 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001474 | 0.001552 | `-5.05%` | `6.62` / `6.56` | `33.1` | `0.197` | `BULLISH_HAMMER` | 0.0014062 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SNXXBUSDT` | 4.2 | 4.195512 | `+0.11%` | `52.64` / `64.55` | `54.04` | `0.509` | `BEARISH_ENGULFING` | 4.0068 | `WATCH` | HOLD |
| `MUBUSDT` | 794.11 | 755.703424 | `+5.08%` | `58.87` / `69.85` | `57.25` | `0.549` | `BEARISH_ENGULFING` | 757.58094 | `WATCH` | HOLD |
| `SOLUSDT` | 83.46 | 88.242383 | `-5.42%` | `37.63` / `52.75` | `42.94` | `0.318` | `BULLISH_HAMMER` | 80.403956 | `WATCH` | HOLD |
