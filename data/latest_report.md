# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T09:32:34Z`
- **Ciclo de ejecucion:** `#124`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado presenta una tendencia predominantemente bajista en la temporalidad de 1H con la mayoría de los activos cotizando por debajo de la EMA 200. No hay posiciones abiertas actualmente para ajustar SL/TP. INITUSDT presenta una señal preliminar de entrada LONG por patrón, pero se descarta al estar sobreextendido a un +33.42% de la EMA 200 (restringido por Pilar 1 a <=3.5%). Ningún otro activo cumple simultáneamente las condiciones rigurosas de sobrecompra/sobreventa y confirmación de velas para los Pilares P1-P4 o S1. Se mantiene liquidez en 100% USDT en espera de retrocesos óptimos a zonas de valor.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 966.8 | 1204.229599 | `-19.72%` | `15.23` / `17.54` | `28.09` | `0.138` | `BEARISH_ENGULFING` | 922.3272 | `EXIT_SHORT_STOCH_20` | **HOLD** (40%) |
| `ONEUSDT` | 0.001552 | 0.001555 | `-0.22%` | `6.36` / `11.32` | `37.91` | `-0.075` | `NONE` | 0.00148061 | `EXIT_SHORT_STOCH_20` | **HOLD** (45%) |
| `UNIUSDT` | 6.364 | 6.97917 | `-8.81%` | `9.78` / `11.66` | `25.31` | `0.004` | `BEARISH_ENGULFING` | 6.1323512 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PEPEUSDT` | 5.02e-06 | 5e-06 | `-0.97%` | `11.95` / `19.59` | `34.96` | `-0.079` | `NONE` | 4.79e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INITUSDT` | 0.229 | 0.171642 | `+33.42%` | `22.24` / `20.62` | `46.42` | `0.105` | `BULLISH_ENGULFING` | 0.218466 | `P1_EMA200_PULLBACK` | **HOLD** (45%) |
| `ARBUSDT` | 0.1586 | 0.166114 | `-4.52%` | `17.46` / `24.11` | `37.45` | `0.272` | `NONE` | 0.15235652 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 177.77 | 193.520966 | `-8.14%` | `17.81` / `27.86` | `31.95` | `0.035` | `BEARISH_ENGULFING` | 172.737966 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRXUSDT` | 0.3179 | 0.318302 | `-0.13%` | `28.21` / `26.05` | `48.7` | `0.469` | `BULLISH_ENGULFING` | 0.3096346 | `WATCH` | HOLD |
| `BTCUSDT` | 73710.0 | 75736.586305 | `-2.68%` | `67.61` / `74.88` | `46.26` | `0.539` | `NONE` | 71793.54 | `WATCH` | **HOLD** (50%) |
| `ETHUSDT` | 2055.25 | 2187.599917 | `-6.05%` | `65.59` / `75.12` | `43.28` | `0.536` | `NONE` | 2001.8135 | `WATCH` | **HOLD** (50%) |
| `CYBERUSDT` | 0.264 | 0.281361 | `-6.17%` | `3.61` / `4.12` | `41.66` | `0.19` | `BEARISH_ENGULFING` | 0.251856 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 83.15 | 88.830903 | `-6.40%` | `50.08` / `51.49` | `44.13` | `0.547` | `NONE` | 80.80993 | `WATCH` | **HOLD** (50%) |
| `XRPUSDT` | 1.0566 | 1.155371 | `-8.55%` | `43.59` / `45.44` | `42.6` | `0.479` | `NONE` | 1.0291284 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0844 | 0.073289 | `+15.16%` | `37.18` / `54.59` | `57.57` | `0.713` | `BULLISH_HAMMER` | 0.0805176 | `WATCH` | HOLD |
| `NEARUSDT` | 3.568 | 3.770315 | `-5.37%` | `34.74` / `46.98` | `44.43` | `0.332` | `BEARISH_ENGULFING` | 3.4396928 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0011 | 1.001203 | `-0.01%` | `46.67` / `51.75` | `47.83` | `0.519` | `BULLISH_HAMMER` | 0.9750714 | `WATCH` | HOLD |
