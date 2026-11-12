# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T15:41:06Z`
- **Ciclo de ejecucion:** `#236`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado muestra un claro régimen bajista macro con precios operando por debajo de la EMA 200 en H1 y pendientes negativas acentuadas. La mayoría de las altcoins presentan sobreventa en el Oscilador Estocástico pero carecen de la confluencia de volumen/divergencia requerida por los Pilares LONG (P1-P4). Se valida una única señal de entrada SHORT en AAVEUSDT por el pilar M15_SCALPER_PULLBACK_SHORT, aprovechando la estructura bajista intradiaria.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71451.93 | 75214.567425 | `-5.00%` | `11.04` / `11.78` | `18.39` | `-0.13` | `NONE` | 69594.17982 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `ETHUSDT` | 2001.12 | 2153.244024 | `-7.06%` | `26.23` / `23.99` | `24.37` | `-0.025` | `BULLISH_HAMMER` | 1949.09088 | `WATCH` | **HOLD** (70%) |
| `PEPEUSDT` | 4.34e-06 | 5e-06 | `-12.36%` | `23.96` / `22.37` | `24.64` | `0.102` | `BULLISH_ENGULFING` | 4.14e-06 | `WATCH` | **HOLD** (65%) |
| `NEARUSDT` | 3.384 | 3.712394 | `-8.85%` | `17.65` / `13.58` | `29.91` | `0.109` | `BULLISH_ENGULFING` | 3.2340656 | `EXIT_SHORT_STOCH_20` | **HOLD** (70%) |
| `SOLUSDT` | 81.16 | 87.330291 | `-7.07%` | `22.64` / `18.44` | `27.74` | `0.02` | `BULLISH_HAMMER` | 78.99912 | `EXIT_SHORT_STOCH_20` | **HOLD** (70%) |
| `ZECUSDT` | 957.09 | 1143.539746 | `-16.30%` | `26.46` / `30.84` | `36.08` | `-0.043` | `BEARISH_SHOOTING_STAR` | 913.06386 | `WATCH` | **HOLD** (75%) |
| `UNIUSDT` | 5.956 | 6.808122 | `-12.52%` | `20.76` / `17.76` | `25.1` | `0.077` | `BULLISH_ENGULFING` | 5.7481288 | `EXIT_SHORT_STOCH_20` | **HOLD** (65%) |
| `XRPUSDT` | 1.0233 | 1.12823 | `-9.30%` | `21.76` / `20.7` | `29.14` | `-0.039` | `BULLISH_HAMMER` | 0.9966942 | `WATCH` | **HOLD** (70%) |
| `ENAUSDT` | 0.138 | 0.157238 | `-12.23%` | `22.12` / `17.72` | `21.43` | `0.093` | `NONE` | 0.13266 | `EXIT_SHORT_STOCH_20` | **HOLD** (65%) |
| `BNBUSDT` | 652.65 | 688.671418 | `-5.23%` | `10.48` / `8.89` | `16.9` | `0.004` | `BULLISH_HAMMER` | 635.6811 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `DOGEUSDT` | 0.06512 | 0.070372 | `-7.46%` | `21.62` / `20.64` | `23.65` | `-0.022` | `BULLISH_HAMMER` | 0.06320458 | `WATCH` | **HOLD** (70%) |
| `AAVEUSDT` | 112.71 | 126.710754 | `-11.05%` | `20.73` / `13.5` | `26.92` | `0.135` | `BULLISH_ENGULFING` | 116.602834 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (83%) |
| `SUIUSDT` | 0.789 | 0.847481 | `-6.90%` | `19.85` / `16.94` | `24.43` | `0.002` | `BULLISH_HAMMER` | 0.765042 | `EXIT_SHORT_STOCH_20` | **HOLD** (70%) |
| `ARBUSDT` | 0.1454 | 0.162734 | `-10.65%` | `30.09` / `22.4` | `24.39` | `0.152` | `BEARISH_SHOOTING_STAR` | 0.1387116 | `WATCH` | **HOLD** (65%) |
| `XAUTUSDT` | 3865.8 | 4017.799783 | `-3.78%` | `6.37` / `9.38` | `18.41` | `-0.075` | `BULLISH_HAMMER` | 3765.2892 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `LINKUSDT` | 9.901 | 10.62848 | `-6.84%` | `26.1` / `21.53` | `27.92` | `0.131` | `BULLISH_HAMMER` | 9.5739602 | `WATCH` | **HOLD** (70%) |
