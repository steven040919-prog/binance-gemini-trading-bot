# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T19:35:10Z`
- **Ciclo de ejecucion:** `#255`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se mantiene bajo una fuerte presión bajista con la mayoría de los activos operando por debajo de la EMA 200 en temporalidad 1H. Se han detectado señales de scalping bajista (Pilar S1/M15) en NEAR y XRP, aprovechando la tendencia macro. No se activan entradas LONG (P1-P4) debido a que, aunque aparecen patrones de velas alcistas, no existe una confluencia robusta de giro en el Estocástico ni una recuperación de la estructura de soporte institucional. Se mantiene una postura de vigilancia estricta.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71556.85 | 75097.863969 | `-4.72%` | `19.12` / `20.18` | `23.36` | `0.102` | `NONE` | 69696.3719 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2011.75 | 2148.528724 | `-6.37%` | `43.98` / `40.3` | `33.51` | `0.208` | `NONE` | 1959.4445 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.44e-06 | 5e-06 | `-9.86%` | `38.28` / `25.63` | `38.96` | `0.445` | `MORNING_STAR` | 4.24e-06 | `WATCH` | HOLD |
| `ZECUSDT` | 944.49 | 1136.405542 | `-16.89%` | `15.84` / `17.38` | `32.76` | `0.053` | `BULLISH_HAMMER` | 901.04346 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 81.57 | 87.092581 | `-6.34%` | `37.83` / `36.47` | `35.89` | `0.205` | `BULLISH_HAMMER` | 79.44918 | `WATCH` | HOLD |
| `NEARUSDT` | 3.4 | 3.698666 | `-8.07%` | `31.63` / `30.17` | `34.56` | `0.224` | `BULLISH_ENGULFING` | 3.54648 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (78%) |
| `UNIUSDT` | 6.016 | 6.778155 | `-11.24%` | `26.41` / `25.59` | `30.92` | `0.196` | `BULLISH_ENGULFING` | 5.7967232 | `WATCH` | HOLD |
| `BNBUSDT` | 654.17 | 687.55822 | `-4.86%` | `18.94` / `19.73` | `23.7` | `0.177` | `BULLISH_HAMMER` | 637.16158 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0277 | 1.124173 | `-8.58%` | `32.1` / `29.57` | `35.01` | `0.183` | `NONE` | 1.05534846 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (75%) |
| `ENAUSDT` | 0.1388 | 0.15657 | `-11.35%` | `32.65` / `29.84` | `27.95` | `0.198` | `BEARISH_ENGULFING` | 0.13304736 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.146 | 1.138053 | `+0.70%` | `19.4` / `42.28` | `37.95` | `0.029` | `NONE` | 1.093284 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3878.2 | 4013.706392 | `-3.38%` | `20.54` / `18.9` | `26.8` | `0.2` | `BULLISH_ENGULFING` | 3777.3668 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 113.31 | 126.23882 | `-10.24%` | `33.52` / `32.22` | `30.07` | `0.26` | `BEARISH_ENGULFING` | 110.076602 | `WATCH` | HOLD |
| `QNTUSDT` | 160.75 | 186.598235 | `-13.85%` | `18.83` / `20.87` | `28.51` | `-0.014` | `BEARISH_ENGULFING` | 155.31105 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TAOUSDT` | 208.9 | 221.064181 | `-5.50%` | `46.44` / `42.53` | `34.86` | `0.231` | `BEARISH_SHOOTING_STAR` | 202.0686 | `WATCH` | HOLD |
| `INJUSDT` | 7.372 | 7.84582 | `-6.04%` | `28.61` / `27.67` | `38.29` | `0.226` | `BULLISH_ENGULFING` | 7.0847888 | `WATCH` | HOLD |
