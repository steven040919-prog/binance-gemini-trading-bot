# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T15:06:50Z`
- **Ciclo de ejecucion:** `#130`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general muestra una tendencia macro bajista con la mayoria de los activos cotizando por debajo de la EMA 200 de 1H. Se identifica un setup de entrada SHORT en NEARUSDT bajo el Pilar S1 (Rechazo Bajista en Resistencia EMA 200 con vela Envolvente Bajista y Estocastico en zona alta). Los demas activos permanecen en observacion o fuera de parametros de entrada sin posiciones abiertas que requieran ajuste dinamico de SL/TP.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.95e-06 | 5e-06 | `-2.30%` | `6.82` / `8.29` | `33.05` | `0.143` | `NONE` | 4.72e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.429 | 6.957354 | `-7.59%` | `24.77` / `26.23` | `34.08` | `0.218` | `BEARISH_ENGULFING` | 6.2338442 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001566 | 0.001556 | `+0.63%` | `10.27` / `7.4` | `40.66` | `0.247` | `NONE` | 0.00149396 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 972.4 | 1190.819367 | `-18.34%` | `22.56` / `25.31` | `33.74` | `0.176` | `BEARISH_ENGULFING` | 927.6696 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1594 | 0.165805 | `-3.86%` | `23.56` / `25.57` | `41.9` | `0.3` | `NONE` | 0.15405424 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3166 | 0.31747 | `-0.27%` | `17.82` / `19.18` | `32.22` | `-0.176` | `NONE` | 0.3083684 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73600.0 | 75634.036149 | `-2.69%` | `46.22` / `57.64` | `44.29` | `0.218` | `NONE` | 71686.4 | `WATCH` | **HOLD** (60%) |
| `QNTUSDT` | 176.24 | 192.722281 | `-8.55%` | `8.0` / `11.81` | `31.05` | `0.048` | `NONE` | 171.65776 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 4005.38 | 4035.43613 | `-0.74%` | `10.78` / `21.82` | `28.69` | `-0.056` | `BULLISH_HAMMER` | 3901.24012 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2054.71 | 2180.513134 | `-5.77%` | `40.7` / `41.51` | `43.58` | `0.353` | `BULLISH_HAMMER` | 2001.28754 | `WATCH` | **HOLD** (60%) |
| `SOLUSDT` | 83.86 | 88.55266 | `-5.30%` | `75.44` / `82.88` | `49.78` | `0.721` | `NONE` | 81.67964 | `EXIT_LONG_STOCH_80` | **HOLD** (65%) |
| `GRAMUSDT` | 1.207 | 1.115503 | `+8.20%` | `73.45` / `79.51` | `62.42` | `0.779` | `NONE` | 1.151478 | `WATCH` | **HOLD** (55%) |
| `XRPUSDT` | 1.0581 | 1.149859 | `-7.98%` | `56.63` / `57.49` | `44.87` | `0.514` | `BEARISH_ENGULFING` | 1.0305894 | `WATCH` | HOLD |
| `NEARUSDT` | 3.726 | 3.767675 | `-1.11%` | `74.25` / `80.37` | `56.46` | `0.755` | `BEARISH_ENGULFING` | 3.897396 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `RLUSDUSDT` | 1.001 | 1.001192 | `-0.02%` | `42.86` / `31.75` | `46.81` | `0.349` | `NONE` | 0.974974 | `WATCH` | HOLD |
| `MUBUSDT` | 794.77 | 750.414841 | `+5.91%` | `94.4` / `92.34` | `76.62` | `0.968` | `NONE` | 758.21058 | `EXIT_LONG_STOCH_80` | HOLD |
