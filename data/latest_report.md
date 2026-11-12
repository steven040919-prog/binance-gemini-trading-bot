# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T08:21:25Z`
- **Ciclo de ejecucion:** `#215`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general presenta un régimen bajista dominante en temporalidad 1H, con casi la totalidad de los activos cotizando por debajo de la EMA 200 y con pendientes negativas. Evaluando la arquitectura de 4 Pilares LONG y 1 Pilar SHORT (S1), ningún activo cumple actualmente con los requisitos estrictos de confluencia (falta de volumen institucional de capitulación en P2, falta de sobrecompra en resistencia EMA 200 para S1, o sobreextensión de precio como en OPGUSDT). No hay posiciones abiertas para gestión dinámica de SL/TP. Se determina mantener liquidez en HOLD.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.47e-06 | 5e-06 | `-10.44%` | `6.98` / `8.14` | `23.77` | `0.202` | `BEARISH_SHOOTING_STAR` | 4.26e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73607.15 | 75412.9631 | `-2.39%` | `12.73` / `12.24` | `43.1` | `0.235` | `BULLISH_ENGULFING` | 71693.3641 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `ETHUSDT` | 2050.5 | 2163.104148 | `-5.21%` | `23.75` / `19.99` | `43.43` | `0.272` | `BULLISH_ENGULFING` | 1997.187 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `NEARUSDT` | 3.493 | 3.741559 | `-6.64%` | `3.91` / `4.09` | `33.51` | `0.131` | `BEARISH_SHOOTING_STAR` | 3.3836072 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 82.98 | 87.7598 | `-5.45%` | `22.35` / `20.54` | `41.84` | `0.228` | `BULLISH_ENGULFING` | 80.82252 | `WATCH` | **HOLD** (80%) |
| `XRPUSDT` | 1.0444 | 1.135111 | `-7.99%` | `18.19` / `13.4` | `39.67` | `0.214` | `NONE` | 1.0172456 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.154 | 6.874517 | `-10.48%` | `8.63` / `12.12` | `32.29` | `0.209` | `BULLISH_HAMMER` | 5.9276876 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1418 | 0.15881 | `-10.71%` | `3.13` / `3.47` | `24.94` | `0.159` | `BEARISH_SHOOTING_STAR` | 0.13693256 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.48 | 7.901443 | `-5.33%` | `12.6` / `10.51` | `35.75` | `0.249` | `BULLISH_ENGULFING` | 7.13592 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 673.82 | 691.209048 | `-2.52%` | `14.85` / `10.05` | `36.66` | `0.125` | `BULLISH_ENGULFING` | 656.30068 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `ARBUSDT` | 0.1492 | 0.163888 | `-8.96%` | `4.33` / `4.81` | `28.51` | `0.196` | `NONE` | 0.1444224 | `EXIT_SHORT_STOCH_20` | HOLD |
| `HYPEUSDT` | 71.42 | 76.770338 | `-6.97%` | `22.24` / `22.31` | `40.5` | `0.195` | `BULLISH_ENGULFING` | 69.374464 | `WATCH` | HOLD |
| `DOGEUSDT` | 0.06705 | 0.070718 | `-5.19%` | `21.7` / `20.07` | `38.01` | `0.222` | `BULLISH_ENGULFING` | 0.0653067 | `WATCH` | HOLD |
| `QNTUSDT` | 165.3 | 189.248592 | `-12.65%` | `11.34` / `10.51` | `32.02` | `0.238` | `BULLISH_ENGULFING` | 157.6962 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3950.0 | 4025.68927 | `-1.88%` | `9.36` / `14.41` | `24.64` | `0.032` | `NONE` | 3847.3 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `OPGUSDT` | 0.1367 | 0.12635 | `+8.19%` | `36.78` / `25.8` | `51.75` | `0.399` | `NONE` | 0.1304118 | `WATCH` | **HOLD** (80%) |
