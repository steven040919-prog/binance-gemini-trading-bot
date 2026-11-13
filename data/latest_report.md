# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T02:53:40Z`
- **Ciclo de ejecucion:** `#293`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado mantiene una tendencia bajista predominante con la mayoría de los activos operando por debajo de la EMA 200. Se ha detectado una oportunidad de entrada en el activo ERAUSDT bajo el Pilar 1 (Pullback a EMA 200) al cumplir con los criterios de reversión y confirmación de vela. El resto de los activos se mantienen en vigilancia debido a la falta de confluencia técnica o patrones de giro validados en el marco de 1 hora.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 70085.13 | 74828.523722 | `-6.34%` | `10.7` / `12.02` | `15.37` | `-0.009` | `NONE` | 68262.91662 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 1982.29 | 2139.998823 | `-7.37%` | `39.37` / `45.97` | `24.43` | `-0.071` | `BEARISH_ENGULFING` | 1930.75046 | `WATCH` | HOLD |
| `SOLUSDT` | 79.94 | 86.70624 | `-7.80%` | `29.82` / `36.24` | `25.69` | `-0.112` | `NONE` | 77.86132 | `WATCH` | HOLD |
| `ZECUSDT` | 945.51 | 1126.546098 | `-16.07%` | `40.84` / `41.43` | `38.79` | `0.215` | `NONE` | 902.01654 | `WATCH` | HOLD |
| `BNBUSDT` | 645.47 | 685.057331 | `-5.78%` | `22.48` / `25.54` | `21.75` | `0.055` | `NONE` | 628.68778 | `WATCH` | HOLD |
| `NBISBUSDT` | 129.13 | 140.228554 | `-7.91%` | `35.29` / `28.62` | `35.71` | `0.352` | `BEARISH_ENGULFING` | 123.19002 | `WATCH` | HOLD |
| `XRPUSDT` | 1.018 | 1.118284 | `-8.97%` | `41.21` / `51.16` | `31.69` | `-0.023` | `NONE` | 0.9910932 | `WATCH` | HOLD |
| `NEARUSDT` | 3.404 | 3.669437 | `-7.23%` | `66.06` / `59.04` | `38.61` | `0.298` | `BEARISH_ENGULFING` | 3.2831992 | `WATCH` | HOLD |
| `UNIUSDT` | 5.875 | 6.728243 | `-12.68%` | `44.32` / `49.7` | `27.24` | `-0.161` | `BULLISH_HAMMER` | 5.670225 | `WATCH` | HOLD |
| `DOGEUSDT` | 0.06516 | 0.06992 | `-6.81%` | `61.43` / `67.39` | `32.26` | `0.052` | `BULLISH_HAMMER` | 0.06340526 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0816 | 0.077776 | `+4.92%` | `10.29` / `6.99` | `40.77` | `0.234` | `MORNING_STAR` | 0.0778464 | `P1_EMA200_PULLBACK` | **BUY** (82%) |
| `GRAMUSDT` | 1.145 | 1.137891 | `+0.62%` | `18.22` / `16.47` | `39.76` | `0.235` | `BEARISH_SHOOTING_STAR` | 1.09233 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1379 | 0.155165 | `-11.13%` | `53.93` / `61.1` | `28.69` | `-0.042` | `BULLISH_HAMMER` | 0.13266656 | `WATCH` | HOLD |
| `SUIUSDT` | 0.7882 | 0.842487 | `-6.44%` | `58.58` / `64.95` | `31.71` | `0.007` | `NONE` | 0.76606792 | `WATCH` | HOLD |
| `AVAXUSDT` | 8.22 | 8.428077 | `-2.47%` | `34.02` / `33.4` | `35.25` | `0.114` | `BULLISH_ENGULFING` | 7.99572 | `WATCH` | HOLD |
| `AAVEUSDT` | 112.66 | 125.354488 | `-10.13%` | `65.33` / `64.63` | `31.9` | `0.243` | `BEARISH_ENGULFING` | 109.65882 | `WATCH` | HOLD |
