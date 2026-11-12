# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T09:11:05Z`
- **Ciclo de ejecucion:** `#220`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado presenta un regimen claramente bajista en H1, con la totalidad de los activos cotizando por debajo de la EMA 200 y pendientes macro negativas. Se identifican setups de venta en corto mediante el pilar M15 Scalper Pullback Short en ETHUSDT y SOLUSDT, aprovechando el alineamiento bajista de las medias dinamicas (EMA 9 < 21 < 50) y el rebote en la zona de control. Se respeta el limite maximo de 2 posiciones abiertas del portafolio.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 73444.16 | 75394.780637 | `-2.59%` | `10.44` / `11.28` | `40.08` | `0.15` | `NONE` | 71534.61184 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `PEPEUSDT` | 4.43e-06 | 5e-06 | `-11.08%` | `6.88` / `6.89` | `21.26` | `0.179` | `BEARISH_SHOOTING_STAR` | 4.23e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `ETHUSDT` | 2044.2 | 2162.220649 | `-5.46%` | `24.56` / `22.4` | `40.25` | `0.182` | `BULLISH_HAMMER` | 2097.3492 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (84%) |
| `NEARUSDT` | 3.467 | 3.73712 | `-7.23%` | `3.09` / `3.45` | `31.75` | `0.118` | `NONE` | 3.3536834 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `SOLUSDT` | 82.82 | 87.71446 | `-5.58%` | `24.61` / `22.28` | `40.28` | `0.212` | `BULLISH_HAMMER` | 84.97332 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (82%) |
| `XRPUSDT` | 1.0445 | 1.134221 | `-7.91%` | `23.57` / `18.65` | `40.12` | `0.24` | `NONE` | 1.017343 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `UNIUSDT` | 6.138 | 6.864341 | `-10.58%` | `8.5` / `9.21` | `31.24` | `0.218` | `BULLISH_HAMMER` | 5.9134048 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `INJUSDT` | 7.381 | 7.895541 | `-6.52%` | `5.62` / `7.09` | `29.71` | `0.182` | `BEARISH_SHOOTING_STAR` | 7.116427 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `BNBUSDT` | 670.81 | 691.097579 | `-2.94%` | `10.49` / `11.17` | `32.42` | `0.051` | `NONE` | 653.36894 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `ENAUSDT` | 0.1413 | 0.1586 | `-10.91%` | `2.78` / `2.49` | `24.41` | `0.171` | `BULLISH_HAMMER` | 0.13667404 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `ARBUSDT` | 0.1486 | 0.163765 | `-9.26%` | `4.72` / `4.33` | `28.05` | `0.199` | `NONE` | 0.14386892 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `XAUTUSDT` | 3928.76 | 4024.556459 | `-2.38%` | `10.09` / `12.54` | `22.01` | `-0.095` | `NONE` | 3826.61224 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `DOGEUSDT` | 0.06687 | 0.070683 | `-5.39%` | `22.38` / `20.53` | `35.9` | `0.2` | `NONE` | 0.06513138 | `WATCH` | **HOLD** (90%) |
| `QNTUSDT` | 164.27 | 188.863746 | `-13.02%` | `11.15` / `10.24` | `30.82` | `0.231` | `BULLISH_HAMMER` | 156.886324 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `HYPEUSDT` | 71.22 | 76.71987 | `-7.17%` | `23.87` / `21.64` | `38.84` | `0.179` | `NONE` | 69.36828 | `WATCH` | **HOLD** (90%) |
| `LINKUSDT` | 10.081 | 10.684068 | `-5.64%` | `14.7` / `12.22` | `36.08` | `0.248` | `BULLISH_HAMMER` | 10.343106 | `M15_SCALPER_PULLBACK_SHORT` | **HOLD** (75%) |
