# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T04:50:48Z`
- **Ciclo de ejecucion:** `#193`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra mayoritariamente bajo régimen bajista, cotizando por debajo de la EMA 200 en la mayoría de los activos evaluados. OPGUSDT muestra una estructura alcista y activa una señal de compra bajo el Pilar 1 (Pullback de valor sobre EMA 200). Para el resto de activos analizados, las condiciones no cumplen con los umbrales estrictos exigidos por los pilares LONG o el pilar SHORT institucional.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.58e-06 | 5e-06 | `-8.69%` | `16.05` / `15.02` | `26.92` | `0.204` | `BULLISH_HAMMER` | 4.37e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73778.8 | 75494.158121 | `-2.27%` | `28.5` / `29.83` | `45.17` | `0.275` | `BEARISH_ENGULFING` | 71860.5512 | `WATCH` | HOLD |
| `ETHUSDT` | 2052.04 | 2167.990647 | `-5.35%` | `28.38` / `29.33` | `42.78` | `0.236` | `NONE` | 1998.68696 | `WATCH` | HOLD |
| `UNIUSDT` | 6.258 | 6.896106 | `-9.25%` | `23.54` / `17.5` | `36.53` | `0.231` | `BULLISH_HAMMER` | 5.970132 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001454 | 0.001547 | `-6.03%` | `8.33` / `7.2` | `32.1` | `0.155` | `BULLISH_HAMMER` | 0.00138712 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.553 | 3.751705 | `-5.30%` | `10.88` / `16.61` | `38.91` | `0.122` | `BULLISH_HAMMER` | 3.4104874 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 83.15 | 87.999538 | `-5.51%` | `30.69` / `31.48` | `41.93` | `0.16` | `BULLISH_HAMMER` | 80.9881 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0453 | 1.138787 | `-8.21%` | `18.01` / `22.81` | `38.46` | `0.033` | `BEARISH_ENGULFING` | 1.0181222 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.533 | 7.923156 | `-4.92%` | `19.53` / `16.96` | `32.72` | `0.151` | `BULLISH_HAMMER` | 7.186482 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1503 | 0.164488 | `-8.63%` | `7.91` / `8.46` | `29.49` | `0.106` | `BEARISH_ENGULFING` | 0.14480022 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.144 | 0.159636 | `-9.79%` | `11.42` / `14.76` | `29.56` | `0.104` | `BEARISH_ENGULFING` | 0.1378432 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 677.23 | 691.675696 | `-2.09%` | `15.64` / `19.82` | `40.0` | `0.079` | `NONE` | 659.62202 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.0673 | 0.070871 | `-5.04%` | `31.77` / `32.15` | `38.73` | `0.15` | `BULLISH_HAMMER` | 0.0655394 | `WATCH` | HOLD |
| `QNTUSDT` | 166.26 | 190.211579 | `-12.59%` | `13.15` / `10.18` | `28.6` | `0.128` | `BEARISH_SHOOTING_STAR` | 158.61204 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LINKUSDT` | 10.118 | 10.725847 | `-5.67%` | `18.94` / `20.88` | `34.34` | `0.117` | `BEARISH_ENGULFING` | 9.8199556 | `EXIT_SHORT_STOCH_20` | HOLD |
| `OPGUSDT` | 0.1363 | 0.126175 | `+8.02%` | `8.67` / `6.2` | `50.91` | `0.382` | `BULLISH_ENGULFING` | 0.1300302 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
