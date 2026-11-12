# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T09:21:17Z`
- **Ciclo de ejecucion:** `#221`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general presenta una estructura macro bajista coherente, con la totalidad de los activos cotizando por debajo de su EMA 200 de 1H y con pendientes negativas. Ningun activo cumple actualmente con los criterios de entrada LONG (Pilares P1 a P4) ni de SHORT (Pilar S1: rechazo en resistencia EMA 200 con Estocastico >= 80 y gatillo bajista). Ademas, no hay posiciones abiertas en el portafolio para aplicar gestion dinamica de SL/TP. Se determina mantener liquidez total en USDT a la espera de confirmaciones cuantitativas en zonas clave.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 73302.01 | 75393.366209 | `-2.77%` | `9.91` / `11.11` | `37.75` | `0.071` | `NONE` | 71396.15774 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `PEPEUSDT` | 4.44e-06 | 5e-06 | `-10.88%` | `7.64` / `7.15` | `21.64` | `0.191` | `BEARISH_SHOOTING_STAR` | 4.24e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (86%) |
| `ETHUSDT` | 2041.7 | 2162.195774 | `-5.57%` | `22.86` / `21.83` | `39.11` | `0.144` | `BULLISH_HAMMER` | 1988.6158 | `WATCH` | **HOLD** (88%) |
| `SOLUSDT` | 82.73 | 87.713564 | `-5.68%` | `23.6` / `21.94` | `39.45` | `0.19` | `BULLISH_HAMMER` | 80.57902 | `WATCH` | **HOLD** (85%) |
| `NEARUSDT` | 3.473 | 3.73718 | `-7.07%` | `3.8` / `3.68` | `32.81` | `0.131` | `NONE` | 3.3535046 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0448 | 1.134224 | `-7.88%` | `23.89` / `18.76` | `40.35` | `0.247` | `BULLISH_HAMMER` | 1.0176352 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.141 | 6.864371 | `-10.54%` | `8.7` / `9.28` | `31.39` | `0.222` | `BULLISH_HAMMER` | 5.9133136 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 670.3 | 691.092505 | `-3.01%` | `10.95` / `11.32` | `31.78` | `0.032` | `NONE` | 652.8722 | `EXIT_SHORT_STOCH_20` | **HOLD** (87%) |
| `ENAUSDT` | 0.1414 | 0.158601 | `-10.85%` | `3.09` / `2.59` | `25.04` | `0.176` | `BULLISH_HAMMER` | 0.13667112 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.379 | 7.895521 | `-6.54%` | `5.62` / `7.09` | `29.64` | `0.18` | `BEARISH_SHOOTING_STAR` | 7.114493 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1485 | 0.163764 | `-9.32%` | `4.42` / `4.23` | `27.57` | `0.195` | `BULLISH_HAMMER` | 0.1438717 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3926.19 | 4024.530887 | `-2.44%` | `8.92` / `12.15` | `20.11` | `-0.116` | `NONE` | 3824.10906 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 164.2 | 188.86305 | `-13.06%` | `11.01` / `10.19` | `30.59` | `0.229` | `NONE` | 156.88904 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06683 | 0.070682 | `-5.45%` | `21.82` / `20.34` | `35.46` | `0.189` | `NONE` | 0.06509242 | `WATCH` | HOLD |
| `HYPEUSDT` | 71.31 | 76.720766 | `-7.05%` | `24.94` / `21.99` | `39.65` | `0.201` | `BULLISH_HAMMER` | 69.45594 | `WATCH` | HOLD |
| `LINKUSDT` | 10.074 | 10.683998 | `-5.71%` | `14.23` / `12.07` | `35.66` | `0.239` | `BULLISH_HAMMER` | 9.812076 | `EXIT_SHORT_STOCH_20` | HOLD |
