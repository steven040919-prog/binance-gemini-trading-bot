# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T09:01:23Z`
- **Ciclo de ejecucion:** `#219`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado opera de manera generalizada bajo la EMA 200 en temporalidad de 1H con un régimen fuertemente bajista. Se evalúan los pilares de la estrategia detectando baja volatilidad en volumen, sin confirmaciones de entrada LONG óptimas bajo los filtros estrictos de los Pilares P1-P4 (ya que la mayoría de activos se encuentran en tendencia bajista primaria sin el cruce alcista definitivo o en zonas de pullback no válidas). Se prioriza la preservación de capital y se mantiene el monitoreo de los activos principales.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 73589.92 | 75396.230986 | `-2.40%` | `13.93` / `12.45` | `42.78` | `0.237` | `NONE` | 71676.58208 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `PEPEUSDT` | 4.46e-06 | 5e-06 | `-10.49%` | `7.78` / `7.19` | `22.45` | `0.215` | `BEARISH_SHOOTING_STAR` | 4.27e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2050.06 | 2162.278958 | `-5.19%` | `28.52` / `23.72` | `43.21` | `0.276` | `BULLISH_HAMMER` | 1996.75844 | `WATCH` | HOLD |
| `NEARUSDT` | 3.464 | 3.73709 | `-7.31%` | `2.26` / `3.17` | `31.2` | `0.112` | `NONE` | 3.3591584 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 82.97 | 87.715952 | `-5.41%` | `26.3` / `22.84` | `41.73` | `0.251` | `BULLISH_HAMMER` | 80.81278 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0455 | 1.134231 | `-7.82%` | `24.63` / `19.0` | `40.9` | `0.263` | `NONE` | 1.018317 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.143 | 6.864391 | `-10.51%` | `8.84` / `9.33` | `31.49` | `0.224` | `BULLISH_HAMMER` | 5.91571 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1412 | 0.158599 | `-10.97%` | `1.85` / `2.18` | `23.77` | `0.166` | `NONE` | 0.13696168 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.397 | 7.8957 | `-6.32%` | `6.05` / `7.24` | `30.31` | `0.198` | `BEARISH_SHOOTING_STAR` | 7.1418166 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 672.74 | 691.116783 | `-2.66%` | `13.03` / `12.02` | `35.09` | `0.126` | `BULLISH_HAMMER` | 655.24876 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1481 | 0.16376 | `-9.56%` | `3.24` / `3.83` | `26.53` | `0.176` | `NONE` | 0.14388282 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3921.95 | 4024.488698 | `-2.55%` | `6.99` / `11.51` | `18.6` | `-0.15` | `NONE` | 3819.9793 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 164.19 | 188.86295 | `-13.06%` | `10.99` / `10.18` | `30.56` | `0.228` | `NONE` | 157.02078 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06693 | 0.070683 | `-5.31%` | `23.22` / `20.81` | `36.58` | `0.217` | `NONE` | 0.06518982 | `WATCH` | HOLD |
| `HYPEUSDT` | 71.29 | 76.720567 | `-7.08%` | `24.7` / `21.91` | `39.43` | `0.196` | `NONE` | 69.43646 | `WATCH` | HOLD |
| `LINKUSDT` | 10.08 | 10.684058 | `-5.65%` | `14.63` / `12.2` | `36.02` | `0.247` | `NONE` | 10.34208 | `M15_SCALPER_PULLBACK_SHORT` | HOLD |
