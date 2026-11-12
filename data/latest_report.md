# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T15:25:22Z`
- **Ciclo de ejecucion:** `#235`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen netamente bajista en temporalidad 1H, con todos los activos cotizando por debajo de la EMA 200 y con pendiente negativa en la media móvil principal. Los osciladores estocásticos y RSI muestran condiciones de sobreventa extrema generalizada, activando salidas de cortos previos y patrones de giro (Martillos y Envolventes alcistas), aunque sin cumplir los filtros estrictos de los Pilares LONG (P1-P4) debido al sesgo bajista macro. No se configuran nuevas entradas en largo ni corto por falta de confluencia institucional completa según la arquitectura de pilares.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71424.01 | 75214.289614 | `-5.04%` | `10.71` / `11.67` | `18.24` | `-0.136` | `NONE` | 69566.98574 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `ETHUSDT` | 2003.22 | 2153.264919 | `-6.97%` | `27.08` / `24.28` | `24.95` | `-0.006` | `BULLISH_HAMMER` | 1951.13628 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.34e-06 | 5e-06 | `-12.36%` | `23.96` / `22.37` | `24.64` | `0.102` | `BULLISH_ENGULFING` | 4.14e-06 | `WATCH` | HOLD |
| `NBISBUSDT` | 126.63 | 141.33744 | `-10.41%` | `14.49` / `14.02` | `28.52` | `-0.047` | `BULLISH_HAMMER` | 120.80502 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.381 | 3.712364 | `-8.93%` | `17.3` / `13.47` | `29.68` | `0.102` | `BULLISH_ENGULFING` | 3.236189 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 80.99 | 87.3286 | `-7.26%` | `21.01` / `17.89` | `26.71` | `-0.013` | `BULLISH_HAMMER` | 78.88426 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0192 | 1.128189 | `-9.66%` | `18.13` / `19.49` | `27.32` | `-0.104` | `NONE` | 0.9927008 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 960.6 | 1143.574672 | `-16.00%` | `28.44` / `31.5` | `37.16` | `0.016` | `BEARISH_SHOOTING_STAR` | 916.4124 | `WATCH` | HOLD |
| `UNIUSDT` | 5.994 | 6.8085 | `-11.96%` | `21.87` / `18.13` | `26.69` | `0.134` | `BULLISH_ENGULFING` | 5.7865716 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 652.14 | 688.666343 | `-5.30%` | `9.94` / `8.71` | `16.63` | `-0.006` | `NONE` | 635.18436 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1378 | 0.157236 | `-12.36%` | `21.41` / `17.48` | `21.07` | `0.081` | `NONE` | 0.13269356 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06471 | 0.070368 | `-8.04%` | `17.44` / `19.25` | `21.18` | `-0.1` | `NONE` | 0.06302754 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3852.97 | 4017.672121 | `-4.10%` | `3.15` / `8.31` | `16.99` | `-0.131` | `NONE` | 3752.79278 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1445 | 0.162725 | `-11.20%` | `27.06` / `21.39` | `21.64` | `0.097` | `BEARISH_SHOOTING_STAR` | 0.1387008 | `WATCH` | HOLD |
| `AAVEUSDT` | 112.9 | 126.712645 | `-10.90%` | `21.44` / `13.74` | `27.34` | `0.148` | `BULLISH_ENGULFING` | 107.98266 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SUIUSDT` | 0.7869 | 0.84746 | `-7.15%` | `18.22` / `16.39` | `23.51` | `-0.028` | `BULLISH_HAMMER` | 0.76493082 | `EXIT_SHORT_STOCH_20` | HOLD |
