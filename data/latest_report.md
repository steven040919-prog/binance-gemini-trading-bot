# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T04:02:49Z`
- **Ciclo de ejecucion:** `#187`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `-100.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de criptomonedas se encuentra en un régimen bajista generalizado en temporalidad de 1H con la mayoría de los activos cotizando por debajo de la EMA 200 y con pendientes negativas. No se activan entradas LONG (P1-P4) debido a que no se cumplen los requisitos estrictos de valor y tendencia alcista en los pilares. Tampoco se activan entradas SHORT (S1) ya que los activos evaluados no están testeando la EMA 200 por debajo con rechazo institucional, sino que se encuentran en zonas de sobreventa profunda y rebotes menores tras caídas recientes. No hay posiciones abiertas reportadas en el portafolio para realizar ajustes dinámicos de SL/TP, por lo que el estado general es de observación (HOLD) con una exposición del 0%.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.58e-06 | 5e-06 | `-8.69%` | `16.05` / `15.02` | `26.92` | `0.204` | `BULLISH_HAMMER` | 4.37e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `UNIUSDT` | 6.235 | 6.895877 | `-9.58%` | `22.22` / `17.06` | `34.54` | `0.196` | `BULLISH_HAMMER` | 5.94819 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001442 | 0.001547 | `-6.80%` | `3.89` / `5.72` | `30.15` | `0.096` | `NONE` | 0.00137567 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.56 | 3.751775 | `-5.11%` | `11.7` / `16.88` | `39.55` | `0.14` | `BULLISH_HAMMER` | 3.42352 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.049 | 1.138824 | `-7.89%` | `21.11` / `23.84` | `41.07` | `0.139` | `BEARISH_ENGULFING` | 1.0194318 | `WATCH` | HOLD |
| `INJUSDT` | 7.565 | 7.923475 | `-4.52%` | `21.08` / `17.47` | `34.44` | `0.188` | `BULLISH_HAMMER` | 7.21701 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1503 | 0.164488 | `-8.63%` | `7.91` / `8.46` | `29.49` | `0.106` | `BEARISH_ENGULFING` | 0.1449904 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1443 | 0.159639 | `-9.61%` | `12.12` / `15.0` | `31.06` | `0.121` | `BEARISH_ENGULFING` | 0.13817634 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 678.91 | 691.692412 | `-1.85%` | `18.68` / `20.84` | `43.06` | `0.195` | `NONE` | 661.25834 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 165.72 | 190.206206 | `-12.87%` | `12.23` / `9.88` | `26.95` | `0.108` | `BEARISH_SHOOTING_STAR` | 158.09688 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LINKUSDT` | 10.125 | 10.725917 | `-5.60%` | `19.35` / `21.02` | `35.04` | `0.128` | `BEARISH_ENGULFING` | 9.825825 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INTCBUSDT` | 60.88 | 59.191547 | `+2.85%` | `27.0` / `30.69` | `47.96` | `0.25` | `NONE` | 58.67272 | `WATCH` | HOLD |
| `AAVEUSDT` | 119.08 | 128.275151 | `-7.17%` | `14.98` / `12.79` | `32.89` | `0.135` | `BEARISH_SHOOTING_STAR` | 114.740104 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3977.08 | 4028.545998 | `-1.28%` | `21.94` / `21.66` | `32.76` | `0.292` | `NONE` | 3873.67592 | `WATCH` | HOLD |
| `SUIUSDT` | 0.8206 | 0.853184 | `-3.82%` | `25.24` / `25.09` | `41.02` | `0.192` | `BULLISH_HAMMER` | 0.79769032 | `WATCH` | HOLD |
| `LTCUSDT` | 50.09 | 52.125544 | `-3.91%` | `26.4` / `25.86` | `38.3` | `0.165` | `BULLISH_HAMMER` | 48.78766 | `WATCH` | HOLD |
