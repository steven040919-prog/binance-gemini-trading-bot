# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T17:11:15Z`
- **Ciclo de ejecucion:** `#138`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `SIDEWAYS`

## Lectura de Mercado de Gemini AI
> Evaluacion del mercado en 1H: No se activan gatillos de entrada bajo los Pilares LONG (P1-P4) ni SHORT (S1). La mayor parte de las altcoins muestran condiciones neutrales o de sobreventa sin patron de giro validado ni confluencia estocastica alcista (stoch_turning_up == false en soportes claves). Sin posiciones abiertas activas para ajustar SL/TP.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ONEUSDT` | 0.001567 | 0.001557 | `+0.67%` | `12.67` / `12.49` | `41.03` | `0.293` | `NONE` | 0.00149492 | `EXIT_SHORT_STOCH_20` | **HOLD** (55%) |
| `PEPEUSDT` | 4.98e-06 | 5e-06 | `-1.57%` | `11.43` / `8.94` | `36.3` | `0.244` | `NONE` | 4.75e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74156.4 | 75608.208671 | `-1.92%` | `70.95` / `61.39` | `53.61` | `0.905` | `MORNING_STAR` | 72228.3336 | `WATCH` | **HOLD** (60%) |
| `TRXUSDT` | 0.3164 | 0.317332 | `-0.29%` | `10.56` / `15.51` | `30.02` | `-0.068` | `NONE` | 0.3081736 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3991.21 | 4034.50883 | `-1.07%` | `3.56` / `6.78` | `24.41` | `-0.03` | `NONE` | 3887.43854 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2079.19 | 2178.749307 | `-4.57%` | `71.19` / `60.29` | `55.85` | `1.018` | `NONE` | 2020.019664 | `WATCH` | **HOLD** (50%) |
| `MUBUSDT` | 821.15 | 751.883357 | `+9.21%` | `96.65` / `96.64` | `79.61` | `0.986` | `BULLISH_HAMMER` | 783.3771 | `EXIT_LONG_STOCH_80` | HOLD |
| `PAXGUSDT` | 3993.97 | 4040.113937 | `-1.14%` | `3.05` / `6.93` | `24.55` | `-0.032` | `NONE` | 3890.12678 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.783 | 3.768417 | `+0.39%` | `85.09` / `79.67` | `60.53` | `0.859` | `BEARISH_SHOOTING_STAR` | 3.608982 | `EXIT_LONG_STOCH_80` | **HOLD** (55%) |
| `SOLUSDT` | 84.82 | 88.47469 | `-4.13%` | `82.05` / `80.84` | `57.65` | `0.931` | `BEARISH_ENGULFING` | 82.031456 | `EXIT_LONG_STOCH_80` | **HOLD** (50%) |
| `SOXSBUSDT` | 43.03 | 60.14484 | `-28.46%` | `3.1` / `8.46` | `26.64` | `0.064` | `NONE` | 41.05062 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SNXXBUSDT` | 4.55 | 4.169728 | `+9.12%` | `95.06` / `95.5` | `75.44` | `0.948` | `BULLISH_HAMMER` | 4.3407 | `EXIT_LONG_STOCH_80` | HOLD |
| `ZECUSDT` | 1008.89 | 1185.957341 | `-14.93%` | `52.36` / `38.24` | `45.01` | `0.553` | `BEARISH_SHOOTING_STAR` | 962.48106 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0704 | 1.148509 | `-6.80%` | `73.54` / `68.43` | `54.25` | `0.978` | `BEARISH_SHOOTING_STAR` | 1.03630464 | `WATCH` | HOLD |
| `SKHYBUSDT` | 144.98 | 135.571883 | `+6.94%` | `95.96` / `93.07` | `74.54` | `0.91` | `MORNING_STAR` | 138.31092 | `EXIT_LONG_STOCH_80` | HOLD |
| `GRAMUSDT` | 1.194 | 1.116899 | `+6.90%` | `51.63` / `58.75` | `58.94` | `0.666` | `BEARISH_SHOOTING_STAR` | 1.139076 | `WATCH` | HOLD |
