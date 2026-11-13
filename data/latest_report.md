# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T19:39:14Z`
- **Ciclo de ejecucion:** `#367`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global en temporalidad 1H se mantiene bajo presión bajista generalizada por debajo de la EMA 200, con la mayoría de activos en régimen BEARISH. Se identifica la activación de estrategias bajo los pilares institucionales: MUBUSDT cumple los requisitos del Pilar 1 LONG (P1_EMA200_PULLBACK) al rebotar sobre la EMA 200 con patrón de giro Morning Star y Estocástico al alza; PAXGUSDT activa el Pilar de alta frecuencia M15 SHORT (M15_SCALPER_PULLBACK_SHORT) con fuerte volumen institucional en zona de resistencia. No hay posiciones abiertas actuales en el portafolio para aplicar ajustes de SL/TP dinámicos.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.0742 | 0.077818 | `-4.65%` | `5.17` / `7.44` | `32.45` | `0.117` | `BEARISH_SHOOTING_STAR` | 0.0707868 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PEPEUSDT` | 4.46e-06 | 5e-06 | `-7.74%` | `27.78` / `25.93` | `43.47` | `0.16` | `NONE` | 4.25e-06 | `WATCH` | HOLD |
| `BTCUSDT` | 69036.53 | 73846.091039 | `-6.51%` | `51.57` / `48.12` | `37.46` | `0.436` | `BULLISH_HAMMER` | 67241.58022 | `WATCH` | HOLD |
| `XAUTUSDT` | 3870.79 | 3989.690043 | `-2.98%` | `32.25` / `27.35` | `39.32` | `0.197` | `NONE` | 3770.14946 | `WATCH` | HOLD |
| `MUBUSDT` | 770.03 | 763.254548 | `+0.89%` | `28.65` / `22.25` | `40.62` | `0.226` | `MORNING_STAR` | 734.973136 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `ETHUSDT` | 1950.59 | 2107.266129 | `-7.44%` | `50.92` / `43.87` | `43.28` | `0.496` | `MORNING_STAR` | 1882.727728 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.118 | 1.136646 | `-1.64%` | `17.86` / `21.43` | `37.13` | `0.023` | `BULLISH_ENGULFING` | 1.0796712 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PAXGUSDT` | 3873.94 | 3993.476657 | `-2.99%` | `34.44` / `28.4` | `39.73` | `0.236` | `NONE` | 3974.66244 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (80%) |
| `SOLUSDT` | 80.08 | 85.527955 | `-6.37%` | `46.03` / `44.35` | `44.51` | `0.492` | `NONE` | 77.550112 | `WATCH` | HOLD |
| `ZECUSDT` | 955.52 | 1090.467237 | `-12.38%` | `58.3` / `58.8` | `50.92` | `0.634` | `BULLISH_ENGULFING` | 911.56608 | `WATCH` | HOLD |
| `NEARUSDT` | 3.547 | 3.624652 | `-2.14%` | `67.18` / `65.23` | `56.71` | `0.717` | `BULLISH_ENGULFING` | 3.383838 | `WATCH` | HOLD |
| `BNBUSDT` | 638.48 | 676.800199 | `-5.66%` | `50.04` / `42.61` | `44.06` | `0.521` | `MORNING_STAR` | 618.124272 | `WATCH` | HOLD |
| `INJUSDT` | 8.292 | 7.804458 | `+6.25%` | `87.48` / `86.8` | `74.89` | `0.89` | `BULLISH_HAMMER` | 7.910568 | `EXIT_LONG_STOCH_80` | HOLD |
| `XRPUSDT` | 1.0288 | 1.103305 | `-6.75%` | `52.5` / `48.46` | `50.83` | `0.674` | `MORNING_STAR` | 0.98929728 | `WATCH` | HOLD |
| `BARDUSDT` | 0.1403 | 0.109443 | `+28.19%` | `27.98` / `41.41` | `51.17` | `0.382` | `BULLISH_HAMMER` | 0.1338462 | `WATCH` | HOLD |
| `SOXSBUSDT` | 51.28 | 55.488337 | `-7.58%` | `67.13` / `73.82` | `61.42` | `0.783` | `BULLISH_HAMMER` | 48.92112 | `WATCH` | HOLD |
