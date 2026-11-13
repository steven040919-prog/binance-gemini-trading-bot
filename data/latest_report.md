# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T15:37:20Z`
- **Ciclo de ejecucion:** `#341`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen netamente bajista en temporalidad de 1H con todos los activos cotizando por debajo de la EMA 200 y con pendientes negativas. No se cumplen las condiciones de los Pilares LONG (P1-P4) ya que no hay retrocesos de valor sobre soportes clave con confirmación alcista y los osciladores estocásticos no muestran giros al alza desde sobreventa profunda con las velas de confirmación requeridas. Tampoco se activa el Pilar SHORT (S1) ya que los precios actuales están muy distanciados de la resistencia de la EMA 200 (-3% a -24%) y no testeando el nivel requerido. No hay posiciones abiertas reportadas, por lo que el bot se mantiene en modo WATCH sin ejecutar nuevas órdenes para preservar capital en este contexto de baja volatilidad bajista.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68242.23 | 74013.963774 | `-7.80%` | `36.56` / `41.81` | `29.08` | `0.184` | `BEARISH_ENGULFING` | 66467.93202 | `WATCH` | **HOLD** (75%) |
| `ETHUSDT` | 1915.24 | 2113.137826 | `-9.37%` | `39.77` / `47.9` | `30.06` | `0.16` | `BEARISH_ENGULFING` | 1856.074992 | `WATCH` | HOLD |
| `SOLUSDT` | 79.05 | 85.682921 | `-7.74%` | `56.95` / `67.72` | `37.05` | `0.191` | `NONE` | 76.67593 | `WATCH` | HOLD |
| `BNBUSDT` | 629.23 | 678.101338 | `-7.21%` | `42.62` / `48.9` | `32.48` | `0.192` | `BEARISH_ENGULFING` | 612.87002 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.115 | 1.137081 | `-1.94%` | `21.54` / `39.28` | `34.58` | `-0.227` | `NONE` | 1.073198 | `WATCH` | HOLD |
| `UNIUSDT` | 5.739 | 6.601821 | `-13.07%` | `51.14` / `51.86` | `37.0` | `0.229` | `NONE` | 5.4809274 | `WATCH` | HOLD |
| `ENAUSDT` | 0.134 | 0.152311 | `-12.02%` | `56.97` / `67.68` | `36.45` | `0.087` | `NONE` | 0.1279164 | `WATCH` | HOLD |
| `INITUSDT` | 0.11381 | 0.150749 | `-24.50%` | `20.64` / `26.92` | `40.52` | `0.223` | `BEARISH_SHOOTING_STAR` | 0.10857474 | `WATCH` | HOLD |
| `XAUTUSDT` | 3867.58 | 3993.460542 | `-3.15%` | `21.3` / `21.3` | `35.55` | `0.105` | `BULLISH_ENGULFING` | 3767.02292 | `WATCH` | HOLD |
| `MUBUSDT` | 756.16 | 762.677029 | `-0.85%` | `7.57` / `16.95` | `31.16` | `-0.229` | `BEARISH_ENGULFING` | 730.090416 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INTCBUSDT` | 57.13 | 59.27352 | `-3.62%` | `10.9` / `22.36` | `26.5` | `-0.339` | `BEARISH_ENGULFING` | 55.161858 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 110.97 | 123.192751 | `-9.92%` | `60.13` / `60.15` | `40.04` | `0.276` | `NONE` | 107.141408 | `WATCH` | HOLD |
| `ONDOUSDT` | 0.3378 | 0.364233 | `-7.26%` | `60.32` / `65.11` | `38.35` | `0.225` | `NONE` | 0.32419872 | `WATCH` | HOLD |
| `PAXGUSDT` | 3867.48 | 3997.350405 | `-3.25%` | `18.53` / `17.17` | `34.42` | `0.086` | `BULLISH_ENGULFING` | 3766.92552 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 923.51 | 1095.158896 | `-15.67%` | `61.66` / `74.84` | `40.11` | `0.204` | `BEARISH_ENGULFING` | 881.02854 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0743 | 0.07784 | `-4.55%` | `17.57` / `19.75` | `33.01` | `-0.089` | `NONE` | 0.0708822 | `EXIT_SHORT_STOCH_20` | HOLD |
