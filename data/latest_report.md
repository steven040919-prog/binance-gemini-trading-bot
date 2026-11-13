# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T13:06:55Z`
- **Ciclo de ejecucion:** `#325`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general muestra una estructura predominantemente bajista con la mayoria de los activos cotizando por debajo de la EMA 200 en 1H. Sin embargo, se identifica una oportunidad de compra valida en ERAUSDT bajo el Pilar 1 (Pullback sobre EMA 200 con pendiente alcista + Estocastico en sobreventa a 16.02 + patron Bullish Hammer). No hay posiciones abiertas actualmente en portafolio para aplicar gestion dinamica de SL/TP.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `GRAMUSDT` | 1.147 | 1.137846 | `+0.80%` | `59.17` / `58.28` | `43.73` | `0.539` | `BEARISH_ENGULFING` | 1.1119664 | `WATCH` | **HOLD** (65%) |
| `BTCUSDT` | 69255.25 | 74138.205171 | `-6.59%` | `42.6` / `42.31` | `34.44` | `0.35` | `BEARISH_SHOOTING_STAR` | 67454.6135 | `WATCH` | **HOLD** (75%) |
| `INITUSDT` | 0.11484 | 0.151677 | `-24.29%` | `31.37` / `44.72` | `41.52` | `0.314` | `NONE` | 0.10955736 | `WATCH` | HOLD |
| `ETHUSDT` | 1960.4 | 2117.125218 | `-7.40%` | `50.93` / `47.64` | `40.93` | `0.415` | `BEARISH_SHOOTING_STAR` | 1903.85248 | `WATCH` | **HOLD** (70%) |
| `TIAUSDT` | 0.4126 | 0.427878 | `-3.57%` | `30.1` / `36.02` | `44.91` | `0.253` | `NONE` | 0.3936204 | `WATCH` | HOLD |
| `SOLUSDT` | 80.77 | 85.839924 | `-5.91%` | `71.69` / `68.2` | `48.53` | `0.565` | `BEARISH_SHOOTING_STAR` | 78.52229 | `WATCH` | **HOLD** (70%) |
| `ERAUSDT` | 0.0778 | 0.077939 | `-0.18%` | `16.02` / `11.05` | `37.9` | `0.154` | `BULLISH_HAMMER` | 0.0742212 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `DODOUSDT` | 0.02929 | 0.023702 | `+23.58%` | `77.55` / `72.47` | `67.46` | `0.881` | `NONE` | 0.02794266 | `WATCH` | HOLD |
| `ZECUSDT` | 970.31 | 1100.075528 | `-11.80%` | `89.75` / `85.52` | `55.59` | `0.837` | `NONE` | 925.67574 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 640.99 | 679.179081 | `-5.62%` | `49.41` / `47.54` | `41.29` | `0.437` | `BULLISH_ENGULFING` | 624.32426 | `WATCH` | HOLD |
| `NEARUSDT` | 3.538 | 3.632492 | `-2.60%` | `90.49` / `86.81` | `57.38` | `0.822` | `NONE` | 3.375252 | `EXIT_LONG_STOCH_80` | HOLD |
| `XRPUSDT` | 1.0194 | 1.107488 | `-7.95%` | `50.43` / `54.27` | `41.12` | `0.335` | `BEARISH_ENGULFING` | 0.9928956 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.55e-06 | 5e-06 | `-6.10%` | `40.74` / `35.39` | `51.6` | `0.653` | `NONE` | 4.34e-06 | `WATCH` | HOLD |
| `HYPEUSDT` | 74.37 | 75.269016 | `-1.19%` | `96.2` / `91.7` | `65.77` | `0.998` | `NONE` | 70.94898 | `EXIT_LONG_STOCH_80` | HOLD |
| `UNIUSDT` | 5.825 | 6.623709 | `-12.06%` | `39.15` / `36.95` | `38.72` | `0.372` | `NONE` | 5.586125 | `WATCH` | HOLD |
| `XAUTUSDT` | 3881.81 | 3996.301005 | `-2.86%` | `17.53` / `24.11` | `38.36` | `0.365` | `NONE` | 3780.88294 | `EXIT_SHORT_STOCH_20` | HOLD |
