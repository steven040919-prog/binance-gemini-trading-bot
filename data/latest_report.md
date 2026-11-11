# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T06:24:01Z`
- **Ciclo de ejecucion:** `#112`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se mantiene bajo un régimen bajista generalizado con la mayoría de los activos cotizando por debajo de la EMA 200 en temporalidad 1H. No se cumplen las condiciones estrictas para las entradas LONG (P1-P4) debido a la falta de capitulación extrema simultánea o divergencias válidas. Sin embargo, se identifica una oportunidad óptima en el Pilar SHORT (S1) en RLUSDUSDT, que testea la resistencia de la EMA 200 con rechazo bajista y confluencia de osciladores.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1005.9 | 1211.593103 | `-16.98%` | `14.14` / `14.75` | `29.65` | `0.254` | `BULLISH_HAMMER` | 959.6286 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.551 | 6.993185 | `-6.32%` | `12.36` / `13.87` | `31.73` | `0.12` | `BEARISH_ENGULFING` | 6.3299884 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1602 | 0.166172 | `-3.59%` | `47.73` / `59.26` | `39.94` | `0.351` | `NONE` | 0.15458524 | `WATCH` | HOLD |
| `QNTUSDT` | 179.93 | 193.790964 | `-7.15%` | `46.98` / `45.61` | `33.73` | `0.262` | `NONE` | 174.90182 | `WATCH` | HOLD |
| `CYBERUSDT` | 0.268 | 0.282765 | `-5.22%` | `3.93` / `4.25` | `43.42` | `0.22` | `BEARISH_ENGULFING` | 0.255672 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRXUSDT` | 0.3179 | 0.318665 | `-0.24%` | `25.9` / `15.96` | `47.22` | `0.386` | `BEARISH_SHOOTING_STAR` | 0.3096346 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73859.77 | 75810.247876 | `-2.57%` | `74.11` / `61.06` | `47.83` | `0.59` | `BULLISH_ENGULFING` | 71939.41598 | `WATCH` | HOLD |
| `INITUSDT` | 0.3125 | 0.170638 | `+83.14%` | `61.32` / `64.49` | `59.28` | `0.752` | `BEARISH_ENGULFING` | 0.298125 | `WATCH` | HOLD |
| `ETHUSDT` | 2066.68 | 2191.728063 | `-5.71%` | `82.79` / `72.13` | `46.64` | `0.615` | `NONE` | 2012.94632 | `EXIT_LONG_STOCH_80` | HOLD |
| `ONEUSDT` | 0.001733 | 0.001555 | `+11.48%` | `31.0` / `31.37` | `48.44` | `0.159` | `NONE` | 0.00165328 | `WATCH` | HOLD |
| `SOLUSDT` | 83.17 | 89.021121 | `-6.57%` | `57.85` / `53.53` | `41.58` | `0.456` | `BULLISH_ENGULFING` | 81.00758 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0603 | 1.15839 | `-8.47%` | `58.42` / `57.87` | `44.09` | `0.51` | `BULLISH_ENGULFING` | 1.028494 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0012 | 1.001213 | `-0.00%` | `71.43` / `75.4` | `54.62` | `0.686` | `BEARISH_SHOOTING_STAR` | 1.0272312 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `PEPEUSDT` | 5.3e-06 | 5e-06 | `+4.48%` | `46.04` / `49.47` | `49.7` | `0.409` | `BULLISH_HAMMER` | 5.06e-06 | `WATCH` | HOLD |
| `BNBUSDT` | 680.3 | 693.38137 | `-1.89%` | `68.56` / `63.4` | `45.64` | `0.501` | `BEARISH_ENGULFING` | 662.6122 | `WATCH` | HOLD |
| `NEARUSDT` | 3.633 | 3.769112 | `-3.61%` | `67.86` / `70.28` | `51.5` | `0.584` | `NONE` | 3.5022982 | `WATCH` | HOLD |
