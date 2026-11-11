# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T14:51:09Z`
- **Ciclo de ejecucion:** `#129`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general presenta una marcada tendencia bajista en la temporalidad de 1H, con la mayoria de los activos cotizando por debajo de su EMA 200 y pendientes negativas. Ningun activo de la lista cumple rigurosamente los criterios de activacion para los Pilares LONG (P1-P4) ni para el Pilar SHORT (S1). No hay posiciones abiertas actualmente que requieran ajustes de Trailing Stop o Break-Even. Se mantiene la liquidez intacta a la espera de confirmaciones cuantitativas mas claras.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 978.81 | 1193.398741 | `-17.98%` | `26.62` / `26.44` | `34.88` | `0.192` | `BULLISH_ENGULFING` | 933.78474 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.95e-06 | 5e-06 | `-2.25%` | `8.45` / `9.29` | `32.49` | `0.097` | `BULLISH_ENGULFING` | 4.72e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.451 | 6.962108 | `-7.34%` | `26.68` / `26.7` | `35.29` | `0.231` | `BULLISH_ENGULFING` | 6.201117 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001566 | 0.001556 | `+0.67%` | `6.45` / `4.62` | `40.05` | `0.225` | `NONE` | 0.00149396 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `TRXUSDT` | 0.3168 | 0.317644 | `-0.27%` | `22.64` / `18.03` | `34.33` | `-0.235` | `BULLISH_HAMMER` | 0.3085632 | `EXIT_SHORT_STOCH_20` | **HOLD** (80%) |
| `BTCUSDT` | 73694.01 | 75657.424729 | `-2.60%` | `60.33` / `70.03` | `45.63` | `0.374` | `BULLISH_HAMMER` | 71777.96574 | `WATCH` | **HOLD** (85%) |
| `XAUTUSDT` | 4008.72 | 4035.749665 | `-0.67%` | `22.81` / `33.91` | `29.81` | `-0.088` | `NONE` | 3904.49328 | `WATCH` | HOLD |
| `QNTUSDT` | 176.61 | 193.07537 | `-8.53%` | `12.53` / `15.8` | `31.88` | `0.022` | `NONE` | 171.620072 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2056.99 | 2181.855787 | `-5.72%` | `42.88` / `44.07` | `44.63` | `0.477` | `BULLISH_ENGULFING` | 2003.50826 | `WATCH` | **HOLD** (85%) |
| `GRAMUSDT` | 1.22 | 1.114667 | `+9.45%` | `86.75` / `81.99` | `66.51` | `0.874` | `BULLISH_HAMMER` | 1.16388 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 84.14 | 88.611121 | `-5.05%` | `84.5` / `87.25` | `52.45` | `0.888` | `BULLISH_ENGULFING` | 81.95236 | `EXIT_LONG_STOCH_80` | **HOLD** (80%) |
| `XRPUSDT` | 1.0582 | 1.150898 | `-8.05%` | `58.41` / `59.6` | `44.7` | `0.485` | `BULLISH_ENGULFING` | 1.0306868 | `WATCH` | HOLD |
| `NEARUSDT` | 3.731 | 3.769534 | `-1.02%` | `79.07` / `81.44` | `57.01` | `0.797` | `BULLISH_ENGULFING` | 3.5642676 | `EXIT_LONG_STOCH_80` | HOLD |
| `RLUSDUSDT` | 1.001 | 1.001194 | `-0.02%` | `33.33` / `19.05` | `46.81` | `0.349` | `MORNING_STAR` | 0.974974 | `EXIT_SHORT_STOCH_20` | HOLD |
| `MUBUSDT` | 778.67 | 749.832444 | `+3.85%` | `92.34` / `91.01` | `71.02` | `0.828` | `BULLISH_HAMMER` | 744.538984 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 681.37 | 692.487009 | `-1.61%` | `62.12` / `62.69` | `48.96` | `0.629` | `BULLISH_ENGULFING` | 663.65438 | `WATCH` | HOLD |
