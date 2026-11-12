# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T09:40:35Z`
- **Ciclo de ejecucion:** `#223`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> Mercado predominantemente bajista con la mayoria de los activos cotizando por debajo de la EMA 200 H1 y mostrando pendientes negativas en temporalidades superiores. Aunque varios activos (como PEPE, UNI, INJ) muestran divergencias alcistas o patrones de vela de giro en zonas de sobreventa, no cumplen con la totalidad de los requisitos cuantitativos institucionales (confluencia de volumen, %B de Bollinger o distancia dinamica a la EMA 200). Para el Pilar S1 SHORT, la sobrecompra requerida (Stoch >= 80) no esta presente cerca de la resistencia. Se permanece en HOLD a la espera de confirmaciones validas.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 73450.01 | 75394.838846 | `-2.58%` | `13.99` / `12.47` | `40.18` | `0.153` | `NONE` | 71540.30974 | `EXIT_SHORT_STOCH_20` | **HOLD** (85%) |
| `PEPEUSDT` | 4.43e-06 | 5e-06 | `-11.08%` | `6.88` / `6.89` | `21.26` | `0.179` | `BEARISH_SHOOTING_STAR` | 4.23e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (82%) |
| `ETHUSDT` | 2044.65 | 2162.225127 | `-5.44%` | `24.86` / `22.5` | `40.46` | `0.189` | `BULLISH_HAMMER` | 1991.4891 | `WATCH` | **HOLD** (80%) |
| `SOLUSDT` | 83.02 | 87.71645 | `-5.35%` | `26.86` / `23.03` | `42.35` | `0.264` | `BULLISH_HAMMER` | 80.86148 | `WATCH` | **HOLD** (80%) |
| `NEARUSDT` | 3.492 | 3.737369 | `-6.57%` | `6.05` / `4.43` | `35.98` | `0.172` | `NONE` | 3.3501448 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0492 | 1.134268 | `-7.50%` | `28.57` / `20.32` | `44.84` | `0.351` | `NONE` | 1.0219208 | `WATCH` | HOLD |
| `UNIUSDT` | 6.181 | 6.864769 | `-9.96%` | `11.39` / `10.18` | `35.39` | `0.273` | `BULLISH_HAMMER` | 5.9059166 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 671.41 | 691.103549 | `-2.85%` | `12.96` / `11.99` | `33.21` | `0.074` | `NONE` | 653.95334 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1416 | 0.158603 | `-10.72%` | `3.72` / `2.8` | `26.27` | `0.186` | `NONE` | 0.13658032 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1485 | 0.163764 | `-9.32%` | `4.42` / `4.23` | `27.57` | `0.195` | `NONE` | 0.1438123 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 164.28 | 188.863846 | `-13.02%` | `11.17` / `10.24` | `30.86` | `0.231` | `NONE` | 156.85308 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.429 | 7.896018 | `-5.91%` | `8.45` / `8.04` | `32.91` | `0.23` | `BEARISH_SHOOTING_STAR` | 7.1098714 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3934.56 | 4024.61417 | `-2.24%` | `12.74` / `13.43` | `25.98` | `-0.042` | `NONE` | 3832.26144 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06713 | 0.070685 | `-5.03%` | `26.01` / `21.74` | `40.23` | `0.274` | `BULLISH_ENGULFING` | 0.06538462 | `WATCH` | HOLD |
| `HYPEUSDT` | 71.52 | 76.722855 | `-6.78%` | `27.43` / `22.82` | `42.29` | `0.253` | `BULLISH_ENGULFING` | 69.592384 | `WATCH` | HOLD |
| `OPGUSDT` | 0.1384 | 0.126399 | `+9.49%` | `49.75` / `37.35` | `54.82` | `0.479` | `BULLISH_ENGULFING` | 0.1320336 | `WATCH` | **HOLD** (85%) |
