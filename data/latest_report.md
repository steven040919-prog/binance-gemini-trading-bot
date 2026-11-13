# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T17:51:33Z`
- **Ciclo de ejecucion:** `#355`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado muestra una tendencia bajista predominante con la mayoría de los activos operando bajo la EMA 200. Se han identificado oportunidades de alta probabilidad bajo el Pilar 1 (MUBUSDT) y el Pilar S1 (GRAMUSDT, SOXSBUSDT). La gestión de riesgo se mantiene estricta, priorizando la entrada en activos con confluencia técnica clara y patrones de velas de reversión.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.0755 | 0.077934 | `-3.12%` | `11.33` / `15.23` | `35.3` | `0.122` | `BEARISH_SHOOTING_STAR` | 0.072027 | `EXIT_SHORT_STOCH_20` | HOLD |
| `GRAMUSDT` | 1.124 | 1.137491 | `-1.19%` | `25.6` / `27.54` | `36.98` | `0.034` | `BEARISH_SHOOTING_STAR` | 1.1733168 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (82%) |
| `BTCUSDT` | 69010.53 | 73929.557732 | `-6.65%` | `44.81` / `42.53` | `36.92` | `0.382` | `BULLISH_HAMMER` | 66695.185188 | `WATCH` | HOLD |
| `MUBUSDT` | 765.55 | 763.329149 | `+0.29%` | `17.29` / `12.47` | `37.17` | `0.087` | `BULLISH_HAMMER` | 730.3347 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `ETHUSDT` | 1944.32 | 2110.448103 | `-7.87%` | `39.36` / `40.69` | `40.24` | `0.393` | `BULLISH_ENGULFING` | 1866.114048 | `WATCH` | HOLD |
| `BARDUSDT` | 0.1495 | 0.108798 | `+37.41%` | `56.9` / `66.42` | `57.55` | `0.58` | `NONE` | 0.142623 | `WATCH` | HOLD |
| `SOLUSDT` | 80.24 | 85.620275 | `-6.28%` | `45.34` / `53.28` | `45.75` | `0.492` | `BULLISH_ENGULFING` | 76.897952 | `WATCH` | HOLD |
| `ZECUSDT` | 946.96 | 1093.665293 | `-13.41%` | `59.47` / `63.88` | `46.87` | `0.51` | `NONE` | 903.39984 | `WATCH` | HOLD |
| `BNBUSDT` | 634.78 | 677.547558 | `-6.31%` | `37.43` / `41.16` | `39.02` | `0.366` | `BULLISH_ENGULFING` | 615.105708 | `WATCH` | HOLD |
| `SOXSBUSDT` | 52.03 | 55.590844 | `-6.41%` | `80.68` / `86.01` | `65.0` | `0.92` | `BEARISH_SHOOTING_STAR` | 54.42338 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (79%) |
| `NEARUSDT` | 3.514 | 3.626884 | `-3.11%` | `65.15` / `70.05` | `52.96` | `0.648` | `BULLISH_ENGULFING` | 3.352356 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0228 | 1.104827 | `-7.42%` | `47.46` / `57.68` | `46.23` | `0.457` | `NONE` | 0.98271632 | `WATCH` | HOLD |
| `INJUSDT` | 8.17 | 7.793118 | `+4.84%` | `89.6` / `90.42` | `72.02` | `0.884` | `BEARISH_ENGULFING` | 7.79418 | `EXIT_LONG_STOCH_80` | HOLD |
| `PEPEUSDT` | 4.51e-06 | 5e-06 | `-6.82%` | `27.78` / `30.76` | `48.33` | `0.397` | `BULLISH_ENGULFING` | 4.3e-06 | `WATCH` | HOLD |
| `UNIUSDT` | 5.772 | 6.593723 | `-12.46%` | `37.97` / `47.73` | `38.67` | `0.321` | `NONE` | 5.506488 | `WATCH` | HOLD |
| `HYPEUSDT` | 72.87 | 75.221824 | `-3.13%` | `54.2` / `61.71` | `52.88` | `0.577` | `BULLISH_HAMMER` | 69.855604 | `WATCH` | HOLD |
