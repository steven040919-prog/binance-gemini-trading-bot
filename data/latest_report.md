# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T15:56:29Z`
- **Ciclo de ejecucion:** `#343`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un regimen bajista generalizado con la mayoria de los activos cotizando por debajo de sus respectivas EMA 200 y pendientes negativas. Se identifica una oportunidad bajo el Pilar S1 SHORT en ZECUSDT debido al rechazo bajista en la zona de resistencia y formacion envolvente. No hay posiciones abiertas actualmente, por lo que se prioriza la ejecucion de cortos en activos seleccionados cumpliendo los filtros institucionales y manteniendo estricta gestion de riesgo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68731.92 | 74018.836312 | `-7.14%` | `41.36` / `43.41` | `32.23` | `0.28` | `BEARISH_ENGULFING` | 66439.687536 | `WATCH` | HOLD |
| `ETHUSDT` | 1930.78 | 2113.292453 | `-8.64%` | `44.21` / `49.38` | `33.3` | `0.254` | `BEARISH_ENGULFING` | 1856.00738 | `WATCH` | HOLD |
| `BNBUSDT` | 633.05 | 678.139348 | `-6.65%` | `46.61` / `50.23` | `35.12` | `0.278` | `BEARISH_ENGULFING` | 612.61053 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.122 | 1.137151 | `-1.33%` | `25.71` / `40.67` | `36.38` | `-0.112` | `NONE` | 1.0731788 | `WATCH` | HOLD |
| `XAUTUSDT` | 3864.62 | 3993.431089 | `-3.23%` | `19.68` / `20.76` | `34.61` | `0.057` | `BULLISH_ENGULFING` | 3764.13988 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INTCBUSDT` | 57.6 | 59.278197 | `-2.83%` | `13.97` / `23.39` | `28.12` | `-0.294` | `BEARISH_ENGULFING` | 55.13768 | `EXIT_SHORT_STOCH_20` | HOLD |
| `MUBUSDT` | 760.59 | 762.721109 | `-0.28%` | `9.94` / `17.74` | `32.65` | `-0.183` | `BEARISH_ENGULFING` | 730.099002 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PAXGUSDT` | 3865.36 | 3997.329311 | `-3.30%` | `17.81` / `16.93` | `33.75` | `0.053` | `BULLISH_ENGULFING` | 3764.86064 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 79.79 | 85.690284 | `-6.89%` | `62.48` / `69.57` | `41.21` | `0.351` | `NONE` | 76.574174 | `WATCH` | HOLD |
| `SOXSBUSDT` | 53.83 | 55.728946 | `-3.41%` | `88.89` / `79.27` | `72.87` | `1.29` | `NONE` | 51.35382 | `EXIT_LONG_STOCH_80` | HOLD |
| `ZECUSDT` | 944.07 | 1095.363473 | `-13.81%` | `67.75` / `76.87` | `45.92` | `0.469` | `BEARISH_ENGULFING` | 987.49722 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `ERAUSDT` | 0.0751 | 0.077848 | `-3.53%` | `20.15` / `20.61` | `34.17` | `-0.032` | `NONE` | 0.0716454 | `WATCH` | HOLD |
| `NEARUSDT` | 3.496 | 3.629178 | `-3.67%` | `74.78` / `82.29` | `51.12` | `0.623` | `NONE` | 3.335184 | `EXIT_LONG_STOCH_80` | HOLD |
| `XRPUSDT` | 1.0184 | 1.106248 | `-7.94%` | `66.85` / `64.9` | `42.43` | `0.308` | `BEARISH_ENGULFING` | 0.9803848 | `WATCH` | HOLD |
| `INJUSDT` | 8.193 | 7.783431 | `+5.26%` | `91.35` / `91.83` | `76.27` | `1.016` | `BULLISH_ENGULFING` | 7.816122 | `EXIT_LONG_STOCH_80` | HOLD |
| `PEPEUSDT` | 4.5e-06 | 5e-06 | `-7.07%` | `38.27` / `41.15` | `45.69` | `0.264` | `BEARISH_ENGULFING` | 4.29e-06 | `WATCH` | HOLD |
