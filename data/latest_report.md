# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T06:39:32Z`
- **Ciclo de ejecucion:** `#113`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado mantiene un sesgo bajista predominante con la mayoría de los activos cotizando por debajo de la EMA 200. Se ha detectado una oportunidad de entrada en corto (S1) para RLUSDUSDT debido al rechazo en la resistencia de la EMA 200 con confirmación de vela bajista. Los demás activos se mantienen en vigilancia o en zonas de consolidación sin cumplir los criterios estrictos de los pilares LONG (P1-P4). No existen posiciones abiertas actualmente, por lo que no se requiere gestión dinámica de SL/TP en este ciclo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1000.52 | 1211.539571 | `-17.42%` | `12.46` / `14.19` | `28.79` | `0.233` | `BULLISH_HAMMER` | 954.49608 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.533 | 6.993006 | `-6.58%` | `16.64` / `15.3` | `30.87` | `0.092` | `BEARISH_ENGULFING` | 6.2531044 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.16 | 0.16617 | `-3.71%` | `47.22` / `59.09` | `39.58` | `0.333` | `NONE` | 0.153896 | `WATCH` | HOLD |
| `QNTUSDT` | 179.77 | 193.789372 | `-7.23%` | `46.3` / `45.38` | `33.36` | `0.246` | `NONE` | 174.680026 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3177 | 0.318663 | `-0.30%` | `20.77` / `14.25` | `43.79` | `0.313` | `BEARISH_SHOOTING_STAR` | 0.3094398 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73862.01 | 75810.270165 | `-2.57%` | `74.17` / `61.08` | `47.87` | `0.591` | `BULLISH_ENGULFING` | 71941.59774 | `WATCH` | HOLD |
| `CYBERUSDT` | 0.268 | 0.282765 | `-5.22%` | `5.35` / `4.73` | `43.42` | `0.22` | `BEARISH_ENGULFING` | 0.255672 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INITUSDT` | 0.28584 | 0.170373 | `+67.77%` | `55.89` / `62.68` | `55.25` | `0.575` | `BEARISH_ENGULFING` | 0.27269136 | `WATCH` | HOLD |
| `ETHUSDT` | 2066.5 | 2191.726272 | `-5.71%` | `82.68` / `72.09` | `46.56` | `0.613` | `NONE` | 2012.771 | `EXIT_LONG_STOCH_80` | HOLD |
| `ONEUSDT` | 0.00175 | 0.001555 | `+12.56%` | `32.8` / `31.97` | `49.6` | `0.228` | `NONE` | 0.0016695 | `WATCH` | HOLD |
| `SOLUSDT` | 83.13 | 89.020723 | `-6.62%` | `57.28` / `53.34` | `41.24` | `0.444` | `BULLISH_ENGULFING` | 80.96862 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0613 | 1.1584 | `-8.38%` | `59.52` / `58.24` | `44.72` | `0.535` | `BULLISH_ENGULFING` | 1.028474 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0011 | 1.001212 | `-0.01%` | `66.67` / `73.81` | `47.73` | `0.509` | `BEARISH_SHOOTING_STAR` | 1.0271286 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (82%) |
| `PEPEUSDT` | 5.29e-06 | 5e-06 | `+4.29%` | `45.12` / `49.16` | `49.0` | `0.38` | `BULLISH_HAMMER` | 5.05e-06 | `WATCH` | HOLD |
| `BNBUSDT` | 680.68 | 693.385151 | `-1.83%` | `69.43` / `63.69` | `46.34` | `0.52` | `BEARISH_ENGULFING` | 662.98232 | `WATCH` | HOLD |
| `NEARUSDT` | 3.632 | 3.769102 | `-3.64%` | `67.73` / `70.23` | `51.38` | `0.58` | `NONE` | 3.48888 | `WATCH` | HOLD |
