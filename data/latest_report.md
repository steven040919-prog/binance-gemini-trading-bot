# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T08:36:21Z`
- **Ciclo de ejecucion:** `#302`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado mantiene una tendencia bajista predominante en temporalidad 1H, con la mayoría de los activos operando por debajo de la EMA 200. Se ha detectado una oportunidad de entrada LONG en BNBUSDT bajo el Pilar 2 (Capitulación Extrema) debido a la confluencia de sobreventa extrema y giro en el estocástico. Se han identificado señales de rechazo bajista en activos como NBISBUSDT y ONEUSDT, los cuales se gestionan bajo el Pilar S1/Scalper para capturar la continuación de la tendencia bajista. No hay posiciones abiertas actualmente, por lo que no se requieren ajustes de gestión dinámica en este ciclo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68795.01 | 74460.550035 | `-7.61%` | `28.44` / `22.34` | `26.69` | `0.158` | `NONE` | 66487.282794 | `WATCH` | HOLD |
| `ETHUSDT` | 1935.66 | 2128.048532 | `-9.04%` | `31.19` / `24.53` | `28.13` | `0.162` | `BEARISH_SHOOTING_STAR` | 1857.411292 | `WATCH` | HOLD |
| `BNBUSDT` | 630.89 | 681.678731 | `-7.45%` | `25.37` / `20.67` | `26.53` | `0.125` | `BULLISH_HAMMER` | 610.715132 | `P2_EXTREME_CAPITULATION` | **BUY** (82%) |
| `NBISBUSDT` | 125.38 | 139.32957 | `-10.01%` | `20.66` / `20.44` | `32.81` | `0.145` | `NONE` | 131.14748 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (75%) |
| `ONEUSDT` | 0.001478 | 0.001547 | `-4.45%` | `20.34` / `19.71` | `39.37` | `0.183` | `BEARISH_SHOOTING_STAR` | 0.00154599 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (72%) |
| `ERAUSDT` | 0.0823 | 0.078249 | `+5.18%` | `38.52` / `29.46` | `44.01` | `0.376` | `BEARISH_ENGULFING` | 0.0785142 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.142 | 1.137908 | `+0.36%` | `31.8` / `23.86` | `41.08` | `0.344` | `BEARISH_SHOOTING_STAR` | 1.0938016 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3109 | 0.317621 | `-2.12%` | `5.4` / `7.96` | `17.2` | `0.083` | `BEARISH_SHOOTING_STAR` | 0.3028166 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 111.56 | 124.385201 | `-10.31%` | `37.21` / `29.21` | `36.23` | `0.285` | `BEARISH_SHOOTING_STAR` | 106.986376 | `WATCH` | HOLD |
| `HBARUSDT` | 0.0621 | 0.066593 | `-6.75%` | `42.9` / `32.72` | `36.26` | `0.269` | `BEARISH_SHOOTING_STAR` | 0.05936782 | `WATCH` | HOLD |
| `TIAUSDT` | 0.4169 | 0.42953 | `-2.94%` | `42.14` / `35.0` | `47.05` | `0.387` | `BEARISH_SHOOTING_STAR` | 0.3977226 | `WATCH` | HOLD |
| `QNTUSDT` | 156.8 | 183.537587 | `-14.57%` | `31.65` / `29.64` | `31.9` | `0.055` | `NONE` | 149.92384 | `WATCH` | HOLD |
| `SOLUSDT` | 80.05 | 86.2787 | `-7.22%` | `50.29` / `38.1` | `41.25` | `0.345` | `NONE` | 76.3677 | `WATCH` | HOLD |
| `ZECUSDT` | 949.73 | 1115.124328 | `-14.83%` | `76.7` / `58.9` | `48.46` | `0.54` | `BULLISH_ENGULFING` | 906.04242 | `WATCH` | HOLD |
| `DODOUSDT` | 0.02712 | 0.023473 | `+15.54%` | `25.97` / `32.02` | `57.23` | `0.523` | `BULLISH_ENGULFING` | 0.02587248 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0314 | 1.112751 | `-7.31%` | `63.58` / `49.49` | `49.75` | `0.606` | `BEARISH_SHOOTING_STAR` | 0.98579664 | `WATCH` | HOLD |
