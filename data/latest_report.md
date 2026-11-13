# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T15:11:25Z`
- **Ciclo de ejecucion:** `#338`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se mantiene bajo un régimen bajista generalizado con la mayoría de los activos cotizando por debajo de la EMA 200. Se evalúan oportunidades bajo los pilares institucionales, destacando el Pilar S1 SHORT en ZECUSDT e HYPEUSDT por rechazo bajista en la resistencia de la EMA 200 con confirmación de velas y osciladores en zona de sobrecompra/giro. No hay posiciones abiertas actuales para ajuste dinámico.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68708.04 | 74018.5987 | `-7.17%` | `41.13` / `43.33` | `32.06` | `0.275` | `BEARISH_ENGULFING` | 66921.63096 | `WATCH` | HOLD |
| `ERAUSDT` | 0.076 | 0.077857 | `-2.38%` | `19.09` / `20.26` | `35.58` | `0.04` | `NONE` | 0.072504 | `EXIT_SHORT_STOCH_20` | HOLD |
| `GRAMUSDT` | 1.126 | 1.137191 | `-0.98%` | `27.16` / `41.15` | `37.49` | `-0.029` | `NONE` | 1.076842 | `WATCH` | HOLD |
| `ETHUSDT` | 1936.58 | 2113.350164 | `-8.36%` | `45.87` / `49.93` | `34.7` | `0.291` | `BEARISH_ENGULFING` | 1881.167708 | `WATCH` | HOLD |
| `MUBUSDT` | 762.47 | 762.739816 | `-0.04%` | `7.14` / `16.81` | `33.32` | `-0.161` | `BEARISH_ENGULFING` | 738.468418 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INTCBUSDT` | 58.08 | 59.282973 | `-2.03%` | `10.52` / `22.24` | `29.99` | `-0.236` | `BEARISH_ENGULFING` | 56.314368 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 948.2 | 1095.404567 | `-13.44%` | `68.98` / `77.28` | `47.3` | `0.524` | `BEARISH_ENGULFING` | 991.8172 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `SOLUSDT` | 80.0 | 85.692373 | `-6.64%` | `64.05` / `70.09` | `42.56` | `0.399` | `NONE` | 77.758 | `WATCH` | HOLD |
| `DODOUSDT` | 0.02789 | 0.023787 | `+17.25%` | `50.75` / `62.11` | `55.21` | `0.484` | `NONE` | 0.02660706 | `WATCH` | HOLD |
| `BNBUSDT` | 634.34 | 678.152183 | `-6.46%` | `47.96` / `50.68` | `36.11` | `0.308` | `BEARISH_ENGULFING` | 617.84716 | `WATCH` | HOLD |
| `NEARUSDT` | 3.518 | 3.629396 | `-3.07%` | `76.74` / `82.94` | `53.42` | `0.687` | `NONE` | 3.356172 | `EXIT_LONG_STOCH_80` | HOLD |
| `XRPUSDT` | 1.0289 | 1.106353 | `-7.00%` | `74.42` / `67.42` | `49.18` | `0.563` | `BEARISH_ENGULFING` | 0.9897775 | `WATCH` | HOLD |
| `INJUSDT` | 8.138 | 7.782883 | `+4.56%` | `89.74` / `91.29` | `73.12` | `0.981` | `NONE` | 7.763652 | `EXIT_LONG_STOCH_80` | HOLD |
| `PEPEUSDT` | 4.5e-06 | 5e-06 | `-7.07%` | `38.27` / `41.15` | `45.69` | `0.264` | `BEARISH_ENGULFING` | 4.29e-06 | `WATCH` | HOLD |
| `UNIUSDT` | 5.873 | 6.603155 | `-11.06%` | `61.7` / `55.38` | `44.52` | `0.474` | `NONE` | 5.602842 | `WATCH` | HOLD |
| `HYPEUSDT` | 73.37 | 75.186533 | `-2.42%` | `71.54` / `80.8` | `57.16` | `0.708` | `BEARISH_ENGULFING` | 76.74502 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (82%) |
