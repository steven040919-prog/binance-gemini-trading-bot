# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T18:01:09Z`
- **Ciclo de ejecucion:** `#356`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado opera predominantemente bajo un régimen bajista en temporalidad 1H, con la mayoría de los activos cotizando por debajo de la EMA 200. Se identifica una oportunidad clave en MUBUSDT bajo el Pilar 1 (Pullback sobre EMA 200 con patrón alcista y estocástico girando al alza) y una oportunidad SHORT en SOXSBUSDT bajo el Pilar S1 (Rechazo bajista en resistencia de la EMA 200 con estocástico en sobrecompra). No hay posiciones abiertas actuales para ajustar.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.075 | 0.077803 | `-3.60%` | `8.09` / `10.24` | `34.14` | `0.134` | `BEARISH_SHOOTING_STAR` | 0.07155 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 5.758 | 6.58421 | `-12.55%` | `31.33` / `38.18` | `37.69` | `0.315` | `BULLISH_HAMMER` | 5.5166216 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.12 | 1.137194 | `-1.51%` | `18.45` / `23.13` | `36.03` | `0.036` | `BEARISH_ENGULFING` | 1.083832 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 68884.27 | 73869.976665 | `-6.75%` | `47.51` / `43.75` | `35.38` | `0.37` | `BULLISH_ENGULFING` | 67047.635162 | `WATCH` | HOLD |
| `MUBUSDT` | 763.67 | 763.376598 | `+0.04%` | `19.57` / `15.01` | `35.86` | `0.115` | `BULLISH_ENGULFING` | 729.411772 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `ETHUSDT` | 1936.36 | 2108.390586 | `-8.16%` | `40.51` / `38.34` | `37.06` | `0.354` | `BULLISH_ENGULFING` | 1875.542808 | `WATCH` | HOLD |
| `AAVEUSDT` | 110.96 | 122.791606 | `-9.64%` | `25.62` / `34.93` | `40.0` | `0.327` | `BULLISH_HAMMER` | 106.71216 | `WATCH` | HOLD |
| `BARDUSDT` | 0.148 | 0.109185 | `+35.55%` | `45.65` / `56.99` | `56.37` | `0.534` | `NONE` | 0.141192 | `WATCH` | HOLD |
| `SOLUSDT` | 79.89 | 85.548813 | `-6.61%` | `41.83` / `45.13` | `42.82` | `0.424` | `NONE` | 77.356662 | `WATCH` | HOLD |
| `BNBUSDT` | 633.66 | 677.075467 | `-6.41%` | `37.73` / `37.44` | `37.57` | `0.357` | `BULLISH_HAMMER` | 616.293336 | `WATCH` | HOLD |
| `ZECUSDT` | 945.14 | 1090.543571 | `-13.33%` | `58.27` / `60.21` | `46.11` | `0.487` | `NONE` | 901.66356 | `WATCH` | HOLD |
| `SOXSBUSDT` | 52.39 | 55.518926 | `-5.64%` | `76.23` / `82.37` | `66.4` | `0.894` | `BEARISH_SHOOTING_STAR` | 54.79994 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (82%) |
| `XRPUSDT` | 1.0201 | 1.103978 | `-7.60%` | `43.4` / `48.71` | `44.27` | `0.405` | `BEARISH_SHOOTING_STAR` | 0.98580956 | `WATCH` | HOLD |
| `NEARUSDT` | 3.496 | 3.625008 | `-3.56%` | `62.75` / `65.24` | `50.92` | `0.581` | `BEARISH_SHOOTING_STAR` | 3.335184 | `WATCH` | HOLD |
| `INJUSDT` | 8.11 | 7.798002 | `+4.00%` | `85.08` / `87.64` | `69.95` | `0.811` | `BEARISH_SHOOTING_STAR` | 7.73694 | `EXIT_LONG_STOCH_80` | HOLD |
| `PEPEUSDT` | 4.48e-06 | 5e-06 | `-7.37%` | `25.0` / `25.46` | `45.34` | `0.235` | `BULLISH_ENGULFING` | 4.27e-06 | `WATCH` | HOLD |
