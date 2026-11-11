# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T00:40:45Z`
- **Ciclo de ejecucion:** `#72`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen predominantemente bajista con la mayoría de los activos cotizando por debajo de la EMA 200 de 1 hora. Tras evaluar los 16 activos candidatos, ninguno cumple cuantitativamente con los requisitos estrictos de entrada para los Pilares LONG (P1-P4) ni para el Pilar SHORT S1 (requiere testeo de EMA 200 con Estocástico >= 80, RSI >= 62 y vela bajista de giro). No hay posiciones abiertas actualmente para aplicar gestión dinámica de Trailing Stop o Break-Even. Se mantiene el 100% del capital en USDT a la espera de confirmación técnica.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1045.52 | 1221.906573 | `-14.44%` | `23.72` / `25.56` | `34.29` | `0.261` | `NONE` | 997.42608 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1607 | 0.16637 | `-3.41%` | `41.52` / `36.22` | `38.38` | `0.354` | `NONE` | 0.15353628 | `WATCH` | HOLD |
| `UNIUSDT` | 6.741 | 7.013633 | `-3.89%` | `14.15` / `14.04` | `42.79` | `0.31` | `BULLISH_HAMMER` | 6.430914 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 4026.45 | 4035.484587 | `-0.22%` | `29.5` / `24.05` | `35.59` | `0.331` | `NONE` | 3921.7623 | `WATCH` | HOLD |
| `BTCUSDT` | 73648.01 | 75911.232435 | `-2.98%` | `46.53` / `47.94` | `43.26` | `0.348` | `BEARISH_ENGULFING` | 71733.16174 | `WATCH` | **HOLD** (0%) |
| `ETHUSDT` | 2054.49 | 2199.283627 | `-6.58%` | `43.53` / `43.0` | `40.16` | `0.365` | `NONE` | 1988.942362 | `WATCH` | **HOLD** (0%) |
| `INITUSDT` | 0.27152 | 0.163956 | `+65.61%` | `57.95` / `60.37` | `58.17` | `0.599` | `BEARISH_ENGULFING` | 0.25903008 | `WATCH` | HOLD |
| `PAXGUSDT` | 4028.16 | 4041.687663 | `-0.33%` | `29.26` / `23.76` | `35.09` | `0.321` | `MORNING_STAR` | 3923.42784 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001829 | 0.00154 | `+18.78%` | `48.67` / `49.4` | `57.93` | `0.61` | `NONE` | 0.00174487 | `WATCH` | HOLD |
| `SOLUSDT` | 83.5 | 89.389547 | `-6.59%` | `45.36` / `41.39` | `41.4` | `0.393` | `BULLISH_ENGULFING` | 80.3889 | `WATCH` | **HOLD** (0%) |
| `XRPUSDT` | 1.0552 | 1.164511 | `-9.39%` | `44.2` / `43.84` | `37.33` | `0.278` | `BULLISH_HAMMER` | 1.02074336 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.42e-06 | 5e-06 | `+7.55%` | `50.33` / `40.52` | `59.4` | `0.86` | `NONE` | 5.17e-06 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.131 | 1.104455 | `+2.40%` | `71.21` / `76.73` | `62.21` | `0.801` | `BEARISH_SHOOTING_STAR` | 1.078974 | `WATCH` | HOLD |
| `BNBUSDT` | 680.7 | 693.984621 | `-1.91%` | `45.67` / `40.46` | `45.97` | `0.416` | `NONE` | 663.0018 | `WATCH` | **HOLD** (0%) |
| `RLUSDUSDT` | 1.0012 | 1.001214 | `-0.00%` | `83.33` / `70.63` | `54.62` | `0.639` | `BULLISH_HAMMER` | 0.9751688 | `EXIT_LONG_STOCH_80` | HOLD |
| `NEARUSDT` | 3.635 | 3.773835 | `-3.68%` | `41.16` / `36.93` | `53.77` | `0.671` | `MORNING_STAR` | 3.46779 | `WATCH` | **HOLD** (0%) |
