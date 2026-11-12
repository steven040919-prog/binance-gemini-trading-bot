# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T06:36:11Z`
- **Ciclo de ejecucion:** `#204`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> Evaluación general del mercado en temporalidad de 1 hora con sesgo bajista consolidado (todos los activos cotizan por debajo de la EMA 200 con pendientes negativas). Se revisan las condiciones de los Pilares Long (P1 a P4) y del Pilar Short (S1). No se cumplen de forma simultánea todos los filtros estrictos de entrada (como giros validados del estocástico desde sobreventa profunda con confirmación de velas alcistas estructurales para long, o rechazos óptimos con estocástico sobrecomprado para short). Por lo tanto, el sistema se mantiene en modo de observación y gestión de riesgo, sin aperturas nuevas y esperando confirmaciones institucionales precisas en los próximos ciclos.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 73659.45 | 75444.633223 | `-2.37%` | `14.99` / `20.89` | `43.6` | `0.225` | `NONE` | 71744.3043 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `PEPEUSDT` | 4.55e-06 | 5e-06 | `-9.02%` | `11.51` / `13.17` | `24.86` | `0.223` | `BULLISH_HAMMER` | 4.38e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2049.74 | 2165.582453 | `-5.35%` | `19.29` / `22.96` | `42.45` | `0.235` | `NONE` | 1996.44676 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.175 | 6.879748 | `-10.24%` | `18.79` / `21.1` | `32.23` | `0.163` | `BEARISH_ENGULFING` | 5.96893 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 82.98 | 87.883875 | `-5.58%` | `21.77` / `25.78` | `40.97` | `0.168` | `BEARISH_SHOOTING_STAR` | 80.82252 | `WATCH` | **HOLD** (70%) |
| `NEARUSDT` | 3.528 | 3.74553 | `-5.81%` | `3.92` / `6.99` | `36.73` | `0.125` | `BEARISH_SHOOTING_STAR` | 3.4127488 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0419 | 1.137041 | `-8.37%` | `8.66` / `12.51` | `36.94` | `0.081` | `BEARISH_SHOOTING_STAR` | 1.0148106 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.415 | 7.910969 | `-6.27%` | `9.81` / `14.85` | `29.64` | `0.111` | `NONE` | 7.109475 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 675.16 | 691.440059 | `-2.35%` | `4.68` / `8.38` | `37.83` | `0.077` | `NONE` | 657.60584 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1428 | 0.159208 | `-10.31%` | `4.54` / `7.52` | `26.99` | `0.129` | `NONE` | 0.13784472 | `EXIT_SHORT_STOCH_20` | HOLD |
| `HYPEUSDT` | 71.55 | 76.872263 | `-6.92%` | `28.51` / `34.74` | `40.15` | `0.152` | `BEARISH_SHOOTING_STAR` | 69.6897 | `WATCH` | HOLD |
| `DOGEUSDT` | 0.06708 | 0.070795 | `-5.25%` | `22.15` / `25.95` | `37.36` | `0.159` | `NONE` | 0.06533592 | `WATCH` | HOLD |
| `QNTUSDT` | 165.45 | 189.751528 | `-12.81%` | `12.43` / `12.81` | `27.31` | `0.174` | `BEARISH_ENGULFING` | 158.01436 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1502 | 0.164206 | `-8.53%` | `6.0` / `7.04` | `30.28` | `0.175` | `BEARISH_SHOOTING_STAR` | 0.14513392 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LINKUSDT` | 10.072 | 10.713565 | `-5.99%` | `9.21` / `13.15` | `33.93` | `0.148` | `NONE` | 9.7953152 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3966.8 | 4027.355228 | `-1.50%` | `16.3` / `17.64` | `30.1` | `0.219` | `BULLISH_HAMMER` | 3863.6632 | `EXIT_SHORT_STOCH_20` | HOLD |
