# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T20:49:18Z`
- **Ciclo de ejecucion:** `#154`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general mantiene una estructura predominantemente bajista con la mayoria de los activos cotizando por debajo de la EMA 200 de 1H. Tras escanear los 5 pilares operativos, no se detectan configuraciones activas para P1, P3, P4 ni S1. Sin embargo, se identifican senales claras de capitulacion extrema bajo el Pilar 2 (P2_EXTREME_CAPITULATION) en XAUTUSDT y PAXGUSDT, respaldadas por doble sobreventa extrema (Stoch < 4, RSI < 24), volumen comprador y patron de vela Bullish Engulfing. No hay posiciones abiertas actualmente para ajustar.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.78e-06 | 5e-06 | `-5.48%` | `3.54` / `4.63` | `25.28` | `0.118` | `NONE` | 4.56e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
| `ONEUSDT` | 0.001499 | 0.001554 | `-3.56%` | `3.87` / `3.77` | `35.35` | `0.248` | `BEARISH_ENGULFING` | 0.00143005 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
| `BTCUSDT` | 74678.0 | 75592.896348 | `-1.21%` | `81.43` / `79.78` | `60.8` | `1.04` | `BULLISH_HAMMER` | 72736.372 | `EXIT_LONG_STOCH_80` | **HOLD** (50%) |
| `ENAUSDT` | 0.1506 | 0.160833 | `-6.36%` | `22.15` / `34.55` | `43.4` | `0.041` | `BULLISH_HAMMER` | 0.14432056 | `WATCH` | HOLD |
| `XAUTUSDT` | 3981.68 | 4032.986506 | `-1.27%` | `3.57` / `2.25` | `22.99` | `0.099` | `BULLISH_ENGULFING` | 3878.15632 | `P2_EXTREME_CAPITULATION` | **BUY** (85%) |
| `INJUSDT` | 7.872 | 7.951817 | `-1.00%` | `22.34` / `24.88` | `42.22` | `0.239` | `BEARISH_ENGULFING` | 7.5746288 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1583 | 0.165533 | `-4.37%` | `22.21` / `27.72` | `40.41` | `0.205` | `BULLISH_HAMMER` | 0.1531676 | `WATCH` | HOLD |
| `PAXGUSDT` | 3983.87 | 4038.538334 | `-1.35%` | `3.37` / `1.77` | `23.08` | `0.098` | `BULLISH_ENGULFING` | 3880.28938 | `P2_EXTREME_CAPITULATION` | **BUY** (85%) |
| `ETHUSDT` | 2081.59 | 2177.145096 | `-4.39%` | `61.95` / `67.13` | `55.17` | `0.846` | `NONE` | 2027.46866 | `WATCH` | **HOLD** (50%) |
| `ZECUSDT` | 1002.55 | 1180.860767 | `-15.10%` | `60.02` / `59.75` | `44.24` | `0.567` | `BULLISH_HAMMER` | 956.4327 | `WATCH` | HOLD |
| `MUBUSDT` | 814.01 | 754.018991 | `+7.96%` | `87.88` / `92.01` | `71.89` | `0.795` | `NONE` | 788.63371 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOXSBUSDT` | 44.95 | 59.643684 | `-24.64%` | `24.84` / `15.39` | `36.64` | `0.301` | `MORNING_STAR` | 42.8823 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SNXXBUSDT` | 4.47 | 4.182537 | `+6.87%` | `86.45` / `90.77` | `69.57` | `0.768` | `BULLISH_HAMMER` | 4.26438 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 85.08 | 88.393331 | `-3.75%` | `75.47` / `78.39` | `58.24` | `0.845` | `BULLISH_HAMMER` | 82.86792 | `WATCH` | **HOLD** (50%) |
| `NEARUSDT` | 3.714 | 3.770108 | `-1.49%` | `61.77` / `68.05` | `53.24` | `0.575` | `BULLISH_HAMMER` | 3.543156 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0642 | 1.146034 | `-7.14%` | `35.95` / `45.05` | `49.62` | `0.673` | `BULLISH_HAMMER` | 1.0344802 | `WATCH` | HOLD |
