# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T02:54:46Z`
- **Ciclo de ejecucion:** `#179`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `-100.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general muestra una fuerte tendencia bajista macro por debajo de la EMA 200 en H1 con correcciones generalizadas. Se han identificado oportunidades de compra por capitulacion extrema (Pilar P2) en UNIUSDT y ARBUSDT con confluencia de envolventes alcistas y divergencias RSI, asi como configuraciones vendedoras intradia (M15 Scalper Short) en activos como BTCUSDT y XRPUSDT.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.62e-06 | 5e-06 | `-8.09%` | `14.81` / `9.5` | `28.42` | `0.201` | `BULLISH_HAMMER` | 4.41e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (60%) |
| `UNIUSDT` | 6.228 | 6.912271 | `-9.90%` | `13.09` / `9.58` | `33.41` | `0.116` | `BULLISH_ENGULFING` | 5.941512 | `P2_EXTREME_CAPITULATION` | **BUY** (85%) |
| `NEARUSDT` | 3.571 | 3.753336 | `-4.86%` | `23.04` / `23.24` | `40.52` | `0.132` | `NONE` | 3.4267304 | `WATCH` | **HOLD** (50%) |
| `XRPUSDT` | 1.0515 | 1.140803 | `-7.83%` | `29.73` / `29.52` | `42.53` | `0.146` | `BEARISH_ENGULFING` | 1.0848639 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (78%) |
| `INJUSDT` | 7.497 | 7.930115 | `-5.46%` | `12.59` / `11.78` | `29.44` | `0.063` | `BEARISH_ENGULFING` | 7.152138 | `EXIT_SHORT_STOCH_20` | **HOLD** (55%) |
| `ARBUSDT` | 0.152 | 0.164799 | `-7.77%` | `9.56` / `8.34` | `32.28` | `0.095` | `BULLISH_ENGULFING` | 0.145008 | `P2_EXTREME_CAPITULATION` | **BUY** (82%) |
| `ENAUSDT` | 0.145 | 0.159968 | `-9.36%` | `19.35` / `19.33` | `31.7` | `0.056` | `BEARISH_ENGULFING` | 0.13869 | `EXIT_SHORT_STOCH_20` | **HOLD** (55%) |
| `QNTUSDT` | 165.76 | 190.788973 | `-13.12%` | `7.94` / `10.43` | `26.95` | `-0.013` | `BULLISH_HAMMER` | 158.13504 | `EXIT_SHORT_STOCH_20` | **HOLD** (60%) |
| `LINKUSDT` | 10.178 | 10.743355 | `-5.26%` | `26.05` / `26.01` | `38.05` | `0.125` | `BEARISH_ENGULFING` | 10.5307704 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (75%) |
| `AAVEUSDT` | 118.93 | 128.577703 | `-7.50%` | `12.04` / `15.9` | `31.21` | `0.003` | `NONE` | 114.506174 | `EXIT_SHORT_STOCH_20` | **HOLD** (55%) |
| `XAUTUSDT` | 3975.95 | 4029.796754 | `-1.34%` | `24.13` / `18.55` | `31.11` | `0.24` | `BULLISH_HAMMER` | 3872.5753 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
| `LTCUSDT` | 50.01 | 52.19914 | `-4.19%` | `27.43` / `28.88` | `36.45` | `0.049` | `BEARISH_ENGULFING` | 48.689784 | `WATCH` | **HOLD** (50%) |
| `BTCUSDT` | 73846.0 | 75518.985593 | `-2.22%` | `34.74` / `39.15` | `46.37` | `0.317` | `BEARISH_ENGULFING` | 75765.996 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (76%) |
| `TAOUSDT` | 215.7 | 223.277973 | `-3.39%` | `27.34` / `25.16` | `37.92` | `0.104` | `NONE` | 209.53296 | `WATCH` | **HOLD** (50%) |
| `ADAUSDT` | 0.1741 | 0.181379 | `-4.01%` | `24.18` / `25.22` | `40.61` | `0.16` | `BEARISH_ENGULFING` | 0.1801266 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (74%) |
| `PAXGUSDT` | 3977.54 | 4035.400267 | `-1.43%` | `22.98` / `17.75` | `30.21` | `0.237` | `BULLISH_HAMMER` | 3874.12396 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
