# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T07:04:38Z`
- **Ciclo de ejecucion:** `#207`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global de criptomonedas se mantiene bajo presión bajista con la mayoría de los activos cotizando por debajo de la EMA 200 en temporalidad 1H. Destaca la activación del Pilar 1 LONG (P1_EMA200_PULLBACK) en INTCBUSDT, que cumple con las condiciones óptimas de pullback sobre la EMA 200 con pendiente positiva, estocástico girando al alza y patrón de vela de giro alcista (BULLISH_ENGULFING). El resto de activos presentan tendencias primarias bajistas sin activaciones de entrada válidas en este ciclo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.48e-06 | 5e-06 | `-10.28%` | `9.39` / `10.63` | `24.78` | `0.18` | `NONE` | 4.27e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73633.02 | 75419.927519 | `-2.37%` | `10.28` / `14.54` | `43.48` | `0.238` | `BULLISH_ENGULFING` | 71718.56148 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2048.59 | 2163.749732 | `-5.32%` | `17.36` / `18.81` | `42.09` | `0.237` | `BULLISH_ENGULFING` | 1995.32666 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 82.89 | 87.799043 | `-5.59%` | `18.43` / `21.08` | `40.6` | `0.182` | `BULLISH_ENGULFING` | 80.73486 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.153 | 6.874296 | `-10.49%` | `11.38` / `16.49` | `32.16` | `0.175` | `NONE` | 5.9227958 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.519 | 3.743886 | `-6.01%` | `5.56` / `5.55` | `36.77` | `0.149` | `NONE` | 3.3888376 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0445 | 1.135713 | `-8.03%` | `13.42` / `11.31` | `39.74` | `0.187` | `BULLISH_HAMMER` | 1.017343 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.443 | 7.905607 | `-5.85%` | `8.79` / `11.64` | `31.96` | `0.176` | `BEARISH_SHOOTING_STAR` | 7.1278468 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 673.95 | 691.217133 | `-2.50%` | `9.75` / `7.06` | `36.64` | `0.09` | `NONE` | 656.4273 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1431 | 0.158991 | `-9.99%` | `5.46` / `5.68` | `30.43` | `0.187` | `BULLISH_ENGULFING` | 0.1374639 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 163.68 | 189.361454 | `-13.56%` | `6.61` / `9.76` | `26.07` | `0.156` | `NONE` | 156.481952 | `EXIT_SHORT_STOCH_20` | HOLD |
| `HYPEUSDT` | 71.29 | 76.829269 | `-7.21%` | `18.68` / `25.9` | `38.86` | `0.134` | `NONE` | 69.305878 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1498 | 0.164019 | `-8.67%` | `4.72` / `5.4` | `30.36` | `0.191` | `NONE` | 0.14503556 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06697 | 0.070742 | `-5.33%` | `18.02` / `20.84` | `36.57` | `0.171` | `BULLISH_ENGULFING` | 0.06522878 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3964.5 | 4026.586065 | `-1.54%` | `18.1` / `18.02` | `31.5` | `0.213` | `NONE` | 3861.423 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INTCBUSDT` | 60.77 | 59.214352 | `+2.63%` | `16.46` / `15.23` | `48.17` | `0.287` | `BULLISH_ENGULFING` | 58.44921 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
