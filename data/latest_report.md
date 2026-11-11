# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T09:01:03Z`
- **Ciclo de ejecucion:** `#122`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado muestra un sesgo bajista generalizado en temporalidad de 1H con la mayoría de los activos cotizando por debajo de la EMA 200. Ningún activo satisface de manera rigurosa las reglas cuantitativas de entrada para los Pilares LONG (P1-P4) o SHORT (S1). Aunque INITUSDT presenta la etiqueta de setup LONG, viola los parámetros del Pilar 1 al estar sobreextendido a un +45.7% de la EMA 200 y con RSI superior a 36. Se preserva el capital intacto en USDT (100% liquidez).

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 970.74 | 1204.268803 | `-19.39%` | `14.98` / `17.46` | `28.62` | `0.156` | `BEARISH_ENGULFING` | 926.08596 | `EXIT_SHORT_STOCH_20` | **HOLD** (60%) |
| `ONEUSDT` | 0.001601 | 0.001556 | `+2.90%` | `8.78` / `12.12` | `40.59` | `0.023` | `BEARISH_SHOOTING_STAR` | 0.00152735 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
| `UNIUSDT` | 6.394 | 6.979469 | `-8.39%` | `10.48` / `11.9` | `26.41` | `0.043` | `BEARISH_ENGULFING` | 6.1612768 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PEPEUSDT` | 5.06e-06 | 5e-06 | `-0.19%` | `11.58` / `19.47` | `36.66` | `-0.018` | `NONE` | 4.83e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1594 | 0.166122 | `-4.05%` | `19.76` / `24.87` | `39.03` | `0.342` | `NONE` | 0.15255424 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 177.7 | 193.52027 | `-8.17%` | `17.09` / `27.62` | `31.65` | `0.027` | `BEARISH_ENGULFING` | 173.00736 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73752.01 | 75737.004315 | `-2.62%` | `69.05` / `75.36` | `46.92` | `0.571` | `NONE` | 71834.45774 | `WATCH` | **HOLD** (55%) |
| `TRXUSDT` | 0.3175 | 0.318298 | `-0.25%` | `17.95` / `22.63` | `41.47` | `0.294` | `NONE` | 0.309245 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2059.94 | 2187.646583 | `-5.84%` | `70.22` / `76.67` | `45.11` | `0.609` | `NONE` | 2006.38156 | `WATCH` | **HOLD** (55%) |
| `INITUSDT` | 0.2504 | 0.171855 | `+45.70%` | `25.69` / `21.77` | `49.59` | `0.264` | `BULLISH_ENGULFING` | 0.2388816 | `P1_EMA200_PULLBACK` | **HOLD** (35%) |
| `CYBERUSDT` | 0.264 | 0.281361 | `-6.17%` | `3.61` / `4.12` | `41.66` | `0.19` | `BEARISH_ENGULFING` | 0.251856 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 83.05 | 88.829908 | `-6.51%` | `48.21` / `50.87` | `43.1` | `0.499` | `NONE` | 80.86154 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0577 | 1.155382 | `-8.45%` | `45.42` / `46.05` | `43.5` | `0.518` | `NONE` | 1.0301998 | `WATCH` | HOLD |
| `NEARUSDT` | 3.597 | 3.770604 | `-4.60%` | `39.73` / `48.64` | `47.58` | `0.448` | `BEARISH_ENGULFING` | 3.454702 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0011 | 1.001203 | `-0.01%` | `46.67` / `51.75` | `47.83` | `0.519` | `BULLISH_HAMMER` | 0.9750714 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0824 | 0.073269 | `+12.46%` | `33.12` / `53.24` | `54.34` | `0.576` | `BULLISH_HAMMER` | 0.0786096 | `WATCH` | HOLD |
