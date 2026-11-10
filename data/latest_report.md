# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-10T23:35:15Z`
- **Ciclo de ejecucion:** `#46`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen general bajista con la gran mayoría de los activos cotizando por debajo de la EMA 200 y con tendencia primaria BEARISH. No se cumplen las condiciones estrictas de los Pilares LONG (P1-P4) ni del Pilar SHORT (S1) de Futuros USDT-M debido a que los estocásticos, las distancias a la EMA 200 y los patrones de velas no coinciden simultáneamente con los umbrales institucionales requeridos (por ejemplo, rechazos en resistencia o sobreventas extremas con volumen). No hay posiciones abiertas con ganancia que requieran ajuste dinámico (ADJUST). Se mantiene la postura de espera (HOLD) para proteger el capital.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1043.54 | 1223.560246 | `-14.71%` | `25.7` / `26.33` | `33.69` | `0.228` | `BEARISH_ENGULFING` | 995.53716 | `WATCH` | HOLD |
| `UNIUSDT` | 6.663 | 7.014943 | `-5.02%` | `13.01` / `15.27` | `36.01` | `0.171` | `BEARISH_ENGULFING` | 6.356502 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1609 | 0.166354 | `-3.28%` | `37.19` / `30.65` | `38.76` | `0.344` | `MORNING_STAR` | 0.1534986 | `WATCH` | HOLD |
| `QNTUSDT` | 180.8 | 194.457817 | `-7.02%` | `37.02` / `37.62` | `32.57` | `0.243` | `NONE` | 172.84032 | `WATCH` | HOLD |
| `AAVEUSDT` | 123.95 | 129.637554 | `-4.39%` | `54.66` / `49.12` | `36.37` | `0.339` | `BEARISH_SHOOTING_STAR` | 119.2136 | `WATCH` | HOLD |
| `XAUTUSDT` | 4028.75 | 4035.484265 | `-0.17%` | `23.78` / `19.22` | `35.98` | `0.328` | `BULLISH_HAMMER` | 3924.0025 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73685.79 | 75927.139265 | `-2.95%` | `47.59` / `46.43` | `43.46` | `0.348` | `BEARISH_ENGULFING` | 71769.95946 | `WATCH` | **HOLD** (75%) |
| `TRXUSDT` | 0.3177 | 0.319092 | `-0.44%` | `13.33` / `14.07` | `42.0` | `0.195` | `NONE` | 0.3094398 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2049.61 | 2200.480214 | `-6.86%` | `41.71` / `41.71` | `38.06` | `0.312` | `NONE` | 1987.020608 | `WATCH` | HOLD |
| `PAXGUSDT` | 4031.97 | 4041.789006 | `-0.24%` | `23.43` / `19.06` | `36.07` | `0.329` | `BULLISH_ENGULFING` | 3927.13878 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001844 | 0.001537 | `+19.96%` | `48.19` / `51.08` | `59.34` | `0.653` | `NONE` | 0.00175918 | `WATCH` | HOLD |
| `SOLUSDT` | 83.11 | 89.429846 | `-7.07%` | `38.91` / `37.98` | `37.18` | `0.309` | `BEARISH_ENGULFING` | 80.28292 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0561 | 1.165365 | `-9.38%` | `44.28` / `43.44` | `37.76` | `0.268` | `BEARISH_ENGULFING` | 1.0198731 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.32e-06 | 5e-06 | `+5.71%` | `35.95` / `32.03` | `54.18` | `0.562` | `MORNING_STAR` | 5.08e-06 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.141 | 1.104038 | `+3.35%` | `80.27` / `78.47` | `66.95` | `0.961` | `BEARISH_SHOOTING_STAR` | 1.088514 | `EXIT_LONG_STOCH_80` | HOLD |
| `NEARUSDT` | 3.561 | 3.773171 | `-5.62%` | `33.56` / `34.13` | `46.64` | `0.314` | `BEARISH_ENGULFING` | 3.397194 | `WATCH` | HOLD |
