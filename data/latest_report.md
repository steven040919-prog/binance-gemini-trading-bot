# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-10T22:28:36Z`
- **Ciclo de ejecucion:** `#21`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de criptomonedas opera mayoritariamente bajo un régimen bajista de temporalidad 1h, con la gran mayoría de los activos cotizando por debajo de la EMA 200 y experimentando correcciones. Los filtros actuales no activan entradas LONG de alta confluencia bajo los Pilares P1-P4 ni entradas SHORT de rechazo en EMA 200 (S1), dado que no se alcanzan las condiciones extremas simultáneas de sobreventa/sobrecompra o proximidad a resistencia requeridas. No hay posiciones abiertas que requieran ajuste dinámico, por lo que el sistema se mantiene en modo de espera prudente.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `UNIUSDT` | 6.694 | 7.022619 | `-4.68%` | `16.85` / `17.09` | `37.21` | `0.176` | `BULLISH_ENGULFING` | 6.4012236 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1604 | 0.166475 | `-3.65%` | `28.34` / `24.83` | `36.87` | `0.303` | `BULLISH_ENGULFING` | 0.1530216 | `WATCH` | HOLD |
| `QNTUSDT` | 181.63 | 194.638691 | `-6.68%` | `39.34` / `37.03` | `34.12` | `0.265` | `NONE` | 173.61643 | `WATCH` | HOLD |
| `AAVEUSDT` | 124.29 | 129.722962 | `-4.19%` | `50.4` / `43.8` | `37.91` | `0.374` | `BULLISH_ENGULFING` | 119.027862 | `WATCH` | HOLD |
| `XAUTUSDT` | 4025.66 | 4035.692169 | `-0.25%` | `18.03` / `16.14` | `33.86` | `0.287` | `BULLISH_HAMMER` | 3920.99284 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 1052.96 | 1226.082865 | `-14.12%` | `29.38` / `26.14` | `34.27` | `0.234` | `NONE` | 1004.52384 | `WATCH` | HOLD |
| `BTCUSDT` | 73694.54 | 75947.985394 | `-2.97%` | `48.01` / `43.12` | `43.56` | `0.334` | `BEARISH_SHOOTING_STAR` | 71778.48196 | `WATCH` | **HOLD** (75%) |
| `ETHUSDT` | 2052.66 | 2202.053943 | `-6.78%` | `43.84` / `40.2` | `38.62` | `0.311` | `BEARISH_SHOOTING_STAR` | 1982.22552 | `WATCH` | HOLD |
| `PAXGUSDT` | 4028.46 | 4041.912415 | `-0.33%` | `17.6` / `16.19` | `33.68` | `0.285` | `BULLISH_ENGULFING` | 3923.72004 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INITUSDT` | 0.23477 | 0.16169 | `+45.20%` | `54.18` / `68.17` | `49.76` | `0.429` | `NONE` | 0.22397058 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001891 | 0.001536 | `+23.13%` | `52.73` / `54.74` | `62.9` | `0.737` | `BULLISH_ENGULFING` | 0.00180401 | `WATCH` | HOLD |
| `SOLUSDT` | 83.22 | 89.533106 | `-7.05%` | `40.25` / `36.91` | `36.87` | `0.303` | `BEARISH_SHOOTING_STAR` | 80.353196 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0621 | 1.166938 | `-8.98%` | `45.04` / `44.8` | `40.7` | `0.324` | `BEARISH_SHOOTING_STAR` | 1.02678668 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.28e-06 | 5e-06 | `+4.85%` | `30.07` / `30.94` | `51.87` | `0.453` | `BULLISH_ENGULFING` | 5.04e-06 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.146 | 1.103446 | `+3.86%` | `81.73` / `77.83` | `69.99` | `1.073` | `MORNING_STAR` | 1.093284 | `EXIT_LONG_STOCH_80` | HOLD |
| `NEARUSDT` | 3.576 | 3.776047 | `-5.30%` | `35.6` / `35.64` | `47.86` | `0.37` | `BULLISH_ENGULFING` | 3.411504 | `WATCH` | HOLD |
