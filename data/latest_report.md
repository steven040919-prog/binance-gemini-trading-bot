# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T13:25:49Z`
- **Ciclo de ejecucion:** `#327`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de criptomonedas en temporalidad 1H se mantiene predominantemente bajista por debajo de la EMA 200 generalizada. Se evalúan candidatos bajo los Pilares LONG y SHORT de la arquitectura institucional. Destaca ERAUSDT cumpliendo con el Pilar 1 LONG (P1_EMA200_PULLBACK) al encontrarse sobre la EMA 200 con patrón de giro alcista, mientras que el resto de los activos muestra sesgo bajista estructural sin señales óptimas o con posiciones sin órdenes abiertas activas para gestión dinámica.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `GRAMUSDT` | 1.12 | 1.137577 | `-1.55%` | `47.04` / `54.24` | `36.21` | `-0.263` | `BEARISH_ENGULFING` | 1.076368 | `WATCH` | HOLD |
| `BTCUSDT` | 69219.05 | 74137.844972 | `-6.63%` | `42.3` / `42.21` | `33.84` | `0.344` | `BEARISH_SHOOTING_STAR` | 67419.3547 | `WATCH` | HOLD |
| `ETHUSDT` | 1956.09 | 2117.082333 | `-7.60%` | `49.78` / `47.26` | `39.33` | `0.388` | `BEARISH_SHOOTING_STAR` | 1903.56384 | `WATCH` | HOLD |
| `SOLUSDT` | 80.85 | 85.84072 | `-5.81%` | `72.37` / `68.43` | `49.34` | `0.583` | `BEARISH_SHOOTING_STAR` | 78.50428 | `WATCH` | HOLD |
| `ZECUSDT` | 973.04 | 1100.102692 | `-11.55%` | `90.7` / `85.83` | `56.42` | `0.87` | `NONE` | 928.28016 | `EXIT_LONG_STOCH_80` | HOLD |
| `ERAUSDT` | 0.079 | 0.077951 | `+1.35%` | `20.62` / `12.58` | `41.2` | `0.272` | `BULLISH_HAMMER` | 0.075366 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `DODOUSDT` | 0.02943 | 0.023704 | `+24.16%` | `78.73` / `72.87` | `68.9` | `0.913` | `BULLISH_HAMMER` | 0.02807622 | `WATCH` | HOLD |
| `BNBUSDT` | 640.72 | 679.176394 | `-5.66%` | `49.16` / `47.45` | `40.9` | `0.43` | `BULLISH_ENGULFING` | 624.06128 | `WATCH` | HOLD |
| `NEARUSDT` | 3.542 | 3.632532 | `-2.49%` | `90.93` / `86.96` | `57.75` | `0.834` | `NONE` | 3.379068 | `EXIT_LONG_STOCH_80` | HOLD |
| `XRPUSDT` | 1.0174 | 1.107468 | `-8.13%` | `48.99` / `53.79` | `39.72` | `0.287` | `BEARISH_ENGULFING` | 0.9909476 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.55e-06 | 5e-06 | `-6.10%` | `40.74` / `35.39` | `51.6` | `0.653` | `NONE` | 4.34e-06 | `WATCH` | HOLD |
| `HYPEUSDT` | 74.42 | 75.269513 | `-1.13%` | `96.57` / `91.82` | `66.02` | `1.007` | `NONE` | 70.99668 | `EXIT_LONG_STOCH_80` | HOLD |
| `UNIUSDT` | 5.85 | 6.623958 | `-11.68%` | `40.95` / `37.55` | `41.43` | `0.416` | `NONE` | 5.58174 | `WATCH` | HOLD |
| `XAUTUSDT` | 3871.36 | 3996.197025 | `-3.12%` | `13.48` / `22.76` | `33.47` | `0.162` | `NONE` | 3770.70464 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INITUSDT` | 0.117 | 0.151698 | `-22.87%` | `35.53` / `46.11` | `43.28` | `0.437` | `BULLISH_HAMMER` | 0.111618 | `WATCH` | HOLD |
| `DOGEUSDT` | 0.06541 | 0.069266 | `-5.57%` | `63.69` / `60.59` | `48.57` | `0.536` | `BEARISH_SHOOTING_STAR` | 0.06348324 | `WATCH` | HOLD |
