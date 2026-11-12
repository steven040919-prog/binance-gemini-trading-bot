# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T15:56:34Z`
- **Ciclo de ejecucion:** `#237`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen netamente bajista con múltiples activos cotizando por debajo de la EMA 200 en temporalidad 1H y RSI de sobreventa generalizada. Sin embargo, se detectan configuraciones institucionales de alta probabilidad en SUIUSDT mediante el Pilar 2 (Capitulación Extrema con volumen institucional y estocástico girando al alza), por lo que se emite orden de compra (BUY). No existen posiciones abiertas actualmente para realizar ajustes de gestión dinámica de SL/TP (ADJUST).

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71392.49 | 75213.975982 | `-5.08%` | `10.34` / `11.54` | `18.06` | `-0.142` | `NONE` | 69536.28526 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2000.22 | 2153.235068 | `-7.11%` | `25.86` / `23.87` | `24.13` | `-0.033` | `BULLISH_HAMMER` | 1948.21428 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.35e-06 | 5e-06 | `-12.16%` | `25.0` / `22.72` | `25.07` | `0.121` | `BULLISH_ENGULFING` | 4.15e-06 | `WATCH` | HOLD |
| `NEARUSDT` | 3.391 | 3.712463 | `-8.66%` | `18.45` / `13.85` | `30.44` | `0.125` | `BULLISH_ENGULFING` | 3.235014 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 81.17 | 87.330391 | `-7.05%` | `22.74` / `18.47` | `27.8` | `0.022` | `BULLISH_HAMMER` | 78.966472 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 958.51 | 1143.553876 | `-16.18%` | `29.46` / `31.84` | `36.51` | `-0.02` | `BEARISH_SHOOTING_STAR` | 914.41854 | `WATCH` | HOLD |
| `UNIUSDT` | 5.979 | 6.808351 | `-12.18%` | `22.99` / `18.5` | `26.04` | `0.111` | `BULLISH_ENGULFING` | 5.74863 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0232 | 1.128229 | `-9.31%` | `21.68` / `20.67` | `29.09` | `-0.04` | `BULLISH_HAMMER` | 0.9965968 | `WATCH` | HOLD |
| `BNBUSDT` | 652.15 | 688.666443 | `-5.30%` | `9.95` / `8.72` | `16.64` | `-0.005` | `NONE` | 635.1941 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1388 | 0.157246 | `-11.73%` | `24.96` / `18.66` | `22.96` | `0.145` | `BULLISH_HAMMER` | 0.13266376 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06523 | 0.070373 | `-7.31%` | `22.74` / `21.02` | `25.7` | `0.001` | `BULLISH_HAMMER` | 0.06316322 | `WATCH` | HOLD |
| `AAVEUSDT` | 112.63 | 126.709958 | `-11.11%` | `20.43` / `13.4` | `26.74` | `0.13` | `BULLISH_ENGULFING` | 107.899198 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1455 | 0.162735 | `-10.59%` | `30.43` / `22.51` | `24.95` | `0.158` | `BEARISH_SHOOTING_STAR` | 0.138807 | `WATCH` | HOLD |
| `SUIUSDT` | 0.7919 | 0.84751 | `-6.56%` | `22.11` / `17.69` | `26.55` | `0.047` | `BULLISH_HAMMER` | 0.76466144 | `P2_EXTREME_CAPITULATION` | **BUY** (85%) |
| `XAUTUSDT` | 3866.65 | 4017.808241 | `-3.76%` | `6.58` / `9.45` | `18.51` | `-0.071` | `BULLISH_HAMMER` | 3766.1171 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LINKUSDT` | 9.92 | 10.628669 | `-6.67%` | `27.51` / `22.0` | `30.26` | `0.161` | `BULLISH_HAMMER` | 9.567632 | `WATCH` | HOLD |
