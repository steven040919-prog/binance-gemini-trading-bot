# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T00:50:04Z`
- **Ciclo de ejecucion:** `#75`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de criptomonedas se encuentra en un régimen bajista generalizado en temporalidad 1H, con la mayoría de los activos cotizando por debajo de sus respectivas EMA 200. No se cumplen los requisitos estrictos de los Pilares Long (P1-P4) debido a la ausencia de capitulaciones extremas simultáneas o soportes institucionales clave validados, y tampoco se activan operaciones Short bajo S1 ya que ningún activo cumple con el rechazo técnico exacto sobre la EMA 200 en este ciclo. Por lo tanto, el bot se mantiene en modo HOLD con gestión defensiva y liquidez protegida.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1040.18 | 1221.853438 | `-14.87%` | `22.85` / `25.27` | `33.34` | `0.24` | `NONE` | 992.33172 | `WATCH` | HOLD |
| `UNIUSDT` | 6.707 | 7.013295 | `-4.37%` | `12.09` / `13.36` | `40.0` | `0.262` | `BULLISH_HAMMER` | 6.398478 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.161 | 0.166373 | `-3.23%` | `42.42` / `36.52` | `39.34` | `0.37` | `NONE` | 0.153594 | `WATCH` | HOLD |
| `AAVEUSDT` | 123.94 | 129.66025 | `-4.41%` | `52.85` / `51.66` | `37.44` | `0.36` | `NONE` | 119.398284 | `WATCH` | HOLD |
| `QNTUSDT` | 181.6 | 194.443316 | `-6.61%` | `41.39` / `40.04` | `34.29` | `0.304` | `BULLISH_HAMMER` | 173.2464 | `WATCH` | HOLD |
| `XAUTUSDT` | 4026.07 | 4035.480806 | `-0.23%` | `29.31` / `23.99` | `35.45` | `0.328` | `NONE` | 3921.39218 | `WATCH` | HOLD |
| `BTCUSDT` | 73575.96 | 75910.51552 | `-3.08%` | `45.39` / `47.56` | `42.4` | `0.319` | `BEARISH_ENGULFING` | 71662.98504 | `WATCH` | **HOLD** (75%) |
| `ETHUSDT` | 2052.46 | 2199.263428 | `-6.68%` | `42.87` / `42.78` | `39.37` | `0.35` | `BEARISH_SHOOTING_STAR` | 1988.995548 | `WATCH` | HOLD |
| `INITUSDT` | 0.25914 | 0.163833 | `+58.17%` | `55.01` / `59.39` | `54.54` | `0.523` | `BEARISH_ENGULFING` | 0.24721956 | `WATCH` | HOLD |
| `PAXGUSDT` | 4027.92 | 4041.685275 | `-0.34%` | `29.13` / `23.71` | `35.0` | `0.319` | `MORNING_STAR` | 3923.19408 | `WATCH` | HOLD |
| `ONEUSDT` | 0.00181 | 0.00154 | `+17.56%` | `46.35` / `48.63` | `56.25` | `0.575` | `BEARISH_SHOOTING_STAR` | 0.00172674 | `WATCH` | HOLD |
| `SOLUSDT` | 83.28 | 89.387357 | `-6.83%` | `43.48` / `40.76` | `39.26` | `0.355` | `BULLISH_ENGULFING` | 80.378096 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0537 | 1.164496 | `-9.51%` | `43.28` / `43.53` | `36.64` | `0.259` | `BULLISH_HAMMER` | 1.02078566 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.42e-06 | 5e-06 | `+7.55%` | `50.33` / `40.52` | `59.4` | `0.86` | `NONE` | 5.17e-06 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.13 | 1.104445 | `+2.31%` | `70.83` / `76.6` | `61.77` | `0.79` | `BEARISH_SHOOTING_STAR` | 1.07802 | `WATCH` | HOLD |
| `BNBUSDT` | 680.28 | 693.980442 | `-1.97%` | `45.02` / `40.25` | `45.25` | `0.401` | `BEARISH_SHOOTING_STAR` | 662.59272 | `WATCH` | HOLD |
