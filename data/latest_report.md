# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T18:55:50Z`
- **Ciclo de ejecucion:** `#251`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un régimen bajista generalizado en temporalidad de 1H, con la mayoría de los activos cotizando por debajo de la EMA 200 y con RSI débil. Se identifican oportunidades en corto bajo el Pilar S1 y M15 Scalper en activos como SOLUSDT y XRPUSDT que muestran rechazos y configuraciones bajistas válidas en futuros USDT-M.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71709.06 | 75149.175531 | `-4.58%` | `20.75` / `18.88` | `24.73` | `0.097` | `BEARISH_ENGULFING` | 69844.62444 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PEPEUSDT` | 4.4e-06 | 5e-06 | `-10.76%` | `22.5` / `19.47` | `34.25` | `0.314` | `BULLISH_ENGULFING` | 4.2e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INITUSDT` | 0.11202 | 0.162698 | `-31.15%` | `9.51` / `18.02` | `33.01` | `0.042` | `BULLISH_HAMMER` | 0.10686708 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 941.22 | 1138.808813 | `-17.35%` | `15.32` / `21.75` | `31.25` | `-0.044` | `BULLISH_HAMMER` | 897.92388 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 81.51 | 87.178696 | `-6.50%` | `35.03` / `33.47` | `35.42` | `0.157` | `NONE` | 83.8902 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (85%) |
| `NEARUSDT` | 3.428 | 3.704219 | `-7.46%` | `32.67` / `27.94` | `37.5` | `0.292` | `BEARISH_ENGULFING` | 3.270312 | `WATCH` | HOLD |
| `UNIUSDT` | 6.021 | 6.788711 | `-11.31%` | `25.62` / `25.73` | `31.04` | `0.18` | `BEARISH_ENGULFING` | 5.7965742 | `WATCH` | HOLD |
| `BNBUSDT` | 654.02 | 688.022752 | `-4.94%` | `19.73` / `18.21` | `23.61` | `0.141` | `BULLISH_HAMMER` | 637.01548 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0283 | 1.125375 | `-8.63%` | `28.3` / `25.6` | `35.49` | `0.17` | `BULLISH_ENGULFING` | 1.055566 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (82%) |
| `ENAUSDT` | 0.1399 | 0.156801 | `-10.78%` | `30.55` / `28.14` | `31.23` | `0.287` | `BULLISH_HAMMER` | 0.1334646 | `WATCH` | HOLD |
| `XAUTUSDT` | 3877.54 | 4014.844598 | `-3.42%` | `19.34` / `15.92` | `26.14` | `0.164` | `BULLISH_ENGULFING` | 3776.72396 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 113.32 | 126.354053 | `-10.32%` | `32.55` / `31.0` | `30.01` | `0.24` | `BEARISH_ENGULFING` | 109.97368 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.17 | 1.138788 | `+2.74%` | `39.45` / `60.36` | `41.57` | `0.153` | `NONE` | 1.11618 | `WATCH` | HOLD |
| `QNTUSDT` | 162.25 | 186.919684 | `-13.20%` | `20.71` / `21.37` | `31.29` | `0.184` | `NONE` | 155.56515 | `WATCH` | HOLD |
| `INJUSDT` | 7.386 | 7.852863 | `-5.95%` | `28.67` / `26.99` | `38.69` | `0.251` | `BEARISH_ENGULFING` | 7.0681252 | `WATCH` | HOLD |
| `AVAXUSDT` | 8.356 | 8.446389 | `-1.07%` | `22.01` / `23.07` | `40.43` | `0.202` | `BULLISH_ENGULFING` | 8.0680728 | `WATCH` | HOLD |
