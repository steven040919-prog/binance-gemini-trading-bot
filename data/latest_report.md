# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T18:44:38Z`
- **Ciclo de ejecucion:** `#145`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado presenta un sesgo bajista predominante con la mayoría de los activos operando por debajo de la EMA 200. Los pilares LONG (P1-P4) no encuentran condiciones de entrada válidas debido a la falta de confluencia técnica en los activos analizados. El pilar SHORT (S1) tampoco presenta señales de entrada claras bajo los criterios de rechazo en resistencia EMA 200. Se mantiene una postura de espera (HOLD) para preservar el capital, ya que no se cumplen los requisitos de alta probabilidad de nuestra arquitectura institucional.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.92e-06 | 5e-06 | `-2.74%` | `7.54` / `7.99` | `31.85` | `0.203` | `BEARISH_SHOOTING_STAR` | 4.69e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001502 | 0.001556 | `-3.45%` | `4.49` / `8.74` | `35.61` | `0.206` | `NONE` | 0.00143291 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74553.7 | 75603.820107 | `-1.39%` | `81.75` / `72.01` | `59.63` | `1.085` | `NONE` | 72615.3038 | `EXIT_LONG_STOCH_80` | **HOLD** (0%) |
| `XAUTUSDT` | 3984.6 | 4033.964787 | `-1.22%` | `2.81` / `3.81` | `22.62` | `-0.008` | `BULLISH_HAMMER` | 3881.0004 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `INJUSDT` | 7.961 | 7.949436 | `+0.15%` | `27.3` / `24.75` | `46.53` | `0.335` | `BEARISH_ENGULFING` | 7.652326 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1592 | 0.165672 | `-3.91%` | `35.6` / `35.75` | `42.3` | `0.263` | `BULLISH_HAMMER` | 0.15369216 | `WATCH` | HOLD |
| `PAXGUSDT` | 3986.49 | 4039.618478 | `-1.32%` | `1.43` / `3.29` | `22.53` | `-0.015` | `NONE` | 3882.84126 | `EXIT_SHORT_STOCH_20` | HOLD |
| `MUBUSDT` | 827.09 | 752.787901 | `+9.87%` | `96.81` / `97.26` | `81.95` | `0.973` | `BULLISH_ENGULFING` | 789.04386 | `EXIT_LONG_STOCH_80` | HOLD |
| `ETHUSDT` | 2088.18 | 2178.034119 | `-4.13%` | `74.68` / `68.54` | `58.9` | `1.042` | `NONE` | 2033.88732 | `WATCH` | HOLD |
| `ZECUSDT` | 1008.62 | 1184.207291 | `-14.83%` | `66.95` / `51.2` | `45.03` | `0.573` | `BULLISH_ENGULFING` | 962.22348 | `WATCH` | HOLD |
| `SOXSBUSDT` | 42.12 | 59.952795 | `-29.74%` | `4.23` / `5.79` | `23.72` | `0.042` | `BEARISH_SHOOTING_STAR` | 40.18248 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SNXXBUSDT` | 4.63 | 4.1748 | `+10.90%` | `96.08` / `96.85` | `79.09` | `0.942` | `BEARISH_ENGULFING` | 4.41702 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 85.26 | 88.44941 | `-3.61%` | `84.13` / `82.14` | `60.75` | `0.966` | `BULLISH_HAMMER` | 82.811852 | `EXIT_LONG_STOCH_80` | HOLD |
| `GRAMUSDT` | 1.228 | 1.118613 | `+9.78%` | `66.41` / `59.76` | `65.05` | `0.84` | `MORNING_STAR` | 1.171512 | `WATCH` | HOLD |
| `NEARUSDT` | 3.738 | 3.768532 | `-0.81%` | `78.24` / `78.36` | `55.75` | `0.697` | `NONE` | 3.5789752 | `WATCH` | HOLD |
| `INTCBUSDT` | 63.28 | 58.879458 | `+7.47%` | `88.08` / `91.63` | `70.76` | `0.86` | `NONE` | 60.712848 | `EXIT_LONG_STOCH_80` | HOLD |
