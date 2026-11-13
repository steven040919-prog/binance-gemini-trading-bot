# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T18:46:19Z`
- **Ciclo de ejecucion:** `#361`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen predominantemente bajista en temporalidad 1H con la mayoría de los activos cotizando por debajo de la EMA 200. No obstante, se identifican oportunidades de alta probabilidad bajo los pilares institucionales: MUBUSDT cumple con los requisitos del Pilar 1 (Pullback sobre EMA 200 con patrón de vela alcista y Estocástico girando al alza), e INJUSDT activa el Pilar Scalper M15 Pullback Long. Los demás activos se mantienen en vigilancia o sin confirmación completa.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68829.0 | 73869.426714 | `-6.82%` | `46.81` / `43.52` | `34.89` | `0.355` | `BULLISH_ENGULFING` | 67034.9416 | `WATCH` | HOLD |
| `ERAUSDT` | 0.075 | 0.077803 | `-3.60%` | `8.09` / `10.24` | `34.14` | `0.134` | `BEARISH_SHOOTING_STAR` | 0.07155 | `EXIT_SHORT_STOCH_20` | HOLD |
| `GRAMUSDT` | 1.13 | 1.137293 | `-0.64%` | `24.4` / `25.12` | `41.18` | `0.233` | `BEARISH_ENGULFING` | 1.081162 | `WATCH` | HOLD |
| `MUBUSDT` | 764.34 | 763.383265 | `+0.13%` | `19.97` / `15.15` | `36.33` | `0.123` | `BULLISH_ENGULFING` | 729.18036 | `P1_EMA200_PULLBACK` | **BUY** (88%) |
| `XAUTUSDT` | 3874.36 | 3990.140431 | `-2.90%` | `29.17` / `23.83` | `40.78` | `0.251` | `NONE` | 3773.62664 | `WATCH` | HOLD |
| `ETHUSDT` | 1939.45 | 2108.421332 | `-8.01%` | `41.61` / `38.7` | `38.18` | `0.378` | `BULLISH_ENGULFING` | 1874.69843 | `WATCH` | HOLD |
| `PAXGUSDT` | 3876.27 | 3993.911282 | `-2.95%` | `29.82` / `23.93` | `40.72` | `0.267` | `NONE` | 3775.48698 | `WATCH` | HOLD |
| `SOLUSDT` | 79.93 | 85.549211 | `-6.57%` | `42.13` / `45.23` | `43.11` | `0.434` | `BEARISH_SHOOTING_STAR` | 77.323722 | `WATCH` | HOLD |
| `ZECUSDT` | 944.62 | 1090.538397 | `-13.38%` | `58.11` / `60.16` | `45.9` | `0.48` | `BULLISH_HAMMER` | 901.16748 | `WATCH` | HOLD |
| `BNBUSDT` | 635.2 | 677.09079 | `-6.19%` | `39.6` / `38.06` | `39.71` | `0.399` | `NONE` | 615.8808 | `WATCH` | HOLD |
| `NEARUSDT` | 3.506 | 3.625108 | `-3.29%` | `63.64` / `65.54` | `52.14` | `0.611` | `BEARISH_SHOOTING_STAR` | 3.344724 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0248 | 1.104025 | `-7.18%` | `47.16` / `49.97` | `47.85` | `0.529` | `BEARISH_SHOOTING_STAR` | 0.98487504 | `WATCH` | HOLD |
| `SOXSBUSDT` | 51.71 | 55.51216 | `-6.85%` | `73.98` / `81.62` | `63.39` | `0.846` | `NONE` | 49.33134 | `EXIT_LONG_STOCH_80` | HOLD |
| `INJUSDT` | 8.076 | 7.797664 | `+3.57%` | `84.09` / `87.31` | `67.61` | `0.789` | `NONE` | 7.704504 | `M15_SCALPER_PULLBACK_LONG` | **BUY** (85%) |
| `PEPEUSDT` | 4.48e-06 | 5e-06 | `-7.37%` | `25.0` / `25.46` | `45.34` | `0.235` | `BULLISH_ENGULFING` | 4.27e-06 | `WATCH` | HOLD |
| `UNIUSDT` | 5.791 | 6.584538 | `-12.05%` | `34.17` / `39.12` | `40.79` | `0.381` | `BULLISH_ENGULFING` | 5.524614 | `WATCH` | HOLD |
