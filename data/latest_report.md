# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T02:01:21Z`
- **Ciclo de ejecucion:** `#174`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `7.00 USDT`
- **Liquidez Disponible:** `7.00 USDT`
- **Rendimiento Diario (UTC):** `-50.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen netamente bajista (BEARISH) con todos los activos evaluados cotizando por debajo de la EMA 200 y pendientes negativas. No se cumplen las condiciones institucionales de los Pilares LONG (P1-P4) ya que los precios están alejados de la zona de valor alcista y el Estocástico/RSI no muestran capitulaciones concurrentes válidas para compra en este marco temporal. Tampoco se activan entradas SHORT bajo el Pilar S1 (falta de pullback alcista a la resistencia de la EMA 200 con sobrecompra). Por lo tanto, el sistema se mantiene en modo de espera (HOLD) protegiendo el capital disponible y sin posiciones abiertas que requieran ajuste dinámico.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.55e-06 | 5e-06 | `-9.47%` | `10.49` / `8.06` | `21.29` | `0.126` | `BULLISH_HAMMER` | 4.34e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73591.58 | 75516.454051 | `-2.55%` | `28.78` / `37.17` | `42.14` | `0.131` | `BEARISH_ENGULFING` | 71678.19892 | `WATCH` | **HOLD** (75%) |
| `ETHUSDT` | 2047.74 | 2170.180002 | `-5.64%` | `26.45` / `29.18` | `40.37` | `0.137` | `BEARISH_ENGULFING` | 1994.49876 | `WATCH` | HOLD |
| `UNIUSDT` | 6.108 | 6.911077 | `-11.62%` | `5.87` / `7.17` | `23.59` | `-0.053` | `NONE` | 5.8858904 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 82.96 | 88.097801 | `-5.83%` | `28.87` / `30.29` | `40.01` | `0.126` | `BEARISH_ENGULFING` | 80.80304 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0468 | 1.140756 | `-8.24%` | `25.8` / `28.21` | `39.02` | `-0.005` | `BEARISH_ENGULFING` | 1.0195832 | `WATCH` | HOLD |
| `NEARUSDT` | 3.581 | 3.753436 | `-4.59%` | `24.21` / `23.63` | `41.38` | `0.161` | `NONE` | 3.4432326 | `WATCH` | HOLD |
| `INJUSDT` | 7.45 | 7.929647 | `-6.05%` | `10.32` / `11.02` | `27.15` | `0.018` | `BEARISH_ENGULFING` | 7.14674 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.15 | 0.164779 | `-8.97%` | `4.76` / `6.74` | `25.43` | `-0.012` | `NONE` | 0.1449 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 677.21 | 691.526591 | `-2.07%` | `18.36` / `24.33` | `39.21` | `0.043` | `BEARISH_ENGULFING` | 659.60254 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1443 | 0.159961 | `-9.79%` | `17.72` / `18.78` | `30.02` | `0.014` | `BEARISH_ENGULFING` | 0.1388609 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 165.06 | 190.782008 | `-13.48%` | `4.7` / `9.35` | `25.28` | `-0.039` | `NONE` | 157.865552 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06703 | 0.070944 | `-5.52%` | `28.53` / `30.63` | `34.31` | `0.009` | `BEARISH_ENGULFING` | 0.06528722 | `WATCH` | HOLD |
| `LINKUSDT` | 10.089 | 10.74247 | `-6.08%` | `20.86` / `24.28` | `31.27` | `-0.022` | `BEARISH_ENGULFING` | 9.8247216 | `WATCH` | HOLD |
| `AAVEUSDT` | 118.06 | 128.569046 | `-8.17%` | `8.12` / `14.6` | `26.16` | `-0.08` | `NONE` | 114.648768 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SUIUSDT` | 0.817 | 0.853892 | `-4.32%` | `22.4` / `23.78` | `36.97` | `0.066` | `BEARISH_ENGULFING` | 0.795758 | `WATCH` | HOLD |
