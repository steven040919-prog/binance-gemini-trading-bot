# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T14:42:39Z`
- **Ciclo de ejecucion:** `#335`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado muestra una tendencia bajista predominante con la mayoría de los activos operando por debajo de la EMA 200. Se identifica una oportunidad de alta probabilidad en el Pilar S1 (Rechazo en EMA 200) para HYPEUSDT y ZECUSDT, aprovechando la sobrecompra en el estocástico y el rechazo en resistencia. No se activan pilares LONG debido a la falta de confluencia en los soportes macro.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.0779 | 0.077903 | `-0.00%` | `24.14` / `17.88` | `38.91` | `0.183` | `BULLISH_ENGULFING` | 0.0814834 | `M15_SCALPER_PULLBACK_SHORT` | HOLD |
| `GRAMUSDT` | 1.126 | 1.137263 | `-0.99%` | `40.62` / `51.0` | `37.57` | `-0.092` | `BEARISH_ENGULFING` | 1.0763916 | `WATCH` | HOLD |
| `BTCUSDT` | 69241.52 | 74097.991816 | `-6.55%` | `45.77` / `44.59` | `36.18` | `0.363` | `BULLISH_ENGULFING` | 67312.183344 | `WATCH` | HOLD |
| `ETHUSDT` | 1965.59 | 2115.694837 | `-7.09%` | `54.8` / `51.99` | `43.53` | `0.462` | `BEARISH_SHOOTING_STAR` | 1899.00466 | `WATCH` | HOLD |
| `INTCBUSDT` | 60.25 | 59.343701 | `+1.53%` | `18.69` / `31.9` | `42.05` | `0.082` | `BEARISH_SHOOTING_STAR` | 58.6835 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 962.56 | 1097.812703 | `-12.32%` | `79.52` / `83.04` | `52.7` | `0.716` | `BEARISH_SHOOTING_STAR` | 1006.83776 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (82%) |
| `DODOUSDT` | 0.0282 | 0.023743 | `+18.77%` | `64.07` / `69.54` | `57.77` | `0.579` | `NONE` | 0.0269028 | `WATCH` | HOLD |
| `SOLUSDT` | 81.26 | 85.768766 | `-5.26%` | `75.4` / `72.86` | `52.72` | `0.675` | `NONE` | 78.41724 | `WATCH` | HOLD |
| `NEARUSDT` | 3.573 | 3.632176 | `-1.63%` | `84.69` / `86.75` | `60.03` | `0.87` | `BULLISH_ENGULFING` | 3.408642 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 640.79 | 678.752799 | `-5.59%` | `54.09` / `51.32` | `41.91` | `0.444` | `BEARISH_SHOOTING_STAR` | 623.155514 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0353 | 1.107473 | `-6.52%` | `68.65` / `60.54` | `54.23` | `0.718` | `BULLISH_ENGULFING` | 0.98982456 | `WATCH` | HOLD |
| `INJUSDT` | 8.229 | 7.783468 | `+5.72%` | `92.92` / `93.33` | `77.08` | `1.136` | `BULLISH_HAMMER` | 7.850466 | `EXIT_LONG_STOCH_80` | HOLD |
| `PEPEUSDT` | 4.5e-06 | 5e-06 | `-7.16%` | `41.98` / `39.51` | `45.77` | `0.286` | `BEARISH_SHOOTING_STAR` | 4.29e-06 | `WATCH` | HOLD |
| `UNIUSDT` | 5.932 | 6.613438 | `-10.30%` | `57.13` / `47.71` | `48.79` | `0.571` | `BULLISH_HAMMER` | 5.659128 | `WATCH` | HOLD |
| `HYPEUSDT` | 74.12 | 75.242888 | `-1.49%` | `82.49` / `88.64` | `64.3` | `0.897` | `BEARISH_SHOOTING_STAR` | 77.529128 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `SUIUSDT` | 0.8224 | 0.835951 | `-1.62%` | `87.98` / `87.49` | `64.54` | `0.949` | `NONE` | 0.7845696 | `EXIT_LONG_STOCH_80` | HOLD |
