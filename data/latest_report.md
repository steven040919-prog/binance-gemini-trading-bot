# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T07:57:25Z`
- **Ciclo de ejecucion:** `#118`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global de criptomonedas en la temporalidad de 1H se mantiene mayoritariamente bajo la EMA 200 con sesgo bajista (régimen BEARISH). Los candidatos evaluados no cumplen estrictamente con los gatillos de entrada de los Pilares Long (P1-P4) debido a que la mayoría de los activos carecen de la confluencia de capitulación o pullback óptimo sobre soportes clave, y no hay posiciones abiertas actuales para activar gestiones de trailing stop (ADJUST). Se emiten órdenes HOLD para conservar el capital y esperar configuraciones de alta probabilidad según los parámetros institucionales.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 997.28 | 1209.431339 | `-17.54%` | `19.73` / `16.52` | `31.58` | `0.25` | `BEARISH_ENGULFING` | 951.40512 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `UNIUSDT` | 6.466 | 6.990242 | `-7.50%` | `14.93` / `14.31` | `28.91` | `0.06` | `BEARISH_ENGULFING` | 6.168564 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `ARBUSDT` | 0.1588 | 0.166154 | `-4.43%` | `31.47` / `45.26` | `37.53` | `0.252` | `BULLISH_HAMMER` | 0.15190552 | `WATCH` | **HOLD** (70%) |
| `INITUSDT` | 0.22434 | 0.170854 | `+31.31%` | `21.11` / `44.67` | `45.18` | `0.103` | `BULLISH_HAMMER` | 0.21402036 | `WATCH` | HOLD |
| `QNTUSDT` | 179.41 | 193.879464 | `-7.46%` | `39.51` / `43.13` | `34.26` | `0.227` | `BULLISH_HAMMER` | 172.788278 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001627 | 0.001555 | `+4.61%` | `18.74` / `22.95` | `42.09` | `-0.086` | `BEARISH_ENGULFING` | 0.00155216 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74104.01 | 75786.378546 | `-2.22%` | `85.14` / `71.8` | `52.25` | `0.79` | `BEARISH_ENGULFING` | 72177.30574 | `EXIT_LONG_STOCH_80` | **HOLD** (80%) |
| `TRXUSDT` | 0.3177 | 0.318549 | `-0.27%` | `26.86` / `20.42` | `43.79` | `0.332` | `BEARISH_SHOOTING_STAR` | 0.3094398 | `WATCH` | HOLD |
| `CYBERUSDT` | 0.269 | 0.282534 | `-4.79%` | `4.42` / `4.01` | `44.56` | `0.23` | `NONE` | 0.256626 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2069.25 | 2190.728582 | `-5.55%` | `85.78` / `78.9` | `48.6` | `0.686` | `BEARISH_ENGULFING` | 2015.4495 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 83.26 | 88.973331 | `-6.42%` | `56.03` / `53.81` | `44.36` | `0.522` | `BEARISH_ENGULFING` | 80.724712 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0595 | 1.157376 | `-8.46%` | `51.11` / `55.11` | `44.4` | `0.524` | `NONE` | 1.0298862 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0855 | 0.073125 | `+16.92%` | `75.81` / `79.31` | `61.0` | `0.808` | `MORNING_STAR` | 0.081567 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.27e-06 | 5e-06 | `+3.91%` | `32.47` / `40.92` | `48.07` | `0.339` | `NONE` | 5.03e-06 | `WATCH` | HOLD |
| `NEARUSDT` | 3.626 | 3.774953 | `-3.95%` | `59.55` / `65.25` | `50.77` | `0.556` | `BULLISH_HAMMER` | 3.459204 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0012 | 1.001212 | `-0.00%` | `62.86` / `68.31` | `53.98` | `0.686` | `BULLISH_HAMMER` | 0.9751688 | `WATCH` | HOLD |
