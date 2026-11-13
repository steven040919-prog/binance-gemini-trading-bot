# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T09:25:44Z`
- **Ciclo de ejecucion:** `#302`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general muestra un régimen predominantemente bajista, con la mayoría de activos cotizando por debajo de sus respectivas EMA 200 y alineados en estructuras de continuación bajista en H1. No hay posiciones abiertas para ajuste dinámico de Stop-Loss. Se identifican dos oportunidades de entrada SHORT bajo el Pilar M15 Scalper Pullback Short en UNIUSDT y AAVEUSDT.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68865.93 | 74398.556081 | `-7.44%` | `27.16` / `25.94` | `27.88` | `0.203` | `NONE` | 67075.41582 | `WATCH` | **HOLD** (50%) |
| `ETHUSDT` | 1937.62 | 2126.448653 | `-8.88%` | `30.23` / `28.46` | `29.95` | `0.209` | `BULLISH_ENGULFING` | 1882.242168 | `WATCH` | **HOLD** (50%) |
| `BNBUSDT` | 634.82 | 681.228253 | `-6.81%` | `26.49` / `24.27` | `32.69` | `0.24` | `BULLISH_HAMMER` | 613.677888 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0811 | 0.078159 | `+3.76%` | `40.43` / `36.28` | `41.68` | `0.329` | `BEARISH_ENGULFING` | 0.0773694 | `WATCH` | HOLD |
| `UNIUSDT` | 5.774 | 6.668897 | `-13.42%` | `34.77` / `34.09` | `33.11` | `0.2` | `NONE` | 6.039604 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (82%) |
| `GRAMUSDT` | 1.141 | 1.137939 | `+0.27%` | `39.4` / `31.06` | `40.8` | `0.357` | `NONE` | 1.1031726 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001477 | 0.001546 | `-4.45%` | `16.53` / `18.97` | `39.84` | `0.209` | `NONE` | 0.00140906 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 110.81 | 124.219886 | `-10.80%` | `31.37` / `32.08` | `32.6` | `0.176` | `NONE` | 115.415384 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (80%) |
| `TRXUSDT` | 0.3111 | 0.317645 | `-2.06%` | `5.49` / `6.8` | `20.19` | `0.15` | `BULLISH_ENGULFING` | 0.3030114 | `EXIT_SHORT_STOCH_20` | HOLD |
| `HBARUSDT` | 0.06202 | 0.066539 | `-6.79%` | `43.79` / `40.39` | `35.62` | `0.271` | `BEARISH_SHOOTING_STAR` | 0.06039988 | `WATCH` | HOLD |
| `TIAUSDT` | 0.4166 | 0.429361 | `-2.97%` | `38.47` / `38.67` | `47.16` | `0.365` | `BEARISH_ENGULFING` | 0.3974364 | `WATCH` | HOLD |
| `QNTUSDT` | 157.75 | 183.325768 | `-13.95%` | `29.04` / `30.79` | `34.27` | `0.167` | `BEARISH_SHOOTING_STAR` | 150.65875 | `WATCH` | HOLD |
| `ZECUSDT` | 943.44 | 1113.351368 | `-15.26%` | `70.28` / `67.83` | `46.64` | `0.471` | `BEARISH_SHOOTING_STAR` | 900.04176 | `WATCH` | HOLD |
| `SOLUSDT` | 79.7 | 86.213354 | `-7.55%` | `44.88` / `43.44` | `38.04` | `0.294` | `BEARISH_SHOOTING_STAR` | 77.6278 | `WATCH` | HOLD |
| `NBISBUSDT` | 125.3 | 138.585785 | `-9.59%` | `19.15` / `19.93` | `32.67` | `0.13` | `BEARISH_SHOOTING_STAR` | 120.97992 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DODOUSDT` | 0.02849 | 0.023509 | `+21.19%` | `41.99` / `33.22` | `64.88` | `0.75` | `BULLISH_ENGULFING` | 0.02717946 | `WATCH` | HOLD |
