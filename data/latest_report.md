# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T13:16:22Z`
- **Ciclo de ejecucion:** `#326`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global opera mayoritariamente bajo la EMA de 200 en temporalidad 1H, reflejando un régimen bajista. Se identifica una oportunidad clave en el activo ERAUSDT que activa el Pilar 1 (P1_EMA200_PULLBACK) con patrón de vela alcista BULLISH_HAMMER y estocástico girando al alza. No hay posiciones abiertas actuales para gestionar con SL/TP dinámico, manteniendo una postura selectiva de bajo riesgo acorde a la volatilidad actual.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `GRAMUSDT` | 1.144 | 1.137816 | `+0.54%` | `56.67` / `57.45` | `42.74` | `0.416` | `BEARISH_ENGULFING` | 1.1095952 | `WATCH` | HOLD |
| `BTCUSDT` | 69209.73 | 74137.752236 | `-6.65%` | `42.22` / `42.18` | `33.69` | `0.342` | `BEARISH_SHOOTING_STAR` | 67410.27702 | `WATCH` | HOLD |
| `INITUSDT` | 0.11437 | 0.151672 | `-24.59%` | `30.47` / `44.42` | `41.18` | `0.288` | `NONE` | 0.10910898 | `WATCH` | HOLD |
| `ETHUSDT` | 1955.77 | 2117.079149 | `-7.62%` | `49.7` / `47.23` | `39.23` | `0.386` | `BEARISH_SHOOTING_STAR` | 1903.57152 | `WATCH` | HOLD |
| `ZECUSDT` | 970.41 | 1100.076523 | `-11.79%` | `89.79` / `85.53` | `55.62` | `0.839` | `NONE` | 925.77114 | `EXIT_LONG_STOCH_80` | HOLD |
| `ERAUSDT` | 0.0784 | 0.077945 | `+0.58%` | `18.32` / `11.81` | `39.6` | `0.211` | `BULLISH_HAMMER` | 0.0747936 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `SOLUSDT` | 80.74 | 85.839626 | `-5.94%` | `71.43` / `68.11` | `48.22` | `0.558` | `BEARISH_SHOOTING_STAR` | 78.52298 | `WATCH` | HOLD |
| `DODOUSDT` | 0.02939 | 0.023703 | `+23.99%` | `78.39` / `72.75` | `68.48` | `0.904` | `BULLISH_HAMMER` | 0.02803806 | `WATCH` | HOLD |
| `NEARUSDT` | 3.551 | 3.632622 | `-2.25%` | `91.91` / `87.28` | `58.56` | `0.86` | `BULLISH_ENGULFING` | 3.387654 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 640.71 | 679.176295 | `-5.66%` | `49.15` / `47.45` | `40.88` | `0.43` | `BULLISH_ENGULFING` | 624.05154 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.55e-06 | 5e-06 | `-6.10%` | `40.74` / `35.39` | `51.6` | `0.653` | `NONE` | 4.34e-06 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0192 | 1.107486 | `-7.97%` | `50.29` / `54.22` | `40.98` | `0.33` | `BEARISH_ENGULFING` | 0.9927008 | `WATCH` | HOLD |
| `HYPEUSDT` | 74.41 | 75.269414 | `-1.14%` | `96.49` / `91.79` | `65.97` | `1.005` | `NONE` | 70.98714 | `EXIT_LONG_STOCH_80` | HOLD |
| `UNIUSDT` | 5.818 | 6.623639 | `-12.16%` | `38.65` / `36.78` | `37.92` | `0.359` | `NONE` | 5.5852064 | `WATCH` | HOLD |
| `XAUTUSDT` | 3876.53 | 3996.248468 | `-3.00%` | `12.98` / `22.6` | `35.43` | `0.259` | `NONE` | 3775.74022 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SUIUSDT` | 0.8079 | 0.835895 | `-3.35%` | `90.74` / `88.07` | `55.96` | `0.736` | `NONE` | 0.77762512 | `EXIT_LONG_STOCH_80` | HOLD |
