# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T16:55:34Z`
- **Ciclo de ejecucion:** `#137`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general opera bajo un régimen bajista con la mayoría de activos cotizando por debajo de la EMA 200. Se identifica una oportunidad válida en el Pilar S1 (SHORT_ENTRY) para NEARUSDT debido al rechazo bajista en la zona de resistencia de la EMA 200, con sobrecompra en Estocástico y patrón de vela BEARISH_SHOOTING_STAR. No hay posiciones abiertas actualmente para realizar ajustes dinámicos, y el capital libre se asignará de forma controlada a futuros USDT-M.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ONEUSDT` | 0.001556 | 0.001556 | `-0.02%` | `12.96` / `10.89` | `39.77` | `0.25` | `BULLISH_HAMMER` | 0.00148442 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PEPEUSDT` | 4.94e-06 | 5e-06 | `-2.46%` | `6.32` / `7.37` | `32.53` | `0.167` | `BEARISH_SHOOTING_STAR` | 4.71e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74192.76 | 75632.18243 | `-1.90%` | `57.74` / `55.76` | `54.54` | `1.032` | `NONE` | 72263.74824 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3164 | 0.317498 | `-0.35%` | `12.78` / `18.98` | `30.09` | `-0.167` | `NONE` | 0.3081736 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3992.12 | 4035.001927 | `-1.06%` | `5.17` / `12.59` | `24.68` | `-0.111` | `NONE` | 3888.32488 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2075.66 | 2179.804959 | `-4.78%` | `57.26` / `49.57` | `54.27` | `1.025` | `NONE` | 2013.2651 | `WATCH` | HOLD |
| `MUBUSDT` | 825.37 | 751.418917 | `+9.84%` | `97.85` / `95.14` | `83.12` | `1.097` | `BULLISH_HAMMER` | 787.40298 | `EXIT_LONG_STOCH_80` | HOLD |
| `PAXGUSDT` | 3994.75 | 4040.632964 | `-1.14%` | `5.35` / `12.98` | `24.78` | `-0.117` | `NONE` | 3890.8865 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.766 | 3.770762 | `-0.13%` | `73.98` / `76.31` | `59.5` | `0.854` | `BEARISH_SHOOTING_STAR` | 3.939236 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `SOLUSDT` | 84.69 | 88.543289 | `-4.35%` | `76.59` / `80.62` | `56.47` | `0.963` | `BULLISH_ENGULFING` | 81.9662 | `EXIT_LONG_STOCH_80` | HOLD |
| `ZECUSDT` | 997.57 | 1189.519064 | `-16.14%` | `30.48` / `27.49` | `41.79` | `0.415` | `BEARISH_SHOOTING_STAR` | 951.68178 | `WATCH` | HOLD |
| `SOXSBUSDT` | 42.88 | 60.316733 | `-28.91%` | `10.31` / `12.42` | `24.94` | `0.001` | `NONE` | 40.90752 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SNXXBUSDT` | 4.63 | 4.166557 | `+11.12%` | `97.27` / `93.16` | `81.04` | `1.074` | `BULLISH_HAMMER` | 4.41702 | `EXIT_LONG_STOCH_80` | HOLD |
| `XRPUSDT` | 1.0675 | 1.149362 | `-7.12%` | `62.43` / `61.41` | `52.09` | `0.954` | `BULLISH_ENGULFING` | 1.032204 | `WATCH` | HOLD |
| `SKHYBUSDT` | 145.42 | 135.480689 | `+7.34%` | `92.61` / `89.72` | `77.51` | `0.971` | `BULLISH_ENGULFING` | 138.73068 | `EXIT_LONG_STOCH_80` | HOLD |
| `INTCBUSDT` | 63.88 | 58.795966 | `+8.65%` | `92.67` / `87.6` | `78.59` | `1.037` | `MORNING_STAR` | 60.94152 | `EXIT_LONG_STOCH_80` | HOLD |
