# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T01:41:20Z`
- **Ciclo de ejecucion:** `#98`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `7.00 USDT`
- **Liquidez Disponible:** `7.00 USDT`
- **Rendimiento Diario (UTC):** `-50.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se mantiene predominantemente bajo un regimen bajista (htf_trend BEARISH con precio debajo de la EMA 200 en la mayoria de los activos principales). Actualmente la cartera cuenta con un capital libre reducido de 7.0 USDT y sin posiciones abiertas. Tras evaluar los 4 Pilares LONG y el Pilar SHORT (S1), ninguno de los candidatos cumple simultaneamente con los estrictos umbrales institucionales de sobreventa/sobrecompra extrema y formacion de patron de vela especificados en la arquitectura autonomes, por lo que se prioriza la conservacion de capital bajo una postura de observacion (HOLD) sin disparar nuevas operaciones en este ciclo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1040.06 | 1220.573774 | `-14.79%` | `21.98` / `23.21` | `34.49` | `0.267` | `BEARISH_ENGULFING` | 992.21724 | `WATCH` | HOLD |
| `BTCUSDT` | 73980.0 | 75899.755884 | `-2.53%` | `49.32` / `47.81` | `48.62` | `0.516` | `BEARISH_ENGULFING` | 72056.52 | `WATCH` | **HOLD** (75%) |
| `TRXUSDT` | 0.3181 | 0.318984 | `-0.28%` | `15.56` / `14.81` | `47.69` | `0.325` | `BULLISH_ENGULFING` | 0.3098294 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2064.07 | 2198.129572 | `-6.10%` | `48.3` / `44.42` | `44.71` | `0.459` | `BULLISH_ENGULFING` | 1988.278552 | `WATCH` | HOLD |
| `INITUSDT` | 0.24057 | 0.164831 | `+45.95%` | `46.9` / `53.8` | `49.58` | `0.392` | `BEARISH_ENGULFING` | 0.22950378 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001904 | 0.001543 | `+23.38%` | `60.42` / `52.84` | `62.95` | `0.768` | `NONE` | 0.00181642 | `WATCH` | HOLD |
| `SOLUSDT` | 83.91 | 89.333804 | `-6.07%` | `52.84` / `45.32` | `46.21` | `0.493` | `BULLISH_ENGULFING` | 80.310866 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.5e-06 | 5e-06 | `+8.80%` | `62.09` / `50.33` | `63.24` | `1.032` | `BEARISH_SHOOTING_STAR` | 5.25e-06 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0623 | 1.163556 | `-8.70%` | `46.32` / `44.29` | `43.48` | `0.403` | `BULLISH_ENGULFING` | 1.01861822 | `WATCH` | HOLD |
| `NEARUSDT` | 3.701 | 3.775289 | `-1.97%` | `57.26` / `44.79` | `59.18` | `0.948` | `MORNING_STAR` | 3.530754 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0013 | 1.001215 | `+0.01%` | `88.89` / `80.69` | `58.73` | `0.787` | `NONE` | 0.9752662 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 683.89 | 693.764987 | `-1.42%` | `53.42` / `46.32` | `51.89` | `0.551` | `BULLISH_ENGULFING` | 665.634538 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.131 | 1.104605 | `+2.39%` | `67.05` / `72.34` | `61.63` | `0.779` | `BULLISH_HAMMER` | 1.078974 | `WATCH` | HOLD |
| `UNIUSDT` | 6.797 | 7.016857 | `-3.13%` | `20.28` / `15.13` | `47.36` | `0.418` | `BEARISH_SHOOTING_STAR` | 6.484338 | `EXIT_SHORT_STOCH_20` | HOLD |
| `HYPEUSDT` | 72.55 | 78.430911 | `-7.50%` | `46.36` / `45.62` | `45.02` | `0.427` | `BEARISH_ENGULFING` | 69.58154 | `WATCH` | HOLD |
| `AVAXUSDT` | 8.48 | 8.391809 | `+1.05%` | `89.68` / `79.58` | `57.92` | `0.879` | `NONE` | 8.098864 | `EXIT_LONG_STOCH_80` | HOLD |
