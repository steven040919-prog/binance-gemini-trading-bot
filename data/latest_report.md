# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T03:33:20Z`
- **Ciclo de ejecucion:** `#183`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `-100.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general presenta una tendencia macro bajista predominante con la mayoria de los activos cotizando por debajo de la EMA 200 en H1. Se identifican capitulaciones extremas de doble sobreventa (Pilar 2) en QNTUSDT y ARBUSDT con confluencia de patrones alcistas, RSI bajo 30 y Estocastico girando al alza. Asimismo, activos como UNIUSDT e INJUSDT muestran retrocesos bajistas de intradia en M15. No hay posiciones abiertas actualmente para ejecucion de trailing stop dinamico.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.62e-06 | 5e-06 | `-8.04%` | `17.9` / `13.36` | `28.5` | `0.219` | `NONE` | 4.41e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
| `UNIUSDT` | 6.222 | 6.90717 | `-9.92%` | `15.54` / `11.98` | `33.37` | `0.146` | `BULLISH_ENGULFING` | 6.4787028 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (75%) |
| `ONEUSDT` | 0.001466 | 0.001549 | `-5.35%` | `9.1` / `7.85` | `33.42` | `0.183` | `BEARISH_SHOOTING_STAR` | 0.00139856 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
| `NEARUSDT` | 3.559 | 3.753982 | `-5.19%` | `15.91` / `21.17` | `39.48` | `0.124` | `BULLISH_HAMMER` | 3.4161642 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
| `XRPUSDT` | 1.0463 | 1.139828 | `-8.21%` | `19.51` / `26.44` | `39.16` | `0.018` | `BEARISH_SHOOTING_STAR` | 1.0190962 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
| `INJUSDT` | 7.498 | 7.929616 | `-5.44%` | `14.24` / `13.7` | `30.97` | `0.078` | `BULLISH_ENGULFING` | 7.8229288 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (74%) |
| `ARBUSDT` | 0.1507 | 0.164688 | `-8.49%` | `9.35` / `8.36` | `29.87` | `0.071` | `BULLISH_ENGULFING` | 0.14475704 | `P2_EXTREME_CAPITULATION` | **BUY** (82%) |
| `ENAUSDT` | 0.1439 | 0.159897 | `-10.00%` | `13.29` / `17.8` | `29.36` | `0.044` | `BEARISH_ENGULFING` | 0.13798936 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
| `BNBUSDT` | 679.09 | 692.034152 | `-1.87%` | `19.06` / `23.5` | `43.1` | `0.189` | `NONE` | 661.43366 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
| `QNTUSDT` | 166.01 | 190.558013 | `-12.88%` | `9.83` / `9.43` | `27.73` | `0.066` | `BULLISH_HAMMER` | 158.37354 | `P2_EXTREME_CAPITULATION` | **BUY** (85%) |
| `INTCBUSDT` | 60.85 | 59.168224 | `+2.84%` | `32.07` / `31.06` | `47.65` | `0.241` | `BEARISH_SHOOTING_STAR` | 58.54978 | `WATCH` | **HOLD** (50%) |
| `LINKUSDT` | 10.136 | 10.738487 | `-5.61%` | `20.4` / `23.93` | `34.99` | `0.098` | `BEARISH_SHOOTING_STAR` | 9.8133824 | `WATCH` | **HOLD** (50%) |
| `AAVEUSDT` | 119.41 | 128.458107 | `-7.04%` | `13.68` / `14.5` | `34.37` | `0.118` | `NONE` | 114.540402 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
| `XAUTUSDT` | 3976.39 | 4029.142129 | `-1.31%` | `19.47` / `20.5` | `32.19` | `0.267` | `NONE` | 3873.00386 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
| `SUIUSDT` | 0.8193 | 0.853737 | `-4.03%` | `23.45` / `25.3` | `39.74` | `0.141` | `NONE` | 0.7967368 | `WATCH` | **HOLD** (50%) |
| `OPGUSDT` | 0.133 | 0.126086 | `+5.48%` | `4.12` / `5.44` | `45.19` | `0.264` | `BEARISH_SHOOTING_STAR` | 0.126882 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
