# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T00:32:21Z`
- **Ciclo de ejecucion:** `#68`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un régimen general bajista (la mayoría de los activos cotizan por debajo de la EMA 200 con pendientes negativas moderadas). No se activan entradas LONG en los Pilares 1-4 debido a que las condiciones de sobreventa extrema con giro alcista y patrones de confirmación no coinciden plenamente de forma simultánea en los candidatos principales. Tampoco se activa el Pilar S1 (Short en resistencia EMA 200) de forma óptima ya que los precios o osciladores no cumplen estrictamente los umbrales requeridos de sobrecompra en resistencia. Las posiciones abiertas se mantienen en 0, conservando el capital disponible (14 USDT) para configuraciones de alta probabilidad.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1045.3 | 1221.904383 | `-14.45%` | `23.68` / `25.55` | `34.22` | `0.26` | `NONE` | 997.2162 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1606 | 0.166369 | `-3.47%` | `41.21` / `36.11` | `38.18` | `0.348` | `NONE` | 0.15357236 | `WATCH` | HOLD |
| `UNIUSDT` | 6.716 | 7.013384 | `-4.24%` | `12.63` / `13.54` | `40.76` | `0.275` | `BULLISH_HAMMER` | 6.407064 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 124.13 | 129.662141 | `-4.27%` | `53.94` / `52.02` | `38.89` | `0.393` | `BULLISH_ENGULFING` | 119.392318 | `WATCH` | HOLD |
| `XAUTUSDT` | 4029.34 | 4035.513343 | `-0.15%` | `30.94` / `24.53` | `36.7` | `0.351` | `BEARISH_SHOOTING_STAR` | 3924.57716 | `WATCH` | HOLD |
| `BTCUSDT` | 73694.95 | 75911.6995 | `-2.92%` | `47.27` / `48.19` | `43.83` | `0.367` | `BULLISH_HAMMER` | 71778.8813 | `WATCH` | **HOLD** (50%) |
| `ETHUSDT` | 2052.86 | 2199.267408 | `-6.66%` | `43.0` / `42.82` | `39.49` | `0.353` | `BULLISH_HAMMER` | 1989.39564 | `WATCH` | HOLD |
| `INITUSDT` | 0.25816 | 0.163823 | `+57.58%` | `54.78` / `59.31` | `54.27` | `0.517` | `BEARISH_ENGULFING` | 0.24628464 | `WATCH` | HOLD |
| `PAXGUSDT` | 4031.28 | 4041.718708 | `-0.26%` | `30.92` / `24.31` | `36.25` | `0.343` | `MORNING_STAR` | 3926.46672 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001878 | 0.00154 | `+21.93%` | `54.65` / `51.4` | `61.5` | `0.698` | `BULLISH_ENGULFING` | 0.00179161 | `WATCH` | HOLD |
| `SOLUSDT` | 83.45 | 89.389049 | `-6.64%` | `44.94` / `41.25` | `40.87` | `0.384` | `BULLISH_ENGULFING` | 80.40692 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0545 | 1.164504 | `-9.45%` | `43.77` / `43.69` | `37.0` | `0.269` | `BULLISH_HAMMER` | 1.0207631 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.41e-06 | 5e-06 | `+7.36%` | `49.67` / `40.3` | `58.91` | `0.831` | `NONE` | 5.16e-06 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.134 | 1.104484 | `+2.67%` | `72.35` / `77.11` | `63.56` | `0.834` | `BEARISH_SHOOTING_STAR` | 1.081836 | `WATCH` | HOLD |
| `BNBUSDT` | 680.6 | 693.983626 | `-1.93%` | `45.52` / `40.41` | `45.77` | `0.412` | `NONE` | 662.9044 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0012 | 1.001214 | `-0.00%` | `83.33` / `70.63` | `54.62` | `0.639` | `BULLISH_HAMMER` | 0.9751688 | `EXIT_LONG_STOCH_80` | HOLD |
