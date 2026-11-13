# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T03:22:39Z`
- **Ciclo de ejecucion:** `#296`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un regimen bajista generalizado en temporalidad de 1H con la gran mayoria de los activos operando por debajo de la EMA 200 y registrando descensos de 24h superiores al 5%. Los indicadores de momentum como el Estocastico y el RSI muestran condiciones de sobreventa extrema, pero sin confirmaciones solidas de giro alcista generalizado ni patrones de velas de inversion validos que activen los Pilares LONG (P1-P4). No se registran posiciones abiertas activas con ganancias para aplicar la gestion dinamica de Stop-Loss (ADJUST), por lo que se prioriza la prudencia institucional manteniendo la observacion y evitando nuevas operaciones en largo hasta que se cumplan las confluencias estrictas de los pilares definidos.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 69274.99 | 74784.796338 | `-7.37%` | `8.52` / `11.44` | `12.11` | `-0.107` | `NONE` | 67473.84026 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `ETHUSDT` | 1955.6 | 2139.212068 | `-8.58%` | `31.64` / `42.67` | `18.51` | `-0.267` | `BEARISH_ENGULFING` | 1904.7544 | `WATCH` | HOLD |
| `SOLUSDT` | 78.92 | 86.658261 | `-8.93%` | `19.77` / `30.92` | `20.75` | `-0.235` | `NONE` | 76.86808 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 934.6 | 1124.455045 | `-16.88%` | `26.69` / `37.87` | `34.99` | `0.084` | `NONE` | 891.78376 | `WATCH` | HOLD |
| `BNBUSDT` | 636.35 | 684.814367 | `-7.08%` | `14.59` / `22.55` | `16.56` | `-0.137` | `NONE` | 619.8049 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NBISBUSDT` | 127.74 | 140.165541 | `-8.86%` | `48.06` / `36.46` | `33.93` | `0.339` | `BEARISH_ENGULFING` | 121.86396 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0069 | 1.11738 | `-9.89%` | `26.67` / `42.73` | `26.44` | `-0.173` | `NONE` | 0.9807206 | `WATCH` | HOLD |
| `NEARUSDT` | 3.353 | 3.668546 | `-8.60%` | `49.35` / `59.99` | `32.92` | `-0.019` | `BEARISH_ENGULFING` | 3.2437276 | `WATCH` | HOLD |
| `UNIUSDT` | 5.832 | 6.720452 | `-13.22%` | `28.86` / `44.57` | `25.18` | `-0.166` | `NONE` | 5.6472064 | `WATCH` | HOLD |
| `DOGEUSDT` | 0.0639 | 0.069881 | `-8.56%` | `41.28` / `59.81` | `24.26` | `-0.237` | `NONE` | 0.0622386 | `WATCH` | HOLD |
| `ENAUSDT` | 0.1352 | 0.155082 | `-12.82%` | `33.82` / `52.51` | `22.2` | `-0.331` | `NONE` | 0.13047616 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.133 | 1.137917 | `-0.43%` | `14.73` / `16.6` | `37.17` | `0.204` | `BEARISH_ENGULFING` | 1.080882 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SUIUSDT` | 0.778 | 0.841855 | `-7.59%` | `37.36` / `56.79` | `26.47` | `-0.172` | `NONE` | 0.757772 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0803 | 0.077787 | `+3.23%` | `9.78` / `9.29` | `38.77` | `0.214` | `NONE` | 0.0766062 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AVAXUSDT` | 8.111 | 8.428669 | `-3.77%` | `28.12` / `34.98` | `30.03` | `-0.058` | `BEARISH_ENGULFING` | 7.900114 | `WATCH` | HOLD |
| `AAVEUSDT` | 111.29 | 125.126939 | `-11.06%` | `43.55` / `59.75` | `27.29` | `0.033` | `NONE` | 108.39646 | `WATCH` | HOLD |
