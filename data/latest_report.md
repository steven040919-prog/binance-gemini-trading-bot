# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T01:20:52Z`
- **Ciclo de ejecucion:** `#89`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado opera mayoritariamente bajo la EMA 200 en temporalidad 1h con sesgo bajista (Regimen BEARISH). No se cumplen los requisitos estrictos de los Pilares LONG (P1-P4) debido a que no hay divergencias de volumen o capitulaciones extremas coincidentes con zonas de soporte validas. Tampoco se activan entradas SHORT bajo el Pilar S1 (Falta de testeo optimo en la resistencia EMA 200 con estocastico en sobrecompra). El portfolio se mantiene en HOLD/WATCH sin posiciones abiertas.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1023.0 | 1220.404023 | `-16.18%` | `19.21` / `22.29` | `30.74` | `0.202` | `BEARISH_ENGULFING` | 975.942 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.051 | 1.163443 | `-9.66%` | `39.32` / `41.95` | `35.44` | `0.245` | `BULLISH_HAMMER` | 1.0199924 | `WATCH` | HOLD |
| `UNIUSDT` | 6.709 | 7.015981 | `-4.38%` | `14.94` / `13.35` | `40.23` | `0.289` | `BEARISH_SHOOTING_STAR` | 6.400386 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 123.75 | 129.748682 | `-4.62%` | `52.73` / `53.43` | `37.38` | `0.34` | `BULLISH_ENGULFING` | 119.429 | `WATCH` | HOLD |
| `QNTUSDT` | 181.17 | 194.270599 | `-6.74%` | `41.43` / `40.63` | `33.37` | `0.298` | `BEARISH_ENGULFING` | 173.224242 | `WATCH` | HOLD |
| `XAUTUSDT` | 4024.36 | 4035.616613 | `-0.28%` | `31.5` / `28.41` | `34.8` | `0.334` | `NONE` | 3919.72664 | `WATCH` | HOLD |
| `BTCUSDT` | 73508.02 | 75895.059565 | `-3.15%` | `41.89` / `45.34` | `41.59` | `0.311` | `BEARISH_ENGULFING` | 71596.81148 | `WATCH` | **HOLD** (75%) |
| `CYBERUSDT` | 0.272 | 0.283231 | `-3.97%` | `14.8` / `21.74` | `45.3` | `0.33` | `BEARISH_SHOOTING_STAR` | 0.259488 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRXUSDT` | 0.3181 | 0.318984 | `-0.28%` | `15.56` / `14.81` | `47.69` | `0.325` | `BULLISH_ENGULFING` | 0.3098294 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2047.83 | 2197.96798 | `-6.83%` | `43.05` / `42.67` | `38.03` | `0.336` | `BULLISH_HAMMER` | 1989.935986 | `WATCH` | HOLD |
| `INITUSDT` | 0.25878 | 0.165012 | `+56.82%` | `51.22` / `55.24` | `54.39` | `0.508` | `BEARISH_ENGULFING` | 0.24687612 | `WATCH` | HOLD |
| `PAXGUSDT` | 4026.98 | 4041.770161 | `-0.37%` | `31.18` / `27.95` | `34.84` | `0.331` | `BEARISH_ENGULFING` | 3922.27852 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001877 | 0.001543 | `+21.65%` | `59.26` / `52.46` | `61.34` | `0.705` | `NONE` | 0.00179066 | `WATCH` | HOLD |
| `SOLUSDT` | 83.06 | 89.325346 | `-7.01%` | `45.57` / `42.89` | `37.7` | `0.336` | `BULLISH_HAMMER` | 80.417216 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.41e-06 | 5e-06 | `+7.04%` | `56.21` / `48.37` | `58.95` | `0.803` | `BEARISH_SHOOTING_STAR` | 5.16e-06 | `WATCH` | HOLD |
| `BNBUSDT` | 679.32 | 693.719514 | `-2.08%` | `46.28` / `43.94` | `43.69` | `0.384` | `NONE` | 661.65768 | `WATCH` | HOLD |
