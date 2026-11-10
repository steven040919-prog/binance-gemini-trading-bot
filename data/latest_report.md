# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-10T23:47:12Z`
- **Ciclo de ejecucion:** `#50`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se mantiene en un régimen predominantemente bajista con la mayoría de los activos cotizando por debajo de la EMA 200. No se han detectado señales de entrada bajo los pilares P1-P4 ni S1, ya que los patrones de velas actuales no presentan la confluencia técnica requerida (sobreventa extrema con giro confirmado o rechazo en resistencia con sobrecompra). Se mantiene una postura de observación (WATCH) para evitar falsas rupturas en un entorno de baja volatilidad y volumen institucional insuficiente.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1045.59 | 1223.580644 | `-14.55%` | `26.03` / `26.44` | `34.3` | `0.236` | `BEARISH_ENGULFING` | 997.49286 | `WATCH` | HOLD |
| `UNIUSDT` | 6.681 | 7.015122 | `-4.76%` | `14.1` / `15.63` | `37.61` | `0.195` | `BEARISH_ENGULFING` | 6.373674 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1609 | 0.166354 | `-3.28%` | `37.19` / `30.65` | `38.76` | `0.344` | `MORNING_STAR` | 0.1534986 | `WATCH` | HOLD |
| `QNTUSDT` | 181.27 | 194.462493 | `-6.78%` | `38.2` / `38.02` | `33.43` | `0.267` | `BULLISH_HAMMER` | 172.93158 | `WATCH` | HOLD |
| `AAVEUSDT` | 123.82 | 129.636261 | `-4.49%` | `53.91` / `48.87` | `35.79` | `0.317` | `BEARISH_SHOOTING_STAR` | 119.21776 | `WATCH` | HOLD |
| `XAUTUSDT` | 4027.82 | 4035.475011 | `-0.19%` | `23.33` / `19.07` | `35.36` | `0.322` | `BULLISH_HAMMER` | 3923.09668 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73832.01 | 75928.594191 | `-2.76%` | `49.9` / `47.2` | `45.66` | `0.406` | `BEARISH_ENGULFING` | 71912.37774 | `WATCH` | **HOLD** (0%) |
| `TRXUSDT` | 0.3178 | 0.319093 | `-0.41%` | `14.44` / `14.44` | `43.11` | `0.227` | `NONE` | 0.3095372 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2052.94 | 2200.513348 | `-6.71%` | `42.79` / `42.07` | `39.48` | `0.335` | `NONE` | 1986.930032 | `WATCH` | HOLD |
| `PAXGUSDT` | 4030.02 | 4041.769603 | `-0.29%` | `22.51` / `18.75` | `34.75` | `0.316` | `BULLISH_ENGULFING` | 3925.23948 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INITUSDT` | 0.27715 | 0.163215 | `+69.81%` | `60.61` / `64.94` | `59.7` | `0.651` | `BULLISH_HAMMER` | 0.2644011 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001851 | 0.001537 | `+20.41%` | `48.72` / `51.25` | `59.97` | `0.663` | `NONE` | 0.00176585 | `WATCH` | HOLD |
| `SOLUSDT` | 83.45 | 89.433229 | `-6.69%` | `41.51` / `38.85` | `40.79` | `0.365` | `BEARISH_ENGULFING` | 80.24002 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0567 | 1.165371 | `-9.33%` | `44.61` / `43.55` | `38.03` | `0.276` | `BEARISH_ENGULFING` | 1.0198557 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.36e-06 | 5e-06 | `+6.49%` | `38.56` / `32.9` | `56.36` | `0.698` | `MORNING_STAR` | 5.11e-06 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.142 | 1.104048 | `+3.44%` | `80.65` / `78.59` | `67.18` | `0.971` | `NONE` | 1.089468 | `EXIT_LONG_STOCH_80` | HOLD |
