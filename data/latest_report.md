# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T00:22:40Z`
- **Ciclo de ejecucion:** `#278`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen claramente bajista con la mayoría de los activos cotizando por debajo de sus respectivas EMA 200 en temporalidad 1H. Tras evaluar los pilares institucionales, destaca ERAUSDT activando el Pilar 1 LONG (P1_EMA200_PULLBACK) al estar sobre la EMA 200 con pendiente positiva, RSI en zona de valor, estocástico girando al alza y patrón de envolvente alcista. El resto de activos presentan configuraciones bajistas o setups de salida/espera, sin activaciones adicionales de compra o venta en corto en este ciclo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71363.85 | 74937.920034 | `-4.77%` | `10.4` / `10.15` | `24.6` | `0.217` | `BULLISH_HAMMER` | 69508.3899 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NBISBUSDT` | 130.69 | 140.515003 | `-6.99%` | `24.61` / `23.6` | `37.25` | `0.352` | `BULLISH_ENGULFING` | 124.67826 | `WATCH` | HOLD |
| `NEARUSDT` | 3.415 | 3.684501 | `-7.31%` | `42.45` / `39.82` | `38.44` | `0.355` | `NONE` | 3.277867 | `WATCH` | HOLD |
| `BNBUSDT` | 657.23 | 685.990454 | `-4.19%` | `26.41` / `21.76` | `34.57` | `0.371` | `BULLISH_ENGULFING` | 640.14202 | `WATCH` | HOLD |
| `INITUSDT` | 0.11778 | 0.158504 | `-25.69%` | `31.75` / `25.49` | `39.76` | `0.346` | `BULLISH_ENGULFING` | 0.11236212 | `WATCH` | HOLD |
| `XAUTUSDT` | 3883.57 | 4007.990053 | `-3.10%` | `29.97` / `26.75` | `33.11` | `0.352` | `NONE` | 3782.59718 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.141 | 1.138103 | `+0.25%` | `12.4` / `12.6` | `38.0` | `0.187` | `BEARISH_SHOOTING_STAR` | 1.088514 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ERAUSDT` | 0.0815 | 0.077754 | `+4.82%` | `4.1` / `2.74` | `39.75` | `0.172` | `BULLISH_ENGULFING` | 0.077751 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `SOXSBUSDT` | 43.94 | 56.309858 | `-21.97%` | `13.94` / `20.89` | `35.36` | `0.102` | `BULLISH_HAMMER` | 41.91876 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PAXGUSDT` | 3886.38 | 4012.393116 | `-3.14%` | `30.74` / `26.92` | `33.01` | `0.353` | `BULLISH_HAMMER` | 3785.33412 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001523 | 0.001554 | `-1.97%` | `2.4` / `5.17` | `43.2` | `0.266` | `BEARISH_SHOOTING_STAR` | 0.00145294 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRXUSDT` | 0.3157 | 0.317814 | `-0.67%` | `19.74` / `16.11` | `36.78` | `0.273` | `NONE` | 0.3074918 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2016.42 | 2143.50653 | `-5.93%` | `49.14` / `47.88` | `38.33` | `0.36` | `BULLISH_ENGULFING` | 1963.99308 | `WATCH` | HOLD |
| `ZECUSDT` | 956.88 | 1130.757963 | `-15.38%` | `34.61` / `29.58` | `42.71` | `0.36` | `MORNING_STAR` | 912.86352 | `WATCH` | HOLD |
| `SOLUSDT` | 81.62 | 86.87649 | `-6.05%` | `39.71` / `35.17` | `39.65` | `0.346` | `NONE` | 79.49788 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0392 | 1.120576 | `-7.26%` | `58.49` / `53.16` | `47.55` | `0.567` | `MORNING_STAR` | 1.01209248 | `WATCH` | HOLD |
