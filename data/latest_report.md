# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-10T23:46:59Z`
- **Ciclo de ejecucion:** `#50`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un régimen general bajista en temporalidad de 1H con la mayoría de los activos cotizando por debajo de la EMA 200. No se cumplen las condiciones de los Pilares Long (P1 a P4) ni del Pilar Short (S1) debido a la ausencia de confluencias extremas simultáneas en el estocástico, RSI y velas de giro. No hay posiciones abiertas actualmente, por lo que se emiten señales de espera (HOLD) para proteger el capital hasta encontrar setups óptimos institucionales.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1045.46 | 1223.579351 | `-14.56%` | `26.01` / `26.43` | `34.26` | `0.235` | `BEARISH_ENGULFING` | 997.36884 | `WATCH` | HOLD |
| `UNIUSDT` | 6.685 | 7.015162 | `-4.71%` | `14.35` / `15.71` | `37.95` | `0.201` | `BEARISH_ENGULFING` | 6.37749 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1609 | 0.166354 | `-3.28%` | `37.19` / `30.65` | `38.76` | `0.344` | `MORNING_STAR` | 0.1534986 | `WATCH` | HOLD |
| `QNTUSDT` | 181.27 | 194.462493 | `-6.78%` | `38.2` / `38.02` | `33.43` | `0.267` | `BULLISH_HAMMER` | 172.93158 | `WATCH` | HOLD |
| `AAVEUSDT` | 123.89 | 129.636957 | `-4.43%` | `54.31` / `49.01` | `36.1` | `0.329` | `BEARISH_SHOOTING_STAR` | 119.21552 | `WATCH` | HOLD |
| `XAUTUSDT` | 4027.82 | 4035.475011 | `-0.19%` | `23.33` / `19.07` | `35.36` | `0.322` | `BULLISH_HAMMER` | 3923.09668 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73827.35 | 75928.547823 | `-2.77%` | `49.82` / `47.17` | `45.59` | `0.404` | `BEARISH_ENGULFING` | 71907.8389 | `WATCH` | **HOLD** (50%) |
| `TRXUSDT` | 0.3177 | 0.319092 | `-0.44%` | `13.33` / `14.07` | `42.0` | `0.195` | `NONE` | 0.3094398 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2053.16 | 2200.515537 | `-6.70%` | `42.86` / `42.09` | `39.57` | `0.336` | `NONE` | 1986.924048 | `WATCH` | HOLD |
| `PAXGUSDT` | 4030.94 | 4041.778757 | `-0.27%` | `22.94` / `18.9` | `35.38` | `0.322` | `BULLISH_ENGULFING` | 3926.13556 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INITUSDT` | 0.27807 | 0.163224 | `+70.36%` | `60.83` / `65.01` | `59.89` | `0.656` | `BULLISH_HAMMER` | 0.26527878 | `WATCH` | HOLD |
| `ONEUSDT` | 0.00185 | 0.001537 | `+20.34%` | `48.65` / `51.23` | `59.87` | `0.662` | `NONE` | 0.0017649 | `WATCH` | HOLD |
| `SOLUSDT` | 83.45 | 89.433229 | `-6.69%` | `41.51` / `38.85` | `40.79` | `0.365` | `BEARISH_ENGULFING` | 80.24002 | `WATCH` | HOLD |
| `XRPUSDT` | 1.057 | 1.165374 | `-9.30%` | `44.78` / `43.61` | `38.17` | `0.28` | `BEARISH_ENGULFING` | 1.019847 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.37e-06 | 5e-06 | `+6.69%` | `39.22` / `33.12` | `56.87` | `0.731` | `MORNING_STAR` | 5.12e-06 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.142 | 1.104048 | `+3.44%` | `80.65` / `78.59` | `67.18` | `0.971` | `NONE` | 1.089468 | `EXIT_LONG_STOCH_80` | HOLD |
