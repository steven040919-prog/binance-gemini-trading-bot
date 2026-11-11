# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T19:46:56Z`
- **Ciclo de ejecucion:** `#150`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado mantiene un sesgo bajista predominante con la gran mayoria de los activos cotizando por debajo de la EMA 200. Sin embargo, destaca la activacion del Pilar 2 (P2_EXTREME_CAPITULATION) en SOXSBUSDT, cumpliendo con condiciones estrictas de sobreventa extrema, estocastico girando al alza y patron de vela envolvente alcista. No hay posiciones abiertas actuales para gestion de ajuste, por lo que se ejecuta la orden de compra con asignacion controlada segun gestion de riesgo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.82e-06 | 5e-06 | `-4.73%` | `4.85` / `6.62` | `26.96` | `0.124` | `NONE` | 4.6e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001489 | 0.001555 | `-4.24%` | `1.33` / `4.83` | `34.63` | `0.209` | `NONE` | 0.00142051 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1498 | 0.160948 | `-6.93%` | `28.34` / `46.19` | `41.23` | `-0.134` | `NONE` | 0.14416672 | `WATCH` | HOLD |
| `BTCUSDT` | 74395.0 | 75599.242937 | `-1.59%` | `77.63` / `77.46` | `56.62` | `0.902` | `BULLISH_HAMMER` | 72460.73 | `WATCH` | HOLD |
| `XAUTUSDT` | 3980.85 | 4033.444599 | `-1.30%` | `1.93` / `2.25` | `21.65` | `0.035` | `NONE` | 3877.3479 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1588 | 0.165586 | `-4.10%` | `24.74` / `31.84` | `41.39` | `0.238` | `BULLISH_HAMMER` | 0.152936 | `WATCH` | HOLD |
| `INJUSDT` | 7.871 | 7.950255 | `-1.00%` | `22.43` / `24.89` | `42.29` | `0.221` | `BEARISH_ENGULFING` | 7.579515 | `WATCH` | HOLD |
| `PAXGUSDT` | 3982.39 | 4038.959774 | `-1.40%` | `1.44` / `1.69` | `21.49` | `0.028` | `NONE` | 3878.84786 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 122.96 | 128.85099 | `-4.57%` | `41.52` / `49.28` | `42.93` | `0.163` | `NONE` | 119.688144 | `WATCH` | HOLD |
| `ETHUSDT` | 2078.54 | 2177.500792 | `-4.54%` | `67.43` / `70.64` | `53.81` | `0.814` | `NONE` | 2024.49796 | `WATCH` | HOLD |
| `MUBUSDT` | 817.73 | 753.33425 | `+8.55%` | `92.03` / `95.07` | `74.93` | `0.856` | `BULLISH_ENGULFING` | 792.812284 | `EXIT_LONG_STOCH_80` | HOLD |
| `ZECUSDT` | 995.91 | 1182.485612 | `-15.78%` | `57.3` / `56.03` | `42.13` | `0.452` | `BULLISH_HAMMER` | 950.09814 | `WATCH` | HOLD |
| `SOXSBUSDT` | 44.14 | 59.801319 | `-26.19%` | `14.61` / `7.94` | `32.95` | `0.214` | `BULLISH_ENGULFING` | 42.10956 | `P2_EXTREME_CAPITULATION` | **BUY** (82%) |
| `SNXXBUSDT` | 4.53 | 4.177198 | `+8.45%` | `90.52` / `93.99` | `73.68` | `0.84` | `BEARISH_SHOOTING_STAR` | 4.32162 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 84.67 | 88.42484 | `-4.25%` | `76.31` / `80.56` | `54.46` | `0.764` | `NONE` | 82.46858 | `EXIT_LONG_STOCH_80` | HOLD |
| `GRAMUSDT` | 1.212 | 1.119022 | `+8.31%` | `71.03` / `65.08` | `60.26` | `0.713` | `BEARISH_ENGULFING` | 1.156248 | `WATCH` | HOLD |
