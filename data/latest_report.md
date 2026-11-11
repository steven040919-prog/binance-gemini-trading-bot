# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T19:31:30Z`
- **Ciclo de ejecucion:** `#149`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se mantiene predominantemente bajista con la mayoria de los activos cotizando por debajo de la EMA 200 en temporalidad 1H. Sin embargo, se identifican oportunidades de alta probabilidad bajo el Pilar 2 de capitulacion extrema en XAUTUSDT, PAXGUSDT y SOXSBUSDT, donde se generan entradas en largo con sobreventa simultanea en Estocastico, RSI y bandas de Bollinger. No hay posiciones abiertas actualmente, por lo que no se requieren ajustes dinamicos (ADJUST), procediendo a ejecutar las compras con gestion de riesgo estricta.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ONEUSDT` | 0.001515 | 0.001555 | `-2.58%` | `3.98` / `5.71` | `37.32` | `0.254` | `NONE` | 0.00144531 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PEPEUSDT` | 4.86e-06 | 5e-06 | `-3.95%` | `3.18` / `6.06` | `28.77` | `0.167` | `NONE` | 4.64e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1502 | 0.160952 | `-6.68%` | `28.89` / `46.37` | `42.31` | `-0.073` | `NONE` | 0.1448434 | `WATCH` | HOLD |
| `BTCUSDT` | 74392.39 | 75599.216967 | `-1.60%` | `77.57` / `77.44` | `56.57` | `0.9` | `BULLISH_HAMMER` | 72458.18786 | `WATCH` | HOLD |
| `XAUTUSDT` | 3982.12 | 4033.457236 | `-1.27%` | `2.48` / `2.43` | `22.24` | `0.045` | `BULLISH_HAMMER` | 3878.58488 | `P2_EXTREME_CAPITULATION` | **BUY** (88%) |
| `ARBUSDT` | 0.1588 | 0.165586 | `-4.10%` | `24.74` / `31.84` | `41.39` | `0.238` | `BULLISH_HAMMER` | 0.152936 | `WATCH` | HOLD |
| `INJUSDT` | 7.886 | 7.950404 | `-0.81%` | `23.44` / `25.22` | `42.94` | `0.241` | `BEARISH_ENGULFING` | 7.6117216 | `WATCH` | HOLD |
| `PAXGUSDT` | 3984.32 | 4038.978978 | `-1.35%` | `2.27` / `1.96` | `22.57` | `0.044` | `BULLISH_HAMMER` | 3880.72768 | `P2_EXTREME_CAPITULATION` | **BUY** (86%) |
| `ETHUSDT` | 2080.49 | 2177.520195 | `-4.46%` | `68.52` / `71.0` | `54.8` | `0.851` | `BULLISH_HAMMER` | 2026.39726 | `WATCH` | HOLD |
| `MUBUSDT` | 818.4 | 753.340917 | `+8.64%` | `92.34` / `95.18` | `75.46` | `0.861` | `BULLISH_ENGULFING` | 792.91272 | `EXIT_LONG_STOCH_80` | HOLD |
| `ZECUSDT` | 992.06 | 1182.447303 | `-16.10%` | `55.28` / `55.36` | `41.06` | `0.403` | `BULLISH_HAMMER` | 946.42524 | `WATCH` | HOLD |
| `SOXSBUSDT` | 43.91 | 59.79903 | `-26.57%` | `13.73` / `7.65` | `31.89` | `0.197` | `BULLISH_ENGULFING` | 41.89014 | `P2_EXTREME_CAPITULATION` | HOLD |
| `SNXXBUSDT` | 4.54 | 4.177298 | `+8.68%` | `90.89` / `94.12` | `74.34` | `0.846` | `BEARISH_SHOOTING_STAR` | 4.33116 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 84.81 | 88.426233 | `-4.09%` | `77.62` / `81.0` | `55.88` | `0.803` | `NONE` | 82.60494 | `EXIT_LONG_STOCH_80` | HOLD |
| `GRAMUSDT` | 1.21 | 1.119002 | `+8.13%` | `70.51` / `64.9` | `59.72` | `0.701` | `BEARISH_ENGULFING` | 1.15434 | `WATCH` | HOLD |
| `NEARUSDT` | 3.706 | 3.767212 | `-1.62%` | `64.42` / `73.43` | `52.52` | `0.561` | `NONE` | 3.5375364 | `WATCH` | HOLD |
