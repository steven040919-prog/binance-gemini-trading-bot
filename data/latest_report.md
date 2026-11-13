# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T14:04:10Z`
- **Ciclo de ejecucion:** `#331`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> Mercado macro predominantemente bajista por debajo de la EMA 200 en la mayoria de los activos. Se detecta una oportunidad alcista clara en ERAUSDT bajo el Pilar 1 (Pullback a la EMA 200 con vela Envolvente Alcista y giro en Estocastico) y una oportunidad de Venta en Corto en HYPEUSDT bajo el Pilar S1 (Rechazo en Resistencia EMA 200 con vela Shooting Star y sobrecompra en Estocastico/RSI/Bollinger). No hay posiciones abiertas pendientes de ajuste dinamico.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.0784 | 0.077908 | `+0.63%` | `26.05` / `18.52` | `39.83` | `0.233` | `BULLISH_ENGULFING` | 0.0747936 | `P1_EMA200_PULLBACK` | **BUY** (86%) |
| `GRAMUSDT` | 1.13 | 1.137303 | `-0.64%` | `43.09` / `51.82` | `38.67` | `0.006` | `BEARISH_ENGULFING` | 1.078066 | `WATCH` | HOLD |
| `BTCUSDT` | 69482.01 | 74100.384752 | `-6.23%` | `47.95` / `45.31` | `38.31` | `0.411` | `BULLISH_ENGULFING` | 67567.328584 | `WATCH` | HOLD |
| `ETHUSDT` | 1965.95 | 2115.698419 | `-7.08%` | `54.9` / `52.03` | `43.66` | `0.464` | `BEARISH_SHOOTING_STAR` | 1900.96125 | `WATCH` | HOLD |
| `SOLUSDT` | 81.47 | 85.770855 | `-5.01%` | `76.97` / `73.38` | `54.79` | `0.72` | `BULLISH_HAMMER` | 78.525838 | `WATCH` | HOLD |
| `DODOUSDT` | 0.02827 | 0.023744 | `+19.06%` | `64.66` / `69.74` | `58.33` | `0.598` | `NONE` | 0.02696958 | `WATCH` | HOLD |
| `ZECUSDT` | 966.17 | 1097.848624 | `-11.99%` | `80.59` / `83.4` | `54.17` | `0.761` | `BEARISH_SHOOTING_STAR` | 1010.61382 | `S1_EMA200_RESISTANCE_REJECT` | HOLD |
| `NEARUSDT` | 3.573 | 3.632176 | `-1.63%` | `84.69` / `86.75` | `60.03` | `0.87` | `BULLISH_ENGULFING` | 3.408642 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 642.2 | 678.766829 | `-5.39%` | `55.46` / `51.78` | `43.35` | `0.477` | `BEARISH_SHOOTING_STAR` | 624.48628 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.55e-06 | 5e-06 | `-6.14%` | `48.15` / `41.57` | `51.44` | `0.638` | `BEARISH_SHOOTING_STAR` | 4.34e-06 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0322 | 1.107442 | `-6.79%` | `66.42` / `59.8` | `51.96` | `0.645` | `BULLISH_ENGULFING` | 0.99093364 | `WATCH` | HOLD |
| `HYPEUSDT` | 74.18 | 75.243485 | `-1.41%` | `82.86` / `88.76` | `64.82` | `0.908` | `BEARISH_SHOOTING_STAR` | 77.42704 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (88%) |
| `INJUSDT` | 8.171 | 7.782891 | `+4.99%` | `91.23` / `92.77` | `75.37` | `1.101` | `NONE` | 7.795134 | `EXIT_LONG_STOCH_80` | HOLD |
| `INITUSDT` | 0.11644 | 0.151252 | `-23.02%` | `26.91` / `36.22` | `42.78` | `0.389` | `NONE` | 0.11108376 | `WATCH` | HOLD |
| `UNIUSDT` | 5.951 | 6.613627 | `-10.02%` | `58.51` / `48.17` | `50.26` | `0.606` | `BULLISH_HAMMER` | 5.677254 | `WATCH` | HOLD |
| `SUIUSDT` | 0.8178 | 0.835906 | `-2.17%` | `85.56` / `86.69` | `61.63` | `0.876` | `NONE` | 0.7801812 | `EXIT_LONG_STOCH_80` | HOLD |
