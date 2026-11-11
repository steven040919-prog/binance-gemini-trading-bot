# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T00:31:06Z`
- **Ciclo de ejecucion:** `#67`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado muestra un dominio bajista generalizado con la mayoría de los activos principales (BTC, ETH, SOL, XRP, BNB) cotizando por debajo de la EMA 200 con pendientes negativas. Ninguno de los candidatos analizados satisface las condiciones estrictas de entrada para los Pilares LONG (P1-P4) ni el filtro de confluencia para el Pilar S1 SHORT (rechazo en EMA 200 con Estocástico en sobrecompra >= 80 y vela bajista de confirmación). Al no haber posiciones abiertas en el portafolio, se mantiene la liquidez al 100% en espera de confirmaciones institucionales.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1043.27 | 1221.884184 | `-14.62%` | `23.35` / `25.44` | `33.84` | `0.252` | `BEARISH_SHOOTING_STAR` | 995.27958 | `WATCH` | **HOLD** (85%) |
| `ARBUSDT` | 0.1608 | 0.166371 | `-3.35%` | `41.82` / `36.32` | `38.7` | `0.359` | `NONE` | 0.15356448 | `WATCH` | **HOLD** (80%) |
| `UNIUSDT` | 6.709 | 7.013315 | `-4.34%` | `12.21` / `13.4` | `40.17` | `0.265` | `BULLISH_HAMMER` | 6.400386 | `EXIT_SHORT_STOCH_20` | **HOLD** (80%) |
| `AAVEUSDT` | 124.08 | 129.661643 | `-4.30%` | `53.66` / `51.93` | `38.52` | `0.384` | `NONE` | 119.393888 | `WATCH` | **HOLD** (82%) |
| `XAUTUSDT` | 4029.14 | 4035.511353 | `-0.16%` | `30.84` / `24.5` | `36.62` | `0.35` | `BEARISH_SHOOTING_STAR` | 3924.38236 | `WATCH` | **HOLD** (85%) |
| `BTCUSDT` | 73648.0 | 75911.232336 | `-2.98%` | `46.53` / `47.94` | `43.26` | `0.348` | `BEARISH_ENGULFING` | 71733.152 | `WATCH` | **HOLD** (90%) |
| `ETHUSDT` | 2051.71 | 2199.255965 | `-6.71%` | `42.63` / `42.7` | `39.15` | `0.345` | `NONE` | 1989.42554 | `WATCH` | **HOLD** (88%) |
| `INITUSDT` | 0.25879 | 0.16383 | `+57.96%` | `54.93` / `59.36` | `54.44` | `0.521` | `BEARISH_ENGULFING` | 0.24688566 | `WATCH` | **HOLD** (85%) |
| `PAXGUSDT` | 4032.39 | 4041.729752 | `-0.23%` | `31.51` / `24.51` | `36.69` | `0.351` | `MORNING_STAR` | 3927.54786 | `WATCH` | **HOLD** (82%) |
| `ONEUSDT` | 0.001887 | 0.00154 | `+22.51%` | `55.75` / `51.76` | `62.03` | `0.714` | `BULLISH_ENGULFING` | 0.0018002 | `WATCH` | **HOLD** (84%) |
| `SOLUSDT` | 83.39 | 89.388452 | `-6.71%` | `44.42` / `41.08` | `40.21` | `0.374` | `BULLISH_ENGULFING` | 80.408504 | `WATCH` | **HOLD** (88%) |
| `XRPUSDT` | 1.0546 | 1.164505 | `-9.44%` | `43.83` / `43.71` | `37.05` | `0.27` | `BULLISH_HAMMER` | 1.0209712 | `WATCH` | **HOLD** (86%) |
| `PEPEUSDT` | 5.4e-06 | 5e-06 | `+7.16%` | `49.02` / `40.09` | `58.41` | `0.801` | `BEARISH_SHOOTING_STAR` | 5.15e-06 | `WATCH` | **HOLD** (80%) |
| `GRAMUSDT` | 1.133 | 1.104474 | `+2.58%` | `71.97` / `76.98` | `63.1` | `0.823` | `BEARISH_SHOOTING_STAR` | 1.0814682 | `WATCH` | **HOLD** (85%) |
| `BNBUSDT` | 680.3 | 693.980641 | `-1.97%` | `45.05` / `40.26` | `45.28` | `0.402` | `NONE` | 662.6122 | `WATCH` | **HOLD** (87%) |
| `RLUSDUSDT` | 1.0012 | 1.001214 | `-0.00%` | `83.33` / `70.63` | `54.62` | `0.639` | `BULLISH_HAMMER` | 0.9751688 | `EXIT_LONG_STOCH_80` | **HOLD** (95%) |
