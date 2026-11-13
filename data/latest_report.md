# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T14:14:09Z`
- **Ciclo de ejecucion:** `#332`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de criptomonedas en temporalidad 1h mantiene un sesgo mayoritariamente bajista con la mayoria de los activos cotizando por debajo de la EMA 200. Se evaluan las oportunidades bajo la arquitectura de pilares institucionales identificando entradas LONG en ERAUSDT (Pilar 1: Pullback de valor sobre EMA 200 con patron envolvente alcista y estocastico girando al alza) y entradas SHORT en Futuros USDT-M para ZECUSDT e HYPEUSDT (Pilar S1: Rechazo bajista en resistencia de EMA 200 con formacion de estrella fugaz y estocastico en sobrecompra). No hay posiciones abiertas actualmente para ajustar.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.0788 | 0.077912 | `+1.14%` | `27.59` / `19.03` | `40.7` | `0.275` | `BULLISH_ENGULFING` | 0.0751752 | `P1_EMA200_PULLBACK` | **BUY** (85%) |
| `GRAMUSDT` | 1.131 | 1.137313 | `-0.56%` | `43.7` / `52.03` | `39.12` | `0.033` | `BEARISH_ENGULFING` | 1.078974 | `WATCH` | HOLD |
| `BTCUSDT` | 69324.38 | 74098.816294 | `-6.44%` | `46.52` / `44.84` | `36.89` | `0.379` | `BULLISH_ENGULFING` | 67521.94612 | `WATCH` | HOLD |
| `ETHUSDT` | 1965.71 | 2115.696031 | `-7.09%` | `54.84` / `52.01` | `43.57` | `0.463` | `BEARISH_SHOOTING_STAR` | 1900.96725 | `WATCH` | HOLD |
| `NEARUSDT` | 3.572 | 3.632166 | `-1.66%` | `84.6` / `86.72` | `59.9` | `0.867` | `BULLISH_ENGULFING` | 3.407688 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 81.31 | 85.769263 | `-5.20%` | `75.78` / `72.99` | `53.2` | `0.686` | `NONE` | 78.513512 | `WATCH` | HOLD |
| `DODOUSDT` | 0.02817 | 0.023743 | `+18.64%` | `63.82` / `69.46` | `57.53` | `0.57` | `NONE` | 0.02687418 | `WATCH` | HOLD |
| `ZECUSDT` | 962.95 | 1097.816584 | `-12.28%` | `79.63` / `83.08` | `52.86` | `0.721` | `BEARISH_SHOOTING_STAR` | 1007.2457 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (82%) |
| `BNBUSDT` | 641.28 | 678.757675 | `-5.52%` | `54.57` / `51.48` | `42.4` | `0.455` | `BEARISH_SHOOTING_STAR` | 624.378816 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.55e-06 | 5e-06 | `-6.14%` | `48.15` / `41.57` | `51.44` | `0.638` | `BEARISH_SHOOTING_STAR` | 4.34e-06 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0307 | 1.107427 | `-6.93%` | `65.33` / `59.43` | `50.78` | `0.608` | `BULLISH_ENGULFING` | 0.99055706 | `WATCH` | HOLD |
| `HYPEUSDT` | 73.91 | 75.240798 | `-1.77%` | `81.19` / `88.2` | `62.24` | `0.856` | `BEARISH_SHOOTING_STAR` | 77.30986 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (80%) |
| `INJUSDT` | 8.211 | 7.783289 | `+5.50%` | `92.4` / `93.16` | `76.74` | `1.126` | `NONE` | 7.833294 | `EXIT_LONG_STOCH_80` | HOLD |
| `UNIUSDT` | 5.913 | 6.613249 | `-10.59%` | `55.75` / `47.25` | `47.4` | `0.536` | `NONE` | 5.641002 | `WATCH` | HOLD |
| `SUIUSDT` | 0.8193 | 0.835921 | `-1.99%` | `86.35` / `86.95` | `62.9` | `0.901` | `BULLISH_HAMMER` | 0.7816122 | `EXIT_LONG_STOCH_80` | HOLD |
| `INITUSDT` | 0.11688 | 0.151256 | `-22.73%` | `27.76` / `36.5` | `43.27` | `0.415` | `NONE` | 0.11150352 | `WATCH` | HOLD |
