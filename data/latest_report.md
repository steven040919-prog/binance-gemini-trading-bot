# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T14:53:46Z`
- **Ciclo de ejecucion:** `#233`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general presenta una fuerte tendencia bajista macro con fuerte capitulacion e indicadores en sobreventa extrema. NEARUSDT y AAVEUSDT activan senales de entrada bajo el Pilar 2 (P2_EXTREME_CAPITULATION) al mostrar giro en Estocastico, sobreventa en RSI, volumen alto y patrones alcistas de vela (Martillo y Envolvente Alcista). El resto de activos permanece en HOLD a la espera de confirmacion o confluencia en niveles estructurales.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71567.01 | 75243.566934 | `-4.89%` | `9.32` / `10.81` | `19.11` | `-0.241` | `NONE` | 69706.26774 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `ETHUSDT` | 1999.93 | 2154.389593 | `-7.17%` | `22.79` / `20.0` | `24.15` | `-0.103` | `BULLISH_HAMMER` | 1947.93182 | `EXIT_SHORT_STOCH_20` | **HOLD** (70%) |
| `PEPEUSDT` | 4.42e-06 | 5e-06 | `-10.80%` | `24.4` / `19.64` | `29.33` | `0.256` | `BULLISH_HAMMER` | 4.22e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (70%) |
| `NEARUSDT` | 3.4 | 3.714134 | `-8.46%` | `13.01` / `10.4` | `30.63` | `0.124` | `BULLISH_HAMMER` | 3.2436 | `P2_EXTREME_CAPITULATION` | **BUY** (85%) |
| `SOLUSDT` | 81.14 | 87.363652 | `-7.12%` | `16.87` / `15.59` | `27.66` | `-0.033` | `BULLISH_HAMMER` | 78.967024 | `EXIT_SHORT_STOCH_20` | **HOLD** (72%) |
| `UNIUSDT` | 6.037 | 6.81278 | `-11.39%` | `18.17` / `13.76` | `28.51` | `0.192` | `NONE` | 5.7780974 | `EXIT_SHORT_STOCH_20` | **HOLD** (70%) |
| `XRPUSDT` | 1.0273 | 1.129067 | `-9.01%` | `22.05` / `21.23` | `31.13` | `-0.042` | `BULLISH_HAMMER` | 0.99957584 | `WATCH` | **HOLD** (70%) |
| `BNBUSDT` | 652.68 | 689.044527 | `-5.28%` | `7.73` / `7.29` | `16.95` | `-0.072` | `NONE` | 635.71032 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `NBISBUSDT` | 131.56 | 141.474051 | `-7.01%` | `11.72` / `21.57` | `33.68` | `-0.041` | `NONE` | 125.50824 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `ENAUSDT` | 0.1392 | 0.157329 | `-11.52%` | `16.96` / `11.97` | `22.46` | `0.159` | `BULLISH_HAMMER` | 0.1327968 | `EXIT_SHORT_STOCH_20` | **HOLD** (70%) |
| `DOGEUSDT` | 0.06514 | 0.070411 | `-7.49%` | `20.47` / `19.97` | `23.48` | `-0.101` | `NONE` | 0.06324417 | `EXIT_SHORT_STOCH_20` | **HOLD** (70%) |
| `ARBUSDT` | 0.1446 | 0.162821 | `-11.19%` | `20.04` / `14.15` | `21.86` | `0.092` | `BULLISH_HAMMER` | 0.13855364 | `EXIT_SHORT_STOCH_20` | **HOLD** (70%) |
| `AAVEUSDT` | 113.27 | 126.824528 | `-10.69%` | `12.5` / `7.13` | `26.91` | `0.15` | `BULLISH_ENGULFING` | 108.05958 | `P2_EXTREME_CAPITULATION` | **BUY** (87%) |
| `XAUTUSDT` | 3879.92 | 4019.273231 | `-3.47%` | `6.97` / `15.4` | `20.15` | `-0.136` | `BEARISH_SHOOTING_STAR` | 3779.04208 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `SUIUSDT` | 0.7904 | 0.847784 | `-6.77%` | `15.85` / `13.83` | `25.1` | `-0.031` | `BULLISH_HAMMER` | 0.76516928 | `EXIT_SHORT_STOCH_20` | **HOLD** (70%) |
| `LINKUSDT` | 9.893 | 10.633546 | `-6.96%` | `21.25` / `16.91` | `27.18` | `0.106` | `NONE` | 9.5681828 | `EXIT_SHORT_STOCH_20` | **HOLD** (70%) |
