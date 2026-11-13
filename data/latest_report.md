# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T17:03:32Z`
- **Ciclo de ejecucion:** `#350`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global en temporalidade 1H se encuentra bajo régimen bajista generalizado, con la mayoría de los activos operando por debajo de la EMA 200. Sin embargo, destaca la activación del Pilar S1 Short en SOXSBUSDT, donde confluyen tendencia macro bajista, rechazo en resistencia de la EMA 200, sobrecompra estocástica y patrón de vela BEARISH_SHOOTING_STAR, validando una entrada en cortos para Binance Futuros USDT-M. El resto del portafolio se mantiene en observación o bajo criterios de salida/espera ya que no cumplen los requisitos estrictos de capitulación o pullback alcista.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68651.62 | 73925.986488 | `-7.13%` | `40.29` / `41.03` | `31.51` | `0.298` | `BULLISH_HAMMER` | 66771.158572 | `WATCH` | HOLD |
| `ETHUSDT` | 1925.14 | 2110.257257 | `-8.77%` | `32.5` / `38.4` | `31.84` | `0.258` | `NONE` | 1868.876864 | `WATCH` | HOLD |
| `BNBUSDT` | 630.49 | 677.504872 | `-6.94%` | `32.21` / `39.42` | `33.11` | `0.259` | `NONE` | 614.09726 | `WATCH` | HOLD |
| `ERAUSDT` | 0.075 | 0.077929 | `-3.76%` | `9.71` / `14.69` | `33.95` | `0.085` | `BEARISH_SHOOTING_STAR` | 0.07155 | `EXIT_SHORT_STOCH_20` | HOLD |
| `GRAMUSDT` | 1.129 | 1.137541 | `-0.75%` | `28.57` / `28.53` | `38.83` | `0.144` | `BEARISH_SHOOTING_STAR` | 1.077066 | `WATCH` | HOLD |
| `UNIUSDT` | 5.75 | 6.593504 | `-12.79%` | `36.09` / `47.11` | `37.16` | `0.279` | `NONE` | 5.5174 | `WATCH` | HOLD |
| `ENAUSDT` | 0.1347 | 0.152076 | `-11.43%` | `35.76` / `50.5` | `37.36` | `0.186` | `NONE` | 0.12877364 | `WATCH` | HOLD |
| `XAUTUSDT` | 3869.39 | 3991.314085 | `-3.05%` | `14.41` / `18.9` | `37.96` | `0.165` | `NONE` | 3768.78586 | `EXIT_SHORT_STOCH_20` | HOLD |
| `MUBUSDT` | 759.74 | 763.271338 | `-0.46%` | `13.82` / `11.31` | `32.78` | `0.017` | `BULLISH_HAMMER` | 728.611696 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 110.61 | 122.937692 | `-10.03%` | `29.8` / `47.8` | `38.49` | `0.253` | `NONE` | 107.298066 | `WATCH` | HOLD |
| `PAXGUSDT` | 3871.2 | 3995.237867 | `-3.10%` | `14.93` / `18.29` | `37.62` | `0.18` | `NONE` | 3770.5488 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BARDUSDT` | 0.1483 | 0.108786 | `+36.32%` | `56.2` / `66.18` | `56.69` | `0.561` | `BULLISH_HAMMER` | 0.1414782 | `WATCH` | HOLD |
| `SOLUSDT` | 79.54 | 85.61331 | `-7.09%` | `39.97` / `51.49` | `39.45` | `0.326` | `BULLISH_HAMMER` | 77.026948 | `WATCH` | HOLD |
| `ZECUSDT` | 945.67 | 1093.652457 | `-13.53%` | `59.09` / `63.75` | `46.35` | `0.493` | `NONE` | 902.16918 | `WATCH` | HOLD |
| `SOXSBUSDT` | 53.03 | 55.600794 | `-4.62%` | `83.99` / `87.11` | `69.81` | `0.989` | `BEARISH_SHOOTING_STAR` | 55.46938 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (89%) |
| `XRPUSDT` | 1.0158 | 1.104758 | `-8.05%` | `41.97` / `55.85` | `40.8` | `0.283` | `BULLISH_HAMMER` | 0.9845208 | `WATCH` | HOLD |
