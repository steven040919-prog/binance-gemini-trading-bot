# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T08:11:46Z`
- **Ciclo de ejecucion:** `#214`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado presenta una clara tendencia bajista macro en la temporalidad de 1h, con la totalidad de los activos cotizando por debajo de la EMA 200 y pendientes negativas. Se detecta un setup activo de Venta en Corto (SHORT) en DOGEUSDT basado en el Pilar M15 Scalper Momentum Pullback Short. El resto de los activos no cumplen las condiciones de confluencia estricta para LONG (P1-P4) ni rechazo en resistencia EMA 200 para SHORT (S1), manteniendose en espera defensiva.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.45e-06 | 5e-06 | `-10.83%` | `5.62` / `7.69` | `21.08` | `0.178` | `BEARISH_SHOOTING_STAR` | 4.25e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73649.39 | 75413.383398 | `-2.34%` | `13.74` / `12.58` | `43.91` | `0.262` | `BULLISH_ENGULFING` | 71734.50586 | `EXIT_SHORT_STOCH_20` | **HOLD** (65%) |
| `ETHUSDT` | 2050.64 | 2163.105541 | `-5.20%` | `23.84` / `20.02` | `43.51` | `0.274` | `BULLISH_ENGULFING` | 1997.32336 | `WATCH` | **HOLD** (65%) |
| `NEARUSDT` | 3.497 | 3.741599 | `-6.54%` | `3.65` / `4.0` | `33.87` | `0.139` | `BEARISH_SHOOTING_STAR` | 3.3908876 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 82.95 | 87.759501 | `-5.48%` | `22.01` / `20.42` | `41.56` | `0.22` | `BULLISH_ENGULFING` | 80.7933 | `WATCH` | **HOLD** (60%) |
| `UNIUSDT` | 6.142 | 6.874397 | `-10.65%` | `7.82` / `11.85` | `31.45` | `0.193` | `BEARISH_SHOOTING_STAR` | 5.9292832 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0436 | 1.135103 | `-8.06%` | `17.33` / `13.11` | `38.93` | `0.196` | `BEARISH_SHOOTING_STAR` | 1.0164664 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.466 | 7.901304 | `-5.51%` | `11.82` / `10.25` | `34.73` | `0.235` | `BULLISH_ENGULFING` | 7.122564 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1416 | 0.158808 | `-10.84%` | `1.86` / `3.05` | `24.54` | `0.15` | `BEARISH_SHOOTING_STAR` | 0.13716704 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 674.14 | 691.212232 | `-2.47%` | `15.48` / `10.26` | `37.15` | `0.139` | `BULLISH_ENGULFING` | 656.61236 | `EXIT_SHORT_STOCH_20` | HOLD |
| `HYPEUSDT` | 71.33 | 76.769442 | `-7.09%` | `21.17` / `21.96` | `39.76` | `0.172` | `BULLISH_ENGULFING` | 69.376336 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1491 | 0.163887 | `-9.02%` | `4.02` / `4.71` | `28.32` | `0.191` | `BEARISH_SHOOTING_STAR` | 0.14445502 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06698 | 0.070717 | `-5.29%` | `20.76` / `19.75` | `37.14` | `0.202` | `BULLISH_ENGULFING` | 0.06872148 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (78%) |
| `QNTUSDT` | 165.43 | 189.249886 | `-12.59%` | `11.6` / `10.59` | `32.22` | `0.243` | `BULLISH_ENGULFING` | 157.82022 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3952.16 | 4025.710762 | `-1.83%` | `10.96` / `14.94` | `25.27` | `0.058` | `NONE` | 3849.40384 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 117.03 | 127.984152 | `-8.56%` | `8.19` / `6.76` | `27.05` | `0.142` | `NONE` | 113.574468 | `EXIT_SHORT_STOCH_20` | HOLD |
