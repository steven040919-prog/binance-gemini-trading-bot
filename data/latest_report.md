# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T01:14:34Z`
- **Ciclo de ejecucion:** `#171`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general de altcoins y BTC se encuentra en un régimen dominantemente BAJISTA, cotizando por debajo de la EMA 200 de 1H con pendientes negativas. Ninguno de los 16 activos evaluados cumple estrictamente con los criterios de entrada de los Pilares LONG (P1-P4) ni con el Pilar SHORT S1. Activos con sobreventa extrema como UNIUSDT o PEPEUSDT presentan señales parciales pero carecen de confirmación en el giro del Estocástico o en la mejora del MACD. XRPUSDT y LTCUSDT muestran indicadores fuera de rango para el Pilar S1. Sin posiciones abiertas para ajustar. Se mantiene capital en preservación (100% USDT líquido).

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.53e-06 | 5e-06 | `-9.91%` | `6.14` / `4.8` | `20.72` | `0.073` | `NONE` | 4.32e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `UNIUSDT` | 6.173 | 6.920786 | `-10.80%` | `7.76` / `11.62` | `25.73` | `-0.074` | `BULLISH_HAMMER` | 5.9242412 | `EXIT_SHORT_STOCH_20` | **HOLD** (88%) |
| `XRPUSDT` | 1.0511 | 1.141714 | `-7.94%` | `32.24` / `28.5` | `41.57` | `0.087` | `BULLISH_ENGULFING` | 1.0842242 | `M15_SCALPER_PULLBACK_SHORT` | **HOLD** (92%) |
| `NEARUSDT` | 3.596 | 3.755899 | `-4.26%` | `24.56` / `24.14` | `42.76` | `0.201` | `BULLISH_ENGULFING` | 3.430584 | `WATCH` | **HOLD** (90%) |
| `INJUSDT` | 7.501 | 7.938823 | `-5.51%` | `12.27` / `10.58` | `28.65` | `0.011` | `BEARISH_ENGULFING` | 7.1744654 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `BNBUSDT` | 679.22 | 691.650634 | `-1.80%` | `27.13` / `31.38` | `42.44` | `0.198` | `BULLISH_ENGULFING` | 661.56028 | `WATCH` | **HOLD** (90%) |
| `ARBUSDT` | 0.1515 | 0.164999 | `-8.18%` | `6.3` / `7.49` | `27.65` | `-0.023` | `NONE` | 0.1461126 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `ENAUSDT` | 0.1454 | 0.160115 | `-9.19%` | `21.91` / `16.68` | `32.25` | `0.01` | `BULLISH_ENGULFING` | 0.1387116 | `EXIT_SHORT_STOCH_20` | **HOLD** (88%) |
| `LINKUSDT` | 10.165 | 10.74881 | `-5.43%` | `29.37` / `25.73` | `34.88` | `0.041` | `BULLISH_ENGULFING` | 9.761809 | `WATCH` | **HOLD** (90%) |
| `SUIUSDT` | 0.8203 | 0.854097 | `-3.96%` | `27.42` / `24.99` | `39.38` | `0.138` | `BEARISH_ENGULFING` | 0.79007686 | `WATCH` | **HOLD** (90%) |
| `OPGUSDT` | 0.1326 | 0.125925 | `+5.30%` | `6.27` / `9.27` | `44.52` | `0.281` | `BEARISH_SHOOTING_STAR` | 0.1265004 | `EXIT_SHORT_STOCH_20` | **HOLD** (92%) |
| `BTCUSDT` | 73843.95 | 75540.4114 | `-2.25%` | `41.75` / `45.59` | `45.84` | `0.323` | `BEARISH_ENGULFING` | 71924.0073 | `WATCH` | **HOLD** (90%) |
| `AAVEUSDT` | 119.7 | 128.745058 | `-7.03%` | `21.12` / `17.59` | `30.8` | `-0.038` | `BULLISH_HAMMER` | 115.58174 | `EXIT_SHORT_STOCH_20` | **HOLD** (88%) |
| `LTCUSDT` | 50.04 | 52.222535 | `-4.18%` | `32.74` / `27.32` | `35.59` | `-0.01` | `BEARISH_ENGULFING` | 51.530808 | `M15_SCALPER_PULLBACK_SHORT` | **HOLD** (92%) |
| `ADAUSDT` | 0.1739 | 0.18142 | `-4.15%` | `27.84` / `27.47` | `37.94` | `0.12` | `BULLISH_ENGULFING` | 0.16755684 | `WATCH` | **HOLD** (90%) |
| `ZECUSDT` | 987.12 | 1170.221052 | `-15.65%` | `39.24` / `33.57` | `43.21` | `0.477` | `BULLISH_ENGULFING` | 941.71248 | `WATCH` | **HOLD** (90%) |
