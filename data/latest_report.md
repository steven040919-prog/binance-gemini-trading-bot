# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T06:08:27Z`
- **Ciclo de ejecucion:** `#111`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> Evaluación institucional de mercado en temporalidad 1H. La mayoría de los activos operan por debajo de la EMA 200 en un régimen bajista generalizado. Se identifica al activo RLUSDUSDT cumpliendo rigurosamente con el Pilar S1 (Rechazo bajista en resistencia de EMA 200, con RSI superior a 62, BB %B elevado y vela BEARISH_SHOOTING_STAR), habilitando una orden SHORT en Binance Futuros USDT-M. No se activan entradas LONG (P1-P4) debido a que los pullbacks alcistas no cumplen simultáneamente con los criterios estrictos de sobreventa extrema en estocástico girando al alza con confirmación de soporte institucional. Las posiciones abiertas se mantienen sin cambios al no registrarse operaciones activas con ganancias.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1009.42 | 1211.628128 | `-16.69%` | `15.79` / `15.3` | `30.24` | `0.269` | `BULLISH_HAMMER` | 962.98668 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.641 | 6.994081 | `-5.05%` | `15.39` / `14.88` | `36.8` | `0.273` | `BEARISH_ENGULFING` | 6.439411 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 180.16 | 193.793253 | `-7.03%` | `47.95` / `45.93` | `34.27` | `0.287` | `NONE` | 174.95584 | `WATCH` | HOLD |
| `CYBERUSDT` | 0.269 | 0.282775 | `-4.87%` | `3.17` / `4.0` | `43.98` | `0.233` | `BEARISH_ENGULFING` | 0.256626 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRXUSDT` | 0.3179 | 0.318665 | `-0.24%` | `25.9` / `15.96` | `47.22` | `0.386` | `BEARISH_SHOOTING_STAR` | 0.3096346 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73898.7 | 75810.635239 | `-2.52%` | `75.13` / `61.4` | `48.51` | `0.614` | `BULLISH_ENGULFING` | 71977.3338 | `WATCH` | HOLD |
| `INITUSDT` | 0.303 | 0.170544 | `+77.67%` | `59.39` / `63.85` | `57.97` | `0.691` | `BEARISH_ENGULFING` | 0.289062 | `WATCH` | HOLD |
| `ETHUSDT` | 2068.31 | 2191.744282 | `-5.63%` | `83.71` / `72.44` | `47.35` | `0.634` | `NONE` | 2014.53394 | `EXIT_LONG_STOCH_80` | HOLD |
| `ONEUSDT` | 0.001756 | 0.001555 | `+12.94%` | `33.44` / `32.19` | `50.03` | `0.254` | `NONE` | 0.00167522 | `WATCH` | HOLD |
| `SOLUSDT` | 83.2 | 89.02142 | `-6.54%` | `58.29` / `53.67` | `41.83` | `0.466` | `BULLISH_ENGULFING` | 81.0368 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0611 | 1.158398 | `-8.40%` | `59.3` / `58.16` | `44.59` | `0.53` | `BULLISH_ENGULFING` | 1.02890244 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.32e-06 | 5e-06 | `+4.87%` | `47.89` / `50.08` | `51.18` | `0.469` | `BULLISH_HAMMER` | 5.08e-06 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0012 | 1.001213 | `-0.00%` | `71.43` / `75.4` | `54.62` | `0.686` | `BEARISH_SHOOTING_STAR` | 1.0272312 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (84%) |
| `NEARUSDT` | 3.638 | 3.769162 | `-3.48%` | `68.53` / `70.5` | `52.09` | `0.604` | `NONE` | 3.5135804 | `WATCH` | HOLD |
| `BNBUSDT` | 681.87 | 693.396991 | `-1.66%` | `72.15` / `64.59` | `48.7` | `0.58` | `BULLISH_HAMMER` | 664.14138 | `WATCH` | HOLD |
| `HYPEUSDT` | 72.08 | 78.032496 | `-7.63%` | `61.6` / `51.29` | `42.09` | `0.435` | `BEARISH_ENGULFING` | 70.199568 | `WATCH` | HOLD |
