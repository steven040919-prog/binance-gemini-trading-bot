# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T17:47:27Z`
- **Ciclo de ejecucion:** `#244`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se mantiene bajo una fuerte presión bajista con la mayoría de los activos operando por debajo de la EMA 200. Se han identificado oportunidades de alta probabilidad bajo el Pilar 2 (Capitulación Extrema) para BTCUSDT y XAUTUSDT, aprovechando la sobreventa extrema y el giro del estocástico. Para los activos en tendencia bajista clara, se han activado señales de scalping (Pilar M15) en SOLUSDT, BNBUSDT y SUIUSDT para posiciones cortas en futuros, aprovechando el rechazo en zonas de resistencia local.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71729.48 | 75142.214622 | `-4.54%` | `17.74` / `15.9` | `22.24` | `0.059` | `BEARISH_SHOOTING_STAR` | 69864.51352 | `P2_EXTREME_CAPITULATION` | **BUY** (85%) |
| `ETHUSDT` | 2010.27 | 2150.191285 | `-6.51%` | `32.82` / `30.6` | `30.57` | `0.141` | `BEARISH_SHOOTING_STAR` | 1958.00298 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.33e-06 | 5e-06 | `-12.24%` | `12.78` / `19.54` | `25.14` | `0.114` | `NONE` | 4.13e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 942.32 | 1139.869431 | `-17.33%` | `19.7` / `26.87` | `31.57` | `-0.138` | `NONE` | 898.97328 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.384 | 3.70421 | `-8.64%` | `23.83` / `22.88` | `30.75` | `0.133` | `BULLISH_ENGULFING` | 3.2513888 | `WATCH` | HOLD |
| `SOLUSDT` | 81.34 | 87.173219 | `-6.69%` | `32.05` / `29.94` | `32.62` | `0.08` | `BEARISH_SHOOTING_STAR` | 83.854264 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (75%) |
| `UNIUSDT` | 5.988 | 6.792156 | `-11.84%` | `23.74` / `25.79` | `27.09` | `0.08` | `BEARISH_SHOOTING_STAR` | 5.7507552 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0232 | 1.12591 | `-9.12%` | `20.97` / `22.38` | `29.17` | `0.039` | `BEARISH_ENGULFING` | 0.9965968 | `WATCH` | HOLD |
| `BNBUSDT` | 655.16 | 687.881899 | `-4.76%` | `17.81` / `15.22` | `24.31` | `0.134` | `BEARISH_SHOOTING_STAR` | 672.19416 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (78%) |
| `ENAUSDT` | 0.1378 | 0.156796 | `-12.12%` | `22.05` / `25.79` | `20.7` | `0.072` | `BEARISH_SHOOTING_STAR` | 0.13274552 | `WATCH` | HOLD |
| `DOGEUSDT` | 0.06569 | 0.070264 | `-6.51%` | `36.39` / `30.41` | `33.43` | `0.161` | `BEARISH_SHOOTING_STAR` | 0.06314051 | `WATCH` | HOLD |
| `AAVEUSDT` | 113.11 | 126.418359 | `-10.53%` | `28.65` / `26.94` | `29.01` | `0.202` | `BEARISH_SHOOTING_STAR` | 109.194384 | `WATCH` | HOLD |
| `XAUTUSDT` | 3869.31 | 4015.223394 | `-3.63%` | `15.91` / `11.57` | `22.35` | `0.078` | `BULLISH_ENGULFING` | 3768.70794 | `P2_EXTREME_CAPITULATION` | **BUY** (82%) |
| `SUIUSDT` | 0.7938 | 0.846269 | `-6.20%` | `31.97` / `28.47` | `31.76` | `0.114` | `BEARISH_SHOOTING_STAR` | 0.82123988 | `M15_SCALPER_PULLBACK_SHORT` | HOLD |
| `LINKUSDT` | 9.95 | 10.608224 | `-6.20%` | `49.41` / `41.02` | `35.43` | `0.195` | `BEARISH_SHOOTING_STAR` | 9.62501 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1461 | 0.162431 | `-10.05%` | `40.41` / `36.7` | `28.99` | `0.201` | `BULLISH_HAMMER` | 0.14043062 | `WATCH` | HOLD |
