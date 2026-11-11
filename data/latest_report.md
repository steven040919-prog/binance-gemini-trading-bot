# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T04:34:50Z`
- **Ciclo de ejecucion:** `#105`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado opera mayoritariamente bajo la EMA 200 en temporalidad 1h con sesgo bajista generalizado. Se identifica al activo RLUSDUSDT activando el Pilar S1 SHORT (S1_EMA200_RESISTANCE_REJECT) cumpliendo con la confluencia de rechazo en la EMA 200, estocástico elevado y vela de giro bajista. No hay posiciones abiertas actuales para aplicar ajuste dinámico de SL/TP, y los candidatos LONG no cumplen estrictamente los criterios institucionales de los Pilares 1-4.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1025.69 | 1214.694933 | `-15.56%` | `15.11` / `14.72` | `32.88` | `0.29` | `BULLISH_HAMMER` | 978.50826 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.716 | 7.003793 | `-4.11%` | `15.91` / `15.95` | `42.27` | `0.364` | `BEARISH_SHOOTING_STAR` | 6.407064 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 180.38 | 194.188827 | `-7.11%` | `42.45` / `42.95` | `33.9` | `0.284` | `NONE` | 173.50708 | `WATCH` | HOLD |
| `XAUTUSDT` | 4035.65 | 4035.530164 | `+0.00%` | `65.64` / `54.08` | `42.6` | `0.506` | `BULLISH_ENGULFING` | 3930.7231 | `WATCH` | HOLD |
| `BTCUSDT` | 73783.75 | 75838.403467 | `-2.71%` | `47.48` / `44.38` | `46.25` | `0.505` | `BULLISH_HAMMER` | 71865.3725 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3175 | 0.318484 | `-0.31%` | `6.25` / `9.37` | `40.98` | `0.207` | `NONE` | 0.309245 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2068.47 | 2194.04128 | `-5.72%` | `60.96` / `53.68` | `47.25` | `0.584` | `BEARISH_SHOOTING_STAR` | 2002.90213 | `WATCH` | HOLD |
| `PAXGUSDT` | 4037.41 | 4041.581913 | `-0.10%` | `66.21` / `55.46` | `42.39` | `0.489` | `BEARISH_SHOOTING_STAR` | 3932.43734 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001723 | 0.00155 | `+11.16%` | `38.17` / `56.94` | `47.6` | `0.085` | `BULLISH_HAMMER` | 0.00164374 | `WATCH` | HOLD |
| `SOLUSDT` | 83.18 | 89.113484 | `-6.66%` | `50.54` / `49.54` | `39.29` | `0.414` | `BEARISH_SHOOTING_STAR` | 80.72368 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0574 | 1.160291 | `-8.87%` | `56.57` / `49.61` | `40.68` | `0.395` | `BEARISH_SHOOTING_STAR` | 1.02003056 | `WATCH` | HOLD |
| `PEPEUSDT` | 5.41e-06 | 5e-06 | `+6.84%` | `56.86` / `58.6` | `57.64` | `0.744` | `BULLISH_ENGULFING` | 5.16e-06 | `M15_SCALPER_PULLBACK_LONG` | HOLD |
| `NEARUSDT` | 3.694 | 3.7703 | `-2.02%` | `74.38` / `69.47` | `58.95` | `0.853` | `BEARISH_SHOOTING_STAR` | 3.524076 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0012 | 1.001206 | `-0.00%` | `79.37` / `82.01` | `54.62` | `0.686` | `BEARISH_SHOOTING_STAR` | 1.0272312 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `BNBUSDT` | 681.46 | 693.425891 | `-1.73%` | `56.39` / `54.32` | `47.79` | `0.515` | `BEARISH_ENGULFING` | 663.74204 | `WATCH` | HOLD |
| `HYPEUSDT` | 72.18 | 78.130176 | `-7.62%` | `39.85` / `38.5` | `42.5` | `0.424` | `BULLISH_ENGULFING` | 69.382268 | `WATCH` | HOLD |
