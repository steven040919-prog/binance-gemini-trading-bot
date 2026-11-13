# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T13:45:00Z`
- **Ciclo de ejecucion:** `#329`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `SIDEWAYS`

## Lectura de Mercado de Gemini AI
> El mercado general muestra una clara debilidad macro con los principales activos (BTC, ETH, BNB, SOL) cotizando por debajo de sus respectivas EMA 200 H1. Sin embargo, en el activo ERAUSDT se valida una entrada LONG bajo el Pilar 1 (P1_EMA200_PULLBACK) dada la confluencia de precio cercano a la EMA 200 ascendente, giro al alza del Estocastico desde sobreventa y patron de vela alcista (BULLISH_HAMMER). No existen posiciones abiertas actualmente que requieran gestion dinamica de SL/TP.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.0793 | 0.077954 | `+1.73%` | `21.77` / `12.96` | `41.97` | `0.303` | `BULLISH_HAMMER` | 0.0756522 | `P1_EMA200_PULLBACK` | **BUY** (86%) |
| `GRAMUSDT` | 1.135 | 1.137726 | `-0.24%` | `56.3` / `57.32` | `40.03` | `0.081` | `BEARISH_ENGULFING` | 1.08279 | `WATCH` | **HOLD** (75%) |
| `BTCUSDT` | 69885.09 | 74144.472236 | `-5.74%` | `47.92` / `44.08` | `43.32` | `0.471` | `BEARISH_SHOOTING_STAR` | 67474.759948 | `WATCH` | **HOLD** (80%) |
| `ETHUSDT` | 1979.55 | 2117.315766 | `-6.51%` | `56.03` / `49.34` | `49.11` | `0.535` | `BEARISH_SHOOTING_STAR` | 1898.6417 | `WATCH` | **HOLD** (80%) |
| `ZECUSDT` | 982.13 | 1100.19314 | `-10.73%` | `88.85` / `85.22` | `59.0` | `0.97` | `NONE` | 936.95202 | `EXIT_LONG_STOCH_80` | **HOLD** (70%) |
| `NEARUSDT` | 3.621 | 3.633318 | `-0.34%` | `92.38` / `87.44` | `63.97` | `1.04` | `BULLISH_ENGULFING` | 3.454434 | `EXIT_LONG_STOCH_80` | **HOLD** (70%) |
| `SOLUSDT` | 82.08 | 85.852959 | `-4.39%` | `78.36` / `70.42` | `59.2` | `0.842` | `BEARISH_SHOOTING_STAR` | 78.30432 | `WATCH` | **HOLD** (75%) |
| `DODOUSDT` | 0.02876 | 0.023697 | `+21.37%` | `73.12` / `71.0` | `62.49` | `0.749` | `NONE` | 0.02743704 | `WATCH` | **HOLD** (75%) |
| `PEPEUSDT` | 4.6e-06 | 5e-06 | `-5.08%` | `46.91` / `37.45` | `56.82` | `0.9` | `NONE` | 4.39e-06 | `WATCH` | **HOLD** (75%) |
| `BNBUSDT` | 647.26 | 679.241469 | `-4.71%` | `55.18` / `49.46` | `49.24` | `0.58` | `BULLISH_ENGULFING` | 623.564116 | `WATCH` | **HOLD** (75%) |
| `XRPUSDT` | 1.0393 | 1.107686 | `-6.17%` | `64.73` / `59.04` | `56.53` | `0.814` | `BEARISH_ENGULFING` | 0.9914922 | `WATCH` | **HOLD** (75%) |
| `HYPEUSDT` | 74.79 | 75.273195 | `-0.64%` | `93.55` / `90.81` | `67.72` | `1.068` | `NONE` | 71.34966 | `EXIT_LONG_STOCH_80` | **HOLD** (70%) |
| `INJUSDT` | 8.209 | 7.778639 | `+5.53%` | `93.34` / `92.61` | `76.66` | `1.288` | `NONE` | 7.831386 | `EXIT_LONG_STOCH_80` | **HOLD** (75%) |
| `INITUSDT` | 0.11712 | 0.151699 | `-22.79%` | `35.76` / `46.18` | `43.4` | `0.444` | `BULLISH_HAMMER` | 0.11173248 | `WATCH` | **HOLD** (75%) |
| `SUIUSDT` | 0.8249 | 0.836064 | `-1.34%` | `90.02` / `87.83` | `65.56` | `1.035` | `NONE` | 0.7869546 | `EXIT_LONG_STOCH_80` | **HOLD** (70%) |
| `UNIUSDT` | 6.005 | 6.6255 | `-9.37%` | `52.08` / `41.26` | `54.02` | `0.692` | `NONE` | 5.72877 | `WATCH` | **HOLD** (75%) |
