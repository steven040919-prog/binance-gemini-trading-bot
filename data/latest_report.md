# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T06:55:07Z`
- **Ciclo de ejecucion:** `#206`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un regimen claramente bajista con la totalidad de los activos evaluados cotizando por debajo de sus respectivas EMA 200 y con pendientes negativas. No se activan nuevos Pilares LONG (P1-P4) debido a que los estocasticos no presentan giros al alza confirmados y la tendencia macro es bajista. Tampoco se activa el Pilar SHORT (S1) ya que los precios actuales se encuentran muy alejados de la resistencia de la EMA 200 en la mayoria de los pares (distancias superiores al -2%), sin testeo activo de la resistencia. Dado que la cartera actual no posee posiciones abiertas (open_positions_count = 0), el sistema se mantiene en modo HOLD / observacion esperando configuraciones optimas.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.46e-06 | 5e-06 | `-10.80%` | `8.84` / `12.28` | `21.41` | `0.117` | `BULLISH_HAMMER` | 4.27e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73473.79 | 75442.78586 | `-2.61%` | `10.79` / `19.49` | `40.03` | `0.104` | `NONE` | 71563.47146 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `ETHUSDT` | 2042.2 | 2165.507428 | `-5.69%` | `15.59` / `21.72` | `38.55` | `0.111` | `BEARISH_SHOOTING_STAR` | 1989.1028 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.128 | 6.87928 | `-10.92%` | `16.09` / `20.2` | `30.25` | `0.1` | `BEARISH_ENGULFING` | 5.9088736 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 82.59 | 87.879995 | `-6.02%` | `18.21` / `24.59` | `37.38` | `0.066` | `NONE` | 80.44266 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.5 | 3.745252 | `-6.55%` | `3.64` / `6.9` | `34.24` | `0.063` | `NONE` | 3.3827 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0392 | 1.137014 | `-8.60%` | `6.57` / `11.81` | `34.82` | `0.022` | `BEARISH_SHOOTING_STAR` | 1.0121808 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.427 | 7.911088 | `-6.12%` | `10.36` / `15.03` | `30.55` | `0.123` | `NONE` | 7.109055 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1421 | 0.159201 | `-10.74%` | `4.27` / `7.43` | `25.61` | `0.094` | `NONE` | 0.13718228 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 672.6 | 691.414587 | `-2.72%` | `1.89` / `7.45` | `33.32` | `-0.044` | `NONE` | 655.1124 | `EXIT_SHORT_STOCH_20` | HOLD |
| `HYPEUSDT` | 71.01 | 76.86689 | `-7.62%` | `23.77` / `33.16` | `35.76` | `0.013` | `NONE` | 69.16374 | `WATCH` | HOLD |
| `QNTUSDT` | 163.3 | 189.730135 | `-13.93%` | `9.22` / `11.74` | `24.6` | `0.098` | `BEARISH_ENGULFING` | 156.4047 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1494 | 0.164198 | `-9.01%` | `5.26` / `6.79` | `28.88` | `0.136` | `BEARISH_SHOOTING_STAR` | 0.1445686 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06667 | 0.070791 | `-5.82%` | `17.87` / `24.52` | `32.57` | `0.04` | `NONE` | 0.06493658 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3959.61 | 4027.283686 | `-1.68%` | `15.5` / `17.37` | `27.69` | `0.142` | `BULLISH_HAMMER` | 3856.66014 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LINKUSDT` | 10.028 | 10.713127 | `-6.40%` | `6.64` / `12.3` | `29.62` | `0.091` | `BEARISH_SHOOTING_STAR` | 9.767272 | `EXIT_SHORT_STOCH_20` | HOLD |
