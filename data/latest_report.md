# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T18:46:12Z`
- **Ciclo de ejecucion:** `#250`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado opera bajo un régimen bajista generalizado en temporalidad de 1H, con la mayoría de los activos cotizando por debajo de sus respectivas EMA 200 y registrando descensos en las últimas 24 horas. Se identifican configuraciones de venta en corto (SHORT) mediante el pilar scalper M15 en SOLUSDT y AAVEUSDT, aprovechando el rechazo en las medias móviles rápidas y la debilidad del estocástico. No se detectan posiciones abiertas previas para realizar ajustes de SL/TP, y el resto de los candidatos se mantiene en observación (WATCH) a la espera de confirmaciones institucionales adicionales.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71752.61 | 75149.608864 | `-4.52%` | `21.34` / `19.08` | `25.11` | `0.108` | `BEARISH_ENGULFING` | 69887.04214 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 937.28 | 1138.769609 | `-17.69%` | `13.39` / `21.11` | `30.18` | `-0.088` | `NONE` | 894.16512 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PEPEUSDT` | 4.39e-06 | 5e-06 | `-10.96%` | `21.36` / `19.09` | `33.05` | `0.287` | `BULLISH_ENGULFING` | 4.19e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 81.6 | 87.179592 | `-6.40%` | `36.01` / `33.8` | `36.15` | `0.182` | `BEARISH_SHOOTING_STAR` | 83.84304 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (78%) |
| `NEARUSDT` | 3.414 | 3.704079 | `-7.83%` | `30.48` / `27.21` | `34.93` | `0.249` | `BEARISH_ENGULFING` | 3.2631176 | `WATCH` | HOLD |
| `UNIUSDT` | 6.0 | 6.788502 | `-11.62%` | `23.44` / `25.01` | `28.17` | `0.127` | `BEARISH_ENGULFING` | 5.7972 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0285 | 1.125377 | `-8.61%` | `28.47` / `25.65` | `35.61` | `0.174` | `BULLISH_ENGULFING` | 0.9999414 | `WATCH` | HOLD |
| `BNBUSDT` | 654.78 | 688.030314 | `-4.83%` | `20.68` / `18.53` | `24.23` | `0.157` | `BULLISH_HAMMER` | 637.75572 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1397 | 0.156799 | `-10.91%` | `29.63` / `27.83` | `29.84` | `0.268` | `BULLISH_HAMMER` | 0.1332738 | `WATCH` | HOLD |
| `AAVEUSDT` | 113.16 | 126.352461 | `-10.44%` | `31.87` / `30.77` | `29.54` | `0.227` | `BEARISH_ENGULFING` | 117.57216 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (76%) |
| `XAUTUSDT` | 3878.76 | 4014.856737 | `-3.39%` | `19.66` / `16.03` | `26.78` | `0.17` | `BULLISH_ENGULFING` | 3777.91224 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SUIUSDT` | 0.7977 | 0.846483 | `-5.76%` | `39.79` / `34.84` | `34.34` | `0.221` | `BULLISH_HAMMER` | 0.7744529 | `WATCH` | HOLD |
| `QNTUSDT` | 161.19 | 186.909137 | `-13.76%` | `15.98` / `19.8` | `28.41` | `0.08` | `BEARISH_ENGULFING` | 155.565348 | `EXIT_SHORT_STOCH_20` | HOLD |
| `GRAMUSDT` | 1.186 | 1.138947 | `+4.13%` | `42.82` / `61.48` | `44.31` | `0.265` | `NONE` | 1.131444 | `WATCH` | HOLD |
| `INJUSDT` | 7.354 | 7.852545 | `-6.35%` | `25.35` / `25.89` | `36.22` | `0.153` | `BEARISH_ENGULFING` | 7.0691428 | `WATCH` | HOLD |
| `AVAXUSDT` | 8.356 | 8.446389 | `-1.07%` | `22.01` / `23.07` | `40.43` | `0.202` | `BULLISH_ENGULFING` | 8.0680728 | `WATCH` | HOLD |
