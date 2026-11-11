# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T09:16:51Z`
- **Ciclo de ejecucion:** `#123`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado presenta un sesgo predominantemente bajista con la mayoria de los activos cotizando por debajo de la EMA 200 de 1H. Se identifica una oportunidad operativa de SHORT en BTCUSDT al activarse el Pilar S1 (Rechazo en Resistencia EMA 200) impulsado por una vela Bearish Shooting Star. El candidato INITUSDT se descarta para entrada LONG debido a una extension sobrecomprada excesiva respecto a la EMA 200 (+33.22%). No hay posiciones abiertas actualmente para ajuste de trailing stop.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 972.14 | 1204.282733 | `-19.28%` | `16.87` / `18.09` | `28.95` | `0.163` | `BEARISH_ENGULFING` | 927.42156 | `EXIT_SHORT_STOCH_20` | **HOLD** (20%) |
| `UNIUSDT` | 6.377 | 6.9793 | `-8.63%` | `9.52` / `11.58` | `25.77` | `0.021` | `BEARISH_ENGULFING` | 6.1514574 | `EXIT_SHORT_STOCH_20` | **HOLD** (20%) |
| `PEPEUSDT` | 4.98e-06 | 5e-06 | `-1.76%` | `9.52` / `18.78` | `33.41` | `-0.132` | `NONE` | 4.75e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001579 | 0.001556 | `+1.50%` | `6.9` / `11.5` | `39.34` | `-0.023` | `NONE` | 0.00150637 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INITUSDT` | 0.22865 | 0.171639 | `+33.22%` | `22.19` / `20.61` | `46.38` | `0.103` | `BULLISH_ENGULFING` | 0.2181321 | `P1_EMA200_PULLBACK` | **HOLD** (35%) |
| `ARBUSDT` | 0.1591 | 0.166119 | `-4.23%` | `18.9` / `24.59` | `38.42` | `0.315` | `BEARISH_SHOOTING_STAR` | 0.15240426 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 177.86 | 193.521862 | `-8.09%` | `18.23` / `28.0` | `32.34` | `0.046` | `BEARISH_ENGULFING` | 172.77136 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRXUSDT` | 0.3177 | 0.3183 | `-0.19%` | `23.08` / `24.34` | `45.32` | `0.38` | `BULLISH_ENGULFING` | 0.3094398 | `WATCH` | HOLD |
| `BTCUSDT` | 73680.01 | 75736.287897 | `-2.72%` | `66.58` / `74.54` | `45.83` | `0.516` | `BEARISH_SHOOTING_STAR` | 75595.69026 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `ETHUSDT` | 2055.34 | 2187.600812 | `-6.05%` | `65.67` / `75.15` | `43.31` | `0.537` | `NONE` | 2001.90116 | `WATCH` | HOLD |
| `CYBERUSDT` | 0.266 | 0.281381 | `-5.47%` | `6.51` / `5.09` | `43.04` | `0.224` | `BEARISH_ENGULFING` | 0.253764 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 82.95 | 88.828913 | `-6.62%` | `46.33` / `50.24` | `42.13` | `0.451` | `BEARISH_SHOOTING_STAR` | 80.7933 | `WATCH` | **HOLD** (30%) |
| `XRPUSDT` | 1.0572 | 1.155377 | `-8.50%` | `44.59` / `45.77` | `43.08` | `0.5` | `BEARISH_SHOOTING_STAR` | 1.0297128 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0837 | 0.073282 | `+14.22%` | `35.76` / `54.12` | `56.49` | `0.666` | `BULLISH_HAMMER` | 0.0798498 | `WATCH` | HOLD |
| `NEARUSDT` | 3.579 | 3.770425 | `-5.08%` | `36.63` / `47.61` | `45.55` | `0.375` | `BEARISH_ENGULFING` | 3.4410192 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.001 | 1.001202 | `-0.02%` | `40.0` / `49.52` | `42.68` | `0.338` | `BULLISH_HAMMER` | 0.974974 | `WATCH` | HOLD |
