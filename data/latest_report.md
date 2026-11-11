# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T15:53:37Z`
- **Ciclo de ejecucion:** `#133`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general muestra una clara dominancia bajista con la mayoría de activos cotizando por debajo de la EMA 200. Se detecta un setup claro de venta corta en NEARUSDT bajo el Pilar S1 (Rechazo en Resistencia EMA 200 con envolvente bajista y sobrecompra en el oscilador estocástico). No existen posiciones abiertas actualmente para realizar ajustes dinámicos de SL/TP.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 983.37 | 1190.928522 | `-17.43%` | `27.26` / `26.88` | `37.19` | `0.265` | `BEARISH_ENGULFING` | 938.13498 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.95e-06 | 5e-06 | `-2.30%` | `7.89` / `8.65` | `33.05` | `0.143` | `BEARISH_SHOOTING_STAR` | 4.72e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001568 | 0.001556 | `+0.76%` | `10.42` / `7.45` | `40.81` | `0.25` | `NONE` | 0.00149587 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73999.86 | 75638.014856 | `-2.17%` | `53.63` / `60.11` | `51.48` | `0.831` | `NONE` | 72075.86364 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3168 | 0.317472 | `-0.21%` | `21.53` / `20.42` | `34.33` | `-0.087` | `NONE` | 0.3085632 | `WATCH` | HOLD |
| `XAUTUSDT` | 3993.31 | 4035.31603 | `-1.04%` | `9.34` / `21.34` | `25.09` | `-0.202` | `NONE` | 3889.48394 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2075.35 | 2180.718508 | `-4.83%` | `51.17` / `45.0` | `54.13` | `1.117` | `BULLISH_HAMMER` | 2013.26975 | `WATCH` | HOLD |
| `MUBUSDT` | 816.23 | 750.628373 | `+8.74%` | `95.39` / `92.67` | `81.55` | `1.146` | `NONE` | 778.68342 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 84.72 | 88.561217 | `-4.34%` | `80.47` / `84.55` | `57.16` | `1.073` | `NONE` | 81.9656 | `EXIT_LONG_STOCH_80` | HOLD |
| `NEARUSDT` | 3.749 | 3.767904 | `-0.50%` | `77.37` / `81.41` | `58.2` | `0.829` | `BEARISH_ENGULFING` | 3.921454 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `XRPUSDT` | 1.0714 | 1.149992 | `-6.83%` | `63.83` / `59.89` | `55.37` | `1.297` | `BEARISH_ENGULFING` | 1.03191484 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.195 | 1.115383 | `+7.14%` | `70.53` / `78.54` | `59.4` | `0.706` | `BULLISH_HAMMER` | 1.14003 | `WATCH` | HOLD |
| `UNIUSDT` | 6.508 | 6.95814 | `-6.47%` | `30.86` / `28.26` | `41.32` | `0.367` | `BEARISH_ENGULFING` | 6.208632 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.001 | 1.001192 | `-0.02%` | `42.86` / `31.75` | `46.81` | `0.349` | `NONE` | 0.974974 | `WATCH` | HOLD |
| `INTCBUSDT` | 63.03 | 58.738632 | `+7.31%` | `87.03` / `85.52` | `75.37` | `0.992` | `BULLISH_ENGULFING` | 60.13062 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 684.52 | 692.275752 | `-1.12%` | `66.32` / `63.22` | `55.5` | `0.997` | `BEARISH_ENGULFING` | 666.72248 | `WATCH` | HOLD |
