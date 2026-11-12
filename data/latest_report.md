# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T21:34:09Z`
- **Ciclo de ejecucion:** `#268`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen netamente bajista con múltiples activos cotizando por debajo de sus EMA 200 y RSI de 1H deprimidos en zona de sobreventa. No se cumplen los requisitos estrictos de los Pilares LONG (P1-P4) ni el Pilar SHORT S1 al no haber cruces exactos de resistencia/soporte con giros estocásticos o patrones de velas válidos bajo la metodología institucional en los candidatos evaluados. El portafolio actual se mantiene sin posiciones abiertas activas (open_positions_count = 0), por lo que no se requieren ajustes dinámicos de SL/TP (action = HOLD). Se mantiene la disciplina de riesgo esperando mejores configuraciones técnicas.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71564.61 | 75051.522896 | `-4.65%` | `12.57` / `16.17` | `25.88` | `0.18` | `NONE` | 69703.93014 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `SOLUSDT` | 81.6 | 87.047975 | `-6.26%` | `34.87` / `36.11` | `38.42` | `0.271` | `BEARISH_ENGULFING` | 79.46536 | `WATCH` | HOLD |
| `NBISBUSDT` | 130.46 | 140.746524 | `-7.31%` | `22.26` / `21.31` | `36.25` | `0.283` | `BULLISH_ENGULFING` | 124.45884 | `WATCH` | HOLD |
| `UNIUSDT` | 6.052 | 6.767277 | `-10.57%` | `38.89` / `34.15` | `35.42` | `0.335` | `NONE` | 5.8327544 | `WATCH` | HOLD |
| `BNBUSDT` | 656.84 | 687.035231 | `-4.40%` | `22.7` / `21.09` | `32.14` | `0.29` | `BULLISH_ENGULFING` | 639.76216 | `WATCH` | HOLD |
| `XAUTUSDT` | 3871.69 | 4010.494014 | `-3.46%` | `21.07` / `21.54` | `26.12` | `0.218` | `BEARISH_ENGULFING` | 3771.02606 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.148 | 1.138131 | `+0.87%` | `11.81` / `12.66` | `39.26` | `0.13` | `BULLISH_HAMMER` | 1.095192 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 162.6 | 186.136313 | `-12.64%` | `27.66` / `25.92` | `35.15` | `0.284` | `BULLISH_ENGULFING` | 155.93736 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0829 | 0.077704 | `+6.69%` | `7.32` / `8.49` | `40.32` | `0.094` | `NONE` | 0.0790866 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PAXGUSDT` | 3874.35 | 4015.169072 | `-3.51%` | `21.67` / `22.34` | `26.02` | `0.217` | `BEARISH_ENGULFING` | 3773.6169 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3157 | 0.317849 | `-0.68%` | `18.1` / `22.28` | `34.48` | `0.201` | `BEARISH_SHOOTING_STAR` | 0.3074918 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOXSBUSDT` | 45.15 | 56.704639 | `-20.38%` | `28.66` / `30.12` | `40.22` | `0.161` | `BEARISH_SHOOTING_STAR` | 43.0731 | `WATCH` | HOLD |
| `ETHUSDT` | 2021.24 | 2147.677653 | `-5.89%` | `49.81` / `48.01` | `40.07` | `0.366` | `BEARISH_SHOOTING_STAR` | 1968.68776 | `WATCH` | HOLD |
| `INITUSDT` | 0.11159 | 0.16141 | `-30.87%` | `14.04` / `13.36` | `33.18` | `0.15` | `BEARISH_ENGULFING` | 0.10645686 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 956.9 | 1135.054616 | `-15.70%` | `36.04` / `28.98` | `40.53` | `0.273` | `BULLISH_ENGULFING` | 912.8826 | `WATCH` | HOLD |
| `NEARUSDT` | 3.448 | 3.6955 | `-6.70%` | `49.7` / `43.1` | `41.6` | `0.429` | `MORNING_STAR` | 3.289392 | `WATCH` | HOLD |
