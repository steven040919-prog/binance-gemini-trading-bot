# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T22:54:04Z`
- **Ciclo de ejecucion:** `#162`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general muestra un dominio de tendencia bajista con el precio de la mayoria de los activos cotizando por debajo de la EMA 200 de 1H. BTCUSDT ha activado una señal de entrada en corto valida bajo el Pilar S1 (S1_EMA200_RESISTANCE_REJECT) tras un rechazo en la zona de resistencia cerca de la EMA 200 confirmado por un patron de vela BEARISH_ENGULFING. No hay posiciones abiertas actualmente para ajustar SL/TP.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.63e-06 | 5e-06 | `-8.29%` | `3.16` / `3.2` | `20.07` | `0.04` | `NONE` | 4.42e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (30%) |
| `ZECUSDT` | 979.16 | 1176.006874 | `-16.74%` | `45.42` / `53.68` | `38.28` | `0.249` | `BEARISH_SHOOTING_STAR` | 934.11864 | `WATCH` | HOLD |
| `ETHUSDT` | 2056.18 | 2174.749093 | `-5.45%` | `42.61` / `53.32` | `43.27` | `0.254` | `NONE` | 2002.71932 | `WATCH` | HOLD |
| `UNIUSDT` | 6.351 | 6.927698 | `-8.32%` | `38.72` / `53.0` | `32.94` | `0.063` | `NONE` | 6.1082276 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0544 | 1.144075 | `-7.84%` | `31.74` / `35.34` | `42.57` | `0.169` | `NONE` | 1.0269856 | `WATCH` | HOLD |
| `NEARUSDT` | 3.601 | 3.763059 | `-4.31%` | `38.76` / `51.54` | `42.27` | `0.141` | `NONE` | 3.4459186 | `WATCH` | HOLD |
| `HYPEUSDT` | 71.69 | 77.273444 | `-7.23%` | `36.09` / `50.38` | `39.9` | `0.144` | `NONE` | 69.770398 | `WATCH` | HOLD |
| `ENAUSDT` | 0.146 | 0.160535 | `-9.05%` | `9.89` / `15.65` | `31.49` | `-0.293` | `NONE` | 0.1400608 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1533 | 0.165349 | `-7.29%` | `6.83` / `14.67` | `30.52` | `-0.178` | `NONE` | 0.14792506 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06732 | 0.071066 | `-5.27%` | `35.24` / `47.52` | `36.68` | `-0.065` | `BEARISH_ENGULFING` | 0.06556968 | `WATCH` | HOLD |
| `INJUSDT` | 7.744 | 7.954565 | `-2.65%` | `10.8` / `16.46` | `36.39` | `0.127` | `NONE` | 7.4690944 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3981.68 | 4031.845324 | `-1.24%` | `5.75` / `4.41` | `23.47` | `0.182` | `BULLISH_ENGULFING` | 3878.15632 | `EXIT_SHORT_STOCH_20` | **HOLD** (45%) |
| `LINKUSDT` | 10.178 | 10.750092 | `-5.32%` | `30.66` / `47.53` | `34.97` | `-0.161` | `NONE` | 9.900906 | `WATCH` | HOLD |
| `SUIUSDT` | 0.82 | 0.854848 | `-4.08%` | `33.94` / `47.95` | `39.05` | `0.046` | `BEARISH_ENGULFING` | 0.79868 | `WATCH` | HOLD |
| `OPGUSDT` | 0.1342 | 0.125688 | `+6.77%` | `22.95` / `31.31` | `46.72` | `0.389` | `BEARISH_ENGULFING` | 0.1280268 | `WATCH` | HOLD |
| `BTCUSDT` | 73926.01 | 75569.927969 | `-2.18%` | `66.93` / `75.62` | `47.17` | `0.416` | `BEARISH_ENGULFING` | 75848.08626 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
