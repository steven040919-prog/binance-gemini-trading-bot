# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T20:33:30Z`
- **Ciclo de ejecucion:** `#153`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se mantiene bajo la EMA 200 con un régimen predominantemente bajista. No se cumplen los requisitos estrictos de los Pilares Long (P1-P4) debido a la ausencia de configuraciones alcistas limpias en zona de valor y divergencias suficientes. Tampoco se activa el Pilar Short (S1) ya que los activos evaluados no están testeando la EMA 200 con sobrecompra en el estocástico. El portafolio permanece en modo HOLD esperando mejores oportunidades.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.8e-06 | 5e-06 | `-5.09%` | `3.01` / `4.46` | `26.11` | `0.139` | `NONE` | 4.58e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001497 | 0.001554 | `-3.69%` | `3.57` / `3.67` | `35.19` | `0.245` | `BEARISH_ENGULFING` | 0.00142814 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1502 | 0.160829 | `-6.61%` | `20.44` / `33.98` | `42.18` | `-0.026` | `BULLISH_HAMMER` | 0.14436356 | `WATCH` | HOLD |
| `BTCUSDT` | 74518.73 | 75591.311572 | `-1.42%` | `77.61` / `78.51` | `58.55` | `0.945` | `BULLISH_HAMMER` | 72581.24302 | `WATCH` | **HOLD** (75%) |
| `XAUTUSDT` | 3978.42 | 4032.954068 | `-1.35%` | `2.18` / `1.79` | `21.0` | `0.073` | `NONE` | 3874.98108 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.86 | 7.951697 | `-1.15%` | `21.53` / `24.61` | `41.68` | `0.224` | `BEARISH_ENGULFING` | 7.573472 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1579 | 0.165529 | `-4.61%` | `20.06` / `27.0` | `39.5` | `0.167` | `BULLISH_HAMMER` | 0.1531788 | `WATCH` | HOLD |
| `PAXGUSDT` | 3980.84 | 4038.508185 | `-1.43%` | `2.08` / `1.34` | `21.08` | `0.073` | `NONE` | 3877.33816 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 123.07 | 128.849444 | `-4.49%` | `38.66` / `46.27` | `43.4` | `0.217` | `BEARISH_ENGULFING` | 119.808618 | `WATCH` | HOLD |
| `ETHUSDT` | 2081.42 | 2177.143404 | `-4.40%` | `61.85` / `67.1` | `55.09` | `0.842` | `NONE` | 2027.30308 | `WATCH` | HOLD |
| `ZECUSDT` | 999.28 | 1180.82823 | `-15.37%` | `58.3` / `59.18` | `43.3` | `0.52` | `BULLISH_HAMMER` | 953.31312 | `WATCH` | HOLD |
| `MUBUSDT` | 813.51 | 754.014015 | `+7.89%` | `87.65` / `91.94` | `71.5` | `0.791` | `NONE` | 788.98821 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOXSBUSDT` | 45.17 | 59.645873 | `-24.27%` | `25.68` / `15.67` | `37.59` | `0.319` | `MORNING_STAR` | 43.09218 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SNXXBUSDT` | 4.46 | 4.182437 | `+6.64%` | `86.08` / `90.65` | `68.95` | `0.762` | `BULLISH_HAMMER` | 4.25484 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 84.94 | 88.391938 | `-3.91%` | `74.16` / `77.95` | `57.08` | `0.808` | `BULLISH_HAMMER` | 82.73156 | `WATCH` | HOLD |
| `NEARUSDT` | 3.713 | 3.770098 | `-1.51%` | `61.64` / `68.01` | `53.13` | `0.571` | `BULLISH_HAMMER` | 3.5424504 | `WATCH` | HOLD |
