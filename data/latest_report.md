# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T06:07:41Z`
- **Ciclo de ejecucion:** `#201`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen netamente bajista con la mayoría de los activos cotizando por debajo de la EMA 200 y con pendientes negativas. No se activan entradas LONG (P1-P4) ni SHORT institucionales (S1) al no cumplirse las condiciones estrictas de confluencia en los osciladores y patrones de velas requeridos. Se mantienen las posiciones abiertas sin cambios ya que no se registran posiciones con ganancias para aplicar la gestión dinámica de trailing stop o break-even.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 73562.01 | 75443.663671 | `-2.49%` | `12.55` / `20.07` | `41.48` | `0.16` | `BEARISH_SHOOTING_STAR` | 71649.39774 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `PEPEUSDT` | 4.56e-06 | 5e-06 | `-8.82%` | `12.16` / `13.38` | `25.31` | `0.235` | `BULLISH_HAMMER` | 4.38e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2048.01 | 2165.565239 | `-5.43%` | `18.44` / `22.67` | `41.36` | `0.205` | `NONE` | 1994.76174 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.194 | 6.879937 | `-9.97%` | `19.87` / `21.46` | `33.11` | `0.189` | `BEARISH_ENGULFING` | 5.9970308 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 83.0 | 87.884074 | `-5.56%` | `21.95` / `25.84` | `41.22` | `0.174` | `NONE` | 80.842 | `WATCH` | HOLD |
| `XRPUSDT` | 1.042 | 1.137042 | `-8.36%` | `8.74` / `12.53` | `37.05` | `0.084` | `NONE` | 1.014908 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.524 | 3.74549 | `-5.91%` | `3.47` / `6.84` | `36.29` | `0.116` | `NONE` | 3.4156896 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.4 | 7.910819 | `-6.46%` | `9.12` / `14.62` | `28.45` | `0.096` | `NONE` | 7.11444 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 674.25 | 691.431005 | `-2.48%` | `2.71` / `7.72` | `35.56` | `0.031` | `BEARISH_SHOOTING_STAR` | 656.7195 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1434 | 0.159214 | `-9.93%` | `5.55` / `7.86` | `29.3` | `0.16` | `NONE` | 0.1383112 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1505 | 0.164209 | `-8.35%` | `6.71` / `7.27` | `30.85` | `0.189` | `BEARISH_SHOOTING_STAR` | 0.1452452 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06695 | 0.070794 | `-5.43%` | `20.79` / `25.5` | `35.18` | `0.12` | `BEARISH_SHOOTING_STAR` | 0.0652093 | `WATCH` | HOLD |
| `HYPEUSDT` | 71.51 | 76.871865 | `-6.98%` | `28.16` / `34.62` | `39.66` | `0.141` | `BEARISH_SHOOTING_STAR` | 69.65074 | `WATCH` | HOLD |
| `QNTUSDT` | 165.55 | 189.752523 | `-12.75%` | `12.6` / `12.87` | `27.45` | `0.177` | `BEARISH_ENGULFING` | 158.47288 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LINKUSDT` | 10.044 | 10.713286 | `-6.25%` | `7.58` / `12.61` | `31.06` | `0.111` | `NONE` | 9.782856 | `EXIT_SHORT_STOCH_20` | HOLD |
| `OPGUSDT` | 0.1353 | 0.126043 | `+7.34%` | `15.81` / `10.98` | `49.47` | `0.335` | `BEARISH_SHOOTING_STAR` | 0.1290762 | `EXIT_SHORT_STOCH_20` | HOLD |
