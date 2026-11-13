# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T10:13:04Z`
- **Ciclo de ejecucion:** `#307`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general presenta un sesgo predominantemente bajista, con la mayoría de activos cotizando por debajo de su EMA 200 H1 y con pendientes de media negativas. Se ha identificado una oportunidad de entrada SHORT de alta probabilidad en NEARUSDT bajo el Pilar S1 (S1_EMA200_RESISTANCE_REJECT), respaldada por un retest a la zona de resistencia de la EMA 200, Estocástico en zona de sobrecompra (>80) y un patrón de vela BEARISH_ENGULFING. No hay posiciones abiertas actualmente para ajuste dinámico.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `GRAMUSDT` | 1.146 | 1.137801 | `+0.72%` | `49.95` / `42.16` | `42.91` | `0.404` | `NONE` | 1.1039324 | `WATCH` | HOLD |
| `BTCUSDT` | 69469.89 | 74325.914716 | `-6.53%` | `37.11` / `31.35` | `36.43` | `0.329` | `MORNING_STAR` | 67057.42231 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3115 | 0.317564 | `-1.91%` | `10.59` / `7.78` | `25.67` | `0.221` | `BULLISH_ENGULFING` | 0.303401 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 110.99 | 123.996201 | `-10.49%` | `29.05` / `31.87` | `34.3` | `0.236` | `NONE` | 107.703052 | `WATCH` | HOLD |
| `ETHUSDT` | 1955.97 | 2123.43087 | `-7.89%` | `37.39` / `33.03` | `38.75` | `0.339` | `BULLISH_ENGULFING` | 1881.02672 | `WATCH` | HOLD |
| `TIAUSDT` | 0.4162 | 0.429067 | `-3.00%` | `33.48` / `37.03` | `46.93` | `0.34` | `BEARISH_SHOOTING_STAR` | 0.3970548 | `WATCH` | HOLD |
| `SOLUSDT` | 80.46 | 86.097166 | `-6.55%` | `54.91` / `50.23` | `45.52` | `0.463` | `MORNING_STAR` | 77.671144 | `WATCH` | HOLD |
| `ZECUSDT` | 952.01 | 1111.109466 | `-14.32%` | `76.61` / `73.78` | `49.48` | `0.61` | `NONE` | 908.21754 | `WATCH` | HOLD |
| `NBISBUSDT` | 126.45 | 138.601851 | `-8.77%` | `18.5` / `19.4` | `36.59` | `0.308` | `BEARISH_SHOOTING_STAR` | 120.67418 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 640.13 | 680.649048 | `-5.95%` | `38.22` / `30.93` | `39.82` | `0.368` | `MORNING_STAR` | 613.30714 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0792 | 0.078097 | `+1.41%` | `22.74` / `30.88` | `39.42` | `0.248` | `NONE` | 0.0755568 | `WATCH` | HOLD |
| `DODOUSDT` | 0.02856 | 0.023561 | `+21.22%` | `53.44` / `40.92` | `64.44` | `0.793` | `NONE` | 0.02724624 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0274 | 1.11064 | `-7.49%` | `65.59` / `63.58` | `46.8` | `0.511` | `BEARISH_SHOOTING_STAR` | 1.0006876 | `WATCH` | HOLD |
| `UNIUSDT` | 5.808 | 6.655325 | `-12.73%` | `33.91` / `35.56` | `36.76` | `0.287` | `BULLISH_ENGULFING` | 5.55472 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.56e-06 | 5e-06 | `-6.12%` | `44.52` / `51.0` | `51.78` | `0.697` | `BULLISH_HAMMER` | 4.35e-06 | `WATCH` | HOLD |
| `NEARUSDT` | 3.507 | 3.64438 | `-3.77%` | `80.94` / `82.74` | `55.24` | `0.836` | `BEARISH_ENGULFING` | 3.668322 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
