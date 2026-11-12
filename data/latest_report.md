# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T04:04:00Z`
- **Ciclo de ejecucion:** `#188`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global opera mayoritariamente bajo un régimen bajista (por debajo de la EMA 200 en la mayoría de los activos). Destaca OPGUSDT cumpliendo las condiciones del Pilar 1 LONG (PULLBACK DE VALOR SOBRE EMA 200) con tendencia primaria alcista, precio en zona de valor, estocástico girando al alza y patrón BULLISH_HAMMER. Para los activos restantes en tendencia bajista, se prioriza la gestión de riesgo sin aperturas en falso.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.57e-06 | 5e-06 | `-8.89%` | `15.43` / `14.81` | `25.75` | `0.192` | `NONE` | 4.78e-06 | `M15_SCALPER_PULLBACK_SHORT` | HOLD |
| `UNIUSDT` | 6.231 | 6.895837 | `-9.64%` | `21.99` / `16.99` | `34.19` | `0.19` | `BULLISH_HAMMER` | 5.944374 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001444 | 0.001547 | `-6.67%` | `4.26` / `5.84` | `30.36` | `0.106` | `NONE` | 0.00137758 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.555 | 3.751725 | `-5.24%` | `11.11` / `16.69` | `39.09` | `0.127` | `BULLISH_HAMMER` | 3.422974 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0494 | 1.138828 | `-7.85%` | `21.44` / `23.95` | `41.45` | `0.151` | `BEARISH_ENGULFING` | 1.01942308 | `WATCH` | HOLD |
| `INJUSDT` | 7.57 | 7.923525 | `-4.46%` | `21.32` / `17.55` | `34.82` | `0.194` | `BULLISH_HAMMER` | 7.22178 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.15 | 0.164485 | `-8.81%` | `7.19` / `8.22` | `28.77` | `0.091` | `BEARISH_ENGULFING` | 0.14497 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1441 | 0.159637 | `-9.73%` | `11.66` / `14.84` | `30.07` | `0.11` | `BEARISH_ENGULFING` | 0.13818358 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 678.81 | 691.691417 | `-1.86%` | `18.41` / `20.75` | `42.83` | `0.188` | `NONE` | 661.16094 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 165.39 | 190.202922 | `-13.05%` | `11.66` / `9.69` | `26.55` | `0.096` | `BEARISH_SHOOTING_STAR` | 157.78206 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LINKUSDT` | 10.122 | 10.725887 | `-5.63%` | `19.17` / `20.96` | `34.74` | `0.123` | `BEARISH_ENGULFING` | 9.8259012 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 118.93 | 128.273659 | `-7.28%` | `14.3` / `12.56` | `31.83` | `0.12` | `BEARISH_SHOOTING_STAR` | 114.744034 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INTCBUSDT` | 60.85 | 59.191248 | `+2.80%` | `26.76` / `30.61` | `47.7` | `0.244` | `BEARISH_SHOOTING_STAR` | 58.67365 | `WATCH` | HOLD |
| `XAUTUSDT` | 3976.97 | 4028.544904 | `-1.28%` | `21.86` / `21.64` | `32.67` | `0.291` | `NONE` | 3873.56878 | `WATCH` | HOLD |
| `SUIUSDT` | 0.8204 | 0.853182 | `-3.84%` | `25.09` / `25.04` | `40.78` | `0.187` | `BULLISH_HAMMER` | 0.79769488 | `WATCH` | HOLD |
| `OPGUSDT` | 0.1331 | 0.126143 | `+5.51%` | `5.13` / `5.02` | `45.32` | `0.262` | `BULLISH_HAMMER` | 0.1269774 | `P1_EMA200_PULLBACK` | **BUY** (88%) |
