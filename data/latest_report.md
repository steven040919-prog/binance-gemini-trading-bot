# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T21:51:45Z`
- **Ciclo de ejecucion:** `#158`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen predominantemente bajista con la mayoría de los activos cotizando por debajo de la EMA 200. No se activan nuevos pilares de entrada LONG (P1-P4) debido a que no cumplen las condiciones estrictas de sobreventa extrema con giro alcista y patrones limpios, ni tampoco se activa el Pilar SHORT (S1) ya que los candidatos no presentan un rechazo bajista válido en la resistencia de la EMA 200 con sobrecompra en el estocástico. Las posiciones abiertas son nulas, por lo que se mantiene la postura de observación y control de riesgo manteniendo liquidez en USD.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 990.41 | 1177.730027 | `-15.91%` | `56.86` / `58.52` | `41.02` | `0.404` | `NONE` | 944.85114 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.67e-06 | 5e-06 | `-7.55%` | `3.49` / `3.57` | `21.31` | `0.038` | `NONE` | 4.46e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001485 | 0.001553 | `-4.40%` | `4.51` / `3.95` | `34.14` | `0.222` | `NONE` | 0.00141669 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOXSBUSDT` | 45.03 | 59.499441 | `-24.32%` | `35.64` / `25.73` | `37.5` | `0.325` | `NONE` | 42.95862 | `WATCH` | HOLD |
| `INJUSDT` | 7.831 | 7.948995 | `-1.48%` | `14.9` / `20.86` | `40.25` | `0.211` | `NONE` | 7.5268784 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74467.37 | 75582.719904 | `-1.48%` | `80.27` / `79.79` | `56.43` | `0.839` | `BULLISH_ENGULFING` | 72531.21838 | `EXIT_LONG_STOCH_80` | **HOLD** (75%) |
| `ENAUSDT` | 0.1496 | 0.160551 | `-6.82%` | `14.96` / `23.39` | `40.24` | `-0.063` | `NONE` | 0.14444272 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1567 | 0.165467 | `-5.30%` | `15.91` / `21.67` | `36.77` | `0.081` | `BEARISH_ENGULFING` | 0.15194972 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3980.16 | 4032.433322 | `-1.30%` | `3.67` / `2.73` | `21.53` | `0.134` | `BULLISH_ENGULFING` | 3876.67584 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LTCUSDT` | 50.71 | 52.265125 | `-2.98%` | `36.37` / `48.32` | `43.61` | `0.141` | `BEARISH_SHOOTING_STAR` | 49.39154 | `WATCH` | HOLD |
| `PAXGUSDT` | 3982.0 | 4037.935954 | `-1.39%` | `3.54` / `2.48` | `21.44` | `0.13` | `BEARISH_SHOOTING_STAR` | 3878.468 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2074.85 | 2175.747029 | `-4.64%` | `57.39` / `62.34` | `51.51` | `0.673` | `NONE` | 2020.9039 | `WATCH` | HOLD |
| `MUBUSDT` | 815.58 | 754.565226 | `+8.09%` | `82.11` / `87.09` | `71.66` | `0.783` | `NONE` | 784.458832 | `EXIT_LONG_STOCH_80` | HOLD |
| `SNXXBUSDT` | 4.48 | 4.183966 | `+7.08%` | `78.85` / `84.54` | `67.53` | `0.756` | `NONE` | 4.27392 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 84.69 | 88.336133 | `-4.13%` | `70.17` / `74.45` | `53.94` | `0.705` | `BULLISH_ENGULFING` | 82.48806 | `WATCH` | HOLD |
| `NEARUSDT` | 3.672 | 3.765963 | `-2.50%` | `54.76` / `60.8` | `48.78` | `0.398` | `BEARISH_ENGULFING` | 3.5225888 | `WATCH` | HOLD |
