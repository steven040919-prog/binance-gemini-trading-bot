# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-10T01:27:12Z`
- **Ciclo de ejecucion:** `#13`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global opera mayoritariamente bajo la EMA 200 con un sesgo bajista generalizado, aunque se detectan activos en zonas de valor y sobreventa extrema. No se cumplen simultáneamente las condiciones estrictas de los Pilares 1, 2 o 3 para nuevas entradas (P1 Pullback EMA200, P2 Capitulación Extrema o P3 Divergencia Spring), ya que el volumen institucional o los cruces estocásticos requeridos no alcanzan los umbrales óptimos en los candidatos evaluados. Tampoco hay posiciones abiertas en cartera para aplicar gestión dinámica de SL/TP. Se prioriza la preservación de capital mediante postura neutral (HOLD) a la espera de configuraciones de alta probabilidad.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1176.21 | 1253.644153 | `-6.18%` | `20.77` / `19.05` | `40.33` | `0.303` | `NONE` | 1122.10434 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `ARBUSDT` | 0.1737 | 0.167213 | `+3.88%` | `6.44` / `11.02` | `46.24` | `0.259` | `BEARISH_SHOOTING_STAR` | 0.16720362 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZROUSDT` | 1.474 | 1.650492 | `-10.69%` | `11.43` / `15.35` | `35.73` | `0.167` | `BULLISH_HAMMER` | 1.406196 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 75155.08 | 76495.571123 | `-1.75%` | `73.6` / `77.31` | `52.19` | `0.716` | `BEARISH_ENGULFING` | 73201.04792 | `WATCH` | HOLD |
| `SOXLBUSDT` | 55.55 | 56.998979 | `-2.54%` | `87.8` / `91.91` | `66.44` | `0.685` | `BEARISH_ENGULFING` | 58.1053 | `S1_EMA200_RESISTANCE_REJECT` | HOLD |
| `QNTUSDT` | 194.4 | 196.904564 | `-1.27%` | `9.39` / `12.27` | `41.76` | `0.213` | `BULLISH_HAMMER` | 188.41224 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRUMPUSDT` | 1.119 | 1.287388 | `-13.08%` | `26.83` / `31.47` | `40.45` | `0.159` | `BEARISH_SHOOTING_STAR` | 1.0745348 | `WATCH` | HOLD |
| `ETHUSDT` | 2128.54 | 2231.769391 | `-4.63%` | `50.8` / `59.68` | `43.06` | `0.592` | `BEARISH_SHOOTING_STAR` | 2073.19796 | `WATCH` | HOLD |
| `AVAXUSDT` | 8.727 | 8.403276 | `+3.85%` | `67.76` / `66.7` | `64.27` | `0.684` | `NONE` | 8.325558 | `WATCH` | HOLD |
| `SNDKBUSDT` | 879.98 | 948.465251 | `-7.22%` | `79.79` / `85.93` | `57.59` | `0.619` | `NONE` | 839.50092 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 86.64 | 90.894237 | `-4.68%` | `33.39` / `38.84` | `45.67` | `0.51` | `NONE` | 84.38736 | `WATCH` | HOLD |
| `XRPUSDT` | 1.1047 | 1.189866 | `-7.16%` | `60.75` / `61.53` | `48.75` | `0.752` | `NONE` | 1.0663778 | `WATCH` | HOLD |
| `TSTUSDT` | 0.01301 | 0.012377 | `+5.11%` | `24.22` / `28.45` | `54.85` | `0.573` | `BULLISH_ENGULFING` | 0.01241154 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.16e-06 | 5e-06 | `+3.51%` | `31.58` / `30.29` | `54.24` | `0.563` | `NONE` | 4.92e-06 | `WATCH` | HOLD |
| `SPCXBUSDT` | 142.02 | 136.023558 | `+4.41%` | `86.03` / `87.52` | `63.24` | `0.694` | `BULLISH_HAMMER` | 137.90354 | `EXIT_LONG_STOCH_80` | HOLD |
| `KORUBUSDT` | 7.47 | 8.332543 | `-10.35%` | `74.6` / `85.47` | `55.0` | `0.609` | `BULLISH_HAMMER` | 7.12638 | `EXIT_LONG_STOCH_80` | HOLD |
