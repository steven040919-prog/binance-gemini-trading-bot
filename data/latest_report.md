# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T01:45:49Z`
- **Ciclo de ejecucion:** `#173`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado en 1H presenta un sesgo marcadamente bajista con la mayoria de los activos cotizando por debajo de la EMA 200 y con pendientes negativas. Ningun activo de la lista cumple con los requisitos estrictos de los Pilares LONG (P1-P4) ni del Pilar SHORT S1 (rechazo en la resistencia de EMA 200 con sobrecompra en Estocastico >= 80). No existen posiciones abiertas en el portafolio, por lo que se mantiene preservacion total del capital en USDT a la espera de retrocesos de valor o capitulaciones validadas.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.55e-06 | 5e-06 | `-9.51%` | `7.37` / `5.21` | `21.32` | `0.093` | `BULLISH_HAMMER` | 4.34e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (86%) |
| `ETHUSDT` | 2052.2 | 2171.403458 | `-5.49%` | `31.11` / `31.24` | `42.15` | `0.208` | `BULLISH_ENGULFING` | 1998.8428 | `WATCH` | **HOLD** (90%) |
| `UNIUSDT` | 6.161 | 6.920667 | `-10.98%` | `7.84` / `11.65` | `25.32` | `-0.091` | `BULLISH_HAMMER` | 5.9057396 | `EXIT_SHORT_STOCH_20` | **HOLD** (87%) |
| `NEARUSDT` | 3.594 | 3.755879 | `-4.31%` | `24.33` / `24.06` | `42.58` | `0.195` | `BULLISH_ENGULFING` | 3.428676 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0512 | 1.141715 | `-7.93%` | `32.33` / `28.53` | `41.63` | `0.091` | `BULLISH_ENGULFING` | 1.01745312 | `WATCH` | HOLD |
| `INJUSDT` | 7.451 | 7.938325 | `-6.14%` | `10.14` / `9.87` | `27.23` | `-0.035` | `BEARISH_ENGULFING` | 7.157764 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1515 | 0.164999 | `-8.18%` | `6.79` / `7.66` | `27.65` | `-0.023` | `BULLISH_HAMMER` | 0.1458217 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1452 | 0.160113 | `-9.31%` | `21.45` / `16.52` | `31.84` | `-0.003` | `BULLISH_ENGULFING` | 0.1385208 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 679.35 | 691.651928 | `-1.78%` | `27.48` / `31.5` | `42.65` | `0.208` | `BULLISH_ENGULFING` | 661.6869 | `WATCH` | HOLD |
| `QNTUSDT` | 166.52 | 190.988343 | `-12.81%` | `11.56` / `12.93` | `26.77` | `-0.096` | `BULLISH_HAMMER` | 158.86008 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LINKUSDT` | 10.154 | 10.748701 | `-5.53%` | `28.73` / `25.52` | `34.32` | `0.021` | `BULLISH_ENGULFING` | 9.755996 | `WATCH` | HOLD |
| `SUIUSDT` | 0.8206 | 0.8541 | `-3.92%` | `27.64` / `25.06` | `39.6` | `0.146` | `BEARISH_ENGULFING` | 0.79006972 | `WATCH` | HOLD |
| `AAVEUSDT` | 118.64 | 128.73451 | `-7.84%` | `17.4` / `16.35` | `27.66` | `-0.154` | `NONE` | 115.102992 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3983.18 | 4030.244196 | `-1.17%` | `20.01` / `12.48` | `33.84` | `0.279` | `BULLISH_ENGULFING` | 3879.61732 | `EXIT_SHORT_STOCH_20` | **HOLD** (88%) |
| `OPGUSDT` | 0.1334 | 0.125933 | `+5.93%` | `7.11` / `9.55` | `45.59` | `0.308` | `BEARISH_SHOOTING_STAR` | 0.1272636 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `LTCUSDT` | 50.07 | 52.222833 | `-4.12%` | `33.19` / `27.47` | `35.97` | `0.004` | `BEARISH_ENGULFING` | 48.438558 | `WATCH` | HOLD |
