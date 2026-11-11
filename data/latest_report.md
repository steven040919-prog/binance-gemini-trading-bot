# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T21:20:39Z`
- **Ciclo de ejecucion:** `#156`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de criptomonedas y activos analizados opera predominantemente bajo un régimen bajista (por debajo de la EMA 200 en temporalidad 1H). Se evalúan los candidatos a través de los pilares de la estrategia Dual. PEPEUSDT y XAUTUSDT muestran condiciones cercanas a rebotes por sobreventa extrema, pero no se configuran entradas ideales bajo los pilares estrictos en este ciclo. No hay posiciones abiertas actuales, por lo que se prioriza la preservación de capital y la espera de configuraciones de alta probabilidad (Pilar 1-4 LONG o Pilar S1 SHORT en resistencias de EMA 200).

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.7e-06 | 5e-06 | `-6.96%` | `4.07` / `3.76` | `22.27` | `0.067` | `NONE` | 4.48e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001492 | 0.001553 | `-3.95%` | `4.33` / `3.89` | `34.72` | `0.237` | `NONE` | 0.00142337 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.828 | 7.948965 | `-1.52%` | `13.89` / `20.52` | `40.12` | `0.207` | `NONE` | 7.564676 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74670.92 | 75584.745277 | `-1.21%` | `85.73` / `81.61` | `60.63` | `0.963` | `BULLISH_ENGULFING` | 72729.47608 | `EXIT_LONG_STOCH_80` | **HOLD** (50%) |
| `XAUTUSDT` | 3979.1 | 4032.422775 | `-1.32%` | `3.18` / `2.57` | `21.16` | `0.125` | `BULLISH_HAMMER` | 3875.6434 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1499 | 0.160554 | `-6.64%` | `16.24` / `23.81` | `41.13` | `-0.02` | `NONE` | 0.1445531 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1577 | 0.165477 | `-4.70%` | `15.61` / `21.57` | `38.96` | `0.173` | `BEARISH_ENGULFING` | 0.15321056 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PAXGUSDT` | 3981.5 | 4037.930979 | `-1.40%` | `3.32` / `2.41` | `21.25` | `0.127` | `NONE` | 3877.981 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 994.74 | 1177.773111 | `-15.54%` | `59.13` / `59.28` | `42.09` | `0.468` | `NONE` | 948.98196 | `WATCH` | HOLD |
| `ETHUSDT` | 2080.09 | 2175.799168 | `-4.40%` | `60.33` / `63.32` | `54.24` | `0.781` | `NONE` | 2026.00766 | `WATCH` | HOLD |
| `SOXSBUSDT` | 45.28 | 59.501929 | `-23.90%` | `36.6` / `26.05` | `38.17` | `0.348` | `NONE` | 43.19712 | `WATCH` | HOLD |
| `MUBUSDT` | 815.5 | 754.56443 | `+8.08%` | `82.07` / `87.08` | `71.64` | `0.782` | `NONE` | 784.7874 | `M15_SCALPER_PULLBACK_LONG` | HOLD |
| `SNXXBUSDT` | 4.45 | 4.183667 | `+6.37%` | `77.65` / `84.14` | `66.69` | `0.736` | `NONE` | 4.2453 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 84.91 | 88.338322 | `-3.88%` | `72.63` / `75.27` | `56.35` | `0.766` | `BULLISH_ENGULFING` | 82.70234 | `WATCH` | HOLD |
| `NEARUSDT` | 3.697 | 3.766212 | `-1.84%` | `58.07` / `61.9` | `51.36` | `0.497` | `BEARISH_ENGULFING` | 3.5460352 | `WATCH` | HOLD |
| `XRPUSDT` | 1.066 | 1.144904 | `-6.89%` | `42.03` / `40.7` | `51.0` | `0.731` | `BULLISH_ENGULFING` | 1.0346592 | `WATCH` | HOLD |
