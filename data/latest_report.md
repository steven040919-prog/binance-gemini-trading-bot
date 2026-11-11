# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T00:01:05Z`
- **Ciclo de ejecucion:** `#55`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado opera bajo un régimen general bajista en temporalidad 1H con la mayoría de los activos cotizando por debajo de la EMA 200 y con baja volatilidad/volumen en este ciclo. No se activan entradas Long (Pilares P1-P4) ni Short (Pilar S1) debido a que ningún candidato cumple simultáneamente con las condiciones estrictas de sobreventa/sobrecompra extrema, giro del estocástico, volumen institucional y patrones de velas exigidos por el sistema autónomo. Tampoco existen posiciones abiertas con ganancia que requieran la acción de ajuste (ADJUST). Se mantiene la vigilancia en HOLD para proteger el capital.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1042.81 | 1221.879607 | `-14.66%` | `23.28` / `25.42` | `33.76` | `0.25` | `NONE` | 994.84074 | `WATCH` | HOLD |
| `UNIUSDT` | 6.664 | 7.012867 | `-4.97%` | `9.48` / `12.49` | `36.34` | `0.203` | `BULLISH_HAMMER` | 6.357456 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1606 | 0.166369 | `-3.47%` | `41.21` / `36.11` | `38.18` | `0.348` | `BULLISH_HAMMER` | 0.15366872 | `WATCH` | HOLD |
| `AAVEUSDT` | 123.51 | 129.655972 | `-4.74%` | `50.37` / `50.83` | `34.43` | `0.287` | `NONE` | 119.510594 | `WATCH` | HOLD |
| `QNTUSDT` | 181.52 | 194.44252 | `-6.65%` | `41.17` / `39.97` | `34.13` | `0.3` | `BULLISH_HAMMER` | 173.211152 | `WATCH` | HOLD |
| `ENAUSDT` | 0.1499 | 0.162843 | `-7.95%` | `29.72` / `29.07` | `44.36` | `0.331` | `BEARISH_ENGULFING` | 0.14336436 | `WATCH` | HOLD |
| `XAUTUSDT` | 4030.78 | 4035.527671 | `-0.12%` | `31.66` / `24.77` | `37.31` | `0.361` | `BEARISH_SHOOTING_STAR` | 3925.97972 | `WATCH` | HOLD |
| `BTCUSDT` | 73748.0 | 75912.22736 | `-2.85%` | `48.1` / `48.47` | `44.5` | `0.389` | `NONE` | 71830.552 | `WATCH` | **HOLD** (75%) |
| `TRXUSDT` | 0.3177 | 0.319057 | `-0.43%` | `11.11` / `13.7` | `41.92` | `0.191` | `NONE` | 0.3094398 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2051.53 | 2199.254174 | `-6.72%` | `42.57` / `42.68` | `39.1` | `0.344` | `NONE` | 1989.840526 | `WATCH` | HOLD |
| `INITUSDT` | 0.27348 | 0.163976 | `+66.78%` | `58.41` / `60.52` | `58.79` | `0.611` | `NONE` | 0.26089992 | `WATCH` | HOLD |
| `PAXGUSDT` | 4033.17 | 4041.737514 | `-0.21%` | `31.92` / `24.64` | `37.0` | `0.356` | `MORNING_STAR` | 3928.30758 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001843 | 0.00154 | `+19.68%` | `50.38` / `49.97` | `59.23` | `0.635` | `NONE` | 0.00175822 | `WATCH` | HOLD |
| `SOLUSDT` | 83.33 | 89.387855 | `-6.78%` | `43.91` / `40.91` | `39.62` | `0.364` | `BULLISH_ENGULFING` | 80.426754 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0562 | 1.16452 | `-9.30%` | `44.82` / `44.04` | `37.8` | `0.291` | `BULLISH_HAMMER` | 1.02177136 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.38e-06 | 5e-06 | `+6.77%` | `47.71` / `39.65` | `57.37` | `0.74` | `NONE` | 5.13e-06 | `WATCH` | HOLD |
