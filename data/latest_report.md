# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T20:17:56Z`
- **Ciclo de ejecucion:** `#152`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general opera predominantemente bajo la EMA 200 en temporalidad de 1H con un régimen bajista. No se cumplen las condiciones estrictas para aperturas LONG (P1-P4) ni para el rechazo SHORT (S1) en este ciclo, dado que los candidatos no alinean de forma simultánea el pullback a la resistencia de la EMA 200 con sobrecompra en estocástico y patrones bajistas de confirmación. Las posiciones abiertas se mantienen en 0 y el portafolio preserva USDT libre en espera de mejores confluencias.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.82e-06 | 5e-06 | `-4.70%` | `4.27` / `4.88` | `27.75` | `0.161` | `NONE` | 4.6e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001505 | 0.001554 | `-3.18%` | `4.77` / `4.07` | `35.98` | `0.259` | `NONE` | 0.00143577 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74591.56 | 75592.036249 | `-1.32%` | `79.36` / `79.09` | `59.61` | `0.99` | `BULLISH_HAMMER` | 72652.17944 | `WATCH` | **HOLD** (50%) |
| `INJUSDT` | 7.931 | 7.952404 | `-0.27%` | `26.34` / `26.21` | `45.41` | `0.315` | `BEARISH_ENGULFING` | 7.5885184 | `WATCH` | HOLD |
| `XAUTUSDT` | 3979.17 | 4032.961531 | `-1.33%` | `2.5` / `1.9` | `21.2` | `0.079` | `BULLISH_HAMMER` | 3875.71158 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1586 | 0.165535 | `-4.19%` | `23.82` / `28.26` | `41.12` | `0.235` | `BULLISH_HAMMER` | 0.15338608 | `WATCH` | HOLD |
| `PAXGUSDT` | 3980.98 | 4038.509578 | `-1.42%` | `2.14` / `1.36` | `21.12` | `0.074` | `NONE` | 3877.47452 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2082.83 | 2177.157434 | `-4.33%` | `62.64` / `67.36` | `55.7` | `0.869` | `NONE` | 2028.67642 | `WATCH` | HOLD |
| `MUBUSDT` | 816.29 | 754.041677 | `+8.26%` | `88.93` / `92.36` | `73.72` | `0.813` | `BULLISH_HAMMER` | 790.574106 | `EXIT_LONG_STOCH_80` | HOLD |
| `ZECUSDT` | 1003.29 | 1180.868131 | `-15.04%` | `60.4` / `59.88` | `44.47` | `0.577` | `BULLISH_HAMMER` | 957.13866 | `WATCH` | HOLD |
| `SOXSBUSDT` | 44.71 | 59.641296 | `-25.04%` | `23.91` / `15.08` | `35.58` | `0.28` | `MORNING_STAR` | 42.65334 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SNXXBUSDT` | 4.53 | 4.183134 | `+8.29%` | `88.64` / `91.5` | `73.58` | `0.806` | `BULLISH_HAMMER` | 4.32162 | `M15_SCALPER_PULLBACK_LONG` | HOLD |
| `SOLUSDT` | 85.02 | 88.392734 | `-3.82%` | `74.91` / `78.2` | `57.75` | `0.829` | `BULLISH_HAMMER` | 82.80948 | `WATCH` | HOLD |
| `NEARUSDT` | 3.727 | 3.770238 | `-1.15%` | `63.49` / `68.62` | `54.59` | `0.625` | `BULLISH_HAMMER` | 3.555558 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.204 | 1.119363 | `+7.56%` | `64.26` / `66.72` | `58.09` | `0.645` | `BEARISH_ENGULFING` | 1.148616 | `WATCH` | HOLD |
| `XRPUSDT` | 1.062 | 1.146012 | `-7.33%` | `33.45` / `44.21` | `47.84` | `0.572` | `BULLISH_HAMMER` | 1.034388 | `WATCH` | HOLD |
