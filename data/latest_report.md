# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T16:45:46Z`
- **Ciclo de ejecucion:** `#303`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de criptomonedas opera predominantemente bajo un régimen bajista (BEARISH) en temporalidad de 1H, con la gran mayoría de los activos cotizando por debajo de la EMA 200 y experimentando presiones vendedoras en las últimas 24 horas. Los Pilares LONG (P1 a P4) no muestran activaciones óptimas debido a la falta de giros alcistas confirmados en el Estocástico simultáneos con los patrones de vela requeridos o se encuentran en zonas neutrales sin la confluencia de volumen y sobreventa extrema. De manera similar, aunque hay activos testeando resistencias o zonas de la EMA 200, no se cumplen todos los criterios estrictos del Pilar SHORT (S1) o de los scalpers M15 de manera simultánea. No hay posiciones abiertas reportadas en el portafolio actual requiriendo ajustes (ADJUST). Se mantiene la postura de observación (WATCH) a la espera de que el precio alcance soportes institucionales o active divergencias y capitulaciones claras (Pilar 2 / Pilar 3).

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68666.9 | 73971.564133 | `-7.17%` | `39.45` / `42.05` | `31.65` | `0.283` | `BULLISH_HAMMER` | 66523.6613 | `WATCH` | **HOLD** (75%) |
| `ETHUSDT` | 1926.52 | 2112.21688 | `-8.79%` | `36.82` / `44.46` | `32.2` | `0.247` | `NONE` | 1858.442744 | `WATCH` | HOLD |
| `BNBUSDT` | 630.95 | 677.998181 | `-6.94%` | `38.57` / `46.17` | `33.46` | `0.247` | `NONE` | 613.42101 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.128 | 1.137852 | `-0.87%` | `28.33` / `33.37` | `38.29` | `0.075` | `BULLISH_HAMMER` | 1.076112 | `WATCH` | HOLD |
| `MUBUSDT` | 758.21 | 763.330958 | `-0.67%` | `8.94` / `10.99` | `31.73` | `-0.093` | `BULLISH_HAMMER` | 726.83728 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INITUSDT` | 0.1131 | 0.150394 | `-24.80%` | `21.28` / `24.37` | `39.98` | `0.153` | `BULLISH_ENGULFING` | 0.1078974 | `WATCH` | HOLD |
| `BARDUSDT` | 0.1517 | 0.108432 | `+39.90%` | `68.87` / `72.92` | `59.12` | `0.633` | `NONE` | 0.1447218 | `WATCH` | HOLD |
| `SOLUSDT` | 79.41 | 85.685862 | `-7.32%` | `48.73` / `61.76` | `38.7` | `0.278` | `NONE` | 76.69652 | `WATCH` | HOLD |
| `SOXSBUSDT` | 53.5 | 55.618103 | `-3.81%` | `91.08` / `87.25` | `72.27` | `1.108` | `NONE` | 51.039 | `EXIT_LONG_STOCH_80` | HOLD |
| `ZECUSDT` | 951.13 | 1095.30597 | `-13.16%` | `64.4` / `70.66` | `48.46` | `0.567` | `BULLISH_HAMMER` | 907.37802 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0757 | 0.077881 | `-2.80%` | `14.87` / `19.4` | `35.56` | `0.083` | `BULLISH_HAMMER` | 0.0722178 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0132 | 1.10583 | `-8.38%` | `54.62` / `63.69` | `39.44` | `0.202` | `BEARISH_ENGULFING` | 0.98134096 | `WATCH` | HOLD |
| `NEARUSDT` | 3.497 | 3.63112 | `-3.69%` | `68.54` / `75.94` | `51.12` | `0.613` | `NONE` | 3.336138 | `WATCH` | HOLD |
| `INJUSDT` | 8.13 | 7.794221 | `+4.31%` | `90.18` / `91.15` | `71.27` | `0.903` | `BULLISH_ENGULFING` | 7.75602 | `EXIT_LONG_STOCH_80` | HOLD |
| `UNIUSDT` | 5.792 | 6.60376 | `-12.29%` | `48.99` / `54.5` | `39.48` | `0.337` | `NONE` | 5.525568 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.43e-06 | 5e-06 | `-8.54%` | `23.67` / `35.46` | `38.7` | `-0.119` | `BULLISH_HAMMER` | 4.23e-06 | `WATCH` | HOLD |
