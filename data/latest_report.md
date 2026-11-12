# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T00:43:22Z`
- **Ciclo de ejecucion:** `#169`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen claramente bajista con la gran mayoría de los activos cotizando por debajo de la EMA 200 en la temporalidad de 1H. Ninguno de los activos evaluados cumple estrictamente con los requisitos cuantitativos completos de los 4 Pilares LONG (P1 a P4) ni del Pilar SHORT (S1) para una ejecución de entrada inmediata, ya que faltan confluencias críticas en los niveles de sobreventa/sobrecompra o en las pendientes de las medias móviles. No hay posiciones abiertas actuales en el portafolio para gestionar con ajuste dinámico (ADJUST), por lo que la decisión global es mantener la postura en observación (HOLD) con los activos evaluados.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.57e-06 | 5e-06 | `-9.26%` | `6.32` / `4.01` | `22.69` | `0.081` | `NONE` | 4.36e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.25 | 6.921004 | `-9.70%` | `10.41` / `22.31` | `29.64` | `-0.013` | `BULLISH_HAMMER` | 5.9625 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.506 | 7.94669 | `-5.55%` | `9.3` / `9.53` | `28.42` | `-0.041` | `NONE` | 7.1742924 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1525 | 0.165127 | `-7.65%` | `10.88` / `9.21` | `30.75` | `-0.05` | `NONE` | 0.145715 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3981.84 | 4030.612125 | `-1.21%` | `9.76` / `6.6` | `30.33` | `0.252` | `BULLISH_ENGULFING` | 3878.31216 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74040.14 | 75548.430315 | `-2.00%` | `42.81` / `53.7` | `49.09` | `0.484` | `BULLISH_HAMMER` | 72115.09636 | `WATCH` | **HOLD** (75%) |
| `AAVEUSDT` | 119.99 | 128.912321 | `-6.92%` | `19.24` / `16.4` | `31.74` | `-0.106` | `BULLISH_HAMMER` | 115.55026 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PAXGUSDT` | 3982.77 | 4036.189072 | `-1.32%` | `9.18` / `6.1` | `28.6` | `0.242` | `BULLISH_ENGULFING` | 3879.21798 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 992.9 | 1172.391064 | `-15.31%` | `33.48` / `35.98` | `44.89` | `0.556` | `BULLISH_ENGULFING` | 947.2266 | `WATCH` | HOLD |
| `ETHUSDT` | 2061.79 | 2172.612514 | `-5.10%` | `30.15` / `35.23` | `46.25` | `0.393` | `BULLISH_HAMMER` | 2001.191928 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001469 | 0.001552 | `-5.32%` | `4.2` / `5.51` | `32.64` | `0.202` | `BEARISH_SHOOTING_STAR` | 0.00140143 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SNXXBUSDT` | 4.24 | 4.195856 | `+1.05%` | `41.84` / `52.59` | `55.55` | `0.524` | `NONE` | 4.04496 | `WATCH` | HOLD |
| `MUBUSDT` | 796.85 | 756.07552 | `+5.39%` | `48.39` / `58.48` | `58.27` | `0.561` | `BULLISH_ENGULFING` | 760.1949 | `WATCH` | HOLD |
| `SOLUSDT` | 83.67 | 88.215167 | `-5.15%` | `30.57` / `39.49` | `45.57` | `0.368` | `BULLISH_HAMMER` | 80.43293 | `WATCH` | HOLD |
| `SOXSBUSDT` | 47.5 | 59.121015 | `-19.66%` | `69.09` / `60.94` | `47.06` | `0.618` | `BEARISH_ENGULFING` | 45.315 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0583 | 1.142732 | `-7.39%` | `28.6` / `28.38` | `46.48` | `0.374` | `BULLISH_HAMMER` | 1.01814072 | `WATCH` | HOLD |
