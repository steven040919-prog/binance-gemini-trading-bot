# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T02:34:34Z`
- **Ciclo de ejecucion:** `#291`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un regimen bajista generalizado en temporalidad de 1H con la mayoria de los activos cotizando por debajo de la EMA 200 y con RSI deprimidos. Se identifica un unico candidato optimo para entrada LONG segun los pilares institucionales: ERAUSDT activa el Pilar 1 (P1_EMA200_PULLBACK) al encontrarse sobre la EMA 200 con pendiente positiva, confluencia con patron MORNING_STAR y estocastico girando al alza. No hay posiciones abiertas actuales para ajustar.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 70391.67 | 74831.573872 | `-5.93%` | `9.39` / `11.59` | `16.95` | `0.053` | `NONE` | 68561.48658 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 1997.36 | 2140.148773 | `-6.67%` | `44.95` / `47.83` | `29.23` | `0.112` | `BEARISH_ENGULFING` | 1945.42864 | `WATCH` | HOLD |
| `SOLUSDT` | 80.64 | 86.713205 | `-7.00%` | `29.08` / `35.99` | `30.19` | `0.064` | `NONE` | 78.54336 | `WATCH` | HOLD |
| `NBISBUSDT` | 130.19 | 140.239101 | `-7.17%` | `37.13` / `29.23` | `37.09` | `0.375` | `BEARISH_ENGULFING` | 124.20126 | `WATCH` | HOLD |
| `BNBUSDT` | 647.93 | 685.081809 | `-5.42%` | `22.02` / `25.38` | `23.59` | `0.122` | `NONE` | 631.08382 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0249 | 1.118353 | `-8.36%` | `47.13` / `53.13` | `35.71` | `0.149` | `NONE` | 0.9982526 | `WATCH` | HOLD |
| `UNIUSDT` | 5.923 | 6.72872 | `-11.97%` | `42.99` / `49.26` | `29.66` | `-0.041` | `BULLISH_HAMMER` | 5.7414176 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0825 | 0.077785 | `+6.06%` | `11.67` / `7.45` | `42.16` | `0.265` | `MORNING_STAR` | 0.078705 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `GRAMUSDT` | 1.146 | 1.137901 | `+0.71%` | `18.41` / `16.54` | `39.97` | `0.24` | `BEARISH_SHOOTING_STAR` | 1.093284 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1392 | 0.155178 | `-10.30%` | `62.27` / `63.88` | `32.94` | `0.226` | `BULLISH_HAMMER` | 0.13437344 | `WATCH` | HOLD |
| `AVAXUSDT` | 8.276 | 8.428634 | `-1.81%` | `37.31` / `34.5` | `38.37` | `0.22` | `BULLISH_ENGULFING` | 8.060824 | `WATCH` | HOLD |
| `AAVEUSDT` | 113.23 | 125.360159 | `-9.68%` | `69.72` / `66.1` | `34.1` | `0.334` | `BEARISH_ENGULFING` | 110.28602 | `WATCH` | HOLD |
| `SOXSBUSDT` | 44.39 | 56.138791 | `-20.93%` | `9.66` / `11.41` | `39.61` | `0.225` | `BEARISH_ENGULFING` | 42.34806 | `EXIT_SHORT_STOCH_20` | HOLD |
| `WLDUSDT` | 0.2987 | 0.327056 | `-8.67%` | `42.94` / `46.43` | `37.33` | `0.118` | `BULLISH_HAMMER` | 0.28799874 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3154 | 0.317848 | `-0.77%` | `10.54` / `13.97` | `33.88` | `0.176` | `BEARISH_SHOOTING_STAR` | 0.3071996 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001505 | 0.001551 | `-2.98%` | `7.37` / `5.9` | `41.04` | `0.136` | `NONE` | 0.00143577 | `EXIT_SHORT_STOCH_20` | HOLD |
