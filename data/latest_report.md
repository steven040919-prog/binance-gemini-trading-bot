# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T18:51:29Z`
- **Ciclo de ejecucion:** `#362`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de temporalidad 1h mantiene un sesgo general bajista dominado por la EMA 200, con la gran mayoria de los activos cotizando por debajo de su media movil principal. Sin embargo, se identifican oportunidades puntuales en base a los pilares operativos y de alta frecuencia en Binance Spot y Futuros USDT-M: MUBUSDT cumple con los requisitos del Pilar 1 para LONG, mientras que activos como PEPEUSDT presentan configuraciones para operaciones en corto (SHORT) bajo la arquitectura de scalping M15.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68917.85 | 73870.310794 | `-6.70%` | `47.93` / `43.89` | `35.68` | `0.379` | `BULLISH_ENGULFING` | 67033.20014 | `WATCH` | HOLD |
| `ERAUSDT` | 0.075 | 0.077803 | `-3.60%` | `8.09` / `10.24` | `34.14` | `0.134` | `BEARISH_SHOOTING_STAR` | 0.07155 | `EXIT_SHORT_STOCH_20` | HOLD |
| `GRAMUSDT` | 1.129 | 1.137283 | `-0.73%` | `23.81` / `24.92` | `40.7` | `0.212` | `BEARISH_ENGULFING` | 1.0811946 | `WATCH` | HOLD |
| `MUBUSDT` | 765.68 | 763.396598 | `+0.30%` | `20.77` / `15.41` | `37.36` | `0.14` | `BULLISH_ENGULFING` | 730.45872 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `XAUTUSDT` | 3873.22 | 3990.129088 | `-2.93%` | `28.42` / `23.58` | `40.34` | `0.231` | `NONE` | 3772.51628 | `WATCH` | HOLD |
| `ETHUSDT` | 1942.3 | 2108.449691 | `-7.88%` | `42.63` / `39.04` | `39.51` | `0.4` | `BULLISH_ENGULFING` | 1874.63402 | `WATCH` | HOLD |
| `PAXGUSDT` | 3876.01 | 3993.908695 | `-2.95%` | `29.65` / `23.87` | `40.62` | `0.262` | `NONE` | 3775.23374 | `WATCH` | HOLD |
| `SOLUSDT` | 80.15 | 85.5514 | `-6.31%` | `43.82` / `45.79` | `45.1` | `0.489` | `NONE` | 77.31831 | `WATCH` | HOLD |
| `ZECUSDT` | 947.44 | 1090.566457 | `-13.12%` | `58.95` / `60.44` | `47.12` | `0.518` | `BULLISH_ENGULFING` | 903.85776 | `WATCH` | HOLD |
| `BNBUSDT` | 636.31 | 677.101835 | `-6.02%` | `40.95` / `38.51` | `41.2` | `0.429` | `MORNING_STAR` | 615.85749 | `WATCH` | HOLD |
| `NEARUSDT` | 3.518 | 3.625227 | `-2.96%` | `64.71` / `65.89` | `53.5` | `0.647` | `BEARISH_SHOOTING_STAR` | 3.356172 | `WATCH` | HOLD |
| `XRPUSDT` | 1.026 | 1.104037 | `-7.07%` | `48.12` / `50.29` | `48.72` | `0.56` | `BEARISH_SHOOTING_STAR` | 0.9848448 | `WATCH` | HOLD |
| `SOXSBUSDT` | 51.5 | 55.51007 | `-7.22%` | `73.28` / `81.39` | `62.43` | `0.83` | `NONE` | 49.131 | `EXIT_LONG_STOCH_80` | HOLD |
| `INJUSDT` | 8.093 | 7.797833 | `+3.79%` | `84.59` / `87.47` | `68.76` | `0.8` | `BULLISH_HAMMER` | 7.720722 | `M15_SCALPER_PULLBACK_LONG` | HOLD |
| `PEPEUSDT` | 4.47e-06 | 5e-06 | `-7.58%` | `23.61` / `25.0` | `44.42` | `0.181` | `BULLISH_ENGULFING` | 4.68e-06 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (82%) |
| `UNIUSDT` | 5.813 | 6.584757 | `-11.72%` | `36.07` / `39.76` | `42.7` | `0.426` | `BULLISH_ENGULFING` | 5.545602 | `WATCH` | HOLD |
