# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T10:52:34Z`
- **Ciclo de ejecucion:** `#311`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de criptomonedas en 1H continúa bajo presión macro bajista con la mayoría de los activos cotizando por debajo de la EMA 200. Se evalúan oportunidades bajo los pilares institucionales. NEARUSDT activa el Pilar S1 (SHORT) por rechazo bajista en la resistencia de la EMA 200 con vela envolvente bajista y estocástico elevado. El resto del portafolio se mantiene en observación (WATCH) a la espera de confirmaciones de sobreventa extrema o pullbacks limpios.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.0771 | 0.078077 | `-1.25%` | `18.29` / `29.39` | `35.34` | `0.133` | `NONE` | 0.0735534 | `EXIT_SHORT_STOCH_20` | HOLD |
| `GRAMUSDT` | 1.143 | 1.137771 | `+0.46%` | `47.45` / `41.33` | `42.02` | `0.386` | `NONE` | 1.1037956 | `WATCH` | HOLD |
| `BTCUSDT` | 69385.0 | 74325.070039 | `-6.65%` | `36.41` / `31.12` | `35.32` | `0.314` | `MORNING_STAR` | 67059.205 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3124 | 0.317573 | `-1.63%` | `16.25` / `9.66` | `36.09` | `0.315` | `BULLISH_ENGULFING` | 0.3042776 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 110.78 | 123.994111 | `-10.66%` | `27.84` / `31.46` | `32.67` | `0.205` | `NONE` | 107.541876 | `WATCH` | HOLD |
| `ETHUSDT` | 1951.71 | 2123.388482 | `-8.09%` | `36.27` / `32.66` | `36.88` | `0.314` | `BULLISH_ENGULFING` | 1881.12896 | `WATCH` | HOLD |
| `TIAUSDT` | 0.4197 | 0.429101 | `-2.19%` | `36.05` / `37.88` | `49.59` | `0.416` | `BEARISH_SHOOTING_STAR` | 0.4003938 | `WATCH` | HOLD |
| `ZECUSDT` | 947.4 | 1111.063595 | `-14.73%` | `74.83` / `73.18` | `47.94` | `0.545` | `NONE` | 903.8196 | `WATCH` | HOLD |
| `SOLUSDT` | 80.41 | 86.096669 | `-6.60%` | `54.48` / `50.09` | `45.05` | `0.453` | `MORNING_STAR` | 77.656242 | `WATCH` | HOLD |
| `BNBUSDT` | 639.35 | 680.641287 | `-6.07%` | `37.5` / `30.69` | `38.83` | `0.351` | `MORNING_STAR` | 613.3243 | `WATCH` | HOLD |
| `NBISBUSDT` | 126.19 | 138.599264 | `-8.95%` | `17.31` / `19.01` | `35.82` | `0.276` | `BEARISH_SHOOTING_STAR` | 120.657158 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DODOUSDT` | 0.02911 | 0.023567 | `+23.52%` | `58.05` / `42.45` | `67.66` | `0.923` | `NONE` | 0.02777094 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0233 | 1.110599 | `-7.86%` | `62.65` / `62.6` | `43.84` | `0.408` | `BEARISH_SHOOTING_STAR` | 0.9966942 | `WATCH` | HOLD |
| `UNIUSDT` | 5.802 | 6.655266 | `-12.82%` | `33.48` / `35.42` | `36.18` | `0.277` | `NONE` | 5.5514488 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.52e-06 | 5e-06 | `-6.93%` | `39.59` / `49.35` | `47.56` | `0.575` | `BULLISH_HAMMER` | 4.31e-06 | `WATCH` | HOLD |
| `NEARUSDT` | 3.492 | 3.64423 | `-4.18%` | `79.26` / `82.18` | `53.76` | `0.782` | `BEARISH_ENGULFING` | 3.652632 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
