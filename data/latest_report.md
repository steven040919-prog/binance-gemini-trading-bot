# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T08:29:04Z`
- **Ciclo de ejecucion:** `#120`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un régimen claramente bajista con la gran mayoría de los activos cotizando por debajo de la EMA 200 en temporalidad de 1H. No se cumplen los requisitos estrictos de los Pilares Long (P1 a P4) al faltar una confluencia alcista robusta en los osciladores o giros válidos del estocástico desde sobreventa. Tampoco se activan operaciones en corto (Pilar S1) debido a que los precios no se encuentran testeando la resistencia dinámica de la EMA 200 con las condiciones de sobrecompra requeridas en este momento exacto. Por lo tanto, el sistema se mantiene en modo HOLD protegiendo el capital disponible.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 977.8 | 1207.459653 | `-19.02%` | `17.97` / `17.58` | `29.55` | `0.179` | `BEARISH_ENGULFING` | 932.8212 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.399 | 6.983527 | `-8.37%` | `9.85` / `12.33` | `26.59` | `0.006` | `BULLISH_HAMMER` | 6.158434 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PEPEUSDT` | 5.18e-06 | 5e-06 | `+2.22%` | `14.58` / `28.52` | `42.41` | `0.114` | `NONE` | 4.94e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001571 | 0.001555 | `+1.02%` | `5.83` / `16.35` | `39.02` | `-0.122` | `NONE` | 0.00149873 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1591 | 0.166051 | `-4.19%` | `21.23` / `32.9` | `38.35` | `0.297` | `BULLISH_HAMMER` | 0.1523088 | `WATCH` | HOLD |
| `QNTUSDT` | 178.01 | 193.770116 | `-8.13%` | `26.89` / `36.59` | `31.86` | `-0.015` | `BULLISH_HAMMER` | 172.786556 | `WATCH` | HOLD |
| `BTCUSDT` | 73840.52 | 75765.799818 | `-2.54%` | `76.27` / `76.27` | `48.11` | `0.637` | `BULLISH_ENGULFING` | 71920.66648 | `WATCH` | **HOLD** (75%) |
| `TRXUSDT` | 0.3175 | 0.31848 | `-0.31%` | `25.64` / `24.42` | `40.71` | `0.27` | `BEARISH_SHOOTING_STAR` | 0.309245 | `WATCH` | HOLD |
| `CYBERUSDT` | 0.267 | 0.282305 | `-5.42%` | `5.07` / `4.46` | `43.37` | `0.223` | `NONE` | 0.254718 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2059.19 | 2189.33995 | `-5.94%` | `74.03` / `78.96` | `44.73` | `0.59` | `BULLISH_ENGULFING` | 2005.65106 | `WATCH` | HOLD |
| `SOLUSDT` | 83.05 | 88.893195 | `-6.57%` | `47.75` / `51.91` | `42.88` | `0.473` | `BULLISH_ENGULFING` | 80.82832 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0564 | 1.156277 | `-8.64%` | `40.87` / `48.57` | `42.5` | `0.457` | `NONE` | 1.0289336 | `WATCH` | HOLD |
| `INITUSDT` | 0.24036 | 0.171259 | `+40.35%` | `17.16` / `28.65` | `48.05` | `0.2` | `NONE` | 0.22930344 | `EXIT_SHORT_STOCH_20` | HOLD |
| `RLUSDUSDT` | 1.0011 | 1.001203 | `-0.01%` | `45.71` / `56.19` | `47.73` | `0.519` | `NONE` | 0.9750714 | `WATCH` | HOLD |
| `BNBUSDT` | 681.05 | 693.044022 | `-1.73%` | `65.49` / `66.07` | `48.15` | `0.6` | `BULLISH_ENGULFING` | 663.3427 | `WATCH` | HOLD |
| `NEARUSDT` | 3.606 | 3.771148 | `-4.38%` | `48.73` / `57.81` | `48.44` | `0.476` | `BULLISH_HAMMER` | 3.4529536 | `WATCH` | HOLD |
