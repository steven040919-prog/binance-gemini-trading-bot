# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T19:25:11Z`
- **Ciclo de ejecucion:** `#254`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general opera bajo un régimen bajista claro con la gran mayoría de los activos cotizando por debajo de la EMA 200 y con un RSI generalizado en zonas de sobreventa o compresión. Evaluando la arquitectura de pilares, se identifican oportunidades de entrada SHORT en Binance Futuros USDT-M mediante el pilar de scalping M15 (M15_SCALPER_PULLBACK_SHORT) para activos como XAUTUSDT, AVAXUSDT y PAXGUSDT, donde confluyen tendencias macro bajistas en H1 con patrones de giro y retrocesos válidos en temporalidades menores. No se registran posiciones abiertas actuales, por lo que no se requieren ajustes dinámicos de SL/TP (ADJUST).

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71620.61 | 75098.498397 | `-4.63%` | `19.97` / `20.46` | `23.9` | `0.117` | `NONE` | 69758.47414 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PEPEUSDT` | 4.4e-06 | 5e-06 | `-10.66%` | `33.52` / `24.04` | `34.25` | `0.332` | `MORNING_STAR` | 4.2e-06 | `WATCH` | HOLD |
| `ZECUSDT` | 945.42 | 1136.414796 | `-16.81%` | `16.3` / `17.53` | `33.36` | `0.064` | `BULLISH_HAMMER` | 901.93068 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 81.64 | 87.093277 | `-6.26%` | `38.6` / `36.72` | `36.77` | `0.225` | `BULLISH_HAMMER` | 79.4772 | `WATCH` | HOLD |
| `NEARUSDT` | 3.416 | 3.698826 | `-7.65%` | `34.15` / `31.01` | `36.18` | `0.274` | `BULLISH_ENGULFING` | 3.2637376 | `WATCH` | HOLD |
| `UNIUSDT` | 6.03 | 6.778295 | `-11.04%` | `27.99` / `26.11` | `32.26` | `0.233` | `BULLISH_ENGULFING` | 5.796306 | `WATCH` | HOLD |
| `BNBUSDT` | 654.84 | 687.564887 | `-4.76%` | `19.79` / `20.01` | `24.4` | `0.192` | `BULLISH_HAMMER` | 637.81416 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0264 | 1.124161 | `-8.70%` | `31.02` / `29.21` | `34.18` | `0.155` | `NONE` | 1.055528 | `M15_SCALPER_PULLBACK_SHORT` | HOLD |
| `ENAUSDT` | 0.1394 | 0.156576 | `-10.97%` | `35.64` / `30.84` | `29.65` | `0.257` | `NONE` | 0.13311132 | `WATCH` | HOLD |
| `XAUTUSDT` | 3876.28 | 4013.687288 | `-3.42%` | `20.02` / `18.73` | `26.42` | `0.19` | `BULLISH_ENGULFING` | 3977.06328 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (76%) |
| `AAVEUSDT` | 113.29 | 126.238621 | `-10.26%` | `33.43` / `32.19` | `29.92` | `0.258` | `BEARISH_ENGULFING` | 110.077118 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.163 | 1.138223 | `+2.18%` | `23.03` / `43.49` | `41.07` | `0.129` | `BULLISH_HAMMER` | 1.109502 | `WATCH` | HOLD |
| `QNTUSDT` | 161.66 | 186.60729 | `-13.37%` | `23.2` / `22.32` | `30.21` | `0.088` | `BEARISH_ENGULFING` | 155.809528 | `WATCH` | HOLD |
| `INJUSDT` | 7.402 | 7.846118 | `-5.66%` | `31.73` / `28.71` | `39.88` | `0.323` | `BULLISH_ENGULFING` | 7.0853812 | `WATCH` | HOLD |
| `AVAXUSDT` | 8.341 | 8.443523 | `-1.21%` | `22.36` / `22.88` | `39.57` | `0.199` | `BULLISH_ENGULFING` | 8.600866 | `M15_SCALPER_PULLBACK_SHORT` | HOLD |
| `PAXGUSDT` | 3880.37 | 4018.424311 | `-3.44%` | `20.84` / `19.24` | `26.45` | `0.198` | `BULLISH_ENGULFING` | 3981.25962 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (75%) |
