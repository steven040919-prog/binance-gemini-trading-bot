# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T19:44:46Z`
- **Ciclo de ejecucion:** `#256`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen general bajista en temporalidad 1H, con la gran mayoría de los activos operando por debajo de la EMA 200 y con tendencias macro en contracción. No se activan nuevas entradas LONG (Pilares P1-P4) ni SHORT (Pilar S1) debido a la ausencia de confluencias completas de giro o volumen institucional necesario. Las posiciones abiertas se mantienen en vigilancia y no requieren ajustes de SL/TP por el momento.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71560.75 | 75097.902775 | `-4.71%` | `19.17` / `20.19` | `23.39` | `0.103` | `NONE` | 69700.1705 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `ETHUSDT` | 2011.0 | 2148.521262 | `-6.40%` | `43.63` / `40.18` | `33.21` | `0.199` | `NONE` | 1958.714 | `WATCH` | HOLD |
| `ZECUSDT` | 947.21 | 1136.432607 | `-16.65%` | `17.18` / `17.83` | `34.48` | `0.086` | `BULLISH_HAMMER` | 903.63834 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 81.58 | 87.09268 | `-6.33%` | `37.94` / `36.5` | `35.97` | `0.208` | `BULLISH_HAMMER` | 79.45892 | `WATCH` | HOLD |
| `INITUSDT` | 0.11352 | 0.16222 | `-30.02%` | `11.8` / `12.69` | `33.98` | `0.132` | `BEARISH_ENGULFING` | 0.10829808 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.411 | 3.698776 | `-7.78%` | `33.36` / `30.74` | `35.66` | `0.258` | `BULLISH_ENGULFING` | 3.2611658 | `WATCH` | HOLD |
| `UNIUSDT` | 6.031 | 6.778305 | `-11.02%` | `28.11` / `26.15` | `32.39` | `0.236` | `BULLISH_ENGULFING` | 5.7962762 | `WATCH` | HOLD |
| `BNBUSDT` | 654.54 | 687.561902 | `-4.80%` | `19.41` / `19.89` | `24.02` | `0.185` | `BULLISH_HAMMER` | 637.52196 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0301 | 1.124197 | `-8.37%` | `34.08` / `30.23` | `36.77` | `0.238` | `BULLISH_HAMMER` | 1.00160402 | `WATCH` | HOLD |
| `ENAUSDT` | 0.1392 | 0.156574 | `-11.10%` | `34.64` / `30.5` | `29.06` | `0.237` | `NONE` | 0.13306208 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.141 | 1.138004 | `+0.26%` | `18.33` / `41.93` | `37.24` | `0.002` | `NONE` | 1.088514 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3879.55 | 4013.719825 | `-3.34%` | `20.9` / `19.02` | `27.2` | `0.207` | `BULLISH_ENGULFING` | 3778.6817 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 113.1 | 126.236731 | `-10.41%` | `32.59` / `31.91` | `29.33` | `0.241` | `BEARISH_ENGULFING` | 110.08202 | `WATCH` | HOLD |
| `QNTUSDT` | 161.9 | 186.609678 | `-13.24%` | `24.66` / `22.81` | `30.69` | `0.118` | `BEARISH_ENGULFING` | 155.30824 | `WATCH` | HOLD |
| `TAOUSDT` | 209.0 | 221.065176 | `-5.46%` | `46.72` / `42.62` | `35.09` | `0.238` | `BEARISH_SHOOTING_STAR` | 201.9824 | `WATCH` | HOLD |
| `INJUSDT` | 7.384 | 7.845939 | `-5.89%` | `29.86` / `28.08` | `38.87` | `0.264` | `BULLISH_ENGULFING` | 7.0829568 | `WATCH` | HOLD |
