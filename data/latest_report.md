# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T15:47:03Z`
- **Ciclo de ejecucion:** `#342`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se mantiene bajo una fuerte presión bajista con la mayoría de los activos cotizando por debajo de la EMA 200. Se observa una capitulación generalizada con patrones de velas bajistas (BEARISH_ENGULFING) en BTC, ETH, BNB y XRP. No se cumplen las condiciones de entrada para los pilares LONG (P1-P4) debido a la falta de giros alcistas confirmados en el estocástico y la tendencia macro bajista. El pilar SHORT (S1) no se activa actualmente ya que los precios están alejados de la EMA 200 (distancia > 0.5%). Se recomienda mantener una postura de vigilancia (WATCH) y esperar a que los activos se acerquen a la EMA 200 para evaluar posibles rechazos bajistas en Futuros.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68320.02 | 74014.737804 | `-7.69%` | `37.33` / `42.06` | `29.54` | `0.199` | `BEARISH_ENGULFING` | 66449.655516 | `WATCH` | **HOLD** (0%) |
| `ETHUSDT` | 1922.61 | 2113.211159 | `-9.02%` | `41.88` / `48.6` | `31.51` | `0.204` | `BEARISH_ENGULFING` | 1855.859788 | `WATCH` | **HOLD** (0%) |
| `BNBUSDT` | 630.07 | 678.109696 | `-7.08%` | `43.5` / `49.19` | `33.03` | `0.21` | `BEARISH_ENGULFING` | 612.686222 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.121 | 1.137141 | `-1.42%` | `25.11` / `40.47` | `36.11` | `-0.131` | `NONE` | 1.0732134 | `WATCH` | HOLD |
| `XAUTUSDT` | 3869.1 | 3993.475667 | `-3.11%` | `22.6` / `21.74` | `36.05` | `0.131` | `BULLISH_ENGULFING` | 3768.5034 | `WATCH` | HOLD |
| `INTCBUSDT` | 57.58 | 59.277998 | `-2.86%` | `13.84` / `23.34` | `28.04` | `-0.296` | `BEARISH_ENGULFING` | 55.138344 | `EXIT_SHORT_STOCH_20` | HOLD |
| `MUBUSDT` | 760.16 | 762.71683 | `-0.34%` | `9.71` / `17.66` | `32.5` | `-0.188` | `BEARISH_ENGULFING` | 730.112848 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PAXGUSDT` | 3870.0 | 3997.37548 | `-3.19%` | `20.72` / `17.9` | `35.25` | `0.127` | `BULLISH_ENGULFING` | 3769.38 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 79.47 | 85.6871 | `-7.26%` | `60.09` / `68.77` | `39.3` | `0.28` | `NONE` | 76.583582 | `WATCH` | HOLD |
| `ZECUSDT` | 933.28 | 1095.25611 | `-14.79%` | `64.56` / `75.8` | `42.68` | `0.326` | `BEARISH_ENGULFING` | 890.34912 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0752 | 0.077849 | `-3.40%` | `20.48` / `20.72` | `34.33` | `-0.025` | `NONE` | 0.0717408 | `WATCH` | HOLD |
| `SOXSBUSDT` | 53.83 | 55.728946 | `-3.41%` | `88.89` / `79.27` | `72.87` | `1.29` | `NONE` | 51.35382 | `EXIT_LONG_STOCH_80` | HOLD |
| `XRPUSDT` | 1.0152 | 1.106216 | `-8.23%` | `64.54` / `64.13` | `40.72` | `0.235` | `BEARISH_ENGULFING` | 0.9804744 | `WATCH` | HOLD |
| `NEARUSDT` | 3.481 | 3.629028 | `-4.08%` | `73.44` / `81.84` | `49.67` | `0.578` | `NONE` | 3.320874 | `EXIT_LONG_STOCH_80` | HOLD |
| `PEPEUSDT` | 4.49e-06 | 5e-06 | `-7.28%` | `37.04` / `40.74` | `44.63` | `0.196` | `BEARISH_ENGULFING` | 4.28e-06 | `WATCH` | HOLD |
| `INJUSDT` | 8.042 | 7.781928 | `+3.34%` | `86.95` / `90.36` | `67.42` | `0.915` | `NONE` | 7.672068 | `EXIT_LONG_STOCH_80` | HOLD |
