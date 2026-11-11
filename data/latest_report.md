# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T04:50:27Z`
- **Ciclo de ejecucion:** `#106`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de 1 hora opera mayoritariamente bajo régimen bajista con la cotización de los activos por debajo de la EMA 200. Se activa una oportunidad SHORT institucional en RLUSDUSDT bajo el Pilar S1 (Rechazo bajista en resistencia de la EMA 200 con vela bajista y estocástico en zona de sobrecompra girando a la baja). No se registran posiciones abiertas previas para la gestión dinámica de SL/TP, y el resto de activos se mantiene en vigilancia.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1020.83 | 1214.646574 | `-15.96%` | `14.32` / `14.45` | `32.04` | `0.27` | `BEARISH_ENGULFING` | 973.87182 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.694 | 7.003574 | `-4.42%` | `14.57` / `15.5` | `40.3` | `0.326` | `BEARISH_SHOOTING_STAR` | 6.386076 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOXSBUSDT` | 49.6 | 61.979432 | `-19.97%` | `3.88` / `7.04` | `32.61` | `0.039` | `BEARISH_SHOOTING_STAR` | 47.3184 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 180.27 | 194.187733 | `-7.17%` | `42.08` / `42.83` | `33.66` | `0.275` | `NONE` | 173.51082 | `WATCH` | HOLD |
| `CYBERUSDT` | 0.273 | 0.282977 | `-3.53%` | `5.91` / `5.43` | `46.26` | `0.301` | `BEARISH_ENGULFING` | 0.260442 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73763.8 | 75838.204959 | `-2.74%` | `47.16` / `44.27` | `45.91` | `0.494` | `BULLISH_HAMMER` | 71845.9412 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3178 | 0.318487 | `-0.22%` | `9.37` / `10.41` | `45.32` | `0.304` | `NONE` | 0.3095372 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2067.28 | 2194.029439 | `-5.78%` | `60.52` / `53.53` | `46.72` | `0.572` | `BEARISH_SHOOTING_STAR` | 2002.513664 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001735 | 0.00155 | `+11.93%` | `39.44` / `57.36` | `48.41` | `0.128` | `BULLISH_HAMMER` | 0.00165519 | `WATCH` | HOLD |
| `SOLUSDT` | 83.05 | 89.11219 | `-6.80%` | `49.39` / `49.15` | `38.19` | `0.381` | `BEARISH_SHOOTING_STAR` | 80.7268 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0551 | 1.160268 | `-9.06%` | `54.83` / `49.03` | `39.37` | `0.351` | `BEARISH_SHOOTING_STAR` | 1.01987842 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.36e-06 | 5e-06 | `+5.86%` | `53.59` / `57.51` | `54.25` | `0.603` | `BEARISH_SHOOTING_STAR` | 5.11e-06 | `WATCH` | HOLD |
| `NEARUSDT` | 3.683 | 3.77019 | `-2.31%` | `73.13` / `69.05` | `57.68` | `0.813` | `BEARISH_SHOOTING_STAR` | 3.513582 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0012 | 1.001206 | `-0.00%` | `79.37` / `82.01` | `54.62` | `0.686` | `BEARISH_SHOOTING_STAR` | 1.0272312 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (84%) |
| `BNBUSDT` | 681.65 | 693.427781 | `-1.70%` | `56.69` / `54.42` | `48.14` | `0.523` | `BEARISH_ENGULFING` | 663.9271 | `WATCH` | HOLD |
| `HYPEUSDT` | 72.24 | 78.130773 | `-7.54%` | `40.36` / `38.67` | `43.2` | `0.439` | `BULLISH_ENGULFING` | 69.366176 | `WATCH` | HOLD |
