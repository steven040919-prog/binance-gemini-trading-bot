# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-10T23:04:20Z`
- **Ciclo de ejecucion:** `#33`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global de criptomonedas se mantiene bajo presión bajista en temporalidad 1H, operando por debajo de la EMA 200 en la gran mayoría de los pares institucionales. No se cumplen los requisitos estrictos de los Pilares LONG (P1-P4) debido a que no se observan retrocesos limpios sobre soporte con sobreventa extrema y giro simultáneo. Tampoco se activan entradas SHORT bajo el Pilar S1 al no encontrarse rebotando directamente sobre la resistencia de la EMA 200 con patrones de velas de rechazo confirmados. Dado que no existen posiciones abiertas con ganancias (`open_positions_count: 0`), se mantiene una postura defensiva en observación (HOLD), resguardando el capital disponible (14.0 USDT) hasta que aparezca una configuración de alta probabilidad alineada con los 5 pilares cuantitativos de la estrategia.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1036.27 | 1223.487908 | `-15.30%` | `24.52` / `25.94` | `31.82` | `0.2` | `BEARISH_ENGULFING` | 988.60158 | `WATCH` | HOLD |
| `SOLUSDT` | 82.81 | 89.426861 | `-7.40%` | `36.61` / `37.22` | `34.26` | `0.261` | `BEARISH_ENGULFING` | 80.501006 | `WATCH` | HOLD |
| `NEARUSDT` | 3.554 | 3.773101 | `-5.81%` | `32.77` / `33.86` | `45.89` | `0.282` | `BEARISH_ENGULFING` | 3.390516 | `WATCH` | HOLD |
| `UNIUSDT` | 6.646 | 7.014774 | `-5.26%` | `11.92` / `14.9` | `34.82` | `0.148` | `BEARISH_ENGULFING` | 6.357514 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1612 | 0.166357 | `-3.10%` | `38.02` / `30.93` | `39.35` | `0.36` | `MORNING_STAR` | 0.1537848 | `WATCH` | HOLD |
| `QNTUSDT` | 180.88 | 194.458613 | `-6.98%` | `37.22` / `37.69` | `32.71` | `0.247` | `NONE` | 173.56568 | `WATCH` | HOLD |
| `AAVEUSDT` | 123.91 | 129.637156 | `-4.42%` | `54.42` / `49.04` | `36.19` | `0.332` | `BEARISH_SHOOTING_STAR` | 119.264444 | `WATCH` | HOLD |
| `LINKUSDT` | 10.277 | 10.830161 | `-5.11%` | `38.74` / `39.1` | `39.37` | `0.248` | `BEARISH_ENGULFING` | 9.9730224 | `WATCH` | HOLD |
| `XAUTUSDT` | 4026.04 | 4035.457299 | `-0.23%` | `22.48` / `18.79` | `34.14` | `0.31` | `BULLISH_HAMMER` | 3921.36296 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73626.01 | 75926.544439 | `-3.03%` | `46.65` / `46.12` | `42.74` | `0.325` | `BEARISH_ENGULFING` | 71711.73374 | `WATCH` | **HOLD** (0%) |
| `WLDUSDT` | 0.3077 | 0.341603 | `-9.92%` | `30.24` / `28.62` | `38.44` | `0.237` | `BEARISH_SHOOTING_STAR` | 0.29457664 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3179 | 0.319094 | `-0.37%` | `15.56` / `14.82` | `44.28` | `0.26` | `NONE` | 0.3096346 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2045.68 | 2200.441109 | `-7.03%` | `40.44` / `41.28` | `36.83` | `0.286` | `NONE` | 1989.855776 | `WATCH` | HOLD |
| `PAXGUSDT` | 4028.56 | 4041.755075 | `-0.33%` | `21.82` / `18.52` | `33.83` | `0.307` | `BULLISH_ENGULFING` | 3923.81744 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001836 | 0.001537 | `+19.44%` | `47.58` / `50.87` | `58.64` | `0.641` | `NONE` | 0.00175154 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0567 | 1.165371 | `-9.33%` | `44.61` / `43.55` | `38.03` | `0.276` | `BEARISH_ENGULFING` | 1.02508972 | `WATCH` | HOLD |
