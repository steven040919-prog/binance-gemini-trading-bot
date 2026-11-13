# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T16:34:43Z`
- **Ciclo de ejecucion:** `#347`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global en temporalidad 1H se encuentra bajo un régimen bajista generalizado, con la mayoría de los activos cotizando por debajo de sus respectivas EMA 200 y con pendientes negativas. No se configuran entradas institucionales óptimas para los pilares LONG (P1-P4) debido a que no confluyen los giros en el estocástico ni las divergencias requeridas. Sin embargo, destaca el activo SOXSBUSDT, que presenta un patrón de velas bajista (BEARISH_SHOOTING_STAR) en zona de sobrecompra extrema (Estocástico > 80 y BB %B > 1.0), habilitando una oportunidad de venta en corto mediante el pilar S1 SHORT en Futuros USDT-M. Para el resto del portafolio sin posiciones abiertas o sin señales válidas, la decisión es HOLD o WATCH.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68690.03 | 73971.794282 | `-7.14%` | `39.73` / `42.14` | `31.82` | `0.288` | `BULLISH_HAMMER` | 66523.12931 | `WATCH` | HOLD |
| `ETHUSDT` | 1930.06 | 2112.252104 | `-8.63%` | `38.03` / `44.86` | `33.05` | `0.27` | `BULLISH_HAMMER` | 1858.730344 | `WATCH` | HOLD |
| `BNBUSDT` | 631.7 | 678.005644 | `-6.83%` | `39.48` / `46.47` | `34.01` | `0.265` | `NONE` | 613.40286 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.133 | 1.137902 | `-0.43%` | `31.31` / `34.36` | `40.73` | `0.201` | `BULLISH_HAMMER` | 1.080882 | `WATCH` | HOLD |
| `MUBUSDT` | 761.98 | 763.36847 | `-0.18%` | `11.18` / `11.74` | `33.13` | `-0.049` | `BULLISH_HAMMER` | 726.92892 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INTCBUSDT` | 58.27 | 59.292614 | `-1.72%` | `14.48` / `16.29` | `33.27` | `-0.04` | `NONE` | 55.58958 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INITUSDT` | 0.11336 | 0.150396 | `-24.63%` | `20.25` / `24.02` | `40.2` | `0.168` | `BULLISH_ENGULFING` | 0.10814544 | `WATCH` | HOLD |
| `BARDUSDT` | 0.1512 | 0.108427 | `+39.45%` | `68.61` / `72.83` | `58.76` | `0.625` | `NONE` | 0.1442448 | `WATCH` | HOLD |
| `SOLUSDT` | 79.56 | 85.687354 | `-7.15%` | `49.85` / `62.13` | `39.61` | `0.312` | `NONE` | 76.69232 | `WATCH` | HOLD |
| `SOXSBUSDT` | 52.92 | 55.612332 | `-4.84%` | `89.18` / `86.61` | `69.36` | `1.071` | `BEARISH_SHOOTING_STAR` | 50.48568 | `EXIT_LONG_STOCH_80` | **SHORT** (85%) |
| `ZECUSDT` | 944.44 | 1095.239403 | `-13.77%` | `62.42` / `70.0` | `45.94` | `0.477` | `BULLISH_HAMMER` | 900.99576 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0756 | 0.07788 | `-2.93%` | `14.54` / `19.29` | `35.25` | `0.075` | `NONE` | 0.0721224 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0122 | 1.10582 | `-8.47%` | `53.9` / `63.45` | `38.93` | `0.18` | `BEARISH_ENGULFING` | 0.98136816 | `WATCH` | HOLD |
| `NEARUSDT` | 3.505 | 3.631199 | `-3.48%` | `69.25` / `76.18` | `52.0` | `0.636` | `NONE` | 3.34377 | `WATCH` | HOLD |
| `UNIUSDT` | 5.792 | 6.60376 | `-12.29%` | `48.99` / `54.5` | `39.48` | `0.337` | `NONE` | 5.525568 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.46e-06 | 5e-06 | `-7.93%` | `28.02` / `36.91` | `41.39` | `0.024` | `BULLISH_HAMMER` | 4.25e-06 | `WATCH` | HOLD |
