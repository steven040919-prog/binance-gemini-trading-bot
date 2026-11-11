# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T08:13:10Z`
- **Ciclo de ejecucion:** `#119`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se halla en un régimen bajista generalizado con la mayoría de los activos cotizando por debajo de la EMA 200 de 1H. Al evaluar los 16 candidatos bajo la arquitectura institucional de 4 Pilares LONG y 1 Pilar SHORT, ningún activo satisface de manera simultánea la totalidad de los filtros gatillo. ZECUSDT registra divergencia alcista en soporte pero carece de patrón de vela de giro; UNIUSDT presenta martillo alcista y clímax de volumen pero su estocástico aún no confirma giro al alza; TRXUSDT testea la EMA 200 pero el estocástico (30.77) no alcanza la sobrecompra extrema (>=80) requerida para la estrategia Short S1. Se mantiene el capital en liquidez total (100% USDT) protegiendo el portfolio.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 998.45 | 1207.665126 | `-17.32%` | `24.6` / `19.79` | `32.64` | `0.27` | `NONE` | 952.5213 | `EXIT_SHORT_STOCH_20` | **HOLD** (80%) |
| `UNIUSDT` | 6.446 | 6.983995 | `-7.70%` | `13.34` / `13.5` | `28.39` | `0.068` | `BULLISH_HAMMER` | 6.163282 | `EXIT_SHORT_STOCH_20` | **HOLD** (82%) |
| `PEPEUSDT` | 5.25e-06 | 5e-06 | `+3.59%` | `17.94` / `29.64` | `46.69` | `0.291` | `NONE` | 5.01e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (80%) |
| `ARBUSDT` | 0.1593 | 0.166053 | `-4.07%` | `21.81` / `33.09` | `38.73` | `0.314` | `BULLISH_HAMMER` | 0.15242984 | `WATCH` | **HOLD** (80%) |
| `QNTUSDT` | 179.29 | 193.782852 | `-7.48%` | `32.97` / `38.62` | `34.58` | `0.165` | `BULLISH_HAMMER` | 172.898756 | `WATCH` | HOLD |
| `ONEUSDT` | 0.0016 | 0.001555 | `+2.86%` | `5.32` / `16.18` | `40.54` | `-0.063` | `NONE` | 0.0015264 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74040.71 | 75767.791758 | `-2.28%` | `84.05` / `78.87` | `51.22` | `0.781` | `BULLISH_ENGULFING` | 72115.65154 | `EXIT_LONG_STOCH_80` | **HOLD** (85%) |
| `TRXUSDT` | 0.3177 | 0.318482 | `-0.25%` | `30.77` / `26.13` | `43.79` | `0.351` | `BEARISH_SHOOTING_STAR` | 0.3094398 | `WATCH` | **HOLD** (85%) |
| `CYBERUSDT` | 0.269 | 0.282325 | `-4.72%` | `6.52` / `4.95` | `44.56` | `0.255` | `NONE` | 0.256626 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2067.68 | 2189.424428 | `-5.56%` | `82.14` / `81.66` | `47.95` | `0.717` | `BULLISH_ENGULFING` | 2013.92032 | `EXIT_LONG_STOCH_80` | **HOLD** (85%) |
| `SOLUSDT` | 83.22 | 88.894886 | `-6.38%` | `50.93` / `52.97` | `44.19` | `0.547` | `BULLISH_ENGULFING` | 80.825328 | `WATCH` | **HOLD** (80%) |
| `XRPUSDT` | 1.0591 | 1.156304 | `-8.41%` | `44.24` / `49.69` | `44.16` | `0.551` | `BULLISH_HAMMER` | 1.0315634 | `WATCH` | HOLD |
| `INITUSDT` | 0.24821 | 0.171337 | `+44.87%` | `18.43` / `29.07` | `49.28` | `0.259` | `BULLISH_ENGULFING` | 0.23679234 | `EXIT_SHORT_STOCH_20` | HOLD |
| `RLUSDUSDT` | 1.0011 | 1.001203 | `-0.01%` | `45.71` / `56.19` | `47.73` | `0.519` | `NONE` | 0.9750714 | `WATCH` | HOLD |
| `BNBUSDT` | 682.24 | 693.055863 | `-1.56%` | `68.97` / `67.23` | `50.24` | `0.671` | `BULLISH_ENGULFING` | 664.50176 | `WATCH` | HOLD |
| `NEARUSDT` | 3.633 | 3.771416 | `-3.67%` | `53.37` / `59.36` | `51.56` | `0.586` | `BULLISH_HAMMER` | 3.465882 | `WATCH` | HOLD |
