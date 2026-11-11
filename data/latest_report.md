# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T00:50:36Z`
- **Ciclo de ejecucion:** `#76`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global en la temporalidad de 1H permanece bajo presión bajista generalizada con la mayoría de los activos cotizando por debajo de sus respectivas EMA 200 y con regímenes de tendencia primaria BEARISH. No se han activado setups de entrada limpios bajo los Pilares LONG (P1-P4) ni el Pilar SHORT (S1) debido a que no coinciden simultáneamente los filtros estrictos de osciladores, pendientes y formaciones de velas exigidos por el motor cuantitativo institucional. Tampoco existen posiciones abiertas con ganancias (`open_positions_count: 0`), por lo que no se requieren ajustes dinámicos de Stop-Loss o Take-Profit mediante la acción ADJUST. Se mantiene la vigilancia en modo HOLD a la espera de un punto óptimo de entrada.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1038.11 | 1221.832841 | `-15.04%` | `22.52` / `25.16` | `33.02` | `0.232` | `BEARISH_ENGULFING` | 990.35694 | `WATCH` | HOLD |
| `UNIUSDT` | 6.697 | 7.013195 | `-4.51%` | `11.48` / `13.15` | `39.12` | `0.248` | `BULLISH_HAMMER` | 6.388938 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1609 | 0.166372 | `-3.29%` | `42.12` / `36.42` | `39.03` | `0.364` | `NONE` | 0.15352836 | `WATCH` | HOLD |
| `AAVEUSDT` | 123.82 | 129.659056 | `-4.50%` | `52.16` / `51.43` | `36.49` | `0.339` | `BEARISH_SHOOTING_STAR` | 119.402052 | `WATCH` | HOLD |
| `QNTUSDT` | 181.56 | 194.442918 | `-6.63%` | `41.28` / `40.0` | `34.21` | `0.302` | `BULLISH_HAMMER` | 173.20824 | `WATCH` | HOLD |
| `XAUTUSDT` | 4026.07 | 4035.480806 | `-0.23%` | `29.31` / `23.99` | `35.45` | `0.328` | `NONE` | 3921.39218 | `WATCH` | HOLD |
| `BTCUSDT` | 73566.0 | 75910.416415 | `-3.09%` | `45.23` / `47.51` | `42.28` | `0.315` | `BEARISH_ENGULFING` | 71653.284 | `WATCH` | **HOLD** (50%) |
| `ETHUSDT` | 2052.01 | 2199.25895 | `-6.70%` | `42.72` / `42.73` | `39.24` | `0.347` | `BEARISH_SHOOTING_STAR` | 1989.007338 | `WATCH` | HOLD |
| `INITUSDT` | 0.25966 | 0.163838 | `+58.49%` | `55.13` / `59.43` | `54.68` | `0.526` | `BEARISH_ENGULFING` | 0.24771564 | `WATCH` | HOLD |
| `PAXGUSDT` | 4027.75 | 4041.683583 | `-0.34%` | `29.04` / `23.68` | `34.94` | `0.318` | `MORNING_STAR` | 3923.0285 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001825 | 0.00154 | `+18.53%` | `48.18` / `49.24` | `57.57` | `0.602` | `NONE` | 0.00174105 | `WATCH` | HOLD |
| `SOLUSDT` | 83.26 | 89.387158 | `-6.85%` | `43.31` / `40.71` | `39.12` | `0.351` | `BULLISH_ENGULFING` | 80.378632 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0533 | 1.164492 | `-9.55%` | `43.03` / `43.45` | `36.46` | `0.253` | `BULLISH_HAMMER` | 1.02079694 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.42e-06 | 5e-06 | `+7.55%` | `50.33` / `40.52` | `59.4` | `0.86` | `NONE` | 5.17e-06 | `WATCH` | HOLD |
| `BNBUSDT` | 680.15 | 693.979149 | `-1.99%` | `44.81` / `40.18` | `45.04` | `0.397` | `BEARISH_SHOOTING_STAR` | 662.4661 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.128 | 1.104425 | `+2.13%` | `70.08` / `76.35` | `60.91` | `0.767` | `BEARISH_SHOOTING_STAR` | 1.0770144 | `WATCH` | HOLD |
