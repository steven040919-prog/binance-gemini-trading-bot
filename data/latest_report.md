# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T19:15:55Z`
- **Ciclo de ejecucion:** `#148`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado presenta un sesgo bajista predominante con la mayoría de los activos operando bajo la EMA 200. Se ha detectado una oportunidad de alta probabilidad en SOXSBUSDT bajo el Pilar 2 (Capitulación Extrema), cumpliendo con los criterios de sobreventa extrema, ratio de volumen y patrón de reversión. El resto de los activos se mantienen en vigilancia o en zonas de salida de posiciones previas. No hay posiciones abiertas actualmente, por lo que no se requiere ajuste dinámico de SL/TP en este ciclo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 985.15 | 1182.378547 | `-16.68%` | `51.65` / `54.15` | `39.53` | `0.315` | `NONE` | 939.8331 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001503 | 0.001555 | `-3.34%` | `2.65` / `5.27` | `35.69` | `0.233` | `BULLISH_HAMMER` | 0.00143386 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PEPEUSDT` | 4.88e-06 | 5e-06 | `-3.56%` | `3.88` / `6.29` | `29.76` | `0.189` | `NONE` | 4.66e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1501 | 0.160951 | `-6.74%` | `28.44` / `46.22` | `42.03` | `-0.089` | `NONE` | 0.1448467 | `WATCH` | HOLD |
| `BTCUSDT` | 74257.89 | 75597.878658 | `-1.77%` | `74.35` / `76.37` | `54.02` | `0.801` | `NONE` | 72327.18486 | `WATCH` | HOLD |
| `XAUTUSDT` | 3980.69 | 4033.443007 | `-1.31%` | `1.21` / `2.01` | `21.61` | `0.033` | `NONE` | 3877.19206 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1581 | 0.165579 | `-4.52%` | `20.98` / `30.58` | `39.81` | `0.168` | `NONE` | 0.15298862 | `WATCH` | HOLD |
| `INJUSDT` | 7.926 | 7.950802 | `-0.31%` | `26.15` / `26.13` | `44.79` | `0.293` | `BEARISH_ENGULFING` | 7.6556864 | `WATCH` | HOLD |
| `PAXGUSDT` | 3982.49 | 4038.960769 | `-1.40%` | `0.95` / `1.52` | `21.52` | `0.029` | `BULLISH_HAMMER` | 3878.94526 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2074.48 | 2177.460394 | `-4.73%` | `65.15` / `69.88` | `51.85` | `0.731` | `NONE` | 2020.54352 | `WATCH` | HOLD |
| `MUBUSDT` | 820.21 | 753.358927 | `+8.87%` | `93.17` / `95.45` | `76.94` | `0.875` | `BULLISH_ENGULFING` | 794.257952 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOXSBUSDT` | 43.67 | 59.796642 | `-26.97%` | `12.8` / `7.34` | `30.75` | `0.179` | `BULLISH_ENGULFING` | 41.66118 | `P2_EXTREME_CAPITULATION` | **BUY** (88%) |
| `SNXXBUSDT` | 4.55 | 4.177397 | `+8.92%` | `91.26` / `94.24` | `75.02` | `0.852` | `BEARISH_SHOOTING_STAR` | 4.3407 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 84.6 | 88.424143 | `-4.32%` | `75.66` / `80.34` | `53.78` | `0.743` | `NONE` | 82.4004 | `EXIT_LONG_STOCH_80` | HOLD |
| `GRAMUSDT` | 1.214 | 1.119042 | `+8.49%` | `71.54` / `65.25` | `60.82` | `0.725` | `BEARISH_ENGULFING` | 1.158156 | `WATCH` | HOLD |
| `NEARUSDT` | 3.697 | 3.767123 | `-1.86%` | `63.23` / `73.03` | `51.65` | `0.526` | `NONE` | 3.5371624 | `WATCH` | HOLD |
