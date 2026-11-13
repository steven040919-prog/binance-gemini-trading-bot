# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T19:00:57Z`
- **Ciclo de ejecucion:** `#363`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global de criptomonedas se mantiene bajo presión bajista (régimen BEARISH generalizado), cotizando mayoritariamente por debajo de la EMA 200 en temporalidad de 1H. Los activos evaluados muestran oportunidades mixtas de corto alcance. Se identifican configuraciones válidas en los activos MUBUSDT (Pilar P1 de pullback sobre EMA 200 con patrón de giro Morning Star), INJUSDT (Pilar de scalper M15 long en tendencia alcista local), así como oportunidades bajistas en XAUTUSDT y PAXGUSDT bajo los filtros de Futuros USDT-M (Pilar S1 / Scalper Short). Se gestionan las reglas de stop-loss estructural basados en volatilidad ATR y soporte/resistencia previos.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68914.42 | 73844.876015 | `-6.68%` | `49.81` / `47.54` | `35.92` | `0.396` | `BULLISH_HAMMER` | 67122.64508 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0749 | 0.077825 | `-3.76%` | `6.8` / `7.99` | `33.78` | `0.164` | `BEARISH_SHOOTING_STAR` | 0.0714546 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3872.72 | 3989.709247 | `-2.93%` | `34.02` / `27.94` | `40.08` | `0.229` | `NONE` | 3973.41072 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (80%) |
| `MUBUSDT` | 767.02 | 763.224597 | `+0.50%` | `26.86` / `21.66` | `38.47` | `0.186` | `MORNING_STAR` | 735.826844 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `ETHUSDT` | 1941.52 | 2107.17588 | `-7.86%` | `47.39` / `42.69` | `39.58` | `0.414` | `MORNING_STAR` | 1884.081296 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.129 | 1.136755 | `-0.68%` | `24.4` / `23.61` | `40.7` | `0.231` | `BULLISH_ENGULFING` | 1.0848074 | `WATCH` | HOLD |
| `PAXGUSDT` | 3875.0 | 3993.487204 | `-2.97%` | `35.36` / `28.71` | `40.17` | `0.253` | `NONE` | 3975.75 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (80%) |
| `SOLUSDT` | 80.0 | 85.527159 | `-6.46%` | `45.39` / `44.13` | `43.88` | `0.47` | `NONE` | 82.42 | `M15_SCALPER_PULLBACK_SHORT` | HOLD |
| `ZECUSDT` | 944.78 | 1090.360371 | `-13.35%` | `54.21` / `57.44` | `45.93` | `0.489` | `BULLISH_ENGULFING` | 988.23988 | `M15_SCALPER_PULLBACK_SHORT` | HOLD |
| `BNBUSDT` | 635.89 | 676.774428 | `-6.04%` | `46.68` / `41.49` | `40.97` | `0.439` | `MORNING_STAR` | 618.426802 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0221 | 1.103239 | `-7.35%` | `46.08` / `46.32` | `45.97` | `0.478` | `MORNING_STAR` | 0.99007402 | `WATCH` | HOLD |
| `NEARUSDT` | 3.506 | 3.624244 | `-3.26%` | `62.93` / `63.82` | `51.95` | `0.596` | `BULLISH_ENGULFING` | 3.344724 | `WATCH` | HOLD |
| `SOXSBUSDT` | 51.62 | 55.49172 | `-6.98%` | `68.26` / `74.2` | `62.59` | `0.809` | `NONE` | 49.24548 | `WATCH` | HOLD |
| `UNIUSDT` | 5.812 | 6.57426 | `-11.59%` | `39.42` / `37.62` | `42.78` | `0.446` | `BULLISH_ENGULFING` | 5.544648 | `WATCH` | HOLD |
| `INJUSDT` | 8.096 | 7.802508 | `+3.76%` | `84.16` / `85.7` | `68.9` | `0.772` | `BULLISH_HAMMER` | 7.723584 | `M15_SCALPER_PULLBACK_LONG` | **BUY** (82%) |
| `PEPEUSDT` | 4.46e-06 | 5e-06 | `-7.74%` | `27.78` / `25.93` | `43.47` | `0.16` | `NONE` | 4.25e-06 | `WATCH` | HOLD |
