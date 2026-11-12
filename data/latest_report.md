# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T17:15:25Z`
- **Ciclo de ejecucion:** `#242`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> Mercado predominantemente bajista con activos cotizando por debajo de la EMA 200 H1. Se identifican dos oportunidades de compra institucional por Capitulación Extrema (Pilar 2 P2_EXTREME_CAPITULATION) en BTCUSDT y XAUTUSDT impulsadas por clímax de volumen, extrema sobreventa en RSI y Estocástico con giro alcista. Los activos en setup de salida por sobreventa (BNBUSDT, PEPEUSDT, QNTUSDT) y ETHUSDT se mantienen en espera o fuera de entradas cortas por falta de confluencia clara.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71717.16 | 75142.092035 | `-4.56%` | `17.58` / `15.85` | `22.14` | `0.056` | `BEARISH_SHOOTING_STAR` | 69852.51384 | `P2_EXTREME_CAPITULATION` | **BUY** (85%) |
| `ETHUSDT` | 2006.78 | 2150.156558 | `-6.67%` | `31.22` / `30.07` | `27.9` | `0.104` | `BEARISH_SHOOTING_STAR` | 2061.432548 | `M15_SCALPER_PULLBACK_SHORT` | **HOLD** (40%) |
| `PEPEUSDT` | 4.31e-06 | 5e-06 | `-12.64%` | `9.48` / `18.44` | `23.24` | `0.07` | `BEARISH_SHOOTING_STAR` | 4.13e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (30%) |
| `ZECUSDT` | 948.92 | 1139.935103 | `-16.76%` | `20.24` / `27.05` | `33.42` | `-0.054` | `NONE` | 905.26968 | `WATCH` | HOLD |
| `NEARUSDT` | 3.386 | 3.70423 | `-8.59%` | `24.13` / `22.98` | `30.91` | `0.138` | `BULLISH_ENGULFING` | 3.2526796 | `WATCH` | HOLD |
| `SOLUSDT` | 81.23 | 87.172125 | `-6.82%` | `30.84` / `29.53` | `31.84` | `0.052` | `BEARISH_SHOOTING_STAR` | 79.090384 | `WATCH` | HOLD |
| `UNIUSDT` | 5.979 | 6.792066 | `-11.97%` | `22.87` / `25.5` | `26.65` | `0.06` | `BEARISH_SHOOTING_STAR` | 5.7510216 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0223 | 1.125901 | `-9.20%` | `20.23` / `22.13` | `28.69` | `0.022` | `BEARISH_ENGULFING` | 0.9957202 | `WATCH` | HOLD |
| `ENAUSDT` | 0.1382 | 0.1568 | `-11.86%` | `23.76` / `26.36` | `21.5` | `0.104` | `BEARISH_SHOOTING_STAR` | 0.1328158 | `WATCH` | HOLD |
| `BNBUSDT` | 655.33 | 687.883591 | `-4.73%` | `18.0` / `15.28` | `24.44` | `0.138` | `BEARISH_SHOOTING_STAR` | 638.29142 | `EXIT_SHORT_STOCH_20` | **HOLD** (30%) |
| `DOGEUSDT` | 0.06564 | 0.070263 | `-6.58%` | `35.82` / `30.22` | `33.02` | `0.147` | `BEARISH_SHOOTING_STAR` | 0.06316782 | `WATCH` | HOLD |
| `AAVEUSDT` | 113.16 | 126.418857 | `-10.49%` | `28.85` / `27.01` | `29.14` | `0.206` | `BEARISH_SHOOTING_STAR` | 109.215736 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1454 | 0.162424 | `-10.48%` | `37.9` / `35.87` | `27.47` | `0.14` | `NONE` | 0.14053592 | `WATCH` | HOLD |
| `XAUTUSDT` | 3871.03 | 4015.240508 | `-3.59%` | `16.36` / `11.72` | `22.62` | `0.086` | `BULLISH_ENGULFING` | 3770.38322 | `P2_EXTREME_CAPITULATION` | **BUY** (88%) |
| `SUIUSDT` | 0.7937 | 0.846268 | `-6.21%` | `31.89` / `28.45` | `31.7` | `0.112` | `BEARISH_SHOOTING_STAR` | 0.76682112 | `WATCH` | HOLD |
| `QNTUSDT` | 160.92 | 187.03559 | `-13.96%` | `18.43` / `21.44` | `26.62` | `0.038` | `NONE` | 155.591136 | `EXIT_SHORT_STOCH_20` | HOLD |
