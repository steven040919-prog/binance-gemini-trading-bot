# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T23:25:17Z`
- **Ciclo de ejecucion:** `#164`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen general bajista (Bearish) con todos los activos cotizando por debajo de la EMA 200 y la mayoría en tendencia primaria bajista. Se evalúan los candidatos bajo los Pilares LONG y SHORT de la arquitectura autónoma. No se detectan activaciones válidas para los Pilares LONG (P1-P4) debido a que no se cumplen las condiciones de giro alcista con confirmación de velas institucionales en soportes críticos. Tampoco se activan operaciones SHORT nuevas ya que no se cumplen simultáneamente los requisitos de resistencia en EMA 200 con sobrecompra en estocástico y patrones bajistas requeridos. Las posiciones abiertas se mantienen en 0, preservando el capital (equity $14.0 USDT).

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.55e-06 | 5e-06 | `-9.75%` | `3.75` / `3.47` | `17.83` | `0.005` | `NONE` | 4.34e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 956.4 | 1174.160603 | `-18.55%` | `26.22` / `42.53` | `33.44` | `-0.061` | `BEARISH_SHOOTING_STAR` | 912.4056 | `WATCH` | HOLD |
| `ETHUSDT` | 2043.78 | 2173.331818 | `-5.96%` | `26.02` / `41.48` | `38.73` | `0.035` | `NONE` | 1990.64172 | `WATCH` | HOLD |
| `UNIUSDT` | 6.248 | 6.922945 | `-9.75%` | `19.5` / `38.18` | `28.54` | `-0.102` | `NONE` | 5.9995696 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 82.78 | 88.235617 | `-6.18%` | `31.44` / `50.69` | `38.27` | `0.132` | `NONE` | 80.401952 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0458 | 1.143185 | `-8.52%` | `19.38` / `29.18` | `37.47` | `-0.107` | `NONE` | 1.0179924 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.541 | 3.759216 | `-5.80%` | `20.73` / `38.08` | `37.7` | `-0.003` | `NONE` | 3.378114 | `WATCH` | HOLD |
| `BNBUSDT` | 678.22 | 691.757263 | `-1.96%` | `33.44` / `55.12` | `39.97` | `0.109` | `NONE` | 660.58628 | `WATCH` | HOLD |
| `HYPEUSDT` | 70.97 | 77.248208 | `-8.13%` | `18.65` / `35.99` | `35.49` | `-0.032` | `NONE` | 68.669616 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1433 | 0.160327 | `-10.62%` | `4.88` / `9.75` | `26.74` | `-0.276` | `NONE` | 0.13728326 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1516 | 0.165207 | `-8.24%` | `6.61` / `10.4` | `27.86` | `-0.217` | `NONE` | 0.14568496 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.516 | 7.949984 | `-5.46%` | `5.75` / `10.52` | `28.71` | `-0.111` | `NONE` | 7.2484624 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06691 | 0.071036 | `-5.81%` | `23.86` / `37.23` | `33.29` | `-0.143` | `NONE` | 0.06497489 | `WATCH` | HOLD |
| `LINKUSDT` | 10.065 | 10.746998 | `-6.35%` | `15.31` / `32.11` | `30.22` | `-0.235` | `NONE` | 9.766362 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SUIUSDT` | 0.814 | 0.854576 | `-4.75%` | `18.77` / `35.05` | `35.36` | `-0.06` | `NONE` | 0.7897384 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AVAXUSDT` | 8.439 | 8.445377 | `-0.08%` | `28.67` / `42.79` | `42.33` | `0.036` | `BEARISH_ENGULFING` | 8.168025 | `WATCH` | **HOLD** (75%) |
