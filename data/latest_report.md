# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T12:00:27Z`
- **Ciclo de ejecucion:** `#318`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> Mercado predominantemente bajista en temporalidad 1H, con BTC, ETH y la mayoria de altcoins cotizando por debajo de la EMA 200 con pendientes negativas. Tras evaluar cuantitativamente los 16 activos candidatos frente a los Pilares LONG (P1-P4) y SHORT (S1), ninguno cumple simultaneamente con la totalidad de los criterios de sobreventa/sobrecompra extrema, confluencia de RSI/Bollinger y patrones de vela confirmados. No se registraron posiciones abiertas para gestion dinamica de SL/TP.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `NBISBUSDT` | 127.33 | 138.399983 | `-8.00%` | `25.62` / `20.45` | `39.29` | `0.433` | `BULLISH_ENGULFING` | 121.47282 | `WATCH` | **HOLD** (0%) |
| `ERAUSDT` | 0.0774 | 0.078017 | `-0.79%` | `7.08` / `18.62` | `36.29` | `0.112` | `NONE` | 0.0738396 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `GRAMUSDT` | 1.152 | 1.138621 | `+1.18%` | `56.5` / `50.68` | `45.3` | `0.475` | `BULLISH_ENGULFING` | 1.1053616 | `WATCH` | **HOLD** (0%) |
| `BTCUSDT` | 69314.22 | 74273.408018 | `-6.68%` | `41.47` / `35.53` | `34.49` | `0.322` | `NONE` | 67183.335692 | `WATCH` | **HOLD** (0%) |
| `TIAUSDT` | 0.4161 | 0.428748 | `-2.95%` | `40.01` / `38.69` | `47.09` | `0.329` | `MORNING_STAR` | 0.3969594 | `WATCH` | **HOLD** (0%) |
| `ETHUSDT` | 1959.18 | 2121.436342 | `-7.65%` | `43.55` / `37.06` | `40.33` | `0.377` | `NONE` | 1884.347844 | `WATCH` | **HOLD** (0%) |
| `SOLUSDT` | 80.66 | 86.032963 | `-6.25%` | `63.59` / `55.54` | `47.41` | `0.519` | `NONE` | 77.766424 | `WATCH` | **HOLD** (0%) |
| `ZECUSDT` | 957.44 | 1107.884352 | `-13.58%` | `81.57` / `76.26` | `51.38` | `0.7` | `NONE` | 913.39776 | `EXIT_LONG_STOCH_80` | **HOLD** (0%) |
| `BNBUSDT` | 639.3 | 680.330584 | `-6.03%` | `45.12` / `37.23` | `38.86` | `0.366` | `BEARISH_SHOOTING_STAR` | 617.27326 | `WATCH` | **HOLD** (0%) |
| `DODOUSDT` | 0.02908 | 0.023568 | `+23.39%` | `66.75` / `54.0` | `67.64` | `0.932` | `BEARISH_SHOOTING_STAR` | 0.02774232 | `WATCH` | **HOLD** (0%) |
| `XRPUSDT` | 1.0235 | 1.108342 | `-7.65%` | `55.56` / `59.13` | `44.12` | `0.42` | `BULLISH_HAMMER` | 0.9947924 | `WATCH` | **HOLD** (0%) |
| `NEARUSDT` | 3.555 | 3.636457 | `-2.24%` | `89.37` / `84.2` | `59.64` | `0.905` | `MORNING_STAR` | 3.39147 | `EXIT_LONG_STOCH_80` | **HOLD** (0%) |
| `UNIUSDT` | 5.814 | 6.636152 | `-12.39%` | `37.36` / `35.01` | `37.51` | `0.336` | `BEARISH_SHOOTING_STAR` | 5.5646728 | `WATCH` | **HOLD** (0%) |
| `PEPEUSDT` | 4.5e-06 | 5e-06 | `-7.15%` | `29.63` / `32.54` | `45.38` | `0.446` | `NONE` | 4.29e-06 | `WATCH` | **HOLD** (0%) |
| `HYPEUSDT` | 73.9 | 75.312521 | `-1.88%` | `96.0` / `84.5` | `63.4` | `0.981` | `BULLISH_HAMMER` | 70.5006 | `EXIT_LONG_STOCH_80` | **HOLD** (0%) |
| `DOGEUSDT` | 0.06534 | 0.069321 | `-5.74%` | `61.43` / `55.8` | `47.72` | `0.51` | `NONE` | 0.06326104 | `WATCH` | **HOLD** (0%) |
