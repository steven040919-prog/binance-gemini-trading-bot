# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-10T23:51:51Z`
- **Ciclo de ejecucion:** `#52`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general mantiene una clara estructura bajista con el bloque mayoritario de activos cotizando por debajo de la EMA 200 de 1H y con pendientes negativas. Ningun activo cumple con los criterios cuantitativos estrictos de los Pilares LONG (P1-P4) ni del Pilar SHORT (S1). En particular, AAVEUSDT esta cerca de la EMA 200 pero carece de sobrecompra en Estocastico y RSI para validar S1; GRAMUSDT cotiza sobre la EMA 200 pero con Estocastico en 79.51 sin haber realizado el pullback a sobreventa (<=20). No hay posiciones abiertas para aplicar gestion dinamica. Se mantiene capital en preservacion al 100% USDT.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1041.11 | 1223.536067 | `-14.91%` | `25.31` / `26.2` | `32.96` | `0.218` | `BEARISH_ENGULFING` | 993.21894 | `WATCH` | **HOLD** (95%) |
| `UNIUSDT` | 6.661 | 7.014923 | `-5.05%` | `12.89` / `15.23` | `35.83` | `0.168` | `BEARISH_ENGULFING` | 6.354594 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `ARBUSDT` | 0.1605 | 0.16635 | `-3.52%` | `36.08` / `30.28` | `38.0` | `0.324` | `MORNING_STAR` | 0.153117 | `WATCH` | **HOLD** (88%) |
| `QNTUSDT` | 181.11 | 194.460901 | `-6.87%` | `37.8` / `37.88` | `33.13` | `0.259` | `BULLISH_HAMMER` | 172.864266 | `WATCH` | **HOLD** (92%) |
| `AAVEUSDT` | 123.47 | 129.632778 | `-4.75%` | `51.89` / `48.2` | `34.31` | `0.26` | `BEARISH_SHOOTING_STAR` | 119.204266 | `WATCH` | **HOLD** (90%) |
| `XAUTUSDT` | 4028.06 | 4035.477399 | `-0.18%` | `23.45` / `19.11` | `35.52` | `0.324` | `BULLISH_HAMMER` | 3923.33044 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `BTCUSDT` | 73776.72 | 75928.044041 | `-2.83%` | `49.03` / `46.91` | `44.84` | `0.384` | `BEARISH_ENGULFING` | 71858.52528 | `WATCH` | **HOLD** (94%) |
| `TRXUSDT` | 0.3177 | 0.319092 | `-0.44%` | `13.33` / `14.07` | `42.0` | `0.195` | `NONE` | 0.3094398 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `ETHUSDT` | 2050.01 | 2200.484194 | `-6.84%` | `41.84` / `41.75` | `38.23` | `0.315` | `NONE` | 1986.599726 | `WATCH` | **HOLD** (93%) |
| `PAXGUSDT` | 4030.39 | 4041.773284 | `-0.28%` | `22.68` / `18.81` | `35.0` | `0.319` | `BULLISH_ENGULFING` | 3925.59986 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `INITUSDT` | 0.27332 | 0.163177 | `+67.50%` | `59.7` / `64.64` | `58.91` | `0.628` | `BULLISH_HAMMER` | 0.26074728 | `WATCH` | **HOLD** (95%) |
| `ONEUSDT` | 0.00186 | 0.001537 | `+20.99%` | `49.41` / `51.48` | `60.79` | `0.677` | `BULLISH_HAMMER` | 0.00177444 | `WATCH` | **HOLD** (93%) |
| `SOLUSDT` | 83.3 | 89.431736 | `-6.86%` | `40.36` / `38.47` | `39.25` | `0.34` | `BEARISH_ENGULFING` | 80.24428 | `WATCH` | **HOLD** (91%) |
| `XRPUSDT` | 1.0553 | 1.165357 | `-9.44%` | `43.83` / `43.29` | `37.41` | `0.258` | `BEARISH_ENGULFING` | 1.0198963 | `WATCH` | **HOLD** (92%) |
| `PEPEUSDT` | 5.36e-06 | 5e-06 | `+6.49%` | `38.56` / `32.9` | `56.36` | `0.698` | `MORNING_STAR` | 5.11e-06 | `WATCH` | **HOLD** (88%) |
| `GRAMUSDT` | 1.139 | 1.104018 | `+3.17%` | `79.51` / `78.21` | `66.47` | `0.941` | `BEARISH_SHOOTING_STAR` | 1.086606 | `WATCH` | **HOLD** (89%) |
