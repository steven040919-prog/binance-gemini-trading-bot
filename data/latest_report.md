# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T00:06:45Z`
- **Ciclo de ejecucion:** `#277`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un régimen bajista generalizado con la mayoría de los activos cotizando por debajo de la EMA 200 en temporalidad 1H. Destaca ERAUSDT cumpliendo las condiciones del Pilar 1 LONG (PULLBACK DE VALOR SOBRE EMA 200) al mantener su tendencia macro alcista, situarse cerca de la EMA 200 con pendiente positiva, y mostrar un estocástico girando al alza con patrón de vela de giro envolvente alcista. El resto de candidatos se mantienen en vigilancia o sin activaciones de pilares válidos debido a la persistencia de la tendencia primaria bajista.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71470.01 | 74938.976352 | `-4.63%` | `11.89` / `10.64` | `25.96` | `0.243` | `BULLISH_HAMMER` | 69611.78974 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NBISBUSDT` | 131.12 | 140.519281 | `-6.69%` | `24.92` / `23.7` | `38.14` | `0.361` | `BULLISH_ENGULFING` | 125.08848 | `WATCH` | HOLD |
| `INITUSDT` | 0.1158 | 0.158484 | `-26.93%` | `29.21` / `24.64` | `37.95` | `0.292` | `NONE` | 0.1104732 | `WATCH` | HOLD |
| `BNBUSDT` | 658.08 | 685.998911 | `-4.07%` | `27.74` / `22.2` | `36.83` | `0.397` | `BULLISH_ENGULFING` | 640.96992 | `WATCH` | HOLD |
| `XAUTUSDT` | 3883.77 | 4007.992043 | `-3.10%` | `30.04` / `26.77` | `33.23` | `0.353` | `NONE` | 3782.79198 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0809 | 0.077748 | `+4.05%` | `3.18` / `2.43` | `38.47` | `0.152` | `BULLISH_ENGULFING` | 0.0771786 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `GRAMUSDT` | 1.136 | 1.138053 | `-0.18%` | `11.43` / `12.27` | `36.66` | `0.165` | `BEARISH_SHOOTING_STAR` | 1.083744 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOXSBUSDT` | 43.74 | 56.307868 | `-22.32%` | `13.02` / `20.59` | `34.64` | `0.079` | `NONE` | 41.72796 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AVAXUSDT` | 8.357 | 8.436898 | `-0.95%` | `29.9` / `24.38` | `42.7` | `0.351` | `MORNING_STAR` | 8.1261744 | `WATCH` | HOLD |
| `PAXGUSDT` | 3885.86 | 4012.387942 | `-3.15%` | `30.56` / `26.86` | `32.69` | `0.35` | `BULLISH_HAMMER` | 3784.82764 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001523 | 0.001554 | `-1.97%` | `2.4` / `5.17` | `43.2` | `0.266` | `NONE` | 0.00145294 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRXUSDT` | 0.3158 | 0.317815 | `-0.63%` | `22.12` / `16.9` | `38.25` | `0.313` | `NONE` | 0.3075892 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2018.88 | 2143.531007 | `-5.82%` | `50.45` / `48.32` | `39.79` | `0.398` | `BULLISH_ENGULFING` | 1966.38912 | `WATCH` | HOLD |
| `ZECUSDT` | 956.88 | 1130.757963 | `-15.38%` | `34.61` / `29.58` | `42.71` | `0.36` | `MORNING_STAR` | 912.86352 | `WATCH` | HOLD |
| `SOLUSDT` | 81.72 | 86.877485 | `-5.94%` | `40.98` / `35.59` | `40.81` | `0.381` | `BEARISH_SHOOTING_STAR` | 79.59528 | `WATCH` | HOLD |
| `NEARUSDT` | 3.424 | 3.684591 | `-7.07%` | `44.36` / `40.46` | `39.75` | `0.404` | `BEARISH_SHOOTING_STAR` | 3.2796496 | `WATCH` | HOLD |
