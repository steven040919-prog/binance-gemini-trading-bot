# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T01:38:09Z`
- **Ciclo de ejecucion:** `#97`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se mantiene bajo un régimen bajista generalizado con la mayoría de los activos cotizando por debajo de la EMA 200 en temporalidad de 1H. No se cumplen los requisitos estrictos de los Pilares Long (P1 a P4) ni del Pilar Short (S1) ya que las confluencias de sobreventa/sobrecompra extrema, volumen institucional y patrones de velas específicos no coinciden simultáneamente con los umbrales requeridos. La cartera se mantiene sin posiciones abiertas (open_positions_count: 0), por lo que se opera en modo HOLD a la espera de mejores configuraciones institucionales.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1035.93 | 1220.53268 | `-15.12%` | `21.31` / `22.99` | `33.18` | `0.251` | `BEARISH_ENGULFING` | 988.27722 | `WATCH` | HOLD |
| `CYBERUSDT` | 0.273 | 0.283241 | `-3.62%` | `15.27` / `21.89` | `45.83` | `0.342` | `BEARISH_SHOOTING_STAR` | 0.260442 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73890.55 | 75898.865834 | `-2.65%` | `47.92` / `47.35` | `47.4` | `0.476` | `BEARISH_ENGULFING` | 71969.3957 | `WATCH` | **HOLD** (50%) |
| `TRXUSDT` | 0.3181 | 0.318984 | `-0.28%` | `15.56` / `14.81` | `47.69` | `0.325` | `BULLISH_ENGULFING` | 0.3098294 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2059.78 | 2198.086885 | `-6.29%` | `46.91` / `43.96` | `43.0` | `0.426` | `BULLISH_ENGULFING` | 1988.391808 | `WATCH` | HOLD |
| `INITUSDT` | 0.24901 | 0.164915 | `+50.99%` | `48.9` / `54.47` | `51.74` | `0.445` | `BEARISH_ENGULFING` | 0.23755554 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001888 | 0.001543 | `+22.36%` | `58.24` / `52.12` | `62.01` | `0.731` | `NONE` | 0.00180115 | `WATCH` | HOLD |
| `SOLUSDT` | 83.72 | 89.331913 | `-6.28%` | `51.21` / `44.77` | `44.44` | `0.458` | `BULLISH_ENGULFING` | 80.332816 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.48e-06 | 5e-06 | `+8.41%` | `60.78` / `49.89` | `62.37` | `0.987` | `BEARISH_SHOOTING_STAR` | 5.23e-06 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0601 | 1.163534 | `-8.89%` | `44.96` / `43.83` | `42.04` | `0.372` | `BULLISH_ENGULFING` | 1.01868114 | `WATCH` | HOLD |
| `NEARUSDT` | 3.691 | 3.775189 | `-2.23%` | `56.12` / `44.41` | `58.45` | `0.911` | `MORNING_STAR` | 3.521214 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.131 | 1.104605 | `+2.39%` | `67.05` / `72.34` | `61.63` | `0.779` | `BULLISH_HAMMER` | 1.078974 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0012 | 1.001214 | `-0.00%` | `83.33` / `78.83` | `54.62` | `0.639` | `NONE` | 0.9751688 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 683.33 | 693.759415 | `-1.50%` | `52.55` / `46.03` | `50.99` | `0.531` | `BULLISH_ENGULFING` | 665.56342 | `WATCH` | HOLD |
| `UNIUSDT` | 6.778 | 7.016668 | `-3.40%` | `19.13` / `14.74` | `45.97` | `0.389` | `BEARISH_SHOOTING_STAR` | 6.466212 | `EXIT_SHORT_STOCH_20` | HOLD |
| `HYPEUSDT` | 72.44 | 78.429816 | `-7.64%` | `45.43` / `45.31` | `44.01` | `0.404` | `BEARISH_ENGULFING` | 69.584752 | `WATCH` | HOLD |
