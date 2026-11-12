# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T08:51:08Z`
- **Ciclo de ejecucion:** `#218`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen bajista generalizado en temporalidad de 1H, con la gran mayoría de los activos cotizando por debajo de la EMA 200 y con pendientes negativas pronunciadas. Se evalúan los pilares de operación, destacando que INJUSDT cumple con los requisitos del Pilar de Scalper M15 para posicionamiento SHORT (M15_SCALPER_PULLBACK_SHORT). No hay posiciones abiertas actualmente para realizar ajustes dinámicos de SL/TP, por lo que la operativa se concentra en gestión de nuevas entradas bajistas de alta probabilidad bajo el Pilar S1 y derivados intradía.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 73567.03 | 75412.563896 | `-2.45%` | `11.76` / `11.92` | `42.37` | `0.21` | `BULLISH_ENGULFING` | 71654.28722 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PEPEUSDT` | 4.49e-06 | 5e-06 | `-10.04%` | `8.34` / `8.59` | `26.28` | `0.225` | `BEARISH_SHOOTING_STAR` | 4.28e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2050.81 | 2163.107233 | `-5.19%` | `23.96` / `20.06` | `43.59` | `0.277` | `BULLISH_ENGULFING` | 1997.48894 | `WATCH` | HOLD |
| `NEARUSDT` | 3.473 | 3.74136 | `-7.17%` | `4.55` / `4.3` | `31.81` | `0.088` | `BEARISH_SHOOTING_STAR` | 3.3540316 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 83.01 | 87.760098 | `-5.41%` | `22.69` / `20.65` | `42.13` | `0.236` | `BULLISH_ENGULFING` | 80.85174 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0451 | 1.135118 | `-7.93%` | `18.93` / `13.64` | `40.44` | `0.23` | `BULLISH_HAMMER` | 1.0179274 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.15 | 6.874477 | `-10.54%` | `8.42` / `12.05` | `31.88` | `0.203` | `BULLISH_HAMMER` | 5.90689 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1415 | 0.158807 | `-10.90%` | `3.09` / `3.46` | `24.34` | `0.145` | `BEARISH_SHOOTING_STAR` | 0.1366135 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.425 | 7.900896 | `-6.02%` | `9.55` / `9.49` | `31.55` | `0.193` | `BEARISH_SHOOTING_STAR` | 7.732965 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (85%) |
| `BNBUSDT` | 672.98 | 691.200689 | `-2.64%` | `13.21` / `9.51` | `35.43` | `0.089` | `BULLISH_ENGULFING` | 655.48252 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1484 | 0.16388 | `-9.45%` | `3.64` / `4.58` | `27.07` | `0.158` | `NONE` | 0.1436964 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 164.07 | 189.236354 | `-13.30%` | `8.92` / `9.7` | `30.28` | `0.195` | `BULLISH_ENGULFING` | 156.52278 | `EXIT_SHORT_STOCH_20` | HOLD |
| `HYPEUSDT` | 71.28 | 76.768945 | `-7.15%` | `20.58` / `21.76` | `39.36` | `0.16` | `BULLISH_ENGULFING` | 69.348864 | `WATCH` | HOLD |
| `XAUTUSDT` | 3933.33 | 4025.523399 | `-2.29%` | `9.36` / `14.41` | `20.68` | `-0.136` | `NONE` | 3831.06342 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06709 | 0.070719 | `-5.13%` | `22.24` / `20.25` | `38.75` | `0.234` | `BULLISH_ENGULFING` | 0.06534554 | `WATCH` | HOLD |
| `AAVEUSDT` | 117.18 | 127.985645 | `-8.44%` | `8.86` / `6.98` | `27.51` | `0.154` | `NONE` | 113.547372 | `EXIT_SHORT_STOCH_20` | HOLD |
