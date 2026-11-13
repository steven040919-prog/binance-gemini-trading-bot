# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T13:35:17Z`
- **Ciclo de ejecucion:** `#328`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global en temporalidad de 1h se encuentra mayoritariamente bajo la EMA 200 con un sesgo bajista generalizado. Sin embargo, ERAUSDT cumple con los requisitos del Pilar 1 (P1_EMA200_PULLBACK) al mantenerse en zona de valor alcista sobre su EMA 200, mostrando un retroceso a sobreventa en el estocástico con giro alcista y un patrón de vela de giro tipo BULLISH_HAMMER. No se detectan posiciones abiertas con ganancias para aplicar gestión dinámica (ADJUST) en este ciclo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.0795 | 0.077956 | `+1.98%` | `22.53` / `13.22` | `42.48` | `0.323` | `BULLISH_HAMMER` | 0.075843 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `GRAMUSDT` | 1.136 | 1.137736 | `-0.15%` | `56.91` / `57.53` | `40.32` | `0.114` | `BEARISH_ENGULFING` | 1.083744 | `WATCH` | HOLD |
| `BTCUSDT` | 69872.11 | 74144.343082 | `-5.76%` | `47.81` / `44.05` | `43.16` | `0.468` | `BEARISH_SHOOTING_STAR` | 67503.004736 | `WATCH` | HOLD |
| `SOXSBUSDT` | 45.18 | 55.598509 | `-18.74%` | `53.53` / `59.71` | `44.29` | `0.329` | `BULLISH_ENGULFING` | 43.10172 | `WATCH` | HOLD |
| `ETHUSDT` | 1976.17 | 2117.282134 | `-6.66%` | `55.13` / `49.04` | `47.83` | `0.514` | `BEARISH_SHOOTING_STAR` | 1899.915282 | `WATCH` | HOLD |
| `ZECUSDT` | 985.37 | 1100.225379 | `-10.44%` | `90.69` / `85.83` | `59.85` | `1.002` | `NONE` | 940.04298 | `EXIT_LONG_STOCH_80` | HOLD |
| `NEARUSDT` | 3.614 | 3.633249 | `-0.53%` | `92.7` / `87.55` | `63.49` | `1.024` | `BULLISH_ENGULFING` | 3.447756 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 81.86 | 85.85077 | `-4.65%` | `79.69` / `70.87` | `57.73` | `0.798` | `BEARISH_SHOOTING_STAR` | 78.3335 | `WATCH` | HOLD |
| `DODOUSDT` | 0.02896 | 0.023699 | `+22.20%` | `74.79` / `71.55` | `64.27` | `0.801` | `NONE` | 0.02762784 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.59e-06 | 5e-06 | `-5.28%` | `45.68` / `37.04` | `55.87` | `0.855` | `NONE` | 4.38e-06 | `WATCH` | HOLD |
| `BNBUSDT` | 646.58 | 679.234703 | `-4.81%` | `54.55` / `49.25` | `48.48` | `0.565` | `BULLISH_ENGULFING` | 624.097292 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0358 | 1.107651 | `-6.49%` | `62.21` / `58.2` | `54.42` | `0.735` | `BEARISH_ENGULFING` | 0.99043364 | `WATCH` | HOLD |
| `HYPEUSDT` | 75.17 | 75.276976 | `-0.14%` | `95.9` / `91.6` | `69.29` | `1.124` | `NONE` | 71.71218 | `EXIT_LONG_STOCH_80` | HOLD |
| `INJUSDT` | 8.192 | 7.77847 | `+5.32%` | `94.36` / `92.95` | `76.35` | `1.28` | `NONE` | 7.815168 | `EXIT_LONG_STOCH_80` | HOLD |
| `SUIUSDT` | 0.8247 | 0.836062 | `-1.36%` | `90.77` / `88.08` | `65.47` | `1.032` | `NONE` | 0.7867638 | `EXIT_LONG_STOCH_80` | HOLD |
| `UNIUSDT` | 5.979 | 6.625241 | `-9.75%` | `50.22` / `40.64` | `52.3` | `0.647` | `NONE` | 5.703966 | `WATCH` | HOLD |
