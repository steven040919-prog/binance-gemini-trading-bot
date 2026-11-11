# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T22:07:17Z`
- **Ciclo de ejecucion:** `#159`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de criptomonedas mantiene un sesgo bajista general en temporalidad 1H con la mayoría de los activos operando por debajo de la EMA 200. No se cumplen los requisitos estrictos de los Pilares Long (P1-P4) debido a que la tendencia principal sigue dominada por los vendedores y las condiciones de sobreventa extrema en el estocástico o divergencias no confluyen de forma perfecta con los patrones de vela requeridos para aperturas alcistas. Tampoco se activan entradas SHORT óptimas bajo el pilar S1 ya que los activos analizados no se encuentran testeando la resistencia dinámica de la EMA 200 en confluencia con sobrecompra en el estocástico. El portafolio permanece en modo HOLD evaluando oportunidades de pullback o gestión dinámica de posiciones si estuviesen abiertas.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.67e-06 | 5e-06 | `-7.50%` | `2.53` / `2.99` | `21.31` | `0.079` | `BEARISH_SHOOTING_STAR` | 4.47e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `OPGUSDT` | 0.1363 | 0.125709 | `+8.42%` | `25.07` / `32.02` | `49.4` | `0.454` | `BEARISH_ENGULFING` | 0.1300302 | `WATCH` | HOLD |
| `INJUSDT` | 7.852 | 7.95564 | `-1.30%` | `15.3` / `17.96` | `41.47` | `0.261` | `NONE` | 7.5607216 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1562 | 0.165378 | `-5.55%` | `6.17` / `14.45` | `35.74` | `0.042` | `NONE` | 0.15165764 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1494 | 0.160569 | `-6.96%` | `10.07` / `15.71` | `40.18` | `0.016` | `BEARISH_SHOOTING_STAR` | 0.14425824 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74462.01 | 75575.261302 | `-1.47%` | `79.5` / `79.81` | `56.11` | `0.81` | `BEARISH_ENGULFING` | 72525.99774 | `WATCH` | **HOLD** (75%) |
| `XAUTUSDT` | 3983.39 | 4031.862339 | `-1.20%` | `6.57` / `4.68` | `24.99` | `0.195` | `BULLISH_ENGULFING` | 3879.82186 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PAXGUSDT` | 3985.77 | 4037.448515 | `-1.28%` | `6.18` / `4.28` | `25.49` | `0.198` | `BULLISH_ENGULFING` | 3882.13998 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 1000.63 | 1176.220506 | `-14.93%` | `56.69` / `57.44` | `44.61` | `0.586` | `BULLISH_ENGULFING` | 954.60102 | `WATCH` | HOLD |
| `ETHUSDT` | 2071.32 | 2174.89974 | `-4.76%` | `51.11` / `56.16` | `49.84` | `0.585` | `BEARISH_SHOOTING_STAR` | 2017.46568 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001496 | 0.001553 | `-3.69%` | `8.85` / `6.68` | `35.15` | `0.238` | `BULLISH_HAMMER` | 0.00142718 | `EXIT_SHORT_STOCH_20` | HOLD |
| `MUBUSDT` | 813.08 | 755.27672 | `+7.65%` | `78.73` / `82.41` | `70.29` | `0.737` | `NONE` | 784.695448 | `EXIT_LONG_STOCH_80` | HOLD |
| `SNXXBUSDT` | 4.43 | 4.187505 | `+5.79%` | `71.45` / `77.41` | `65.78` | `0.7` | `BEARISH_SHOOTING_STAR` | 4.22622 | `WATCH` | HOLD |
| `SOXSBUSDT` | 45.91 | 59.357507 | `-22.66%` | `44.25` / `36.22` | `40.81` | `0.428` | `BULLISH_HAMMER` | 43.79814 | `WATCH` | HOLD |
| `SOLUSDT` | 84.58 | 88.310847 | `-4.22%` | `63.87` / `69.26` | `52.8` | `0.656` | `BEARISH_SHOOTING_STAR` | 82.38092 | `WATCH` | HOLD |
| `NEARUSDT` | 3.684 | 3.763885 | `-2.12%` | `49.74` / `55.2` | `50.08` | `0.449` | `NONE` | 3.5299552 | `WATCH` | HOLD |
