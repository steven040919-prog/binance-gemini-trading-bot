# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T16:40:07Z`
- **Ciclo de ejecucion:** `#136`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `SIDEWAYS`

## Lectura de Mercado de Gemini AI
> Analisis de mercado en temporalidad 1H. Se identifica la oportunidad de entrada en ONEUSDT bajo el Pilar 1 (P1_EMA200_PULLBACK) cumpliendo las condiciones de valor sobre EMA 200 con estocastico girando al alza y patron de martillo alcista. No hay posiciones abiertas actuales para gestionar, por lo que el capital disponible se asigna de forma eficiente.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.96e-06 | 5e-06 | `-2.07%` | `7.51` / `7.76` | `34.12` | `0.191` | `BEARISH_SHOOTING_STAR` | 4.73e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001563 | 0.001556 | `+0.42%` | `13.58` / `11.1` | `40.31` | `0.262` | `BULLISH_HAMMER` | 0.0014911 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `BTCUSDT` | 74286.79 | 75633.118052 | `-1.78%` | `60.64` / `56.72` | `55.89` | `1.12` | `MORNING_STAR` | 72355.33346 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3163 | 0.317497 | `-0.38%` | `11.11` / `18.43` | `29.19` | `-0.2` | `NONE` | 0.3080762 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3993.65 | 4035.017151 | `-1.03%` | `4.8` / `12.46` | `25.11` | `-0.095` | `NONE` | 3889.8151 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2077.64 | 2179.824661 | `-4.69%` | `58.69` / `50.05` | `55.14` | `1.071` | `NONE` | 2013.650928 | `WATCH` | HOLD |
| `PAXGUSDT` | 3996.52 | 4040.650576 | `-1.09%` | `5.38` / `12.99` | `25.27` | `-0.099` | `NONE` | 3892.61048 | `EXIT_SHORT_STOCH_20` | HOLD |
| `MUBUSDT` | 820.49 | 751.37036 | `+9.20%` | `97.74` / `95.1` | `82.01` | `1.064` | `BULLISH_HAMMER` | 782.74746 | `EXIT_LONG_STOCH_80` | HOLD |
| `NEARUSDT` | 3.775 | 3.770851 | `+0.11%` | `75.2` / `76.72` | `60.15` | `0.882` | `BEARISH_SHOOTING_STAR` | 3.60135 | `WATCH` | HOLD |
| `SOLUSDT` | 84.77 | 88.544085 | `-4.26%` | `77.45` / `80.91` | `57.27` | `0.988` | `BULLISH_ENGULFING` | 81.981554 | `EXIT_LONG_STOCH_80` | HOLD |
| `ZECUSDT` | 1011.65 | 1189.659164 | `-14.96%` | `36.51` / `29.5` | `45.73` | `0.548` | `BEARISH_SHOOTING_STAR` | 965.1141 | `WATCH` | HOLD |
| `SOXSBUSDT` | 43.73 | 60.325191 | `-27.51%` | `10.57` / `12.5` | `26.35` | `0.053` | `BEARISH_SHOOTING_STAR` | 41.71842 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SNXXBUSDT` | 4.59 | 4.166159 | `+10.17%` | `97.23` / `93.15` | `79.46` | `1.052` | `BULLISH_HAMMER` | 4.37886 | `EXIT_LONG_STOCH_80` | HOLD |
| `XRPUSDT` | 1.0713 | 1.1494 | `-6.79%` | `66.68` / `62.83` | `55.02` | `1.096` | `BULLISH_ENGULFING` | 1.03213104 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.195 | 1.116285 | `+7.05%` | `55.33` / `69.27` | `59.13` | `0.687` | `NONE` | 1.14003 | `WATCH` | HOLD |
| `SKHYBUSDT` | 145.15 | 135.478003 | `+7.14%` | `93.33` / `89.96` | `77.11` | `0.958` | `BULLISH_ENGULFING` | 138.4731 | `EXIT_LONG_STOCH_80` | HOLD |
