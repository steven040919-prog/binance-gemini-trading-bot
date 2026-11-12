# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T00:27:56Z`
- **Ciclo de ejecucion:** `#168`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un regimen claramente bajista con la mayoria de los activos cotizando por debajo de la EMA 200 en temporalidad 1H. No se cumplen los requisitos estrictos de los Pilares LONG (P1-P4) debido a la ausencia de confluencias optimas de sobreventa extrema, divergencias validas o posicionamiento sobre valor dinamico. Tampoco se activan entradas SHORT (S1) al carecer de tests limpios en la resistencia de la EMA 200 con sobrecompra en Estocastico. El equity se mantiene en HOLD para preservar capital.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.56e-06 | 5e-06 | `-9.46%` | `5.71` / `3.81` | `21.63` | `0.071` | `NONE` | 4.35e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.21 | 6.920606 | `-10.27%` | `7.94` / `21.48` | `27.13` | `-0.077` | `BULLISH_HAMMER` | 5.927892 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.5 | 7.94663 | `-5.62%` | `9.0` / `9.43` | `28.26` | `-0.047` | `NONE` | 7.1745 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1521 | 0.165123 | `-7.89%` | `9.83` / `8.86` | `29.28` | `-0.075` | `NONE` | 0.1457286 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3979.0 | 4030.583867 | `-1.28%` | `8.59` / `6.21` | `27.71` | `0.23` | `NONE` | 3875.546 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74080.01 | 75548.827031 | `-1.94%` | `43.75` / `54.01` | `49.79` | `0.516` | `BULLISH_HAMMER` | 72153.92974 | `WATCH` | **HOLD** (50%) |
| `AAVEUSDT` | 119.84 | 128.910828 | `-7.04%` | `18.48` / `16.14` | `31.26` | `-0.125` | `BULLISH_HAMMER` | 115.530192 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PAXGUSDT` | 3980.57 | 4036.167181 | `-1.38%` | `8.26` / `5.8` | `26.46` | `0.225` | `NONE` | 3877.07518 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 984.05 | 1172.303005 | `-16.06%` | `29.46` / `34.64` | `42.16` | `0.398` | `BULLISH_ENGULFING` | 938.7837 | `WATCH` | HOLD |
| `ETHUSDT` | 2061.99 | 2172.614504 | `-5.09%` | `30.25` / `35.26` | `46.35` | `0.397` | `BULLISH_HAMMER` | 2001.188568 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001469 | 0.001552 | `-5.32%` | `4.2` / `5.51` | `32.64` | `0.202` | `BEARISH_SHOOTING_STAR` | 0.00140143 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SNXXBUSDT` | 4.28 | 4.196254 | `+2.00%` | `43.67` / `53.2` | `57.0` | `0.558` | `BULLISH_ENGULFING` | 4.08312 | `WATCH` | HOLD |
| `MUBUSDT` | 801.4 | 756.120793 | `+5.99%` | `50.75` / `59.27` | `60.18` | `0.607` | `BULLISH_ENGULFING` | 764.5356 | `WATCH` | HOLD |
| `SOLUSDT` | 83.74 | 88.215864 | `-5.07%` | `31.2` / `39.7` | `46.22` | `0.39` | `BULLISH_HAMMER` | 80.43146 | `WATCH` | HOLD |
| `SOXSBUSDT` | 47.11 | 59.117135 | `-20.31%` | `67.59` / `60.44` | `45.77` | `0.575` | `BEARISH_ENGULFING` | 44.94294 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0555 | 1.142705 | `-7.63%` | `26.25` / `27.6` | `44.13` | `0.251` | `BULLISH_HAMMER` | 1.0186234 | `WATCH` | HOLD |
