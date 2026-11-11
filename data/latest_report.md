# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T01:36:14Z`
- **Ciclo de ejecucion:** `#96`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global opera mayoritariamente por debajo de la EMA 200 en temporalidad de 1H con un sesgo bajista (Regimen BEARISH). No se cumplen los requisitos estrictos de los Pilares de entrada LONG (P1-P4) ni del Pilar SHORT de Futuros (S1), ya que ningun activo presenta simultaneamente los umbrales extremos de sobreventa/sobrecompra con patron de giro y cruce optimos. La cartera no posee posiciones abiertas (open_positions_count = 0), por lo que se mantiene en modo WATCH sin ejecutar nuevas ordenes de compra o venta en este ciclo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1034.47 | 1220.518153 | `-15.24%` | `21.07` / `22.91` | `32.7` | `0.246` | `BEARISH_ENGULFING` | 986.88438 | `WATCH` | HOLD |
| `UNIUSDT` | 6.766 | 7.016548 | `-3.57%` | `18.4` / `14.5` | `45.05` | `0.372` | `BEARISH_SHOOTING_STAR` | 6.454764 | `EXIT_SHORT_STOCH_20` | HOLD |
| `CYBERUSDT` | 0.273 | 0.283241 | `-3.62%` | `15.27` / `21.89` | `45.83` | `0.342` | `BEARISH_SHOOTING_STAR` | 0.260442 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73814.22 | 75898.106332 | `-2.75%` | `46.71` / `46.94` | `46.31` | `0.443` | `BEARISH_ENGULFING` | 71895.05028 | `WATCH` | **HOLD** (50%) |
| `TRXUSDT` | 0.318 | 0.318983 | `-0.31%` | `14.44` / `14.44` | `46.17` | `0.29` | `BULLISH_ENGULFING` | 0.309732 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2057.93 | 2198.068477 | `-6.38%` | `46.31` / `43.76` | `42.22` | `0.412` | `BULLISH_ENGULFING` | 1988.852234 | `WATCH` | HOLD |
| `INITUSDT` | 0.24752 | 0.1649 | `+50.10%` | `48.55` / `54.35` | `51.35` | `0.436` | `BEARISH_ENGULFING` | 0.23613408 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001895 | 0.001543 | `+22.81%` | `59.19` / `52.43` | `62.43` | `0.747` | `NONE` | 0.00180783 | `WATCH` | HOLD |
| `SOLUSDT` | 83.6 | 89.330719 | `-6.42%` | `50.19` / `44.43` | `43.26` | `0.435` | `BULLISH_ENGULFING` | 80.3528 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0576 | 1.163509 | `-9.10%` | `43.41` / `43.32` | `40.3` | `0.336` | `BULLISH_ENGULFING` | 1.01917568 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.46e-06 | 5e-06 | `+8.02%` | `59.48` / `49.46` | `61.45` | `0.939` | `BEARISH_SHOOTING_STAR` | 5.21e-06 | `WATCH` | HOLD |
| `NEARUSDT` | 3.695 | 3.775229 | `-2.13%` | `56.58` / `44.56` | `58.74` | `0.926` | `MORNING_STAR` | 3.52503 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0012 | 1.001214 | `-0.00%` | `83.33` / `78.83` | `54.62` | `0.639` | `NONE` | 0.9751688 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 682.79 | 693.754042 | `-1.58%` | `51.7` / `45.75` | `50.09` | `0.511` | `BULLISH_ENGULFING` | 665.03746 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.128 | 1.104575 | `+2.12%` | `65.91` / `71.96` | `60.79` | `0.746` | `NONE` | 1.076112 | `WATCH` | HOLD |
| `HYPEUSDT` | 72.22 | 78.427627 | `-7.92%` | `43.57` / `44.69` | `41.85` | `0.36` | `BEARISH_ENGULFING` | 69.634508 | `WATCH` | HOLD |
