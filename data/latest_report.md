# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T19:15:31Z`
- **Ciclo de ejecucion:** `#253`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un regimen bajista generalizado con la mayoria de los activos cotizando por debajo de la EMA 200 y con sesgo contractivo en temporalidad de 1H. Se identifican oportunidades de entrada corta (SHORT) en Binance Futuros USDT-M bajo el Pilar S1 de rechazo en resistencia EMA 200 y el Pilar Scalper M15 para XAUTUSDT y AVAXUSDT que cumplen con los criterios institucionales de sobreventa/sobrecompra y patron de velas.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71645.0 | 75098.741084 | `-4.60%` | `20.3` / `20.57` | `24.11` | `0.123` | `NONE` | 69782.23 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.43e-06 | 5e-06 | `-10.06%` | `37.09` / `25.23` | `37.84` | `0.417` | `MORNING_STAR` | 4.23e-06 | `WATCH` | HOLD |
| `ZECUSDT` | 946.87 | 1136.429224 | `-16.68%` | `17.01` / `17.77` | `34.27` | `0.082` | `BULLISH_HAMMER` | 903.31398 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 81.53 | 87.092183 | `-6.39%` | `37.39` / `36.32` | `35.54` | `0.194` | `BULLISH_HAMMER` | 79.41022 | `WATCH` | HOLD |
| `NEARUSDT` | 3.426 | 3.698925 | `-7.38%` | `35.72` / `31.53` | `37.28` | `0.306` | `BULLISH_ENGULFING` | 3.268404 | `WATCH` | HOLD |
| `UNIUSDT` | 6.036 | 6.778354 | `-10.95%` | `28.68` / `26.34` | `33.07` | `0.249` | `BULLISH_ENGULFING` | 5.7985416 | `WATCH` | HOLD |
| `BNBUSDT` | 654.18 | 687.55832 | `-4.85%` | `18.95` / `19.73` | `23.7` | `0.178` | `BULLISH_HAMMER` | 637.17132 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0275 | 1.124171 | `-8.60%` | `31.93` / `29.52` | `34.88` | `0.179` | `NONE` | 1.000785 | `WATCH` | HOLD |
| `ENAUSDT` | 0.1395 | 0.156577 | `-10.91%` | `36.14` / `31.0` | `29.95` | `0.267` | `NONE` | 0.133136 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.15 | 1.138093 | `+1.05%` | `20.25` / `42.57` | `38.53` | `0.052` | `BULLISH_HAMMER` | 1.0971 | `WATCH` | HOLD |
| `XAUTUSDT` | 3876.43 | 4013.68878 | `-3.42%` | `20.06` / `18.74` | `26.45` | `0.191` | `BULLISH_ENGULFING` | 3977.21718 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (85%) |
| `AAVEUSDT` | 113.36 | 126.239318 | `-10.20%` | `33.75` / `32.3` | `30.44` | `0.264` | `BEARISH_ENGULFING` | 110.097984 | `WATCH` | HOLD |
| `TAOUSDT` | 209.3 | 221.068161 | `-5.32%` | `47.58` / `42.91` | `35.8` | `0.259` | `BEARISH_SHOOTING_STAR` | 202.10006 | `WATCH` | HOLD |
| `QNTUSDT` | 161.93 | 186.609976 | `-13.23%` | `24.58` / `22.78` | `30.75` | `0.122` | `NONE` | 155.866416 | `WATCH` | HOLD |
| `INJUSDT` | 7.407 | 7.846168 | `-5.60%` | `32.25` / `28.88` | `40.27` | `0.34` | `BULLISH_ENGULFING` | 7.0867156 | `WATCH` | HOLD |
| `AVAXUSDT` | 8.346 | 8.443572 | `-1.16%` | `22.71` / `22.99` | `39.88` | `0.208` | `BULLISH_ENGULFING` | 8.600996 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (82%) |
