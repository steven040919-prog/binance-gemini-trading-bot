# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T23:41:36Z`
- **Ciclo de ejecucion:** `#165`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se mantiene bajo una presión bajista generalizada con la mayoría de los activos cotizando por debajo de la EMA 200 en temporalidad 1H. No se han detectado señales de entrada bajo los pilares P1-P4 (LONG) ni S1 (SHORT) debido a que, aunque existen patrones de velas (Martillo), los indicadores estocásticos no muestran el giro alcista confirmado necesario o la confluencia de volumen institucional requerida. La estrategia se mantiene en modo observador (WATCH) para preservar el capital ante la falta de setups de alta probabilidad.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.56e-06 | 5e-06 | `-9.55%` | `4.35` / `3.67` | `18.08` | `0.014` | `NONE` | 4.35e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 966.64 | 1174.262493 | `-17.68%` | `31.02` / `44.13` | `35.47` | `0.069` | `BEARISH_SHOOTING_STAR` | 922.17456 | `WATCH` | HOLD |
| `ETHUSDT` | 2052.59 | 2173.41948 | `-5.56%` | `30.34` / `42.92` | `41.82` | `0.192` | `BULLISH_HAMMER` | 1999.22266 | `WATCH` | HOLD |
| `UNIUSDT` | 6.258 | 6.923045 | `-9.61%` | `20.22` / `38.42` | `28.92` | `-0.085` | `NONE` | 5.9992216 | `WATCH` | HOLD |
| `SOLUSDT` | 83.01 | 88.237906 | `-5.92%` | `33.53` / `51.39` | `39.73` | `0.192` | `BULLISH_HAMMER` | 80.396984 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0493 | 1.14322 | `-8.22%` | `22.32` / `30.16` | `39.39` | `-0.002` | `BULLISH_HAMMER` | 1.01812526 | `WATCH` | HOLD |
| `NEARUSDT` | 3.568 | 3.759485 | `-5.09%` | `23.89` / `39.14` | `39.63` | `0.072` | `NONE` | 3.403872 | `WATCH` | HOLD |
| `BNBUSDT` | 678.86 | 691.763632 | `-1.87%` | `35.16` / `55.69` | `40.97` | `0.156` | `NONE` | 661.20964 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1513 | 0.165204 | `-8.42%` | `5.82` / `10.13` | `27.45` | `-0.231` | `NONE` | 0.14569528 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1451 | 0.160345 | `-9.51%` | `9.07` / `11.14` | `29.73` | `-0.183` | `BULLISH_HAMMER` | 0.1384254 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.495 | 7.949775 | `-5.72%` | `6.19` / `10.67` | `28.16` | `-0.129` | `NONE` | 7.213172 | `EXIT_SHORT_STOCH_20` | HOLD |
| `OPGUSDT` | 0.1357 | 0.125795 | `+7.87%` | `13.19` / `22.52` | `48.84` | `0.422` | `BEARISH_SHOOTING_STAR` | 0.1294578 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LINKUSDT` | 10.153 | 10.747873 | `-5.53%` | `20.44` / `33.82` | `33.76` | `-0.103` | `BULLISH_HAMMER` | 9.766175 | `WATCH` | HOLD |
| `XAUTUSDT` | 3974.68 | 4031.165578 | `-1.40%` | `5.0` / `5.04` | `21.18` | `0.16` | `BEARISH_SHOOTING_STAR` | 3871.33832 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SUIUSDT` | 0.8201 | 0.854637 | `-4.04%` | `23.34` / `36.58` | `39.04` | `0.09` | `BULLISH_HAMMER` | 0.78975358 | `WATCH` | HOLD |
| `BTCUSDT` | 73866.48 | 75554.512195 | `-2.23%` | `47.53` / `64.42` | `46.25` | `0.363` | `BULLISH_HAMMER` | 71945.95152 | `WATCH` | **HOLD** (0%) |
