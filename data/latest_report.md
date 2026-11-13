# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T17:13:28Z`
- **Ciclo de ejecucion:** `#351`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un regimen predominantemente bajista, con la mayoria de los activos cotizando por debajo de la EMA 200 en temporalidad 1H. Aplicando la arquitectura institucional, se identifica una oportunidad SHORT clara en SOXSBUSDT bajo el Pilar S1 por rechazo en resistencia EMA 200 y sobrecompra estocastica con patron bajista. No hay posiciones abiertas actualmente para requerir ajuste dinamico.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68797.65 | 73927.439523 | `-6.94%` | `42.13` / `41.64` | `33.6` | `0.332` | `BULLISH_HAMMER` | 66740.80653 | `WATCH` | HOLD |
| `ETHUSDT` | 1931.73 | 2110.322829 | `-8.46%` | `34.86` / `39.19` | `34.49` | `0.303` | `NONE` | 1867.956556 | `WATCH` | HOLD |
| `BNBUSDT` | 632.03 | 677.520195 | `-6.71%` | `34.08` / `40.04` | `35.2` | `0.297` | `NONE` | 615.543776 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0753 | 0.077932 | `-3.38%` | `10.68` / `15.02` | `34.64` | `0.107` | `BEARISH_SHOOTING_STAR` | 0.0718362 | `EXIT_SHORT_STOCH_20` | HOLD |
| `GRAMUSDT` | 1.13 | 1.137551 | `-0.66%` | `29.17` / `28.73` | `39.37` | `0.167` | `BEARISH_SHOOTING_STAR` | 1.07802 | `WATCH` | HOLD |
| `UNIUSDT` | 5.753 | 6.593534 | `-12.75%` | `36.35` / `47.19` | `37.32` | `0.285` | `BULLISH_HAMMER` | 5.516139 | `WATCH` | HOLD |
| `MUBUSDT` | 761.24 | 763.286264 | `-0.27%` | `14.72` / `11.61` | `33.97` | `0.034` | `BULLISH_HAMMER` | 728.110552 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 110.53 | 122.936896 | `-10.09%` | `29.37` / `47.66` | `38.21` | `0.241` | `NONE` | 107.220418 | `WATCH` | HOLD |
| `SOLUSDT` | 79.74 | 85.6153 | `-6.86%` | `41.5` / `52.0` | `41.22` | `0.373` | `NONE` | 77.00624 | `WATCH` | HOLD |
| `ZECUSDT` | 943.67 | 1093.632556 | `-13.71%` | `58.5` / `63.55` | `45.6` | `0.466` | `NONE` | 900.26118 | `WATCH` | HOLD |
| `BARDUSDT` | 0.1506 | 0.108809 | `+38.41%` | `57.54` / `66.63` | `58.31` | `0.598` | `BULLISH_HAMMER` | 0.1436724 | `WATCH` | HOLD |
| `NEARUSDT` | 3.507 | 3.626814 | `-3.30%` | `64.53` / `69.84` | `52.21` | `0.628` | `BULLISH_HAMMER` | 3.345678 | `WATCH` | HOLD |
| `SOXSBUSDT` | 52.39 | 55.594426 | `-5.76%` | `81.87` / `86.4` | `66.69` | `0.946` | `BEARISH_SHOOTING_STAR` | 54.79994 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `XRPUSDT` | 1.0203 | 1.104802 | `-7.65%` | `45.5` / `57.03` | `44.36` | `0.394` | `NONE` | 0.98380062 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.43e-06 | 5e-06 | `-8.46%` | `16.67` / `27.06` | `38.7` | `-0.023` | `NONE` | 4.23e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 8.096 | 7.792382 | `+3.90%` | `87.44` / `89.7` | `69.05` | `0.837` | `BEARISH_ENGULFING` | 7.723584 | `EXIT_LONG_STOCH_80` | HOLD |
