# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T07:14:10Z`
- **Ciclo de ejecucion:** `#208`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general opera predominantemente bajo la EMA 200 en un régimen bajista, activando principalmente señales de salida o vacantes para cortos. Sin embargo, destaca INTCBUSDT bajo el Pilar 1 LONG cumpliendo con la confluencia de pullback sobre la EMA 200 alcista, estocástico girando al alza y patrón de vela BULLISH_ENGULFING, justificando una entrada en compra.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.47e-06 | 5e-06 | `-10.48%` | `8.76` / `10.42` | `23.58` | `0.168` | `NONE` | 4.26e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73504.5 | 75418.648713 | `-2.54%` | `7.19` / `13.51` | `40.49` | `0.157` | `BEARISH_SHOOTING_STAR` | 71593.383 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2047.07 | 2163.734608 | `-5.39%` | `16.48` / `18.52` | `41.07` | `0.212` | `NONE` | 1993.84618 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 82.77 | 87.797848 | `-5.73%` | `17.19` / `20.67` | `39.02` | `0.152` | `BEARISH_SHOOTING_STAR` | 80.61798 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.127 | 6.874037 | `-10.87%` | `9.76` / `15.95` | `30.18` | `0.142` | `BEARISH_SHOOTING_STAR` | 5.919936 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0428 | 1.135696 | `-8.18%` | `11.71` / `10.74` | `37.93` | `0.148` | `BULLISH_HAMMER` | 1.0156872 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.521 | 3.743906 | `-5.95%` | `5.82` / `5.64` | `37.09` | `0.153` | `NONE` | 3.3880742 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.411 | 7.905289 | `-6.25%` | `7.06` / `11.07` | `30.84` | `0.143` | `NONE` | 7.1229548 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 673.51 | 691.212755 | `-2.56%` | `8.93` / `6.78` | `35.52` | `0.07` | `NONE` | 655.99874 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1425 | 0.158985 | `-10.37%` | `3.7` / `5.09` | `27.15` | `0.156` | `BEARISH_SHOOTING_STAR` | 0.137454 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 163.86 | 189.363245 | `-13.47%` | `6.97` / `9.88` | `26.71` | `0.162` | `NONE` | 156.475004 | `EXIT_SHORT_STOCH_20` | HOLD |
| `HYPEUSDT` | 71.16 | 76.827976 | `-7.38%` | `17.43` / `25.49` | `37.23` | `0.102` | `BEARISH_SHOOTING_STAR` | 69.308712 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1488 | 0.164009 | `-9.27%` | `2.85` / `4.78` | `27.83` | `0.143` | `NONE` | 0.14454432 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06692 | 0.070742 | `-5.40%` | `17.42` / `20.64` | `35.64` | `0.156` | `BEARISH_SHOOTING_STAR` | 0.06518008 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3954.6 | 4026.487557 | `-1.79%` | `11.79` / `15.91` | `26.12` | `0.098` | `NONE` | 3851.7804 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INTCBUSDT` | 60.77 | 59.214352 | `+2.63%` | `16.46` / `15.23` | `48.17` | `0.287` | `BULLISH_ENGULFING` | 58.424902 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
