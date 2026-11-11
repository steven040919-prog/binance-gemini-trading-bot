# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T22:22:51Z`
- **Ciclo de ejecucion:** `#160`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado opera bajo un regimen predominantemente bajista con la mayoria de los activos cotizando por debajo de la EMA 200. No se cumplen los requisitos estrictos de los Pilares LONG (P1-P4) ni del Pilar SHORT (S1) ya que los gatillos de sobrecompra/sobreventa o las confluencias institucionales de volumen y divergencias no se alinean completamente en los candidatos evaluados. El portafolio permanece en modo WATCH con 0 posiciones abiertas, preservando el capital mientras se esperan configuraciones de alta probabilidad segun el backtesting institucional.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.74e-06 | 5e-06 | `-6.13%` | `8.09` / `4.84` | `29.01` | `0.152` | `NONE` | 4.52e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74452.0 | 75575.1617 | `-1.49%` | `79.26` / `79.73` | `55.96` | `0.803` | `BEARISH_ENGULFING` | 72516.248 | `WATCH` | **HOLD** (50%) |
| `ARBUSDT` | 0.1567 | 0.165383 | `-5.25%` | `8.36` / `15.18` | `37.44` | `0.09` | `NONE` | 0.15158106 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.874 | 7.955859 | `-1.03%` | `17.63` / `18.74` | `42.99` | `0.291` | `NONE` | 7.5553548 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1501 | 0.160576 | `-6.52%` | `12.91` / `16.65` | `43.11` | `0.114` | `NONE` | 0.14417692 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3983.81 | 4031.866518 | `-1.19%` | `6.77` / `4.75` | `25.43` | `0.199` | `BULLISH_ENGULFING` | 3880.23094 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PAXGUSDT` | 3986.78 | 4037.458565 | `-1.26%` | `6.66` / `4.44` | `26.53` | `0.206` | `BULLISH_ENGULFING` | 3883.12372 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2077.91 | 2174.965312 | `-4.46%` | `54.81` / `57.39` | `52.91` | `0.726` | `NONE` | 2023.88434 | `WATCH` | HOLD |
| `ZECUSDT` | 1007.3 | 1176.286874 | `-14.37%` | `60.19` / `58.6` | `46.73` | `0.691` | `BULLISH_ENGULFING` | 960.9642 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001494 | 0.001553 | `-3.82%` | `8.36` / `6.51` | `34.89` | `0.232` | `BULLISH_HAMMER` | 0.00142528 | `EXIT_SHORT_STOCH_20` | HOLD |
| `MUBUSDT` | 808.61 | 755.232242 | `+7.07%` | `76.52` / `81.67` | `66.72` | `0.698` | `BEARISH_ENGULFING` | 784.139978 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOXSBUSDT` | 46.27 | 59.361089 | `-22.05%` | `45.64` / `36.68` | `42.36` | `0.465` | `BULLISH_HAMMER` | 44.14158 | `WATCH` | HOLD |
| `SNXXBUSDT` | 4.38 | 4.187008 | `+4.61%` | `69.31` / `76.69` | `62.86` | `0.664` | `BEARISH_ENGULFING` | 4.17852 | `WATCH` | HOLD |
| `SOLUSDT` | 84.71 | 88.31214 | `-4.08%` | `65.33` / `69.75` | `54.02` | `0.694` | `NONE` | 82.50754 | `WATCH` | HOLD |
| `NEARUSDT` | 3.688 | 3.763925 | `-2.02%` | `50.26` / `55.38` | `50.49` | `0.465` | `NONE` | 3.5283312 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0618 | 1.144149 | `-7.20%` | `38.57` / `37.62` | `47.81` | `0.521` | `BEARISH_SHOOTING_STAR` | 1.0341932 | `WATCH` | HOLD |
