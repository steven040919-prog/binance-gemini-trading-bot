# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T08:31:09Z`
- **Ciclo de ejecucion:** `#216`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> Mercado predominantemente bajista en temporalidad de 1H con la totalidad de los activos cotizando por debajo de la EMA 200. No se activan señales de compra bajo los Pilares P1-P4 debido a la falta de confluencia extrema en sobreventa y volumen. Tampoco se activa el Pilar S1 de Short en resistencia ya que los osciladores (Estocástico y RSI) se encuentran en zonas de sobreventa/compresión en lugar de sobrecompra. No existen posiciones abiertas activas para gestión dinámica de SL/TP. Se mantiene liquidez total en HOLD a la espera de confirmaciones cuantitativas.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 73521.54 | 75412.111259 | `-2.51%` | `10.67` / `11.56` | `41.56` | `0.182` | `BULLISH_ENGULFING` | 71609.97996 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `PEPEUSDT` | 4.49e-06 | 5e-06 | `-10.04%` | `8.34` / `8.59` | `26.28` | `0.225` | `BEARISH_SHOOTING_STAR` | 4.28e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `ETHUSDT` | 2047.58 | 2163.075093 | `-5.34%` | `21.77` / `19.33` | `42.0` | `0.223` | `BULLISH_ENGULFING` | 1994.34292 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `NEARUSDT` | 3.47 | 3.74133 | `-7.25%` | `3.6` / `3.99` | `31.56` | `0.082` | `BEARISH_SHOOTING_STAR` | 3.359818 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `SOLUSDT` | 82.86 | 87.758606 | `-5.58%` | `21.0` / `20.09` | `40.74` | `0.197` | `BULLISH_ENGULFING` | 80.70564 | `WATCH` | **HOLD** (0%) |
| `XRPUSDT` | 1.0426 | 1.135093 | `-8.15%` | `16.27` / `12.76` | `38.23` | `0.174` | `NONE` | 1.0154924 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `UNIUSDT` | 6.135 | 6.874327 | `-10.75%` | `7.35` / `11.7` | `31.12` | `0.184` | `NONE` | 5.927042 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `ENAUSDT` | 0.1416 | 0.158808 | `-10.84%` | `2.49` / `3.26` | `24.54` | `0.15` | `BEARISH_SHOOTING_STAR` | 0.13693872 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `INJUSDT` | 7.476 | 7.901403 | `-5.38%` | `12.38` / `10.43` | `35.46` | `0.245` | `BULLISH_ENGULFING` | 7.132104 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `BNBUSDT` | 673.08 | 691.201684 | `-2.62%` | `13.4` / `9.57` | `35.57` | `0.093` | `BULLISH_ENGULFING` | 655.57992 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `ARBUSDT` | 0.1493 | 0.163889 | `-8.90%` | `4.65` / `4.92` | `28.98` | `0.2` | `NONE` | 0.1444196 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `HYPEUSDT` | 71.23 | 76.768447 | `-7.21%` | `19.98` / `21.56` | `38.97` | `0.148` | `BULLISH_ENGULFING` | 69.36417 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `DOGEUSDT` | 0.06697 | 0.070717 | `-5.30%` | `20.62` / `19.71` | `37.03` | `0.199` | `BULLISH_ENGULFING` | 0.06522878 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `QNTUSDT` | 164.33 | 189.238941 | `-13.16%` | `9.44` / `9.87` | `30.63` | `0.204` | `BULLISH_ENGULFING` | 156.77082 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `XAUTUSDT` | 3944.0 | 4025.629568 | `-2.03%` | `11.09` / `14.99` | `23.05` | `-0.035` | `NONE` | 3841.456 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `LINKUSDT` | 10.09 | 10.689168 | `-5.61%` | `13.41` / `10.42` | `36.59` | `0.234` | `MORNING_STAR` | 9.79402 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
