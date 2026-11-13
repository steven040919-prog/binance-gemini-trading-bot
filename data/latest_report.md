# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T00:48:27Z`
- **Ciclo de ejecucion:** `#280`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un régimen bajista generalizado con la mayoría de los activos cotizando por debajo de sus respectivas EMA 200. Destaca ERAUSDT cumpliendo con los criterios del Pilar 1 LONG (P1_EMA200_PULLBACK) al presentar tendencia alcista, precio en zona de valor sobre la EMA 200, estocástico en zona de sobreventa girando al alza y patrón de vela envolvente alcista. El resto de activos se mantienen en observación o sin posiciones abiertas con ganancia que requieran ajuste dinámico de SL/TP.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71130.0 | 74935.593168 | `-5.08%` | `12.14` / `10.73` | `22.4` | `0.16` | `BULLISH_HAMMER` | 69280.62 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 655.87 | 685.976921 | `-4.39%` | `24.3` / `21.05` | `32.33` | `0.331` | `BULLISH_ENGULFING` | 638.81738 | `WATCH` | HOLD |
| `NBISBUSDT` | 129.58 | 140.503958 | `-7.77%` | `23.79` / `23.33` | `35.69` | `0.329` | `BULLISH_ENGULFING` | 123.61932 | `WATCH` | HOLD |
| `XAUTUSDT` | 3886.2 | 4008.016222 | `-3.04%` | `30.84` / `27.04` | `34.67` | `0.369` | `NONE` | 3785.1588 | `WATCH` | HOLD |
| `INITUSDT` | 0.11569 | 0.158483 | `-27.00%` | `29.07` / `24.6` | `37.85` | `0.289` | `BEARISH_SHOOTING_STAR` | 0.11036826 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0809 | 0.077748 | `+4.05%` | `3.18` / `2.43` | `38.47` | `0.152` | `BULLISH_ENGULFING` | 0.0771786 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `GRAMUSDT` | 1.145 | 1.138143 | `+0.60%` | `13.18` / `12.86` | `39.24` | `0.206` | `BEARISH_SHOOTING_STAR` | 1.09233 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOXSBUSDT` | 44.61 | 56.316525 | `-20.79%` | `17.01` / `21.92` | `39.08` | `0.185` | `NONE` | 42.55794 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AVAXUSDT` | 8.332 | 8.436649 | `-1.24%` | `27.09` / `23.45` | `40.73` | `0.303` | `MORNING_STAR` | 8.0980296 | `WATCH` | HOLD |
| `PAXGUSDT` | 3888.14 | 4012.410628 | `-3.10%` | `31.35` / `27.12` | `34.09` | `0.365` | `BULLISH_HAMMER` | 3787.04836 | `WATCH` | HOLD |
| `ONEUSDT` | 0.00152 | 0.001554 | `-2.16%` | `2.67` / `5.26` | `42.73` | `0.256` | `NONE` | 0.00145008 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRXUSDT` | 0.3156 | 0.317813 | `-0.70%` | `17.35` / `15.31` | `35.41` | `0.234` | `BULLISH_HAMMER` | 0.3073944 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 162.27 | 185.292987 | `-12.43%` | `46.71` / `45.81` | `36.12` | `0.263` | `NONE` | 157.261164 | `WATCH` | HOLD |
| `ETHUSDT` | 2012.6 | 2143.46852 | `-6.11%` | `47.11` / `47.21` | `36.25` | `0.303` | `BULLISH_ENGULFING` | 1960.2724 | `WATCH` | HOLD |
| `ZECUSDT` | 955.56 | 1130.744829 | `-15.49%` | `33.93` / `29.35` | `42.16` | `0.341` | `MORNING_STAR` | 911.60424 | `WATCH` | HOLD |
| `SOLUSDT` | 81.51 | 86.875395 | `-6.18%` | `38.3` / `34.7` | `38.45` | `0.308` | `BULLISH_HAMMER` | 79.350894 | `WATCH` | HOLD |
