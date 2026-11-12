# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T00:58:54Z`
- **Ciclo de ejecucion:** `#170`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general presenta un régimen dominantemente bajista con la mayoría de los activos cotizando por debajo de la EMA 200 y pendientes negativas. Se identifica una oportunidad de entrada alcista en ENAUSDT activando el Pilar 2 (P2_EXTREME_CAPITULATION) debido a la capitulación extrema con volumen institucional elevado, estocástico recuperándose desde sobreventa y vela Martillo Alcista. El resto de activos se mantiene en observación hasta confirmar confluencia técnica en soporte o resistencia clave.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.55e-06 | 5e-06 | `-9.65%` | `5.09` / `3.6` | `20.55` | `0.062` | `NONE` | 4.34e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.229 | 6.920795 | `-10.00%` | `9.11` / `21.87` | `27.84` | `-0.047` | `BULLISH_HAMMER` | 5.942466 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.514 | 7.94677 | `-5.45%` | `9.71` / `9.67` | `28.65` | `-0.034` | `NONE` | 7.1740156 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.152 | 0.165122 | `-7.95%` | `9.57` / `8.77` | `28.9` | `-0.081` | `NONE` | 0.1457016 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1467 | 0.160295 | `-8.48%` | `18.34` / `12.82` | `35.57` | `0.043` | `BULLISH_HAMMER` | 0.1399518 | `P2_EXTREME_CAPITULATION` | **BUY** (85%) |
| `BTCUSDT` | 74104.01 | 75549.065837 | `-1.91%` | `44.31` / `54.2` | `50.19` | `0.535` | `BULLISH_HAMMER` | 72177.30574 | `WATCH` | **HOLD** (70%) |
| `AAVEUSDT` | 119.91 | 128.911525 | `-6.98%` | `18.83` / `16.26` | `31.48` | `-0.117` | `BULLISH_HAMMER` | 115.528358 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PAXGUSDT` | 3990.41 | 4036.265092 | `-1.14%` | `12.37` / `7.17` | `35.17` | `0.302` | `BULLISH_ENGULFING` | 3886.65934 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 988.24 | 1172.344696 | `-15.70%` | `31.37` / `35.28` | `43.48` | `0.473` | `BULLISH_ENGULFING` | 942.78096 | `WATCH` | HOLD |
| `ETHUSDT` | 2062.5 | 2172.619579 | `-5.07%` | `30.5` / `35.34` | `46.61` | `0.408` | `BULLISH_HAMMER` | 2001.18 | `WATCH` | **HOLD** (70%) |
| `ONEUSDT` | 0.001474 | 0.001552 | `-5.00%` | `5.29` / `5.87` | `33.41` | `0.217` | `BEARISH_SHOOTING_STAR` | 0.0014062 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 83.62 | 88.21467 | `-5.21%` | `30.11` / `39.34` | `45.09` | `0.353` | `BULLISH_HAMMER` | 80.417256 | `WATCH` | **HOLD** (70%) |
| `SNXXBUSDT` | 4.16 | 4.19506 | `-0.84%` | `38.19` / `51.37` | `52.22` | `0.457` | `BEARISH_SHOOTING_STAR` | 3.96864 | `WATCH` | HOLD |
| `MUBUSDT` | 790.32 | 756.010545 | `+4.54%` | `44.99` / `57.35` | `55.01` | `0.495` | `BEARISH_SHOOTING_STAR` | 753.96528 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0587 | 1.142736 | `-7.35%` | `28.93` / `28.49` | `46.8` | `0.392` | `BULLISH_HAMMER` | 1.01792034 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0893 | 0.074949 | `+19.15%` | `75.96` / `67.35` | `64.03` | `0.893` | `MORNING_STAR` | 0.0851922 | `WATCH` | HOLD |
