# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-10T22:21:46Z`
- **Ciclo de ejecucion:** `#19`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general opera bajo un régimen bajista (Bearish) con la mayoría de los activos cotizando por debajo de la EMA 200 en la temporalidad de 1H. No se presentan activaciones válidas para los Pilares LONG (P1-P4) ni para el Pilar SHORT (S1) debido a que no se cumplen de forma simultánea todos los filtros de sobreventa/sobrecompra extrema, volumen institucional y patrones de velas requeridos. La cartera se mantiene sin posiciones abiertas (open_positions_count: 0), por lo que no hay ajustes de stop-loss dinámico requeridos en este ciclo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `UNIUSDT` | 6.735 | 7.023027 | `-4.10%` | `19.34` / `17.92` | `39.61` | `0.238` | `BULLISH_ENGULFING` | 6.42519 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1606 | 0.166477 | `-3.53%` | `28.82` / `24.99` | `37.48` | `0.312` | `BULLISH_ENGULFING` | 0.1532124 | `WATCH` | HOLD |
| `XAUTUSDT` | 4025.0 | 4035.685601 | `-0.26%` | `17.8` / `16.07` | `33.42` | `0.282` | `BULLISH_HAMMER` | 3920.35 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73820.01 | 75949.233852 | `-2.80%` | `49.98` / `43.77` | `45.03` | `0.384` | `BEARISH_SHOOTING_STAR` | 71900.68974 | `WATCH` | HOLD |
| `ZECUSDT` | 1056.54 | 1226.118487 | `-13.83%` | `29.96` / `26.34` | `34.84` | `0.248` | `BEARISH_SHOOTING_STAR` | 1007.93916 | `WATCH` | HOLD |
| `ETHUSDT` | 2055.48 | 2202.082002 | `-6.66%` | `44.67` / `40.47` | `39.38` | `0.33` | `BEARISH_SHOOTING_STAR` | 1982.557656 | `WATCH` | HOLD |
| `PAXGUSDT` | 4028.28 | 4041.910624 | `-0.34%` | `17.54` / `16.17` | `33.56` | `0.284` | `BULLISH_ENGULFING` | 3923.54472 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INITUSDT` | 0.25811 | 0.161922 | `+59.40%` | `59.72` / `70.01` | `54.96` | `0.562` | `NONE` | 0.24623694 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001904 | 0.001536 | `+23.97%` | `53.73` / `55.07` | `63.56` | `0.754` | `BULLISH_ENGULFING` | 0.00181642 | `WATCH` | HOLD |
| `SOLUSDT` | 83.32 | 89.534101 | `-6.94%` | `40.98` / `37.15` | `37.55` | `0.319` | `BEARISH_SHOOTING_STAR` | 80.36704 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0629 | 1.166946 | `-8.92%` | `45.49` / `44.95` | `41.23` | `0.334` | `BEARISH_SHOOTING_STAR` | 1.02676332 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.153 | 1.103515 | `+4.48%` | `84.39` / `78.71` | `73.64` | `1.132` | `MORNING_STAR` | 1.099962 | `EXIT_LONG_STOCH_80` | HOLD |
| `PEPEUSDT` | 5.28e-06 | 5e-06 | `+4.85%` | `30.07` / `30.94` | `51.87` | `0.453` | `BULLISH_ENGULFING` | 5.04e-06 | `WATCH` | HOLD |
| `NEARUSDT` | 3.593 | 3.776216 | `-4.85%` | `37.53` / `36.28` | `49.5` | `0.452` | `BULLISH_ENGULFING` | 3.427722 | `WATCH` | HOLD |
| `BNBUSDT` | 678.6 | 694.311506 | `-2.26%` | `35.33` / `30.16` | `41.83` | `0.31` | `NONE` | 660.9564 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0011 | 1.001213 | `-0.01%` | `53.17` / `46.1` | `50.68` | `0.483` | `BEARISH_SHOOTING_STAR` | 0.9750714 | `WATCH` | HOLD |
