# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T00:39:15Z`
- **Ciclo de ejecucion:** `#71`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen macro bajista generalizado con la mayoría de los activos cotizando por debajo de la EMA 200 y con baja volatilidad de volumen institucional (volume_ratio < 1.0). No se cumplen de forma estricta los requisitos de entrada de los Pilares LONG (P1-P4) ni del Pilar SHORT (S1) debido a que los osciladores y patrones de velas no convergen en los niveles de activación exactos requeridos. No hay posiciones abiertas con ganancias que requieran ajuste dinámico (ADJUST), por lo que el sistema se mantiene en modo HOLD / WATCH.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1046.93 | 1221.920602 | `-14.32%` | `23.95` / `25.64` | `34.74` | `0.267` | `NONE` | 998.77122 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1612 | 0.166375 | `-3.11%` | `43.02` / `36.72` | `39.97` | `0.38` | `NONE` | 0.1537848 | `WATCH` | HOLD |
| `UNIUSDT` | 6.741 | 7.013633 | `-3.89%` | `14.15` / `14.04` | `42.79` | `0.31` | `BULLISH_HAMMER` | 6.430914 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 4027.85 | 4035.498517 | `-0.19%` | `30.2` / `24.29` | `36.12` | `0.341` | `NONE` | 3923.1259 | `WATCH` | HOLD |
| `BTCUSDT` | 73758.01 | 75912.326962 | `-2.84%` | `48.26` / `48.52` | `44.63` | `0.394` | `BULLISH_HAMMER` | 71840.30174 | `WATCH` | **HOLD** (75%) |
| `ETHUSDT` | 2057.24 | 2199.31099 | `-6.46%` | `44.41` / `43.29` | `41.34` | `0.384` | `NONE` | 1988.870312 | `WATCH` | HOLD |
| `INITUSDT` | 0.26824 | 0.163924 | `+63.64%` | `57.17` / `60.11` | `57.16` | `0.579` | `BEARISH_ENGULFING` | 0.25590096 | `WATCH` | HOLD |
| `PAXGUSDT` | 4029.75 | 4041.703484 | `-0.30%` | `30.1` / `24.04` | `35.67` | `0.332` | `MORNING_STAR` | 3924.9765 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001824 | 0.00154 | `+18.46%` | `48.06` / `49.2` | `57.48` | `0.6` | `NONE` | 0.0017401 | `WATCH` | HOLD |
| `SOLUSDT` | 83.61 | 89.390641 | `-6.47%` | `46.3` / `41.7` | `42.54` | `0.412` | `BULLISH_ENGULFING` | 80.385974 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0562 | 1.16452 | `-9.30%` | `44.82` / `44.04` | `37.8` | `0.291` | `BULLISH_HAMMER` | 1.0209264 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.45e-06 | 5e-06 | `+8.14%` | `52.29` / `41.18` | `60.8` | `0.942` | `NONE` | 5.2e-06 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.131 | 1.104455 | `+2.40%` | `71.21` / `76.73` | `62.21` | `0.801` | `BEARISH_SHOOTING_STAR` | 1.078974 | `WATCH` | HOLD |
| `NEARUSDT` | 3.649 | 3.773974 | `-3.31%` | `42.74` / `37.45` | `54.94` | `0.735` | `MORNING_STAR` | 3.481146 | `WATCH` | HOLD |
| `BNBUSDT` | 681.5 | 693.992582 | `-1.80%` | `46.92` / `40.88` | `47.47` | `0.444` | `NONE` | 663.781 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0012 | 1.001214 | `-0.00%` | `83.33` / `70.63` | `54.62` | `0.639` | `BULLISH_HAMMER` | 0.9751688 | `EXIT_LONG_STOCH_80` | HOLD |
