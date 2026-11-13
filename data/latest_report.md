# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T01:45:54Z`
- **Ciclo de ejecucion:** `#286`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global de criptomonedas en temporalidad 1H se encuentra bajo un régimen bajista generalizado, cotizando mayoritariamente por debajo de la EMA 200 con pendientes negativas. Sin embargo, se identifican oportunidades de entrada LONG de alta probabilidad mediante los Pilares 1 y 2 en activos seleccionados (como GRAMUSDT y ERAUSDT) que muestran formaciones de pullback de valor sobre EMA 200 y patrones alcistas confirmados (Morning Star / Bullish Engulfing) con estocásticos girando al alza desde zonas de sobreventa. No hay posiciones abiertas actuales para gestionar (ADJUST), por lo que se prioriza la ejecución de nuevas entradas controladas.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71000.18 | 74880.784193 | `-5.18%` | `14.01` / `12.37` | `21.27` | `0.16` | `BEARISH_ENGULFING` | 69154.17532 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NBISBUSDT` | 130.89 | 140.319965 | `-6.72%` | `25.78` / `24.61` | `37.73` | `0.374` | `NONE` | 124.86906 | `WATCH` | HOLD |
| `BNBUSDT` | 654.43 | 685.504147 | `-4.53%` | `29.26` / `25.24` | `30.36` | `0.304` | `BULLISH_HAMMER` | 637.41482 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.153 | 1.13783 | `+1.33%` | `17.05` / `14.66` | `41.62` | `0.26` | `BULLISH_ENGULFING` | 1.099962 | `P1_EMA200_PULLBACK` | **BUY** (88%) |
| `SOXSBUSDT` | 44.14 | 56.244544 | `-21.52%` | `10.45` / `15.73` | `36.7` | `0.152` | `BEARISH_ENGULFING` | 42.10956 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ERAUSDT` | 0.0829 | 0.077768 | `+6.60%` | `7.8` / `4.11` | `42.85` | `0.256` | `MORNING_STAR` | 0.0790866 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `ONEUSDT` | 0.001523 | 0.001552 | `-1.87%` | `5.54` / `4.19` | `43.37` | `0.222` | `BULLISH_ENGULFING` | 0.00145294 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRXUSDT` | 0.3156 | 0.31776 | `-0.68%` | `16.4` / `15.82` | `36.59` | `0.246` | `BEARISH_SHOOTING_STAR` | 0.3073944 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2011.55 | 2141.659421 | `-6.08%` | `51.77` / `48.77` | `35.74` | `0.308` | `NONE` | 1959.2497 | `WATCH` | HOLD |
| `ZECUSDT` | 953.5 | 1128.69647 | `-15.52%` | `42.76` / `36.27` | `41.98` | `0.32` | `BULLISH_HAMMER` | 909.639 | `WATCH` | HOLD |
| `SOLUSDT` | 81.42 | 86.787539 | `-6.18%` | `41.67` / `38.61` | `37.41` | `0.294` | `BULLISH_HAMMER` | 79.30308 | `WATCH` | HOLD |
| `NEARUSDT` | 3.437 | 3.672536 | `-6.41%` | `59.49` / `48.18` | `42.46` | `0.503` | `BULLISH_HAMMER` | 3.2832026 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0321 | 1.119302 | `-7.79%` | `57.65` / `55.05` | `41.15` | `0.348` | `NONE` | 1.0052654 | `WATCH` | HOLD |
| `XAUTUSDT` | 3903.21 | 4006.562001 | `-2.58%` | `39.76` / `32.28` | `43.88` | `0.514` | `NONE` | 3801.72654 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.55e-06 | 5e-06 | `-7.14%` | `90.8` / `87.74` | `49.82` | `0.855` | `NONE` | 4.34e-06 | `EXIT_LONG_STOCH_80` | HOLD |
| `UNIUSDT` | 6.037 | 6.734518 | `-10.36%` | `54.2` / `46.17` | `37.72` | `0.357` | `BULLISH_HAMMER` | 5.840001 | `WATCH` | HOLD |
