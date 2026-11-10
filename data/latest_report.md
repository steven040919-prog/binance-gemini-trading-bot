# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-10T23:21:31Z`
- **Ciclo de ejecucion:** `#40`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen claramente bajista con la mayoría de los activos cotizando por debajo de sus respectivas EMA 200 y con pendientes negativas. No se activan entradas LONG (Pilares P1-P4) debido a que no confluyen las condiciones estrictas de sobreventa extrema, divergencias o soportes mayores con giro alcista. Tampoco se activan cortos institucionales bajo el Pilar S1 ya que ningún activo cumple con el testeo exacto de resistencia en la EMA 200 bajo sobrecompra estocástica con patrón bajista confirmado. La cartera se mantiene en HOLD a la espera de mejores configuraciones.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1045.45 | 1223.579251 | `-14.56%` | `26.01` / `26.43` | `34.26` | `0.235` | `BEARISH_ENGULFING` | 997.3593 | `WATCH` | HOLD |
| `UNIUSDT` | 6.664 | 7.014953 | `-5.00%` | `13.07` / `15.29` | `36.1` | `0.172` | `BEARISH_ENGULFING` | 6.357456 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 123.75 | 129.635564 | `-4.54%` | `53.5` / `48.74` | `35.48` | `0.306` | `BEARISH_SHOOTING_STAR` | 119.19525 | `WATCH` | HOLD |
| `QNTUSDT` | 181.25 | 194.462294 | `-6.79%` | `38.15` / `38.0` | `33.39` | `0.266` | `BULLISH_HAMMER` | 172.9125 | `WATCH` | HOLD |
| `XAUTUSDT` | 4026.3 | 4035.459887 | `-0.23%` | `22.6` / `18.83` | `34.32` | `0.312` | `BULLISH_HAMMER` | 3921.6162 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73748.01 | 75927.75837 | `-2.87%` | `48.57` / `46.76` | `44.4` | `0.373` | `BEARISH_ENGULFING` | 71830.56174 | `WATCH` | **HOLD** (50%) |
| `TRXUSDT` | 0.318 | 0.319095 | `-0.34%` | `16.67` / `15.19` | `45.52` | `0.294` | `BULLISH_HAMMER` | 0.309732 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2051.64 | 2200.500413 | `-6.76%` | `42.37` / `41.93` | `38.93` | `0.326` | `BULLISH_HAMMER` | 1986.965392 | `WATCH` | HOLD |
| `PAXGUSDT` | 4029.44 | 4041.763832 | `-0.30%` | `22.23` / `18.66` | `34.35` | `0.312` | `BULLISH_ENGULFING` | 3924.67456 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001856 | 0.001537 | `+20.73%` | `49.1` / `51.38` | `60.42` | `0.671` | `BULLISH_HAMMER` | 0.00177062 | `WATCH` | HOLD |
| `SOLUSDT` | 83.07 | 89.429448 | `-7.11%` | `38.6` / `37.88` | `36.72` | `0.302` | `BEARISH_ENGULFING` | 80.300654 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0549 | 1.165353 | `-9.48%` | `43.6` / `43.21` | `37.24` | `0.253` | `BEARISH_ENGULFING` | 1.0199079 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.31e-06 | 5e-06 | `+5.51%` | `35.29` / `31.81` | `53.6` | `0.527` | `MORNING_STAR` | 5.07e-06 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.145 | 1.104077 | `+3.71%` | `81.79` / `78.97` | `67.86` | `1.0` | `NONE` | 1.09233 | `EXIT_LONG_STOCH_80` | HOLD |
| `NEARUSDT` | 3.564 | 3.773201 | `-5.54%` | `33.9` / `34.24` | `46.95` | `0.328` | `BEARISH_ENGULFING` | 3.400056 | `WATCH` | HOLD |
| `BNBUSDT` | 677.71 | 693.962047 | `-2.34%` | `36.61` / `33.64` | `40.3` | `0.3` | `BEARISH_SHOOTING_STAR` | 660.08954 | `WATCH` | HOLD |
