# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T18:20:32Z`
- **Ciclo de ejecucion:** `#358`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen mayoritariamente bajista (BEARISH) con la mayoría de los activos cotizando por debajo de sus respectivas EMA 200 en temporalidad 1H. Se identifican configuraciones válidas en el Pilar S1 (Rechazo bajista en resistencia de EMA 200) y en el Pilar Scalper M15 para operaciones SHORT en futuros USDT-M, aprovechando las tendencias macro bajistas. No hay posiciones abiertas actuales en el portafolio para realizar ajustes de SL/TP dinámicos.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.0755 | 0.077808 | `-2.97%` | `9.71` / `10.78` | `35.87` | `0.17` | `BEARISH_SHOOTING_STAR` | 0.072027 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 68880.92 | 73869.943331 | `-6.75%` | `47.46` / `43.74` | `35.35` | `0.369` | `BULLISH_ENGULFING` | 67033.923968 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.121 | 1.137203 | `-1.42%` | `19.05` / `23.33` | `36.58` | `0.054` | `BEARISH_ENGULFING` | 1.0823522 | `EXIT_SHORT_STOCH_20` | HOLD |
| `MUBUSDT` | 761.94 | 763.359384 | `-0.19%` | `18.54` / `14.67` | `35.11` | `0.094` | `BULLISH_ENGULFING` | 729.156128 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 1939.46 | 2108.421432 | `-8.01%` | `41.62` / `38.71` | `38.18` | `0.378` | `BULLISH_ENGULFING` | 1875.086096 | `WATCH` | HOLD |
| `SOLUSDT` | 80.15 | 85.5514 | `-6.31%` | `43.82` / `45.79` | `45.1` | `0.489` | `NONE` | 77.33434 | `WATCH` | HOLD |
| `ZECUSDT` | 944.14 | 1090.533621 | `-13.42%` | `57.97` / `60.11` | `45.7` | `0.473` | `NONE` | 900.70956 | `WATCH` | HOLD |
| `BNBUSDT` | 635.71 | 677.095865 | `-6.11%` | `40.22` / `38.27` | `40.41` | `0.413` | `MORNING_STAR` | 615.997232 | `WATCH` | HOLD |
| `BARDUSDT` | 0.1486 | 0.109191 | `+36.09%` | `46.05` / `57.12` | `56.83` | `0.545` | `BULLISH_HAMMER` | 0.1417644 | `WATCH` | HOLD |
| `SOXSBUSDT` | 52.47 | 55.519722 | `-5.49%` | `76.5` / `82.46` | `66.61` | `0.9` | `BEARISH_SHOOTING_STAR` | 54.88362 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `NEARUSDT` | 3.495 | 3.624998 | `-3.59%` | `62.66` / `65.21` | `50.8` | `0.578` | `BEARISH_SHOOTING_STAR` | 3.33423 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0258 | 1.104035 | `-7.09%` | `47.96` / `50.23` | `48.57` | `0.555` | `BEARISH_SHOOTING_STAR` | 0.985055 | `WATCH` | HOLD |
| `INJUSDT` | 8.062 | 7.797525 | `+3.39%` | `83.68` / `87.17` | `66.68` | `0.78` | `NONE` | 7.691148 | `EXIT_LONG_STOCH_80` | HOLD |
| `PEPEUSDT` | 4.47e-06 | 5e-06 | `-7.58%` | `23.61` / `25.0` | `44.42` | `0.181` | `BULLISH_ENGULFING` | 4.68e-06 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (78%) |
| `UNIUSDT` | 5.786 | 6.584488 | `-12.13%` | `33.74` / `38.98` | `40.34` | `0.371` | `BULLISH_ENGULFING` | 5.519844 | `WATCH` | HOLD |
| `ENAUSDT` | 0.1364 | 0.151931 | `-10.22%` | `38.18` / `42.93` | `42.95` | `0.373` | `BULLISH_HAMMER` | 0.1301256 | `WATCH` | HOLD |
