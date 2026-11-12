# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T14:37:55Z`
- **Ciclo de ejecucion:** `#232`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado presenta una tendencia bajista generalizada con todos los activos operando bajo la EMA 200. Se han detectado oportunidades de entrada bajo el Pilar 2 (Capitulación Extrema) en NEARUSDT y AAVEUSDT, donde la confluencia de sobreventa extrema, divergencia alcista y patrones de vela de giro (Martillo/Envolvente) ofrecen una alta probabilidad de rebote técnico. El resto de los activos se mantienen en vigilancia o en fase de salida de posiciones cortas previas.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 72192.79 | 75249.793601 | `-4.06%` | `14.62` / `12.58` | `23.51` | `-0.097` | `NONE` | 70315.77746 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2014.76 | 2154.537156 | `-6.49%` | `28.85` / `22.02` | `29.55` | `0.036` | `BULLISH_HAMMER` | 1951.986792 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.44e-06 | 5e-06 | `-10.40%` | `26.49` / `20.34` | `31.79` | `0.295` | `BULLISH_HAMMER` | 4.24e-06 | `WATCH` | HOLD |
| `NEARUSDT` | 3.405 | 3.714184 | `-8.32%` | `13.59` / `10.6` | `31.48` | `0.135` | `BULLISH_HAMMER` | 3.24837 | `P2_EXTREME_CAPITULATION` | **BUY** (85%) |
| `SOLUSDT` | 81.6 | 87.368229 | `-6.60%` | `21.3` / `17.07` | `32.05` | `0.062` | `BULLISH_HAMMER` | 78.97488 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.088 | 6.813288 | `-10.65%` | `23.59` / `15.57` | `34.01` | `0.268` | `BULLISH_ENGULFING` | 5.807952 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0325 | 1.129119 | `-8.56%` | `26.47` / `22.7` | `33.97` | `0.065` | `BULLISH_HAMMER` | 0.9996825 | `WATCH` | HOLD |
| `BNBUSDT` | 655.59 | 689.073482 | `-4.86%` | `10.77` / `8.31` | `18.56` | `-0.016` | `BULLISH_HAMMER` | 638.54466 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NBISBUSDT` | 129.53 | 141.453852 | `-8.43%` | `10.22` / `21.07` | `30.99` | `-0.084` | `BULLISH_HAMMER` | 123.57162 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1404 | 0.15734 | `-10.77%` | `21.01` / `13.32` | `29.42` | `0.237` | `BULLISH_HAMMER` | 0.1339416 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.0655 | 0.070415 | `-6.98%` | `24.19` / `21.21` | `25.67` | `-0.025` | `BULLISH_HAMMER` | 0.06325 | `WATCH` | HOLD |
| `AAVEUSDT` | 113.26 | 126.824429 | `-10.70%` | `12.46` / `7.12` | `26.85` | `0.149` | `BULLISH_ENGULFING` | 108.05004 | `P2_EXTREME_CAPITULATION` | **BUY** (83%) |
| `ARBUSDT` | 0.1459 | 0.162834 | `-10.40%` | `24.42` / `15.61` | `24.4` | `0.166` | `BULLISH_HAMMER` | 0.1391886 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SUIUSDT` | 0.7938 | 0.847818 | `-6.37%` | `18.5` / `14.72` | `26.71` | `0.022` | `BULLISH_HAMMER` | 0.76525392 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3891.75 | 4019.390942 | `-3.18%` | `9.2` / `16.14` | `22.88` | `-0.07` | `BEARISH_SHOOTING_STAR` | 3790.5645 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TAOUSDT` | 207.9 | 221.669376 | `-6.21%` | `16.39` / `13.59` | `27.87` | `0.013` | `BULLISH_HAMMER` | 199.45988 | `EXIT_SHORT_STOCH_20` | HOLD |
