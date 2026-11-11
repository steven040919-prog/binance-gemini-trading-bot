# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T18:29:11Z`
- **Ciclo de ejecucion:** `#143`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general opera bajo un régimen bajista con la mayoría de los activos cotizando por debajo de la EMA 200 en la temporalidad de 1H. TRXUSDT activa una oportunidad de alta probabilidad mediante el Pilar 2 LONG (Capitulación Institucional de Doble Sobreventa), mostrando una fuerte envolvente alcista con estocástico girando al alza desde sobreventa y volumen institucional superior a la media. No existen posiciones abiertas que requieran ajuste dinámico.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.91e-06 | 5e-06 | `-2.93%` | `6.81` / `7.74` | `31.31` | `0.191` | `BEARISH_SHOOTING_STAR` | 4.68e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001508 | 0.001556 | `-3.07%` | `4.04` / `8.59` | `36.05` | `0.216` | `NONE` | 0.00143863 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74460.0 | 75602.887768 | `-1.51%` | `79.5` / `71.26` | `57.98` | `1.025` | `NONE` | 72524.04 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3168 | 0.317392 | `-0.19%` | `12.86` / `12.06` | `40.18` | `0.203` | `BULLISH_ENGULFING` | 0.3085632 | `P2_EXTREME_CAPITULATION` | **BUY** (88%) |
| `INJUSDT` | 7.938 | 7.949208 | `-0.14%` | `25.77` / `24.24` | `45.21` | `0.304` | `BEARISH_ENGULFING` | 7.653108 | `WATCH` | HOLD |
| `XAUTUSDT` | 3985.36 | 4033.972349 | `-1.21%` | `3.15` / `3.92` | `22.82` | `-0.001` | `BULLISH_HAMMER` | 3881.74064 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1588 | 0.165668 | `-4.15%` | `33.55` / `35.07` | `41.41` | `0.221` | `NONE` | 0.15367248 | `WATCH` | HOLD |
| `ETHUSDT` | 2087.28 | 2178.025164 | `-4.17%` | `74.17` / `68.37` | `58.4` | `1.028` | `NONE` | 2033.01072 | `WATCH` | HOLD |
| `MUBUSDT` | 824.67 | 752.763821 | `+9.55%` | `95.7` / `96.89` | `81.48` | `0.956` | `NONE` | 788.609504 | `EXIT_LONG_STOCH_80` | HOLD |
| `PAXGUSDT` | 3988.1 | 4039.634498 | `-1.28%` | `2.15` / `3.53` | `22.96` | `-0.0` | `BULLISH_HAMMER` | 3884.4094 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 1006.75 | 1184.188684 | `-14.98%` | `65.97` / `50.87` | `44.48` | `0.551` | `NONE` | 960.4395 | `WATCH` | HOLD |
| `SOXSBUSDT` | 42.24 | 59.953989 | `-29.55%` | `4.69` / `5.94` | `23.91` | `0.049` | `BEARISH_SHOOTING_STAR` | 40.29696 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 85.14 | 88.448216 | `-3.74%` | `83.01` / `81.77` | `59.41` | `0.936` | `NONE` | 82.814228 | `EXIT_LONG_STOCH_80` | HOLD |
| `SNXXBUSDT` | 4.62 | 4.174701 | `+10.67%` | `95.71` / `96.72` | `78.9` | `0.936` | `BEARISH_ENGULFING` | 4.40748 | `EXIT_LONG_STOCH_80` | HOLD |
| `NEARUSDT` | 3.728 | 3.768432 | `-1.07%` | `76.91` / `77.92` | `54.73` | `0.662` | `NONE` | 3.5803712 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.206 | 1.118394 | `+7.83%` | `60.77` / `57.88` | `59.89` | `0.711` | `MORNING_STAR` | 1.150524 | `WATCH` | HOLD |
