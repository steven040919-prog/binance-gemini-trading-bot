# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T15:27:53Z`
- **Ciclo de ejecucion:** `#340`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un regimen general bajista con la mayoria de los activos cotizando por debajo de la EMA 200 en temporalidad 1H. Se evalua con exito el Pilar S1 (SHORT_ENTRY) para ZECUSDT debido al rechazo bajista en la zona de resistencia de la EMA 200 confluente con sobrecompra en el estocastico y patron de velas bajista. No hay posiciones abiertas actuales, por lo que no se requieren ajustes dinamicos de SL/TP, priorizando la operativa corta en Futuros USDT-M sobre los activos seleccionados en tendencia bajista macro.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68548.03 | 74017.006561 | `-7.39%` | `39.56` / `42.81` | `30.97` | `0.243` | `BEARISH_ENGULFING` | 66765.78122 | `WATCH` | HOLD |
| `ETHUSDT` | 1924.86 | 2113.233548 | `-8.91%` | `42.52` / `48.81` | `31.99` | `0.218` | `BEARISH_ENGULFING` | 1869.638948 | `WATCH` | HOLD |
| `BNBUSDT` | 632.15 | 678.130392 | `-6.78%` | `45.67` / `49.92` | `34.46` | `0.257` | `BEARISH_ENGULFING` | 615.7141 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.119 | 1.137121 | `-1.59%` | `22.84` / `39.71` | `35.59` | `-0.166` | `NONE` | 1.0761778 | `WATCH` | HOLD |
| `INTCBUSDT` | 57.42 | 59.276406 | `-3.13%` | `11.63` / `22.61` | `27.47` | `-0.312` | `BEARISH_ENGULFING` | 55.366624 | `EXIT_SHORT_STOCH_20` | HOLD |
| `MUBUSDT` | 761.55 | 762.730661 | `-0.15%` | `8.83` / `17.37` | `32.99` | `-0.172` | `BEARISH_ENGULFING` | 733.91733 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PAXGUSDT` | 3871.19 | 3997.387321 | `-3.16%` | `20.9` / `17.96` | `35.66` | `0.147` | `BULLISH_ENGULFING` | 3770.53906 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 79.52 | 85.687597 | `-7.20%` | `60.46` / `68.89` | `39.59` | `0.291` | `NONE` | 77.175728 | `WATCH` | HOLD |
| `ZECUSDT` | 940.0 | 1095.322975 | `-14.18%` | `66.55` / `76.47` | `44.64` | `0.414` | `BEARISH_ENGULFING` | 983.24 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `ERAUSDT` | 0.0751 | 0.077848 | `-3.53%` | `17.59` / `19.76` | `34.17` | `-0.032` | `NONE` | 0.0716454 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DODOUSDT` | 0.02776 | 0.023786 | `+16.71%` | `49.66` / `61.75` | `54.21` | `0.447` | `NONE` | 0.02648304 | `WATCH` | HOLD |
| `NEARUSDT` | 3.472 | 3.628939 | `-4.32%` | `72.64` / `81.57` | `48.83` | `0.551` | `NONE` | 3.312288 | `EXIT_LONG_STOCH_80` | HOLD |
| `XRPUSDT` | 1.02 | 1.106264 | `-7.80%` | `68.0` / `65.28` | `43.33` | `0.346` | `BEARISH_ENGULFING` | 0.988368 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.47e-06 | 5e-06 | `-7.69%` | `34.57` / `39.92` | `42.66` | `0.07` | `BEARISH_ENGULFING` | 4.26e-06 | `WATCH` | HOLD |
| `SOXSBUSDT` | 53.49 | 55.725563 | `-4.01%` | `89.17` / `79.36` | `72.25` | `1.272` | `NONE` | 51.02946 | `EXIT_LONG_STOCH_80` | HOLD |
| `INJUSDT` | 8.057 | 7.782077 | `+3.53%` | `87.38` / `90.5` | `68.25` | `0.925` | `NONE` | 7.686378 | `EXIT_LONG_STOCH_80` | HOLD |
