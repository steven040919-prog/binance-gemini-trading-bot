# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T14:35:28Z`
- **Ciclo de ejecucion:** `#128`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se mantiene en un régimen bajista predominante con la mayoría de los activos cotizando por debajo de la EMA 200. No se han detectado señales de entrada bajo los pilares P1-P4 (LONG) ni S1 (SHORT) debido a que los patrones de velas alcistas actuales no cumplen con la confluencia estricta de sobreventa extrema y giro del estocástico requerida por la arquitectura institucional. Se mantiene una postura de observación (WATCH) para evitar falsas rupturas en un entorno de baja volatilidad y volumen insuficiente.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 976.14 | 1193.372174 | `-18.20%` | `25.54` / `26.08` | `34.4` | `0.17` | `BULLISH_ENGULFING` | 931.23756 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.95e-06 | 5e-06 | `-2.25%` | `7.91` / `9.11` | `32.49` | `0.097` | `BULLISH_ENGULFING` | 4.72e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.438 | 6.961979 | `-7.53%` | `25.79` / `26.41` | `34.59` | `0.207` | `BULLISH_ENGULFING` | 6.201546 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001533 | 0.001555 | `-1.43%` | `3.93` / `3.78` | `36.74` | `0.17` | `NONE` | 0.00146248 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.874 | 7.949449 | `-0.95%` | `8.55` / `8.73` | `41.67` | `0.181` | `BEARISH_SHOOTING_STAR` | 7.511796 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRXUSDT` | 0.3168 | 0.317644 | `-0.27%` | `17.08` / `16.17` | `34.33` | `-0.235` | `BULLISH_HAMMER` | 0.3085632 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73406.82 | 75654.567117 | `-2.97%` | `50.47` / `66.74` | `41.32` | `0.001` | `NONE` | 71498.24268 | `WATCH` | **HOLD** (0%) |
| `QNTUSDT` | 176.14 | 193.070694 | `-8.77%` | `10.6` / `15.16` | `30.88` | `-0.027` | `NONE` | 171.56036 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 4012.62 | 4035.788471 | `-0.57%` | `19.47` / `32.8` | `31.21` | `-0.022` | `NONE` | 3908.29188 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2045.53 | 2181.741757 | `-6.24%` | `30.08` / `39.81` | `39.79` | `0.073` | `BULLISH_ENGULFING` | 1992.34622 | `WATCH` | HOLD |
| `SOLUSDT` | 83.87 | 88.608434 | `-5.35%` | `80.9` / `86.05` | `50.0` | `0.762` | `BULLISH_ENGULFING` | 81.68938 | `EXIT_LONG_STOCH_80` | HOLD |
| `GRAMUSDT` | 1.209 | 1.114558 | `+8.47%` | `84.11` / `81.11` | `63.27` | `0.814` | `BULLISH_HAMMER` | 1.153386 | `EXIT_LONG_STOCH_80` | HOLD |
| `XRPUSDT` | 1.0534 | 1.15085 | `-8.47%` | `50.65` / `57.01` | `41.33` | `0.152` | `BULLISH_ENGULFING` | 1.0260116 | `WATCH` | HOLD |
| `NEARUSDT` | 3.733 | 3.769554 | `-0.97%` | `79.35` / `81.54` | `57.21` | `0.803` | `BULLISH_ENGULFING` | 3.5649334 | `EXIT_LONG_STOCH_80` | HOLD |
| `MUBUSDT` | 767.75 | 749.723787 | `+2.40%` | `84.18` / `88.29` | `62.3` | `0.701` | `NONE` | 747.7885 | `EXIT_LONG_STOCH_80` | HOLD |
| `RLUSDUSDT` | 1.001 | 1.001194 | `-0.02%` | `33.33` / `19.05` | `46.81` | `0.349` | `MORNING_STAR` | 0.974974 | `EXIT_SHORT_STOCH_20` | HOLD |
