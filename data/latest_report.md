# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T00:38:11Z`
- **Ciclo de ejecucion:** `#279`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se mantiene bajo una fuerte presión bajista con la mayoría de los activos operando por debajo de la EMA 200. Aunque se detectan patrones de reversión alcista (BULLISH_HAMMER en BTC, BULLISH_ENGULFING en BNB y ETH), las condiciones de los pilares P1-P4 no se cumplen plenamente debido a la falta de giro confirmado en el Estocástico o la debilidad en la pendiente de las medias móviles. Se mantiene una postura de vigilancia (WATCH) para evitar trampas de liquidez en un entorno de tendencia macro bajista.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 70944.07 | 74933.743119 | `-5.32%` | `9.93` / `9.99` | `20.91` | `0.116` | `BULLISH_HAMMER` | 69099.52418 | `EXIT_SHORT_STOCH_20` | **HOLD** (45%) |
| `SOLUSDT` | 81.31 | 86.873405 | `-6.40%` | `35.75` / `33.85` | `36.45` | `0.241` | `BEARISH_ENGULFING` | 79.19594 | `WATCH` | HOLD |
| `INITUSDT` | 0.11481 | 0.158474 | `-27.55%` | `27.94` / `24.22` | `37.0` | `0.265` | `BEARISH_SHOOTING_STAR` | 0.10952874 | `WATCH` | HOLD |
| `NBISBUSDT` | 129.47 | 140.502864 | `-7.85%` | `23.71` / `23.3` | `35.56` | `0.327` | `BULLISH_ENGULFING` | 123.51438 | `WATCH` | HOLD |
| `NEARUSDT` | 3.409 | 3.684442 | `-7.48%` | `41.18` / `39.4` | `37.65` | `0.322` | `NONE` | 3.2760028 | `WATCH` | HOLD |
| `BNBUSDT` | 654.29 | 685.9612 | `-4.62%` | `21.85` / `20.24` | `30.38` | `0.286` | `BULLISH_ENGULFING` | 637.27846 | `WATCH` | **HOLD** (50%) |
| `XAUTUSDT` | 3883.37 | 4007.988063 | `-3.11%` | `29.9` / `26.73` | `32.99` | `0.35` | `NONE` | 3782.40238 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0808 | 0.077747 | `+3.93%` | `3.03` / `2.38` | `38.25` | `0.148` | `NONE` | 0.0770832 | `EXIT_SHORT_STOCH_20` | HOLD |
| `GRAMUSDT` | 1.143 | 1.138123 | `+0.43%` | `12.79` / `12.73` | `38.63` | `0.197` | `BEARISH_SHOOTING_STAR` | 1.090422 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOXSBUSDT` | 44.59 | 56.316326 | `-20.82%` | `16.92` / `21.89` | `38.96` | `0.182` | `NONE` | 42.53886 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AVAXUSDT` | 8.326 | 8.43659 | `-1.31%` | `26.42` / `23.22` | `40.28` | `0.291` | `MORNING_STAR` | 8.109524 | `WATCH` | HOLD |
| `PAXGUSDT` | 3886.2 | 4012.391325 | `-3.15%` | `30.68` / `26.9` | `32.9` | `0.352` | `BULLISH_HAMMER` | 3785.1588 | `WATCH` | HOLD |
| `ONEUSDT` | 0.00152 | 0.001554 | `-2.16%` | `2.67` / `5.26` | `42.73` | `0.256` | `NONE` | 0.00145008 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRXUSDT` | 0.3154 | 0.317811 | `-0.76%` | `12.59` / `13.72` | `32.97` | `0.159` | `NONE` | 0.3071996 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 162.5 | 185.295276 | `-12.30%` | `47.87` / `46.2` | `36.71` | `0.298` | `NONE` | 157.9925 | `WATCH` | HOLD |
| `ETHUSDT` | 2008.1 | 2143.423744 | `-6.31%` | `44.72` / `46.41` | `34.08` | `0.237` | `BULLISH_ENGULFING` | 1955.8894 | `WATCH` | HOLD |
