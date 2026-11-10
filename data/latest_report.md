# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-10T22:13:26Z`
- **Ciclo de ejecucion:** `#17`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general presenta una estructura predominantemente bajista con las principales criptomonedas (BTC, ETH, SOL, BNB) cotizando por debajo de sus respectivas EMA 200 con pendientes negativas. Evaluando los activos frente a los 4 Pilares LONG y el Pilar S1 SHORT de Futuros, ninguno cumple con la confluencia estricta exigida: activos en sobreventa como XAUT y PAXG no alcanzan la compresion requerida en Bollinger Bands (%B <= 0.12), mientras que las velas de rechazo bajista como BTC y ETH carecen de sobrecompra en Estocastico (>= 80) y RSI (>= 62) para validar el pilar S1. No habiendo posiciones abiertas que requieran gestion dinamica de trailing/break-even, se preserva el 100% de la liquidez en USDT en modo HOLD.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `UNIUSDT` | 6.761 | 7.023286 | `-3.73%` | `20.92` / `18.45` | `41.85` | `0.278` | `BULLISH_ENGULFING` | 6.449994 | `EXIT_SHORT_STOCH_20` | **HOLD** (68%) |
| `ARBUSDT` | 0.1607 | 0.166478 | `-3.47%` | `29.06` / `25.07` | `37.79` | `0.317` | `BULLISH_ENGULFING` | 0.1533078 | `WATCH` | **HOLD** (65%) |
| `XAUTUSDT` | 4024.33 | 4035.678935 | `-0.28%` | `17.57` / `15.99` | `32.98` | `0.278` | `BULLISH_HAMMER` | 3919.69742 | `EXIT_SHORT_STOCH_20` | **HOLD** (70%) |
| `BTCUSDT` | 73917.53 | 75950.2042 | `-2.68%` | `51.52` / `44.29` | `46.38` | `0.423` | `BEARISH_SHOOTING_STAR` | 71995.67422 | `WATCH` | **HOLD** (75%) |
| `ZECUSDT` | 1061.65 | 1226.169333 | `-13.42%` | `30.79` / `26.61` | `36.02` | `0.269` | `NONE` | 1012.8141 | `WATCH` | HOLD |
| `ETHUSDT` | 2058.63 | 2202.113346 | `-6.52%` | `45.61` / `40.79` | `40.51` | `0.351` | `BEARISH_SHOOTING_STAR` | 1982.881812 | `WATCH` | **HOLD** (72%) |
| `PAXGUSDT` | 4027.28 | 4041.900674 | `-0.36%` | `17.19` / `16.06` | `32.89` | `0.277` | `BULLISH_ENGULFING` | 3922.57072 | `EXIT_SHORT_STOCH_20` | **HOLD** (71%) |
| `INITUSDT` | 0.27305 | 0.162071 | `+68.48%` | `63.27` / `71.2` | `58.91` | `0.645` | `NONE` | 0.2604897 | `WATCH` | **HOLD** (80%) |
| `ONEUSDT` | 0.001876 | 0.001536 | `+22.17%` | `51.59` / `54.36` | `62.1` | `0.717` | `BULLISH_ENGULFING` | 0.0017897 | `WATCH` | HOLD |
| `SOLUSDT` | 83.41 | 89.534997 | `-6.84%` | `41.63` / `37.37` | `38.45` | `0.333` | `BEARISH_SHOOTING_STAR` | 80.36452 | `WATCH` | **HOLD** (70%) |
| `XRPUSDT` | 1.0629 | 1.166946 | `-8.92%` | `45.49` / `44.95` | `41.23` | `0.334` | `BEARISH_SHOOTING_STAR` | 1.0269759 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.29e-06 | 5e-06 | `+5.05%` | `30.72` / `31.16` | `52.44` | `0.485` | `BULLISH_ENGULFING` | 5.05e-06 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.156 | 1.103545 | `+4.75%` | `85.88` / `79.21` | `74.58` | `1.155` | `MORNING_STAR` | 1.102824 | `EXIT_LONG_STOCH_80` | **HOLD** (75%) |
| `RLUSDUSDT` | 1.001 | 1.001212 | `-0.02%` | `47.62` / `44.25` | `46.01` | `0.329` | `BEARISH_SHOOTING_STAR` | 0.974974 | `WATCH` | HOLD |
| `NEARUSDT` | 3.607 | 3.776356 | `-4.48%` | `39.12` / `36.81` | `50.89` | `0.521` | `BULLISH_ENGULFING` | 3.441078 | `WATCH` | HOLD |
| `BNBUSDT` | 679.06 | 694.316083 | `-2.20%` | `36.05` / `30.4` | `42.71` | `0.325` | `NONE` | 661.40444 | `WATCH` | **HOLD** (68%) |
