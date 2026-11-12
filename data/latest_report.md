# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T07:52:39Z`
- **Ciclo de ejecucion:** `#212`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen netamente bajista con la mayoría de los activos cotizando por debajo de la EMA 200 y con pendientes negativas. No se activan entradas LONG (P1-P4) debido a que los filtros de tendencia macro y patrones de giro no coinciden plenamente. Tampoco se activan entradas SHORT bajo el Pilar S1 (ya que el precio está muy distanciado de la EMA 200 hacia la baja). No hay posiciones abiertas actualmente, por lo que no se requieren ajustes dinámicos de SL/TP.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.45e-06 | 5e-06 | `-10.88%` | `7.5` / `10.0` | `21.08` | `0.146` | `BEARISH_SHOOTING_STAR` | 4.25e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73623.39 | 75419.831698 | `-2.38%` | `10.05` / `14.46` | `43.26` | `0.232` | `BULLISH_ENGULFING` | 71709.18186 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
| `ETHUSDT` | 2050.46 | 2163.768339 | `-5.24%` | `18.45` / `19.17` | `43.3` | `0.268` | `BULLISH_ENGULFING` | 1997.14804 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 82.96 | 87.799739 | `-5.51%` | `19.15` / `21.32` | `41.48` | `0.201` | `BULLISH_ENGULFING` | 80.80304 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.507 | 3.743767 | `-6.32%` | `4.03` / `5.04` | `34.81` | `0.122` | `BEARISH_SHOOTING_STAR` | 3.3870886 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.153 | 6.874296 | `-10.49%` | `11.38` / `16.49` | `32.16` | `0.175` | `NONE` | 5.919104 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0445 | 1.135713 | `-8.03%` | `13.42` / `11.31` | `39.74` | `0.187` | `BULLISH_HAMMER` | 1.017343 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.401 | 7.90519 | `-6.38%` | `6.52` / `10.89` | `30.5` | `0.133` | `NONE` | 7.1188462 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1423 | 0.158983 | `-10.49%` | `3.12` / `4.9` | `25.99` | `0.146` | `BEARISH_SHOOTING_STAR` | 0.13740332 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 673.95 | 691.217133 | `-2.50%` | `9.75` / `7.06` | `36.64` | `0.09` | `NONE` | 656.4273 | `EXIT_SHORT_STOCH_20` | HOLD |
| `HYPEUSDT` | 71.36 | 76.829966 | `-7.12%` | `19.36` / `26.13` | `39.71` | `0.151` | `NONE` | 69.29008 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06702 | 0.070743 | `-5.26%` | `18.62` / `21.04` | `37.46` | `0.185` | `BULLISH_ENGULFING` | 0.06527748 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1492 | 0.164013 | `-9.03%` | `4.62` / `5.37` | `28.51` | `0.162` | `NONE` | 0.14433288 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 165.49 | 189.379464 | `-12.61%` | `10.17` / `10.95` | `32.05` | `0.219` | `NONE` | 157.87746 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3955.15 | 4026.49303 | `-1.77%` | `15.13` / `17.03` | `26.28` | `0.104` | `NONE` | 3852.3161 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LINKUSDT` | 10.098 | 10.700182 | `-5.63%` | `8.47` / `9.58` | `36.67` | `0.222` | `NONE` | 9.7877852 | `EXIT_SHORT_STOCH_20` | HOLD |
