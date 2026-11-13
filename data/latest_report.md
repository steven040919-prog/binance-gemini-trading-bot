# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T01:55:40Z`
- **Ciclo de ejecucion:** `#287`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un regimen bajista generalizado con la mayoria de los activos cotizando por debajo de sus respectivas EMA 200 en temporalidad 1H. Destaca GRAMUSDT cumpliendo con los requisitos del Pilar 1 LONG (PULLBACK DE VALOR SOBRE EMA 200), mostrando divergencia y patron alcista, por lo que se emite orden de COMPRA. No hay posiciones abiertas actuales para ajustar, por lo que el sistema opera con cautela priorizando la gestion de riesgo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 70880.95 | 74879.597825 | `-5.34%` | `12.4` / `11.84` | `20.32` | `0.132` | `BEARISH_ENGULFING` | 69038.0453 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 952.02 | 1128.681743 | `-15.65%` | `41.91` / `35.99` | `41.41` | `0.298` | `BULLISH_HAMMER` | 908.22708 | `WATCH` | HOLD |
| `SOLUSDT` | 81.28 | 86.786146 | `-6.34%` | `39.67` / `37.94` | `35.96` | `0.246` | `BULLISH_HAMMER` | 79.16672 | `WATCH` | HOLD |
| `NBISBUSDT` | 131.23 | 140.323348 | `-6.48%` | `26.03` / `24.69` | `38.48` | `0.381` | `NONE` | 125.19342 | `WATCH` | HOLD |
| `BNBUSDT` | 653.47 | 685.494595 | `-4.67%` | `27.15` / `24.54` | `29.21` | `0.275` | `BULLISH_HAMMER` | 636.47978 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0822 | 0.077761 | `+5.71%` | `6.72` / `3.75` | `41.4` | `0.232` | `NONE` | 0.0784188 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.02 | 6.734349 | `-10.61%` | `51.36` / `45.23` | `36.37` | `0.289` | `BULLISH_HAMMER` | 5.84046 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.152 | 1.13782 | `+1.25%` | `16.86` / `14.6` | `41.32` | `0.255` | `BULLISH_ENGULFING` | 1.099008 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `SOXSBUSDT` | 43.79 | 56.241062 | `-22.14%` | `8.85` / `15.19` | `35.36` | `0.108` | `BEARISH_ENGULFING` | 41.77566 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRXUSDT` | 0.3155 | 0.317759 | `-0.71%` | `13.83` / `14.97` | `34.15` | `0.202` | `BEARISH_SHOOTING_STAR` | 0.307297 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2010.27 | 2141.646685 | `-6.13%` | `50.86` / `48.46` | `35.05` | `0.289` | `NONE` | 1958.00298 | `WATCH` | HOLD |
| `NEARUSDT` | 3.438 | 3.672546 | `-6.39%` | `59.74` / `48.27` | `42.61` | `0.509` | `BULLISH_HAMMER` | 3.2831724 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0302 | 1.119283 | `-7.96%` | `55.36` / `54.29` | `39.67` | `0.289` | `NONE` | 1.0034148 | `WATCH` | HOLD |
| `XAUTUSDT` | 3905.5 | 4006.584787 | `-2.52%` | `40.58` / `32.55` | `44.91` | `0.53` | `NONE` | 3803.957 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.55e-06 | 5e-06 | `-7.14%` | `90.8` / `87.74` | `49.82` | `0.855` | `NONE` | 4.34e-06 | `EXIT_LONG_STOCH_80` | HOLD |
| `DOGEUSDT` | 0.06633 | 0.069985 | `-5.22%` | `73.09` / `67.36` | `44.97` | `0.517` | `BULLISH_HAMMER` | 0.06458707 | `WATCH` | HOLD |
