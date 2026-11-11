# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T17:57:44Z`
- **Ciclo de ejecucion:** `#141`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra mayoritariamente bajo la EMA 200 en temporalidad 1H con un sesgo bajista predominante. No se activan nuevos pilares de entrada LONG (P1-P4) ni SHORT (S1) debido a que los candidatos evaluados no cumplen estrictamente los umbrales de confluencia simultánea exigidos por la arquitectura cuantitativa. La cartera mantiene 0 posiciones abiertas y 14.0 USDT libres.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.94e-06 | 5e-06 | `-2.35%` | `8.91` / `8.1` | `32.99` | `0.196` | `BEARISH_SHOOTING_STAR` | 4.71e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001531 | 0.001556 | `-1.62%` | `9.08` / `11.29` | `37.79` | `0.231` | `NONE` | 0.00146057 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74545.52 | 75612.080512 | `-1.41%` | `75.09` / `62.77` | `59.49` | `1.209` | `MORNING_STAR` | 72490.544656 | `WATCH` | HOLD |
| `INJUSDT` | 7.936 | 7.94825 | `-0.15%` | `24.56` / `21.28` | `45.12` | `0.293` | `BEARISH_SHOOTING_STAR` | 7.570944 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1598 | 0.165754 | `-3.59%` | `37.58` / `33.56` | `43.69` | `0.315` | `MORNING_STAR` | 0.15351424 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3164 | 0.317332 | `-0.29%` | `12.06` / `16.01` | `30.02` | `-0.068` | `NONE` | 0.3081736 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3988.01 | 4034.476989 | `-1.15%` | `3.27` / `6.69` | `23.53` | `-0.061` | `NONE` | 3884.32174 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2092.38 | 2178.880551 | `-3.97%` | `73.04` / `60.91` | `61.05` | `1.235` | `NONE` | 2016.900396 | `WATCH` | HOLD |
| `PAXGUSDT` | 3990.87 | 4040.083091 | `-1.22%` | `3.05` / `6.93` | `23.69` | `-0.063` | `NONE` | 3887.10738 | `EXIT_SHORT_STOCH_20` | HOLD |
| `MUBUSDT` | 823.46 | 751.906342 | `+9.52%` | `97.28` / `96.85` | `81.49` | `1.002` | `BULLISH_HAMMER` | 785.58084 | `EXIT_LONG_STOCH_80` | HOLD |
| `ZECUSDT` | 1009.76 | 1185.965998 | `-14.86%` | `52.77` / `38.38` | `45.26` | `0.563` | `NONE` | 963.31104 | `WATCH` | HOLD |
| `SOLUSDT` | 85.38 | 88.480263 | `-3.50%` | `83.95` / `81.47` | `62.0` | `1.078` | `NONE` | 81.918248 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOXSBUSDT` | 42.22 | 60.13678 | `-29.79%` | `2.23` / `8.17` | `23.9` | `0.015` | `BEARISH_SHOOTING_STAR` | 40.27788 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.753 | 3.768118 | `-0.40%` | `80.42` / `78.12` | `57.32` | `0.768` | `NONE` | 3.580362 | `EXIT_LONG_STOCH_80` | HOLD |
| `SNXXBUSDT` | 4.61 | 4.170325 | `+10.54%` | `97.21` / `96.22` | `79.18` | `0.982` | `BULLISH_HAMMER` | 4.39794 | `EXIT_LONG_STOCH_80` | HOLD |
| `GRAMUSDT` | 1.22 | 1.117158 | `+9.21%` | `58.3` / `60.98` | `63.69` | `0.825` | `MORNING_STAR` | 1.16388 | `WATCH` | HOLD |
