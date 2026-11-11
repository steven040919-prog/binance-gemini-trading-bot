# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T05:06:00Z`
- **Ciclo de ejecucion:** `#107`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un régimen claramente bajista con la mayoría de los activos cotizando por debajo de la EMA 200 y presiones vendedoras predominantes. Se evalúan los pilares LONG (P1-P4) sin activaciones óptimas por falta de sobreventa extrema generalizada en zonas clave, y se revisa el Pilar SHORT (S1) en Futuros USDT-M. Se identifican patrones en activos como CYBERUSDT, pero sin la confluencia completa requerida para una ejecución inmediata. Las posiciones abiertas están vacías, por lo que se prioriza la gestión de vigilancia (WATCH) manteniendo capital disponible.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1017.22 | 1213.051336 | `-16.14%` | `16.4` / `14.73` | `31.59` | `0.28` | `BEARISH_ENGULFING` | 970.42788 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.668 | 6.9988 | `-4.73%` | `15.85` / `14.98` | `38.59` | `0.303` | `BEARISH_ENGULFING` | 6.4429576 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOXSBUSDT` | 49.62 | 61.873906 | `-19.80%` | `3.6` / `5.32` | `33.51` | `0.087` | `NONE` | 47.33748 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 180.43 | 193.96974 | `-6.98%` | `47.3` / `44.48` | `34.59` | `0.3` | `NONE` | 174.624046 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3178 | 0.318516 | `-0.22%` | `15.23` / `11.09` | `45.44` | `0.327` | `BULLISH_HAMMER` | 0.3095372 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73830.88 | 75814.310314 | `-2.62%` | `60.0` / `50.46` | `47.29` | `0.559` | `BULLISH_HAMMER` | 71911.27712 | `WATCH` | HOLD |
| `CYBERUSDT` | 0.272 | 0.282783 | `-3.81%` | `5.31` / `4.54` | `45.65` | `0.273` | `BEARISH_SHOOTING_STAR` | 0.284512 | `M15_SCALPER_PULLBACK_SHORT` | **HOLD** (75%) |
| `ETHUSDT` | 2067.02 | 2192.67238 | `-5.73%` | `73.26` / `62.02` | `46.7` | `0.601` | `NONE` | 2013.27748 | `WATCH` | HOLD |
| `ONEUSDT` | 0.00173 | 0.001552 | `+11.46%` | `21.55` / `39.61` | `48.25` | `0.152` | `BULLISH_HAMMER` | 0.00165042 | `WATCH` | HOLD |
| `SOLUSDT` | 82.94 | 89.055194 | `-6.87%` | `49.5` / `49.02` | `38.03` | `0.372` | `NONE` | 80.78356 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0577 | 1.15922 | `-8.76%` | `56.65` / `53.76` | `41.8` | `0.427` | `BEARISH_ENGULFING` | 1.02833446 | `WATCH` | HOLD |
| `NEARUSDT` | 3.671 | 3.769204 | `-2.61%` | `73.52` / `71.79` | `56.14` | `0.751` | `BEARISH_ENGULFING` | 3.5094388 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0012 | 1.001199 | `+0.00%` | `75.4` / `79.37` | `54.62` | `0.686` | `BEARISH_SHOOTING_STAR` | 0.9751688 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.3e-06 | 5e-06 | `+4.62%` | `47.47` / `52.64` | `49.91` | `0.421` | `NONE` | 5.06e-06 | `WATCH` | HOLD |
| `BNBUSDT` | 682.15 | 693.464079 | `-1.63%` | `65.54` / `59.14` | `49.3` | `0.573` | `BEARISH_ENGULFING` | 664.4141 | `WATCH` | HOLD |
| `HYPEUSDT` | 72.19 | 78.110685 | `-7.58%` | `50.37` / `42.48` | `42.67` | `0.451` | `MORNING_STAR` | 70.08182 | `WATCH` | HOLD |
