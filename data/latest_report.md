# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T09:48:33Z`
- **Ciclo de ejecucion:** `#125`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global opera mayoritariamente bajo la EMA 200 en temporalidad de 1H con un régimen bajista generalizado. No obstante, INITUSDT activa el Pilar 1 LONG (P1_EMA200_PULLBACK) al mantenerse sobre la EMA 200 con retroceso alcista en estocástico y vela envolvente alcista. El resto de candidatos se encuentran en zonas neutrales o bajo resistencia, sin cumplir los estrictos filtros de entrada de los pilares LONG o el pilar SHORT de futuros (S1). No hay posiciones abiertas previas que requieran ajuste dinámico.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 979.19 | 1204.352882 | `-18.70%` | `19.02` / `18.81` | `31.26` | `0.197` | `BEARISH_ENGULFING` | 934.14726 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001551 | 0.001555 | `-0.28%` | `6.28` / `11.29` | `37.85` | `-0.077` | `NONE` | 0.00147965 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.37 | 6.97923 | `-8.73%` | `10.85` / `12.02` | `25.52` | `0.012` | `BEARISH_ENGULFING` | 6.120872 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PEPEUSDT` | 5.02e-06 | 5e-06 | `-0.97%` | `11.95` / `19.59` | `34.96` | `-0.079` | `NONE` | 4.79e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INITUSDT` | 0.2174 | 0.171527 | `+26.74%` | `20.38` / `20.0` | `44.87` | `0.029` | `BULLISH_ENGULFING` | 0.2073996 | `P1_EMA200_PULLBACK` | **BUY** (88%) |
| `QNTUSDT` | 178.97 | 193.532906 | `-7.52%` | `23.44` / `29.74` | `36.76` | `0.194` | `BEARISH_ENGULFING` | 172.673132 | `WATCH` | HOLD |
| `BTCUSDT` | 73679.56 | 75736.28342 | `-2.72%` | `66.56` / `74.53` | `45.82` | `0.516` | `NONE` | 71763.89144 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3177 | 0.3183 | `-0.19%` | `23.08` / `24.34` | `45.32` | `0.38` | `BULLISH_ENGULFING` | 0.3094398 | `WATCH` | HOLD |
| `ETHUSDT` | 2054.36 | 2187.591061 | `-6.09%` | `64.71` / `74.83` | `42.96` | `0.522` | `NONE` | 2000.94664 | `WATCH` | HOLD |
| `CYBERUSDT` | 0.265 | 0.281371 | `-5.82%` | `5.06` / `4.6` | `42.24` | `0.207` | `BEARISH_ENGULFING` | 0.25281 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 83.43 | 88.833689 | `-6.08%` | `55.32` / `53.24` | `46.8` | `0.679` | `BULLISH_ENGULFING` | 80.78826 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0866 | 0.073311 | `+18.13%` | `41.65` / `56.08` | `60.64` | `0.852` | `BULLISH_HAMMER` | 0.0826164 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0582 | 1.155387 | `-8.41%` | `46.25` / `46.33` | `43.92` | `0.536` | `BULLISH_HAMMER` | 1.0306868 | `WATCH` | HOLD |
| `NEARUSDT` | 3.608 | 3.770713 | `-4.32%` | `41.62` / `49.27` | `48.89` | `0.494` | `BEARISH_ENGULFING` | 3.442032 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.001 | 1.001202 | `-0.02%` | `40.0` / `49.52` | `42.68` | `0.338` | `BULLISH_HAMMER` | 0.974974 | `WATCH` | HOLD |
| `BNBUSDT` | 679.32 | 693.14556 | `-1.99%` | `64.13` / `66.1` | `45.25` | `0.508` | `NONE` | 661.65768 | `WATCH` | HOLD |
