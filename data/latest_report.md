# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T01:36:19Z`
- **Ciclo de ejecucion:** `#285`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen netamente bajista con la gran mayoría de los activos cotizando por debajo de la EMA 200 en temporalidad 1H. Los candidatos en LONG (como ERAUSDT y GRAMUSDT) cumplen con el Pilar 1 de pullback de valor sobre EMA 200 con estocástico girando al alza y patrones de vela confirmados, por lo que se priorizan compras selectivas en Spot. No existen posiciones abiertas con ganancias para aplicar ajustes dinámicos de SL/TP, manteniendo una postura disciplinada acorde al riesgo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71052.01 | 74881.299914 | `-5.11%` | `14.71` / `12.61` | `21.7` | `0.172` | `BEARISH_ENGULFING` | 69204.65774 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NBISBUSDT` | 130.86 | 140.319667 | `-6.74%` | `25.76` / `24.6` | `37.67` | `0.373` | `NONE` | 124.84044 | `WATCH` | HOLD |
| `BNBUSDT` | 655.2 | 685.511809 | `-4.42%` | `30.94` / `25.8` | `31.36` | `0.328` | `BULLISH_HAMMER` | 638.1648 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0833 | 0.077772 | `+7.11%` | `8.41` / `4.31` | `43.65` | `0.27` | `MORNING_STAR` | 0.0794682 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `GRAMUSDT` | 1.155 | 1.13785 | `+1.51%` | `17.44` / `14.79` | `42.22` | `0.27` | `BULLISH_ENGULFING` | 1.10187 | `P1_EMA200_PULLBACK` | **BUY** (82%) |
| `SOXSBUSDT` | 43.8 | 56.241161 | `-22.12%` | `8.89` / `15.21` | `35.4` | `0.109` | `BEARISH_ENGULFING` | 41.7852 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRXUSDT` | 0.3157 | 0.317761 | `-0.65%` | `18.96` / `16.68` | `38.85` | `0.291` | `BULLISH_ENGULFING` | 0.3074918 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2013.59 | 2141.67972 | `-5.98%` | `53.23` / `49.25` | `37.65` | `0.34` | `NONE` | 1961.23666 | `WATCH` | HOLD |
| `ZECUSDT` | 955.68 | 1128.718161 | `-15.33%` | `44.03` / `36.69` | `42.84` | `0.353` | `BULLISH_HAMMER` | 911.71872 | `WATCH` | HOLD |
| `SOLUSDT` | 81.51 | 86.788434 | `-6.08%` | `42.95` / `39.04` | `38.4` | `0.326` | `BULLISH_HAMMER` | 79.39074 | `WATCH` | HOLD |
| `NEARUSDT` | 3.445 | 3.672615 | `-6.20%` | `61.48` / `48.85` | `44.04` | `0.553` | `BULLISH_HAMMER` | 3.28653 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0319 | 1.1193 | `-7.81%` | `57.41` / `54.97` | `40.99` | `0.342` | `NONE` | 1.0050706 | `WATCH` | HOLD |
| `XAUTUSDT` | 3907.89 | 4006.608568 | `-2.46%` | `41.43` / `32.84` | `45.95` | `0.548` | `NONE` | 3806.28486 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.56e-06 | 5e-06 | `-6.93%` | `91.95` / `88.12` | `50.83` | `0.885` | `NONE` | 4.35e-06 | `EXIT_LONG_STOCH_80` | HOLD |
| `UNIUSDT` | 6.041 | 6.734558 | `-10.30%` | `54.86` / `46.39` | `38.05` | `0.374` | `BULLISH_HAMMER` | 5.8435176 | `WATCH` | HOLD |
| `DOGEUSDT` | 0.06637 | 0.069985 | `-5.17%` | `73.69` / `67.56` | `45.54` | `0.535` | `BULLISH_HAMMER` | 0.06458623 | `WATCH` | HOLD |
