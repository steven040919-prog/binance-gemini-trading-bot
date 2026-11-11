# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T00:53:42Z`
- **Ciclo de ejecucion:** `#77`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un régimen general bajista (la mayoría de los activos cotizan por debajo de la EMA 200 con pendientes negativas). Tras evaluar los candidatos bajo los 4 pilares LONG y el pilar SHORT (S1), no se detectan configuraciones completas de entrada que cumplan estrictamente con las condiciones de sobreventa/sobrecompra, giro estocástico, bandas de Bollinger y patrones de velas institucionales requeridas simultáneamente. Por lo tanto, el bot se mantiene en estado HOLD / WATCH, preservando el capital y esperando un pullback claro a resistencias para futuros shorts o capitulaciones profundas para entradas en spot.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1035.04 | 1221.802294 | `-15.29%` | `22.02` / `25.0` | `32.55` | `0.22` | `BEARISH_ENGULFING` | 987.42816 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0517 | 1.164476 | `-9.68%` | `42.04` / `43.12` | `35.76` | `0.233` | `BULLISH_HAMMER` | 1.02063172 | `WATCH` | HOLD |
| `UNIUSDT` | 6.692 | 7.013145 | `-4.58%` | `11.18` / `13.05` | `38.68` | `0.241` | `BULLISH_HAMMER` | 6.384168 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1613 | 0.166376 | `-3.05%` | `43.32` / `36.82` | `40.28` | `0.386` | `BULLISH_ENGULFING` | 0.1538802 | `WATCH` | HOLD |
| `AAVEUSDT` | 124.0 | 129.660847 | `-4.37%` | `53.2` / `51.77` | `37.91` | `0.371` | `NONE` | 119.3964 | `WATCH` | HOLD |
| `QNTUSDT` | 181.51 | 194.442421 | `-6.65%` | `41.14` / `39.96` | `34.11` | `0.299` | `BULLISH_HAMMER` | 173.16054 | `WATCH` | HOLD |
| `XAUTUSDT` | 4025.02 | 4035.470358 | `-0.26%` | `28.79` / `23.82` | `35.07` | `0.321` | `BEARISH_ENGULFING` | 3920.36948 | `WATCH` | HOLD |
| `BTCUSDT` | 73543.37 | 75910.191241 | `-3.12%` | `44.88` / `47.39` | `42.02` | `0.306` | `BEARISH_ENGULFING` | 71631.24238 | `WATCH` | **HOLD** (75%) |
| `ETHUSDT` | 2051.02 | 2199.2491 | `-6.74%` | `42.4` / `42.62` | `38.96` | `0.34` | `BEARISH_SHOOTING_STAR` | 1988.623072 | `WATCH` | HOLD |
| `INITUSDT` | 0.26333 | 0.163875 | `+60.69%` | `56.0` / `59.72` | `55.72` | `0.549` | `BEARISH_ENGULFING` | 0.25121682 | `WATCH` | HOLD |
| `PAXGUSDT` | 4027.49 | 4041.680996 | `-0.35%` | `28.9` / `23.64` | `34.85` | `0.316` | `MORNING_STAR` | 3922.77526 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001817 | 0.00154 | `+18.01%` | `47.21` / `48.92` | `56.86` | `0.588` | `BEARISH_SHOOTING_STAR` | 0.00173342 | `WATCH` | HOLD |
| `SOLUSDT` | 83.2 | 89.386561 | `-6.92%` | `42.8` / `40.54` | `38.69` | `0.341` | `BULLISH_ENGULFING` | 80.3636 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.43e-06 | 5e-06 | `+7.75%` | `50.98` / `40.74` | `59.88` | `0.888` | `NONE` | 5.18e-06 | `WATCH` | HOLD |
| `BNBUSDT` | 679.71 | 693.974771 | `-2.06%` | `44.13` / `39.95` | `44.35` | `0.381` | `NONE` | 662.03754 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.127 | 1.104415 | `+2.05%` | `69.7` / `76.22` | `60.49` | `0.756` | `BEARISH_SHOOTING_STAR` | 1.075158 | `WATCH` | HOLD |
