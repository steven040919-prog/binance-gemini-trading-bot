# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T15:20:55Z`
- **Ciclo de ejecucion:** `#339`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general opera bajo un régimen bajista claro con la mayoría de los activos cotizando por debajo de sus respectivas EMA 200 y presiones vendedoras predominantes. Se identifica una oportunidad óptima para abrir cortos bajo el Pilar S1 en ZECUSDT debido al rechazo bajista en la resistencia de la EMA 200 con confirmación de osciladores y patrones de velas institucionales.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68779.25 | 74019.307257 | `-7.08%` | `41.83` / `43.56` | `32.57` | `0.289` | `BEARISH_ENGULFING` | 66990.9895 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.123 | 1.137161 | `-1.25%` | `25.31` / `40.54` | `36.65` | `-0.093` | `NONE` | 1.076941 | `WATCH` | HOLD |
| `MUBUSDT` | 761.12 | 762.726383 | `-0.21%` | `7.48` / `16.92` | `32.84` | `-0.177` | `BEARISH_ENGULFING` | 736.083056 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INTCBUSDT` | 57.47 | 59.276903 | `-3.05%` | `10.99` / `22.39` | `27.65` | `-0.307` | `BEARISH_ENGULFING` | 55.537972 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 1935.56 | 2113.340015 | `-8.41%` | `45.58` / `49.83` | `34.44` | `0.285` | `BEARISH_ENGULFING` | 1881.195656 | `WATCH` | HOLD |
| `ZECUSDT` | 941.78 | 1095.340687 | `-14.02%` | `67.08` / `76.64` | `45.19` | `0.438` | `BEARISH_ENGULFING` | 985.10188 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `SOLUSDT` | 79.87 | 85.69108 | `-6.79%` | `63.08` / `69.77` | `41.71` | `0.37` | `NONE` | 77.635588 | `WATCH` | HOLD |
| `DODOUSDT` | 0.02789 | 0.023787 | `+17.25%` | `50.75` / `62.11` | `55.21` | `0.484` | `NONE` | 0.02660706 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0751 | 0.077848 | `-3.53%` | `17.24` / `19.64` | `34.17` | `-0.032` | `NONE` | 0.0716454 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 634.16 | 678.150392 | `-6.49%` | `47.77` / `50.62` | `35.97` | `0.303` | `BEARISH_ENGULFING` | 617.67184 | `WATCH` | HOLD |
| `NEARUSDT` | 3.501 | 3.629227 | `-3.53%` | `75.22` / `82.43` | `51.63` | `0.638` | `NONE` | 3.339954 | `EXIT_LONG_STOCH_80` | HOLD |
| `XRPUSDT` | 1.0258 | 1.106322 | `-7.28%` | `72.18` / `66.68` | `46.97` | `0.487` | `BEARISH_ENGULFING` | 0.98923952 | `WATCH` | HOLD |
| `SOXSBUSDT` | 53.72 | 55.727851 | `-3.60%` | `90.58` / `79.83` | `72.67` | `1.284` | `NONE` | 51.24888 | `EXIT_LONG_STOCH_80` | HOLD |
| `PEPEUSDT` | 4.5e-06 | 5e-06 | `-7.07%` | `38.27` / `41.15` | `45.69` | `0.264` | `BEARISH_ENGULFING` | 4.29e-06 | `WATCH` | HOLD |
| `INJUSDT` | 8.116 | 7.782664 | `+4.28%` | `89.1` / `91.08` | `71.73` | `0.966` | `NONE` | 7.742664 | `EXIT_LONG_STOCH_80` | HOLD |
| `UNIUSDT` | 5.826 | 6.602687 | `-11.76%` | `58.0` / `54.15` | `41.56` | `0.386` | `NONE` | 5.5654644 | `WATCH` | HOLD |
