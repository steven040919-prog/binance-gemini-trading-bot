# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T09:50:15Z`
- **Ciclo de ejecucion:** `#224`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado presenta un régimen claramente bajista (BEARISH) con la totalidad de los activos cotizando por debajo de sus respectivas EMA 200 en H1 y con pendientes negativas. Ningún activo cumple con los criterios de entrada institucionales para los Pilares LONG (P1-P4) ni con el Pilar S1 SHORT (requiere retroceso a la resistencia de la EMA 200 con sobrecompra Estocástica >= 80). No hay posiciones abiertas para gestión dinámica. Se mantiene una postura de neutralidad y preservación de capital.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 73422.0 | 75394.56014 | `-2.62%` | `13.39` / `12.27` | `39.69` | `0.137` | `NONE` | 71513.028 | `EXIT_SHORT_STOCH_20` | **HOLD** (95%) |
| `PEPEUSDT` | 4.44e-06 | 5e-06 | `-10.88%` | `7.64` / `7.15` | `21.64` | `0.191` | `BEARISH_SHOOTING_STAR` | 4.24e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (95%) |
| `ETHUSDT` | 2044.98 | 2162.228411 | `-5.42%` | `25.08` / `22.57` | `40.62` | `0.194` | `BULLISH_HAMMER` | 1991.81052 | `WATCH` | **HOLD** (90%) |
| `SOLUSDT` | 83.1 | 87.717246 | `-5.26%` | `27.76` / `23.33` | `43.44` | `0.285` | `BULLISH_HAMMER` | 80.9394 | `WATCH` | **HOLD** (90%) |
| `NEARUSDT` | 3.5 | 3.737449 | `-6.35%` | `7.0` / `4.75` | `37.23` | `0.19` | `NONE` | 3.3492 | `EXIT_SHORT_STOCH_20` | **HOLD** (95%) |
| `UNIUSDT` | 6.195 | 6.864909 | `-9.76%` | `12.32` / `10.49` | `36.74` | `0.292` | `BULLISH_HAMMER` | 5.91003 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `BNBUSDT` | 671.55 | 691.104942 | `-2.83%` | `13.21` / `12.08` | `33.39` | `0.079` | `BULLISH_HAMMER` | 654.0897 | `EXIT_SHORT_STOCH_20` | **HOLD** (92%) |
| `ENAUSDT` | 0.1419 | 0.158606 | `-10.53%` | `4.67` / `3.12` | `28.04` | `0.2` | `NONE` | 0.13659976 | `EXIT_SHORT_STOCH_20` | **HOLD** (95%) |
| `QNTUSDT` | 163.99 | 188.86096 | `-13.17%` | `10.6` / `10.05` | `30.16` | `0.221` | `NONE` | 156.831592 | `EXIT_SHORT_STOCH_20` | **HOLD** (95%) |
| `ARBUSDT` | 0.149 | 0.163769 | `-9.02%` | `5.9` / `4.72` | `29.93` | `0.219` | `NONE` | 0.1437684 | `EXIT_SHORT_STOCH_20` | **HOLD** (92%) |
| `INJUSDT` | 7.453 | 7.896257 | `-5.61%` | `9.81` / `8.49` | `34.8` | `0.254` | `BEARISH_SHOOTING_STAR` | 7.110162 | `EXIT_SHORT_STOCH_20` | **HOLD** (95%) |
| `XAUTUSDT` | 3938.5 | 4024.653374 | `-2.14%` | `14.53` / `14.02` | `28.46` | `-0.003` | `NONE` | 3836.099 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `DOGEUSDT` | 0.06717 | 0.070686 | `-4.97%` | `26.56` / `21.92` | `40.95` | `0.286` | `BULLISH_ENGULFING` | 0.06542358 | `WATCH` | **HOLD** (90%) |
| `AAVEUSDT` | 117.29 | 127.875113 | `-8.28%` | `10.61` / `8.65` | `28.68` | `0.195` | `BULLISH_ENGULFING` | 113.70504 | `EXIT_SHORT_STOCH_20` | **HOLD** (92%) |
| `HYPEUSDT` | 71.61 | 76.723751 | `-6.67%` | `28.5` / `23.18` | `43.35` | `0.276` | `BULLISH_ENGULFING` | 69.590512 | `WATCH` | **HOLD** (90%) |
| `LINKUSDT` | 10.107 | 10.684327 | `-5.40%` | `16.45` / `12.81` | `38.75` | `0.283` | `BULLISH_ENGULFING` | 9.837646 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
