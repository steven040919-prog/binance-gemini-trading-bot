# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-10T22:59:50Z`
- **Ciclo de ejecucion:** `#31`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de criptomonedas en temporalidad 1H se encuentra bajo un régimen BEARISH generalizado, con la mayoría de los activos cotizando por debajo de la EMA 200 y presiones bajistas acumuladas. No se cumplen los requisitos estrictos de los Pilares 1 al 4 Long debido a la tendencia macro y falta de confirmaciones de sobreventa extrema con giro alcista simultáneo. Tampoco se activa el Pilar S1 Short en los candidatos evaluados, ya que no presentan el rechazo exacto en la resistencia de la EMA 200 con sobrecompra en estocástico. Portfolio sin posiciones abiertas (open_positions_count = 0), por lo que no se requieren ajustes dinámicos de SL/TP (ADJUST). Se mantiene la disciplina de espera institucional (HOLD / WATCH).

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1038.8 | 1225.941969 | `-15.27%` | `27.09` / `25.38` | `32.19` | `0.177` | `BEARISH_ENGULFING` | 991.0152 | `WATCH` | HOLD |
| `UNIUSDT` | 6.654 | 7.022221 | `-5.24%` | `14.42` / `16.28` | `35.23` | `0.12` | `BULLISH_ENGULFING` | 6.360532 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1613 | 0.166484 | `-3.11%` | `30.5` / `25.55` | `39.55` | `0.346` | `BULLISH_ENGULFING` | 0.1538802 | `WATCH` | HOLD |
| `QNTUSDT` | 181.62 | 194.638592 | `-6.69%` | `39.31` / `37.02` | `34.1` | `0.264` | `NONE` | 173.544172 | `WATCH` | HOLD |
| `AAVEUSDT` | 124.11 | 129.721171 | `-4.33%` | `49.37` / `43.46` | `37.1` | `0.348` | `BULLISH_ENGULFING` | 118.984014 | `WATCH` | HOLD |
| `XAUTUSDT` | 4025.44 | 4035.68998 | `-0.25%` | `17.96` / `16.12` | `33.72` | `0.285` | `BULLISH_HAMMER` | 3920.77856 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73692.0 | 75947.96012 | `-2.97%` | `47.97` / `43.1` | `43.53` | `0.333` | `BEARISH_SHOOTING_STAR` | 71776.008 | `WATCH` | **HOLD** (75%) |
| `TRXUSDT` | 0.318 | 0.319204 | `-0.38%` | `15.56` / `14.07` | `45.52` | `0.297` | `BEARISH_SHOOTING_STAR` | 0.309732 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2048.47 | 2202.012251 | `-6.97%` | `42.6` / `39.78` | `37.56` | `0.284` | `BEARISH_SHOOTING_STAR` | 1981.523452 | `WATCH` | HOLD |
| `PAXGUSDT` | 4028.84 | 4041.916196 | `-0.32%` | `17.73` / `16.24` | `33.93` | `0.287` | `BULLISH_ENGULFING` | 3924.09016 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001871 | 0.001536 | `+21.85%` | `51.2` / `54.23` | `61.83` | `0.71` | `BULLISH_ENGULFING` | 0.00178493 | `WATCH` | HOLD |
| `SOLUSDT` | 82.92 | 89.530121 | `-7.38%` | `38.07` / `36.18` | `34.96` | `0.255` | `BEARISH_SHOOTING_STAR` | 80.311904 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0581 | 1.166898 | `-9.32%` | `42.81` / `44.06` | `38.67` | `0.272` | `BEARISH_SHOOTING_STAR` | 1.02478024 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.3e-06 | 5e-06 | `+5.24%` | `31.37` / `31.37` | `53.01` | `0.517` | `BULLISH_ENGULFING` | 5.06e-06 | `WATCH` | HOLD |
| `NEARUSDT` | 3.555 | 3.775838 | `-5.85%` | `33.22` / `34.84` | `45.97` | `0.271` | `BULLISH_ENGULFING` | 3.39147 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.138 | 1.103366 | `+3.14%` | `78.7` / `76.82` | `66.23` | `0.995` | `MORNING_STAR` | 1.085652 | `WATCH` | HOLD |
