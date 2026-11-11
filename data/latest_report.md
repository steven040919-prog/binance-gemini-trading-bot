# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T01:04:12Z`
- **Ciclo de ejecucion:** `#81`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen mayoritariamente bajista (BEARISH) con la mayoría de los activos cotizando por debajo de la EMA 200 en la temporalidad de 1H. No se cumplen las condiciones estrictas de los Pilares LONG (P1-P4) debido a que los estocásticos no están en zonas de sobreventa extrema girando al alza o la tendencia es fuertemente bajista. Tampoco se activan operaciones SHORT bajo el Pilar S1 ya que ningún activo cumple simultáneamente con un testeo cercano a la resistencia de la EMA 200 en tendencia bajista con estocástico en sobrecompra y vela bajista de rechazo confirmada. El portfolio actual se mantiene con liquidez libre (14.0 USDT) y 0 posiciones abiertas, por lo que no se requieren ajustes (ADJUST). Se mantiene la vigilancia (WATCH) en los candidatos evaluados.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1027.53 | 1220.449098 | `-15.81%` | `19.95` / `22.53` | `31.4` | `0.219` | `BEARISH_ENGULFING` | 980.26362 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73433.8 | 75894.321058 | `-3.24%` | `40.72` / `44.95` | `40.72` | `0.28` | `BEARISH_ENGULFING` | 71524.5212 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0504 | 1.163437 | `-9.72%` | `38.95` / `41.83` | `35.17` | `0.237` | `NONE` | 1.02020896 | `WATCH` | HOLD |
| `UNIUSDT` | 6.684 | 7.015732 | `-4.73%` | `13.42` / `12.84` | `38.4` | `0.253` | `BEARISH_SHOOTING_STAR` | 6.376536 | `EXIT_SHORT_STOCH_20` | HOLD |
| `HYPEUSDT` | 71.78 | 78.423249 | `-8.47%` | `39.85` / `43.45` | `37.92` | `0.273` | `BEARISH_ENGULFING` | 69.715804 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1611 | 0.166414 | `-3.19%` | `46.64` / `42.4` | `40.01` | `0.393` | `BULLISH_ENGULFING` | 0.15404264 | `WATCH` | HOLD |
| `QNTUSDT` | 180.95 | 194.26841 | `-6.86%` | `40.83` / `40.43` | `32.91` | `0.285` | `BEARISH_ENGULFING` | 173.23247 | `WATCH` | HOLD |
| `AAVEUSDT` | 123.91 | 129.750274 | `-4.50%` | `53.66` / `53.74` | `38.12` | `0.37` | `BULLISH_ENGULFING` | 119.44879 | `WATCH` | HOLD |
| `XAUTUSDT` | 4025.58 | 4035.628753 | `-0.25%` | `32.11` / `28.62` | `35.29` | `0.343` | `NONE` | 3920.91492 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3181 | 0.318984 | `-0.28%` | `15.56` / `14.81` | `47.69` | `0.325` | `BULLISH_ENGULFING` | 0.3098294 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2046.07 | 2197.950467 | `-6.91%` | `42.48` / `42.48` | `37.52` | `0.323` | `NONE` | 1990.390608 | `WATCH` | HOLD |
| `INITUSDT` | 0.25678 | 0.164992 | `+55.63%` | `50.75` / `55.08` | `53.9` | `0.495` | `BEARISH_ENGULFING` | 0.24496812 | `WATCH` | HOLD |
| `PAXGUSDT` | 4027.1 | 4041.771355 | `-0.36%` | `31.24` / `27.97` | `34.92` | `0.332` | `BEARISH_ENGULFING` | 3922.3954 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001859 | 0.001543 | `+20.50%` | `56.55` / `51.55` | `60.19` | `0.662` | `BEARISH_SHOOTING_STAR` | 0.00177349 | `WATCH` | HOLD |
| `SOLUSDT` | 83.02 | 89.324948 | `-7.06%` | `45.23` / `42.78` | `37.41` | `0.328` | `NONE` | 80.434876 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.38e-06 | 5e-06 | `+6.45%` | `54.25` / `47.71` | `56.92` | `0.714` | `BEARISH_SHOOTING_STAR` | 5.13e-06 | `WATCH` | HOLD |
