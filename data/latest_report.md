# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T16:24:38Z`
- **Ciclo de ejecucion:** `#135`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BULLISH`

## Lectura de Mercado de Gemini AI
> Evaluación horaria (1H) completada bajo la estrategia multi-pilar. Se detecta configuración alcista limpia en ONEUSDT activando el Pilar 1 LONG (Pullback de valor sobre EMA 200 con patrón de martillo y estocástico girando al alza). El resto de activos se mantienen en vigilancia o sin posiciones abiertas con ganancia que requieran ajuste dinámico (ADJUST).

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ONEUSDT` | 0.001571 | 0.001556 | `+0.93%` | `14.28` / `11.33` | `40.96` | `0.276` | `BULLISH_HAMMER` | 0.00149873 | `P1_EMA200_PULLBACK` | **BUY** (89%) |
| `PEPEUSDT` | 5e-06 | 5e-06 | `-1.29%` | `9.89` / `8.56` | `38.06` | `0.24` | `BEARISH_SHOOTING_STAR` | 4.77e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74272.04 | 75632.971286 | `-1.80%` | `60.18` / `56.57` | `55.69` | `1.107` | `MORNING_STAR` | 72340.96696 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3164 | 0.317498 | `-0.35%` | `12.78` / `18.98` | `30.09` | `-0.167` | `NONE` | 0.3081736 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3997.96 | 4035.060036 | `-0.92%` | `7.07` / `13.22` | `26.75` | `-0.047` | `NONE` | 3894.01304 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2079.86 | 2179.84675 | `-4.59%` | `60.29` / `50.58` | `56.07` | `1.118` | `BULLISH_HAMMER` | 2013.618072 | `WATCH` | HOLD |
| `ZECUSDT` | 1009.14 | 1189.634188 | `-15.17%` | `35.43` / `29.14` | `45.07` | `0.524` | `BEARISH_SHOOTING_STAR` | 962.71956 | `WATCH` | HOLD |
| `PAXGUSDT` | 3999.75 | 4040.682715 | `-1.01%` | `7.1` / `13.57` | `26.22` | `-0.063` | `NONE` | 3895.7565 | `EXIT_SHORT_STOCH_20` | HOLD |
| `MUBUSDT` | 817.23 | 751.337922 | `+8.77%` | `96.38` / `94.65` | `79.4` | `1.041` | `NONE` | 779.63742 | `EXIT_LONG_STOCH_80` | HOLD |
| `NEARUSDT` | 3.791 | 3.771011 | `+0.53%` | `77.37` / `77.44` | `61.26` | `0.928` | `BEARISH_SHOOTING_STAR` | 3.616614 | `WATCH` | HOLD |
| `SOLUSDT` | 84.93 | 88.545677 | `-4.08%` | `79.16` / `81.48` | `58.69` | `1.036` | `BULLISH_ENGULFING` | 81.978386 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOXSBUSDT` | 44.42 | 60.332057 | `-26.37%` | `11.48` / `12.81` | `28.78` | `0.098` | `BEARISH_SHOOTING_STAR` | 42.37668 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SNXXBUSDT` | 4.51 | 4.165363 | `+8.27%` | `94.42` / `92.21` | `74.72` | `1.005` | `NONE` | 4.30254 | `EXIT_LONG_STOCH_80` | HOLD |
| `XRPUSDT` | 1.0759 | 1.149446 | `-6.40%` | `71.83` / `64.54` | `58.21` | `1.225` | `BULLISH_ENGULFING` | 1.03247308 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.202 | 1.116354 | `+7.67%` | `57.13` / `69.87` | `60.42` | `0.732` | `NONE` | 1.146708 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0011 | 1.001191 | `-0.01%` | `42.86` / `38.1` | `52.34` | `0.545` | `BULLISH_ENGULFING` | 0.9750714 | `WATCH` | HOLD |
