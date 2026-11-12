# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T21:05:13Z`
- **Ciclo de ejecucion:** `#265`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un régimen bajista generalizado con la mayoría de los activos cotizando por debajo de la EMA 200 en temporalidad 1H. No se cumplen las condiciones estoscásticas estrictas ni los patrones de giro requeridos para aperturas en los Pilares LONG (P1-P4). Para el Pilar SHORT (S1) en Futuros USDT-M, aunque varios activos se acercan a zonas de resistencia de la EMA 200, los filtros de sobrecompra en el estocástico (>=80) no están activos en este momento, ya que la mayoría se encuentra en zonas de sobreventa o rango medio bajo. No hay posiciones abiertas, por lo que se mantiene una postura de observación (HOLD) sin ejecuciones nuevas para proteger el capital.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71480.42 | 75050.685184 | `-4.76%` | `11.42` / `15.79` | `23.45` | `0.16` | `NONE` | 69621.92908 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `ZECUSDT` | 953.35 | 1135.019292 | `-16.01%` | `34.3` / `28.4` | `38.54` | `0.223` | `NONE` | 909.4959 | `WATCH` | HOLD |
| `SOLUSDT` | 81.33 | 87.045289 | `-6.57%` | `31.91` / `35.13` | `34.1` | `0.193` | `BEARISH_ENGULFING` | 79.21542 | `WATCH` | HOLD |
| `NBISBUSDT` | 129.22 | 140.734186 | `-8.18%` | `21.34` / `21.0` | `33.99` | `0.259` | `BULLISH_ENGULFING` | 123.27588 | `WATCH` | HOLD |
| `NEARUSDT` | 3.434 | 3.695361 | `-7.07%` | `47.13` / `42.24` | `38.79` | `0.372` | `BEARISH_SHOOTING_STAR` | 3.284546 | `WATCH` | HOLD |
| `UNIUSDT` | 6.049 | 6.767247 | `-10.61%` | `38.55` / `34.04` | `34.98` | `0.326` | `NONE` | 5.8328378 | `WATCH` | HOLD |
| `BNBUSDT` | 654.93 | 687.016226 | `-4.67%` | `20.12` / `20.23` | `27.2` | `0.245` | `NONE` | 637.90182 | `WATCH` | HOLD |
| `ENAUSDT` | 0.1403 | 0.156366 | `-10.27%` | `51.62` / `45.08` | `34.71` | `0.392` | `BULLISH_ENGULFING` | 0.13408234 | `WATCH` | HOLD |
| `XAUTUSDT` | 3871.58 | 4010.492919 | `-3.46%` | `21.04` / `21.53` | `26.1` | `0.218` | `BEARISH_ENGULFING` | 3770.91892 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.142 | 1.138071 | `+0.35%` | `10.64` / `12.27` | `37.72` | `0.1` | `BULLISH_HAMMER` | 1.089468 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 162.56 | 186.135915 | `-12.67%` | `27.46` / `25.85` | `34.97` | `0.278` | `BULLISH_ENGULFING` | 155.938416 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0823 | 0.077698 | `+5.92%` | `6.38` / `8.18` | `39.18` | `0.07` | `BULLISH_HAMMER` | 0.0785142 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AVAXUSDT` | 8.344 | 8.43795 | `-1.11%` | `21.24` / `21.64` | `40.46` | `0.261` | `NONE` | 8.0860688 | `WATCH` | HOLD |
| `INJUSDT` | 7.412 | 7.839128 | `-5.45%` | `46.63` / `42.15` | `40.98` | `0.382` | `BEARISH_SHOOTING_STAR` | 7.1455344 | `WATCH` | HOLD |
| `PAXGUSDT` | 3874.85 | 4015.174047 | `-3.49%` | `21.83` / `22.39` | `26.13` | `0.22` | `BEARISH_ENGULFING` | 3774.1039 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3158 | 0.31785 | `-0.64%` | `19.86` / `22.87` | `36.75` | `0.235` | `BEARISH_SHOOTING_STAR` | 0.3075892 | `EXIT_SHORT_STOCH_20` | HOLD |
