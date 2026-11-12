# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T09:59:56Z`
- **Ciclo de ejecucion:** `#225`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen bajista generalizado en temporalidad de 1H con la mayoría de los activos operando por debajo de la EMA 200 y con pendiente negativa. Se identifica una oportunidad de entrada alcista institucional bajo el Pilar 2 (Capitulación Extrema) en NEARUSDT, el cual cumple con la sobreventa simultánea en RSI, estocástico, bandas de Bollinger y volumen institucional relevante. No se detectan posiciones abiertas con ganancias previas para ajustes dinámicos de SL/TP, manteniendo el resto de activos en observación o salida de cortos.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 73492.48 | 75395.261433 | `-2.52%` | `14.9` / `12.77` | `40.93` | `0.178` | `BULLISH_HAMMER` | 71581.67552 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PEPEUSDT` | 4.43e-06 | 5e-06 | `-11.08%` | `6.88` / `6.89` | `21.26` | `0.179` | `BEARISH_SHOOTING_STAR` | 4.23e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2046.39 | 2162.24244 | `-5.36%` | `26.04` / `22.89` | `41.31` | `0.216` | `BULLISH_HAMMER` | 1993.18386 | `WATCH` | HOLD |
| `SOLUSDT` | 83.16 | 87.717843 | `-5.20%` | `28.43` / `23.55` | `44.23` | `0.301` | `BULLISH_HAMMER` | 80.99784 | `WATCH` | HOLD |
| `NEARUSDT` | 3.502 | 3.737469 | `-6.30%` | `7.24` / `4.83` | `37.53` | `0.194` | `BULLISH_ENGULFING` | 3.3491384 | `P2_EXTREME_CAPITULATION` | **BUY** (85%) |
| `UNIUSDT` | 6.19 | 6.864859 | `-9.83%` | `11.99` / `10.38` | `36.26` | `0.285` | `BULLISH_HAMMER` | 5.905634 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 671.56 | 691.105042 | `-2.83%` | `13.23` / `12.08` | `33.41` | `0.08` | `BULLISH_HAMMER` | 654.09944 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1418 | 0.158605 | `-10.60%` | `4.35` / `3.01` | `27.45` | `0.196` | `NONE` | 0.13657436 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1489 | 0.163768 | `-9.08%` | `5.6` / `4.62` | `29.47` | `0.214` | `NONE` | 0.14377124 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.444 | 7.896168 | `-5.73%` | `9.3` / `8.32` | `34.1` | `0.245` | `BEARISH_SHOOTING_STAR` | 7.1063928 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 164.68 | 188.867826 | `-12.81%` | `11.96` / `10.51` | `32.15` | `0.245` | `BULLISH_HAMMER` | 157.10472 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06723 | 0.070686 | `-4.89%` | `27.4` / `22.2` | `41.98` | `0.304` | `BULLISH_ENGULFING` | 0.06548202 | `WATCH` | HOLD |
| `AAVEUSDT` | 116.72 | 127.869441 | `-8.72%` | `8.0` / `7.78` | `26.05` | `0.148` | `NONE` | 113.68528 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3938.84 | 4024.656757 | `-2.13%` | `14.69` / `14.08` | `28.66` | `0.0` | `NONE` | 3836.43016 | `EXIT_SHORT_STOCH_20` | HOLD |
| `HYPEUSDT` | 71.58 | 76.723452 | `-6.70%` | `28.14` / `23.06` | `43.0` | `0.269` | `BULLISH_ENGULFING` | 69.591136 | `WATCH` | HOLD |
| `LINKUSDT` | 10.103 | 10.684287 | `-5.44%` | `16.18` / `12.72` | `38.35` | `0.278` | `NONE` | 9.837734 | `EXIT_SHORT_STOCH_20` | HOLD |
