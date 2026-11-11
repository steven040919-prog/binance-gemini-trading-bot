# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T10:04:23Z`
- **Ciclo de ejecucion:** `#126`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra predominantemente en tendencia bajista macro con BTC y ETH cotizando por debajo de sus respectivas EMA 200. Tras evaluar los 16 candidatos bajo la arquitectura de 4 Pilares LONG y 1 Pilar SHORT (S1), ninguno cumple con la totalidad de los criterios de entrada institucional (falta de giro confirmado en el Estocastico, confluencia de sobreventa/sobrecompra extrema o patrones de gatillo especificos). No hay posiciones abiertas para ajustar SL/TP. Se preserva el capital manteniendo liquidez del 100%.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 980.36 | 1202.668024 | `-18.48%` | `13.72` / `16.41` | `31.72` | `0.134` | `BEARISH_SHOOTING_STAR` | 935.26344 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `UNIUSDT` | 6.397 | 6.975272 | `-8.29%` | `9.57` / `10.73` | `26.79` | `0.038` | `BULLISH_HAMMER` | 6.1327372 | `EXIT_SHORT_STOCH_20` | **HOLD** (82%) |
| `INITUSDT` | 0.20336 | 0.171611 | `+18.50%` | `16.47` / `18.28` | `43.06` | `0.013` | `BEARISH_ENGULFING` | 0.19400544 | `EXIT_SHORT_STOCH_20` | **HOLD** (80%) |
| `PEPEUSDT` | 5.02e-06 | 5e-06 | `-0.91%` | `9.94` / `12.83` | `34.9` | `-0.036` | `BULLISH_HAMMER` | 4.79e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (80%) |
| `ONEUSDT` | 0.001556 | 0.001557 | `-0.06%` | `5.72` / `7.06` | `38.11` | `0.016` | `NONE` | 0.00148442 | `EXIT_SHORT_STOCH_20` | **HOLD** (80%) |
| `ARBUSDT` | 0.1588 | 0.166148 | `-4.42%` | `16.38` / `19.7` | `38.06` | `0.302` | `BULLISH_HAMMER` | 0.15330896 | `EXIT_SHORT_STOCH_20` | **HOLD** (80%) |
| `QNTUSDT` | 178.55 | 193.534769 | `-7.74%` | `20.33` / `23.56` | `36.46` | `0.146` | `NONE` | 172.86193 | `WATCH` | **HOLD** (80%) |
| `TRXUSDT` | 0.3177 | 0.318079 | `-0.12%` | `23.08` / `23.08` | `45.32` | `0.394` | `BULLISH_ENGULFING` | 0.3094398 | `WATCH` | **HOLD** (85%) |
| `BTCUSDT` | 73768.01 | 75731.30492 | `-2.59%` | `56.98` / `66.59` | `47.2` | `0.627` | `BULLISH_HAMMER` | 71850.04174 | `WATCH` | **HOLD** (85%) |
| `CYBERUSDT` | 0.266 | 0.281153 | `-5.39%` | `6.51` / `5.78` | `43.04` | `0.246` | `BEARISH_SHOOTING_STAR` | 0.253764 | `EXIT_SHORT_STOCH_20` | **HOLD** (80%) |
| `ETHUSDT` | 2055.25 | 2186.641679 | `-6.01%` | `51.36` / `64.54` | `43.2` | `0.562` | `BULLISH_HAMMER` | 2001.8135 | `WATCH` | **HOLD** (85%) |
| `ERAUSDT` | 0.0867 | 0.073416 | `+18.09%` | `43.52` / `45.36` | `60.91` | `0.834` | `BULLISH_ENGULFING` | 0.0827118 | `WATCH` | **HOLD** (80%) |
| `SOLUSDT` | 83.44 | 88.798778 | `-6.03%` | `58.99` / `54.65` | `46.96` | `0.74` | `BULLISH_ENGULFING` | 81.27056 | `WATCH` | **HOLD** (80%) |
| `XRPUSDT` | 1.058 | 1.15467 | `-8.37%` | `51.54` / `47.22` | `43.97` | `0.541` | `BULLISH_ENGULFING` | 1.030492 | `WATCH` | **HOLD** (80%) |
| `GRAMUSDT` | 1.193 | 1.111308 | `+7.35%` | `88.64` / `84.01` | `75.27` | `1.069` | `NONE` | 1.138122 | `EXIT_LONG_STOCH_80` | **HOLD** (85%) |
| `RLUSDUSDT` | 1.001 | 1.0012 | `-0.02%` | `33.33` / `41.9` | `42.68` | `0.349` | `BULLISH_HAMMER` | 0.974974 | `WATCH` | **HOLD** (90%) |
