# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T05:48:47Z`
- **Ciclo de ejecucion:** `#199`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen netamente bajista en temporalidad de 1H, con la gran mayoría de los activos cotizando por debajo de la EMA 200 y con pendientes negativas. Evaluando los pilares de la estrategia, no se cumplen las condiciones de sobreventa extrema con giro alcista ni los patrones de capitulación para activar los Pilares LONG (P1-P4). No obstante, se identifica oportunidad bajo los criterios del Pilar S1 Short y configuraciones intradía en UNIUSDT (M15_SCALPER_PULLBACK_SHORT), manteniendo la gestión de riesgo estricta y sin posiciones abiertas que requieran ajuste por el momento.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 73608.49 | 75468.444331 | `-2.46%` | `20.84` / `25.13` | `42.25` | `0.157` | `BEARISH_ENGULFING` | 71694.66926 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.56e-06 | 5e-06 | `-8.91%` | `12.56` / `14.27` | `25.31` | `0.208` | `BULLISH_HAMMER` | 4.37e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2047.58 | 2166.748045 | `-5.50%` | `22.44` / `26.04` | `40.84` | `0.171` | `BULLISH_HAMMER` | 1994.34292 | `WATCH` | HOLD |
| `UNIUSDT` | 6.221 | 6.889746 | `-9.71%` | `22.28` / `20.28` | `34.38` | `0.196` | `BEARISH_ENGULFING` | 6.4785372 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (82%) |
| `SOLUSDT` | 82.99 | 87.943257 | `-5.63%` | `26.32` / `29.08` | `40.6` | `0.134` | `BULLISH_HAMMER` | 80.83226 | `WATCH` | HOLD |
| `NEARUSDT` | 3.541 | 3.748381 | `-5.53%` | `7.47` / `11.34` | `37.81` | `0.118` | `BULLISH_HAMMER` | 3.4165208 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0428 | 1.138152 | `-8.38%` | `12.99` / `17.17` | `36.93` | `0.032` | `BULLISH_HAMMER` | 1.0156872 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.389 | 7.917039 | `-6.67%` | `14.13` / `16.98` | `27.77` | `0.028` | `BEARISH_SHOOTING_STAR` | 7.112996 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1433 | 0.159413 | `-10.11%` | `7.33` / `10.68` | `28.04` | `0.11` | `NONE` | 0.13841378 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 675.15 | 691.628839 | `-2.38%` | `8.18` / `13.3` | `36.81` | `0.001` | `NONE` | 657.5961 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1508 | 0.164334 | `-8.24%` | `6.47` / `7.91` | `31.4` | `0.17` | `NONE` | 0.14508552 | `EXIT_SHORT_STOCH_20` | HOLD |
| `HYPEUSDT` | 71.57 | 76.93265 | `-6.97%` | `35.35` / `38.92` | `39.98` | `0.119` | `BEARISH_ENGULFING` | 69.70918 | `WATCH` | HOLD |
| `DOGEUSDT` | 0.06709 | 0.070838 | `-5.29%` | `26.12` / `29.26` | `36.55` | `0.116` | `BULLISH_HAMMER` | 0.06534566 | `WATCH` | HOLD |
| `QNTUSDT` | 165.65 | 189.915051 | `-12.78%` | `12.81` / `11.76` | `27.6` | `0.145` | `BULLISH_HAMMER` | 158.10461 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LINKUSDT` | 10.054 | 10.720747 | `-6.22%` | `12.82` / `16.84` | `30.81` | `0.068` | `NONE` | 9.792596 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3969.0 | 4027.934472 | `-1.46%` | `16.47` / `17.54` | `29.51` | `0.234` | `BEARISH_ENGULFING` | 3865.806 | `EXIT_SHORT_STOCH_20` | HOLD |
