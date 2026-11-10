# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-10T23:31:34Z`
- **Ciclo de ejecucion:** `#44`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se mantiene bajo una presión bajista generalizada con la mayoría de los activos cotizando por debajo de la EMA 200. No se han detectado configuraciones de entrada (P1-P4 o S1) que cumplan con la confluencia estricta de los pilares institucionales. La mayoría de los activos muestran patrones de velas de reversión (como BEARISH_ENGULFING en ZEC, UNIU, LINK, SOL, XRP) pero sin la confirmación de volumen o sobrecompra necesaria para activar el pilar S1. Se mantiene una postura de observación (HOLD) para preservar el capital ante la falta de setups de alta probabilidad.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1042.72 | 1223.552087 | `-14.78%` | `25.57` / `26.29` | `33.45` | `0.225` | `BEARISH_ENGULFING` | 994.75488 | `WATCH` | HOLD |
| `UNIUSDT` | 6.665 | 7.014963 | `-4.99%` | `13.13` / `15.31` | `36.19` | `0.173` | `BEARISH_ENGULFING` | 6.35841 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1613 | 0.166358 | `-3.04%` | `38.3` / `31.02` | `39.55` | `0.365` | `MORNING_STAR` | 0.1538802 | `WATCH` | HOLD |
| `QNTUSDT` | 180.94 | 194.45921 | `-6.95%` | `37.37` / `37.74` | `32.82` | `0.25` | `NONE` | 172.834776 | `WATCH` | HOLD |
| `AAVEUSDT` | 123.88 | 129.636858 | `-4.44%` | `54.25` / `48.99` | `36.05` | `0.327` | `BEARISH_SHOOTING_STAR` | 119.21584 | `WATCH` | HOLD |
| `LINKUSDT` | 10.258 | 10.829972 | `-5.28%` | `37.48` / `38.68` | `38.44` | `0.22` | `BEARISH_ENGULFING` | 9.9284148 | `WATCH` | HOLD |
| `XAUTUSDT` | 4028.73 | 4035.484066 | `-0.17%` | `23.77` / `19.22` | `35.97` | `0.328` | `BULLISH_HAMMER` | 3923.98302 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73692.91 | 75927.210111 | `-2.94%` | `47.71` / `46.47` | `43.55` | `0.351` | `BEARISH_ENGULFING` | 71776.89434 | `WATCH` | **HOLD** (0%) |
| `TRXUSDT` | 0.3178 | 0.319093 | `-0.41%` | `14.44` / `14.44` | `43.11` | `0.227` | `NONE` | 0.3095372 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2050.82 | 2200.492254 | `-6.80%` | `42.1` / `41.84` | `38.58` | `0.32` | `BULLISH_HAMMER` | 1986.987696 | `WATCH` | HOLD |
| `PAXGUSDT` | 4031.86 | 4041.787911 | `-0.25%` | `23.37` / `19.04` | `35.99` | `0.328` | `BULLISH_ENGULFING` | 3927.03164 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001846 | 0.001537 | `+20.09%` | `48.34` / `51.13` | `59.52` | `0.656` | `NONE` | 0.00176108 | `WATCH` | HOLD |
| `SOLUSDT` | 83.08 | 89.429547 | `-7.10%` | `38.68` / `37.91` | `36.84` | `0.304` | `BEARISH_ENGULFING` | 80.28376 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0566 | 1.16537 | `-9.33%` | `44.56` / `43.53` | `37.99` | `0.274` | `BEARISH_ENGULFING` | 1.0198586 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.33e-06 | 5e-06 | `+5.90%` | `36.6` / `32.24` | `54.75` | `0.597` | `MORNING_STAR` | 5.08e-06 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.14 | 1.104028 | `+3.26%` | `79.89` / `78.34` | `66.71` | `0.951` | `BEARISH_SHOOTING_STAR` | 1.08756 | `WATCH` | HOLD |
