# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T05:00:28Z`
- **Ciclo de ejecucion:** `#194`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global de criptomonedas se mantiene bajo presión bajista por debajo de la EMA 200 en temporalidad de 1 hora. Sin embargo, destaca la activación de configuraciones de alta precisión: INJUSDT cumple con los requisitos del Pilar S1 / M15_SCALPER_PULLBACK_SHORT para una entrada en SHORT debido al rechazo bajista en resistencia y formación de vela de giro bajista. Asimismo, OPGUSDT muestra fortaleza en tendencia alcista principal cumpliendo con el Pilar P1 (Pullback sobre EMA 200) permitiendo una ejecución LONG. No hay posiciones abiertas actuales para ajustes de SL/TP, operando estrictamente bajo la gestión de riesgo institucional.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 73732.0 | 75469.673287 | `-2.30%` | `23.94` / `26.16` | `44.38` | `0.245` | `BEARISH_ENGULFING` | 71814.968 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.57e-06 | 5e-06 | `-8.72%` | `13.22` / `14.49` | `25.75` | `0.22` | `BULLISH_HAMMER` | 4.38e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2050.45 | 2166.776602 | `-5.37%` | `23.85` / `26.51` | `42.1` | `0.222` | `NONE` | 1997.1383 | `WATCH` | HOLD |
| `UNIUSDT` | 6.249 | 6.890024 | `-9.30%` | `23.88` / `20.81` | `35.76` | `0.238` | `NONE` | 5.999032 | `WATCH` | HOLD |
| `SOLUSDT` | 83.1 | 87.944352 | `-5.51%` | `27.32` / `29.42` | `41.53` | `0.166` | `NONE` | 80.9394 | `WATCH` | HOLD |
| `NEARUSDT` | 3.549 | 3.74846 | `-5.32%` | `8.07` / `11.54` | `38.56` | `0.138` | `NONE` | 3.4248202 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001457 | 0.001546 | `-5.78%` | `11.5` / `8.43` | `32.89` | `0.206` | `BULLISH_HAMMER` | 0.00138998 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0444 | 1.138168 | `-8.24%` | `11.89` / `16.81` | `37.91` | `0.072` | `NONE` | 1.0172456 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.541 | 7.918551 | `-4.77%` | `20.2` / `19.01` | `33.02` | `0.193` | `BEARISH_SHOOTING_STAR` | 7.8523284 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (85%) |
| `ARBUSDT` | 0.1509 | 0.164335 | `-8.18%` | `6.71` / `7.99` | `31.8` | `0.175` | `NONE` | 0.14523336 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 676.61 | 691.643366 | `-2.17%` | `6.2` / `12.64` | `39.04` | `0.083` | `BEARISH_SHOOTING_STAR` | 659.01814 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1439 | 0.159419 | `-9.73%` | `8.84` / `11.18` | `29.34` | `0.143` | `NONE` | 0.13853764 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06722 | 0.070839 | `-5.11%` | `27.48` / `29.71` | `37.98` | `0.159` | `NONE` | 0.06547228 | `WATCH` | HOLD |
| `QNTUSDT` | 166.25 | 189.921021 | `-12.46%` | `13.84` / `12.1` | `28.59` | `0.167` | `BULLISH_HAMMER` | 158.6025 | `EXIT_SHORT_STOCH_20` | HOLD |
| `OPGUSDT` | 0.1357 | 0.126102 | `+7.61%` | `10.69` / `7.72` | `49.93` | `0.347` | `BULLISH_ENGULFING` | 0.1294578 | `P1_EMA200_PULLBACK` | **BUY** (82%) |
| `LINKUSDT` | 10.107 | 10.721274 | `-5.73%` | `15.91` / `17.87` | `33.5` | `0.143` | `NONE` | 9.844218 | `EXIT_SHORT_STOCH_20` | HOLD |
