# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T11:31:50Z`
- **Ciclo de ejecucion:** `#315`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general muestra un régimen predominantemente bajista, con la mayoría de activos cotizando por debajo de su EMA 200 de 1H y pendientes negativas. Evaluación de activos: Ningún candidato cumple con la confluencia estricta de los Pilares alcistas (P1-P4) ni con los criterios del Pilar bajista S1 (resistencia en EMA 200 con sobrecompra Estocástica >= 80 y giro bajista). No existen posiciones abiertas en el portafolio, por lo que no aplica la gestión dinámica de SL/TP.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `NBISBUSDT` | 126.34 | 138.390133 | `-8.71%` | `21.07` / `18.93` | `36.29` | `0.31` | `BULLISH_ENGULFING` | 120.930336 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 69228.01 | 74272.550207 | `-6.79%` | `40.75` / `35.29` | `33.84` | `0.307` | `BEARISH_SHOOTING_STAR` | 67199.026188 | `WATCH` | **HOLD** (85%) |
| `GRAMUSDT` | 1.154 | 1.138641 | `+1.35%` | `58.17` / `51.23` | `46.09` | `0.491` | `BULLISH_ENGULFING` | 1.1053032 | `WATCH` | **HOLD** (80%) |
| `ETHUSDT` | 1955.51 | 2121.399824 | `-7.82%` | `42.58` / `36.74` | `38.68` | `0.355` | `BEARISH_SHOOTING_STAR` | 1884.045556 | `WATCH` | **HOLD** (85%) |
| `TIAUSDT` | 0.4178 | 0.428764 | `-2.56%` | `41.26` / `39.11` | `48.17` | `0.366` | `MORNING_STAR` | 0.3985812 | `WATCH` | HOLD |
| `SOLUSDT` | 80.46 | 86.030973 | `-6.48%` | `61.88` / `54.97` | `45.55` | `0.476` | `BEARISH_SHOOTING_STAR` | 77.771144 | `WATCH` | HOLD |
| `ZECUSDT` | 956.16 | 1107.871615 | `-13.69%` | `81.08` / `76.1` | `50.97` | `0.682` | `BEARISH_SHOOTING_STAR` | 912.17664 | `EXIT_LONG_STOCH_80` | **HOLD** (83%) |
| `ERAUSDT` | 0.0779 | 0.078022 | `-0.16%` | `9.19` / `19.32` | `37.61` | `0.146` | `NONE` | 0.0743166 | `EXIT_SHORT_STOCH_20` | **HOLD** (80%) |
| `BNBUSDT` | 639.4 | 680.331579 | `-6.02%` | `45.21` / `37.26` | `38.95` | `0.368` | `BEARISH_SHOOTING_STAR` | 617.27108 | `WATCH` | HOLD |
| `DODOUSDT` | 0.0292 | 0.02357 | `+23.89%` | `67.76` / `54.33` | `68.18` | `0.962` | `BEARISH_SHOOTING_STAR` | 0.0278568 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0187 | 1.109777 | `-8.21%` | `56.02` / `60.9` | `40.74` | `0.301` | `BEARISH_ENGULFING` | 0.9922138 | `WATCH` | HOLD |
| `UNIUSDT` | 5.802 | 6.648177 | `-12.73%` | `33.26` / `33.74` | `36.18` | `0.298` | `BEARISH_SHOOTING_STAR` | 5.549128 | `WATCH` | HOLD |
| `NEARUSDT` | 3.528 | 3.640617 | `-3.09%` | `80.94` / `80.71` | `57.31` | `0.878` | `MORNING_STAR` | 3.365712 | `EXIT_LONG_STOCH_80` | **HOLD** (82%) |
| `PEPEUSDT` | 4.49e-06 | 5e-06 | `-7.43%` | `29.63` / `38.43` | `44.34` | `0.455` | `BEARISH_SHOOTING_STAR` | 4.28e-06 | `WATCH` | HOLD |
| `DOGEUSDT` | 0.0651 | 0.069431 | `-6.24%` | `54.56` / `48.9` | `45.12` | `0.448` | `BEARISH_SHOOTING_STAR` | 0.06295062 | `WATCH` | HOLD |
| `XAUTUSDT` | 3877.84 | 3999.76696 | `-3.05%` | `28.12` / `34.81` | `35.86` | `0.312` | `BEARISH_ENGULFING` | 3777.01616 | `WATCH` | HOLD |
