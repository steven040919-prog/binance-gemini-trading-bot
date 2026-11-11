# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T04:18:50Z`
- **Ciclo de ejecucion:** `#104`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global de 1H se encuentra bajo un régimen bajista generalizado con la mayoría de los activos cotizando por debajo de la EMA 200 y con pendientes negativas. Ninguno de los activos cumple con los requisitos estrictos de los Pilares Long (P1-P4) debido a la ausencia de confluencias alcistas extremas y rupturas de soporte estructural o divergencias. Asimismo, en el Pilar Short (S1) de Futuros USDT-M no se cumplen de forma simultánea las condiciones de resistencia de la EMA 200 combinada con estocástico en sobrecompra y giro bajista, ya que la mayoría de los activos muestran lecturas de sobreventa o rangos medios. No hay posiciones abiertas con ganancias para aplicar la gestión dinámica de ajuste (ADJUST), por lo que se mantiene la postura de observación (HOLD/WATCH) preservando el capital libre.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1017.28 | 1214.611251 | `-16.25%` | `13.74` / `14.26` | `31.45` | `0.257` | `BEARISH_ENGULFING` | 970.48512 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.677 | 7.003404 | `-4.66%` | `13.54` / `15.16` | `39.17` | `0.297` | `BEARISH_SHOOTING_STAR` | 6.369858 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 180.45 | 194.189524 | `-7.08%` | `42.69` / `43.03` | `34.06` | `0.289` | `NONE` | 173.90297 | `WATCH` | HOLD |
| `CYBERUSDT` | 0.27 | 0.282947 | `-4.58%` | `3.53` / `4.64` | `44.37` | `0.264` | `BEARISH_ENGULFING` | 0.25758 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73600.1 | 75836.576103 | `-2.95%` | `44.59` / `43.42` | `43.49` | `0.402` | `BEARISH_ENGULFING` | 71686.4974 | `WATCH` | **HOLD** (75%) |
| `TRXUSDT` | 0.3174 | 0.318483 | `-0.34%` | `5.21` / `9.03` | `39.86` | `0.177` | `BEARISH_ENGULFING` | 0.3091476 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2060.37 | 2193.960683 | `-6.09%` | `57.98` / `52.68` | `43.69` | `0.503` | `BEARISH_SHOOTING_STAR` | 2003.484304 | `WATCH` | HOLD |
| `PAXGUSDT` | 4037.17 | 4041.579525 | `-0.11%` | `65.99` / `55.38` | `42.29` | `0.486` | `BEARISH_SHOOTING_STAR` | 3932.20358 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001673 | 0.00155 | `+7.97%` | `32.86` / `55.17` | `44.51` | `-0.072` | `NONE` | 0.00159604 | `WATCH` | HOLD |
| `SOLUSDT` | 83.01 | 89.111792 | `-6.85%` | `49.03` / `49.03` | `37.86` | `0.371` | `BEARISH_SHOOTING_STAR` | 80.85174 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0528 | 1.160245 | `-9.26%` | `53.08` / `48.44` | `38.15` | `0.308` | `BEARISH_SHOOTING_STAR` | 1.02035888 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.37e-06 | 5e-06 | `+6.06%` | `54.25` / `57.73` | `55.02` | `0.632` | `BEARISH_SHOOTING_STAR` | 5.12e-06 | `WATCH` | HOLD |
| `NEARUSDT` | 3.661 | 3.769971 | `-2.89%` | `70.63` / `68.22` | `55.02` | `0.728` | `BEARISH_SHOOTING_STAR` | 3.492594 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0014 | 1.001208 | `+0.02%` | `88.89` / `85.18` | `63.66` | `0.99` | `BEARISH_SHOOTING_STAR` | 0.9753636 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 681.1 | 693.422309 | `-1.78%` | `55.83` / `54.13` | `47.12` | `0.499` | `BEARISH_ENGULFING` | 663.3914 | `WATCH` | HOLD |
| `HYPEUSDT` | 71.83 | 78.126694 | `-8.06%` | `36.89` / `37.51` | `38.56` | `0.337` | `BULLISH_ENGULFING` | 69.406224 | `WATCH` | HOLD |
