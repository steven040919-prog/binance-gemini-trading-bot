# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T14:33:08Z`
- **Ciclo de ejecucion:** `#334`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de criptomonedas en 1H permanece bajo presión bajista general con la mayoría de los activos cotizando por debajo de la EMA 200. Se activa una oportunidad LONG en ERAUSDT bajo el Pilar 1 (Pullback sobre EMA 200 con patrón alcista y estocástico girando) y una oportunidad SHORT en ZECUSDT en Futuros USDT-M bajo el Pilar S1 (Rechazo bajista en resistencia de la EMA 200). Las posiciones abiertas sin ganancia activa se mantienen en observación o salida técnica según los niveles de sobrecompra.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.0781 | 0.077905 | `+0.25%` | `24.9` / `18.14` | `39.27` | `0.203` | `BULLISH_ENGULFING` | 0.0745074 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `GRAMUSDT` | 1.134 | 1.137343 | `-0.29%` | `45.56` / `52.65` | `40.42` | `0.122` | `BEARISH_ENGULFING` | 1.081836 | `WATCH` | HOLD |
| `BTCUSDT` | 69400.01 | 74099.568831 | `-6.34%` | `47.21` / `45.07` | `37.56` | `0.394` | `BULLISH_ENGULFING` | 67527.459778 | `WATCH` | HOLD |
| `ETHUSDT` | 1968.6 | 2115.724787 | `-6.95%` | `55.62` / `52.27` | `44.78` | `0.482` | `BEARISH_SHOOTING_STAR` | 1899.71384 | `WATCH` | HOLD |
| `SOLUSDT` | 81.65 | 85.772647 | `-4.81%` | `78.32` / `73.83` | `56.31` | `0.758` | `BULLISH_HAMMER` | 78.45609 | `WATCH` | HOLD |
| `NEARUSDT` | 3.59 | 3.632345 | `-1.17%` | `86.2` / `87.25` | `61.81` | `0.913` | `BULLISH_ENGULFING` | 3.42486 | `EXIT_LONG_STOCH_80` | HOLD |
| `DODOUSDT` | 0.02815 | 0.023743 | `+18.56%` | `63.65` / `69.4` | `57.37` | `0.565` | `NONE` | 0.0268551 | `WATCH` | HOLD |
| `ZECUSDT` | 966.79 | 1097.854793 | `-11.94%` | `80.77` / `83.46` | `54.43` | `0.769` | `BEARISH_SHOOTING_STAR` | 1011.26234 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (82%) |
| `BNBUSDT` | 642.21 | 678.766928 | `-5.39%` | `55.47` / `51.78` | `43.36` | `0.477` | `BEARISH_SHOOTING_STAR` | 624.357612 | `WATCH` | HOLD |
| `XRPUSDT` | 1.036 | 1.10748 | `-6.45%` | `69.16` / `60.71` | `54.7` | `0.734` | `BULLISH_ENGULFING` | 0.9900144 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.56e-06 | 5e-06 | `-5.94%` | `49.38` / `41.98` | `52.75` | `0.707` | `BEARISH_SHOOTING_STAR` | 4.35e-06 | `WATCH` | HOLD |
| `HYPEUSDT` | 74.48 | 75.24647 | `-1.02%` | `84.71` / `89.38` | `66.42` | `0.962` | `BEARISH_SHOOTING_STAR` | 77.524816 | `S1_EMA200_RESISTANCE_REJECT` | HOLD |
| `INJUSDT` | 8.201 | 7.783189 | `+5.37%` | `92.11` / `93.06` | `76.54` | `1.12` | `NONE` | 7.823754 | `EXIT_LONG_STOCH_80` | HOLD |
| `SUIUSDT` | 0.824 | 0.835967 | `-1.43%` | `88.82` / `87.77` | `65.33` | `0.973` | `NONE` | 0.786096 | `EXIT_LONG_STOCH_80` | HOLD |
| `UNIUSDT` | 5.943 | 6.613547 | `-10.14%` | `57.93` / `47.97` | `49.63` | `0.591` | `BULLISH_HAMMER` | 5.669622 | `WATCH` | HOLD |
| `DOGEUSDT` | 0.06626 | 0.069237 | `-4.30%` | `78.7` / `69.93` | `57.29` | `0.738` | `NONE` | 0.06350374 | `WATCH` | HOLD |
