# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T19:20:03Z`
- **Ciclo de ejecucion:** `#365`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general opera bajo una estructura bajista con la gran mayoria de los activos cotizando por debajo de su EMA 200 en temporalidad de 1H y con baja volatilidad/volumen. Se evaluan los pilares de la estrategia sin activacion de entradas LONG (P1-P4) debido a la ausencia de capitulaciones extremas o soportes claros de 12h cumpliendo todos los filtros exigidos. En el lado de Futuros USDT-M, se identifica a GRAMUSDT bajo el pilar M15_SCALPER_PULLBACK_SHORT con patron de giro bajista y estructura institucional descendente, generando una senal SHORT.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.0743 | 0.077819 | `-4.52%` | `5.48` / `7.55` | `32.64` | `0.123` | `BEARISH_SHOOTING_STAR` | 0.0708822 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PEPEUSDT` | 4.46e-06 | 5e-06 | `-7.74%` | `27.78` / `25.93` | `43.47` | `0.16` | `NONE` | 4.25e-06 | `WATCH` | HOLD |
| `BTCUSDT` | 69036.39 | 73846.089646 | `-6.51%` | `51.57` / `48.12` | `37.46` | `0.436` | `BULLISH_HAMMER` | 67241.44386 | `WATCH` | HOLD |
| `XAUTUSDT` | 3874.0 | 3989.721984 | `-2.90%` | `35.19` / `28.33` | `40.6` | `0.252` | `BULLISH_HAMMER` | 3773.276 | `WATCH` | HOLD |
| `ETHUSDT` | 1949.93 | 2107.259562 | `-7.47%` | `50.66` / `43.78` | `42.99` | `0.49` | `MORNING_STAR` | 1882.741456 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.126 | 1.136725 | `-0.94%` | `22.62` / `23.02` | `39.66` | `0.17` | `BULLISH_ENGULFING` | 1.1686808 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (75%) |
| `SOLUSDT` | 80.24 | 85.529547 | `-6.18%` | `47.3` / `44.77` | `45.99` | `0.535` | `BULLISH_HAMMER` | 77.562384 | `WATCH` | HOLD |
| `ZECUSDT` | 959.48 | 1090.50664 | `-12.02%` | `59.8` / `59.3` | `52.58` | `0.687` | `BULLISH_ENGULFING` | 915.34392 | `WATCH` | HOLD |
| `BNBUSDT` | 637.89 | 676.794329 | `-5.75%` | `49.28` / `42.36` | `43.3` | `0.502` | `MORNING_STAR` | 618.262824 | `WATCH` | HOLD |
| `NEARUSDT` | 3.541 | 3.624592 | `-2.31%` | `66.56` / `65.03` | `56.08` | `0.7` | `BULLISH_ENGULFING` | 3.378114 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0265 | 1.103282 | `-6.96%` | `50.3` / `47.73` | `49.16` | `0.608` | `MORNING_STAR` | 0.989764 | `WATCH` | HOLD |
| `INJUSDT` | 8.21 | 7.803642 | `+5.21%` | `87.56` / `86.83` | `72.85` | `0.842` | `BULLISH_HAMMER` | 7.83234 | `EXIT_LONG_STOCH_80` | HOLD |
| `UNIUSDT` | 5.877 | 6.574907 | `-10.61%` | `45.46` / `39.63` | `47.89` | `0.596` | `BULLISH_ENGULFING` | 5.606658 | `WATCH` | HOLD |
| `SOXSBUSDT` | 50.72 | 55.482764 | `-8.58%` | `65.28` / `73.2` | `58.88` | `0.74` | `NONE` | 48.38688 | `WATCH` | HOLD |
| `HYPEUSDT` | 72.9 | 75.172086 | `-3.02%` | `50.64` / `51.46` | `53.12` | `0.575` | `MORNING_STAR` | 70.10254 | `WATCH` | HOLD |
| `ENAUSDT` | 0.1374 | 0.151864 | `-9.52%` | `42.18` / `40.95` | `46.33` | `0.502` | `BULLISH_HAMMER` | 0.1310796 | `WATCH` | HOLD |
