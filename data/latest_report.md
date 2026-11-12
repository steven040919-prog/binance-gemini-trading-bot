# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T01:30:13Z`
- **Ciclo de ejecucion:** `#172`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general presenta un régimen dominantemente bajista con la gran mayoría de activos cotizando por debajo de su EMA 200 en 1H y con pendientes negativas. Ningún activo cumple con los criterios estrictos de entrada cuantitativos para los Pilares LONG (P1-P4) ni para el Pilar SHORT S1 (se requiere rechazo en EMA 200 con Estocástico en sobrecompra >= 80). No existen posiciones abiertas que requieran ajuste dinámico de SL/TP. Se preserva el capital en USDT al 100%.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.55e-06 | 5e-06 | `-9.51%` | `7.37` / `5.21` | `21.32` | `0.093` | `BULLISH_HAMMER` | 4.34e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `BTCUSDT` | 73640.86 | 75538.390604 | `-2.51%` | `36.98` / `44.0` | `42.92` | `0.174` | `BEARISH_ENGULFING` | 71726.19764 | `WATCH` | **HOLD** (90%) |
| `ETHUSDT` | 2051.56 | 2171.39709 | `-5.52%` | `30.79` / `31.13` | `41.9` | `0.195` | `BULLISH_ENGULFING` | 1998.21944 | `WATCH` | **HOLD** (90%) |
| `UNIUSDT` | 6.171 | 6.920767 | `-10.83%` | `8.44` / `11.85` | `25.66` | `-0.077` | `BULLISH_HAMMER` | 5.9053756 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `SOLUSDT` | 83.15 | 88.157689 | `-5.68%` | `31.79` / `32.66` | `41.43` | `0.206` | `BULLISH_ENGULFING` | 80.37733 | `WATCH` | **HOLD** (90%) |
| `NEARUSDT` | 3.591 | 3.755849 | `-4.39%` | `23.98` / `23.95` | `42.33` | `0.186` | `BULLISH_ENGULFING` | 3.425814 | `WATCH` | **HOLD** (88%) |
| `XRPUSDT` | 1.0501 | 1.141704 | `-8.02%` | `31.41` / `28.22` | `40.97` | `0.052` | `BULLISH_ENGULFING` | 1.01747776 | `WATCH` | **HOLD** (88%) |
| `INJUSDT` | 7.498 | 7.938793 | `-5.55%` | `12.12` / `10.53` | `28.56` | `0.008` | `BEARISH_ENGULFING` | 7.1700704 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `ARBUSDT` | 0.1514 | 0.164998 | `-8.24%` | `6.53` / `7.57` | `27.5` | `-0.029` | `BULLISH_HAMMER` | 0.14582492 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `BNBUSDT` | 678.32 | 691.641679 | `-1.93%` | `24.72` / `30.58` | `41.0` | `0.132` | `BULLISH_ENGULFING` | 660.68368 | `WATCH` | **HOLD** (90%) |
| `ENAUSDT` | 0.1449 | 0.160111 | `-9.50%` | `20.75` / `16.29` | `31.24` | `-0.023` | `BULLISH_ENGULFING` | 0.1382346 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `QNTUSDT` | 167.7 | 191.000084 | `-12.20%` | `13.81` / `13.68` | `28.98` | `-0.047` | `BULLISH_HAMMER` | 159.9858 | `EXIT_SHORT_STOCH_20` | **HOLD** (87%) |
| `LINKUSDT` | 10.144 | 10.748601 | `-5.62%` | `28.15` / `25.32` | `33.83` | `0.003` | `BULLISH_ENGULFING` | 9.756256 | `WATCH` | **HOLD** (90%) |
| `SUIUSDT` | 0.8199 | 0.854093 | `-4.00%` | `27.12` / `24.89` | `39.08` | `0.128` | `BEARISH_ENGULFING` | 0.79008638 | `WATCH` | **HOLD** (90%) |
| `AAVEUSDT` | 119.03 | 128.738391 | `-7.54%` | `17.73` / `16.46` | `28.74` | `-0.115` | `NONE` | 115.503802 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `OPGUSDT` | 0.1336 | 0.125935 | `+6.09%` | `7.31` / `9.61` | `45.86` | `0.315` | `BEARISH_SHOOTING_STAR` | 0.1274544 | `EXIT_SHORT_STOCH_20` | **HOLD** (88%) |
