# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T17:26:40Z`
- **Ciclo de ejecucion:** `#139`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global de criptomonedas se mantiene bajo un sesgo bajista generalizado con la mayoría de los activos operando por debajo de la EMA 200 en temporalidad de 1H. No se cumplen los requisitos estrictos de los Pilares 1 al 4 para aperturas LONG, ni tampoco se activa el Pilar S1 SHORT ya que los candidatos bajistas no muestran simultáneamente el rebote exacto hacia la resistencia de la EMA 200 con sobrecompra en el estocástico requerida. Con 0 posiciones abiertas y un portafolio libre de USDT de 14.0, el bot permanece en modo de observación (HOLD) esperando formaciones de alta probabilidad institucional.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.98e-06 | 5e-06 | `-1.57%` | `11.43` / `8.94` | `36.3` | `0.244` | `NONE` | 4.75e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001552 | 0.001556 | `-0.29%` | `11.18` / `11.99` | `39.43` | `0.267` | `BEARISH_SHOOTING_STAR` | 0.00148061 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74601.42 | 75612.636731 | `-1.34%` | `76.43` / `63.22` | `60.19` | `1.239` | `MORNING_STAR` | 72489.862676 | `WATCH` | **HOLD** (50%) |
| `TRXUSDT` | 0.3165 | 0.317333 | `-0.26%` | `12.22` / `16.06` | `31.05` | `-0.029` | `NONE` | 0.308271 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3996.29 | 4034.559377 | `-0.95%` | `6.14` / `7.64` | `28.05` | `0.024` | `NONE` | 3892.38646 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2096.07 | 2178.917267 | `-3.80%` | `75.12` / `61.6` | `62.29` | `1.277` | `NONE` | 2016.842094 | `WATCH` | HOLD |
| `MUBUSDT` | 823.87 | 751.910422 | `+9.57%` | `97.91` / `97.06` | `81.83` | `1.005` | `BULLISH_HAMMER` | 785.97198 | `EXIT_LONG_STOCH_80` | HOLD |
| `PAXGUSDT` | 3998.64 | 4040.160405 | `-1.03%` | `5.46` / `7.73` | `28.03` | `0.018` | `NONE` | 3894.67536 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.789 | 3.768476 | `+0.54%` | `85.18` / `79.7` | `61.14` | `0.877` | `BEARISH_SHOOTING_STAR` | 3.614706 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 85.55 | 88.481954 | `-3.31%` | `85.55` / `82.01` | `63.1` | `1.116` | `NONE` | 81.91478 | `EXIT_LONG_STOCH_80` | HOLD |
| `ZECUSDT` | 1014.43 | 1186.012465 | `-14.47%` | `54.98` / `39.11` | `46.57` | `0.612` | `NONE` | 967.76622 | `WATCH` | HOLD |
| `SOXSBUSDT` | 42.42 | 60.13877 | `-29.46%` | `2.0` / `8.09` | `24.22` | `0.027` | `BEARISH_SHOOTING_STAR` | 40.46868 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SNXXBUSDT` | 4.55 | 4.169728 | `+9.12%` | `95.06` / `95.5` | `75.44` | `0.948` | `BULLISH_HAMMER` | 4.3407 | `EXIT_LONG_STOCH_80` | HOLD |
| `XRPUSDT` | 1.0756 | 1.14856 | `-6.35%` | `78.15` / `69.96` | `57.89` | `1.133` | `BULLISH_ENGULFING` | 1.03534848 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.218 | 1.117138 | `+9.03%` | `57.79` / `60.81` | `63.36` | `0.813` | `MORNING_STAR` | 1.161972 | `WATCH` | HOLD |
| `SKHYBUSDT` | 144.95 | 135.571584 | `+6.92%` | `95.83` / `93.03` | `74.39` | `0.908` | `MORNING_STAR` | 138.2823 | `EXIT_LONG_STOCH_80` | HOLD |
