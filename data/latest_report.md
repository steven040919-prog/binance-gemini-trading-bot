# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T10:32:49Z`
- **Ciclo de ejecucion:** `#309`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general mantiene un sesgo marcadamente bajista con los principales activos (BTC, ETH, SOL, BNB) cotizando por debajo de la EMA 200 con pendientes negativas. Se detecta una oportunidad clara de entrada SHORT en NEARUSDT bajo el Pilar S1 (Rechazo en Resistencia EMA 200) tras confirmar patron BEARISH_ENGULFING y giro del oscilador. No se registraron posiciones abiertas activas para gestion dinamica de Stop-Loss.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `UNIUSDT` | 5.778 | 6.655027 | `-13.18%` | `31.75` / `34.84` | `33.72` | `0.237` | `BEARISH_SHOOTING_STAR` | 5.5523032 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.144 | 1.137781 | `+0.55%` | `48.29` / `41.61` | `42.31` | `0.392` | `NONE` | 1.1037648 | `WATCH` | HOLD |
| `BTCUSDT` | 69281.23 | 74324.037502 | `-6.78%` | `35.56` / `30.83` | `33.91` | `0.296` | `MORNING_STAR` | 67061.38417 | `WATCH` | **HOLD** (75%) |
| `AAVEUSDT` | 110.6 | 123.99232 | `-10.80%` | `26.79` / `31.11` | `31.82` | `0.179` | `BEARISH_SHOOTING_STAR` | 107.66864 | `WATCH` | HOLD |
| `TRXUSDT` | 0.312 | 0.317569 | `-1.75%` | `13.73` / `8.82` | `31.85` | `0.273` | `BULLISH_ENGULFING` | 0.303888 | `EXIT_SHORT_STOCH_20` | **HOLD** (70%) |
| `ETHUSDT` | 1950.08 | 2123.372263 | `-8.16%` | `35.84` / `32.52` | `36.13` | `0.305` | `BULLISH_ENGULFING` | 1881.16808 | `WATCH` | HOLD |
| `TIAUSDT` | 0.4193 | 0.429097 | `-2.28%` | `35.76` / `37.79` | `49.3` | `0.407` | `BEARISH_SHOOTING_STAR` | 0.4000122 | `WATCH` | HOLD |
| `ZECUSDT` | 944.3 | 1111.03275 | `-15.01%` | `73.63` / `72.78` | `46.98` | `0.5` | `BEARISH_SHOOTING_STAR` | 900.8622 | `WATCH` | HOLD |
| `SOLUSDT` | 80.41 | 86.096669 | `-6.60%` | `54.48` / `50.09` | `45.05` | `0.453` | `MORNING_STAR` | 77.656242 | `WATCH` | HOLD |
| `BNBUSDT` | 638.26 | 680.630441 | `-6.23%` | `36.5` / `30.35` | `37.4` | `0.329` | `MORNING_STAR` | 613.220628 | `WATCH` | HOLD |
| `NBISBUSDT` | 125.2 | 138.589413 | `-9.66%` | `12.76` / `17.49` | `32.72` | `0.161` | `BEARISH_SHOOTING_STAR` | 120.6636 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ERAUSDT` | 0.0778 | 0.078083 | `-0.36%` | `16.67` / `28.85` | `36.36` | `0.17` | `BEARISH_SHOOTING_STAR` | 0.0742212 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DODOUSDT` | 0.02918 | 0.023567 | `+23.82%` | `58.63` / `42.65` | `67.96` | `0.939` | `NONE` | 0.02783772 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0258 | 1.110624 | `-7.64%` | `64.44` / `63.2` | `45.6` | `0.471` | `BEARISH_SHOOTING_STAR` | 0.9991292 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.52e-06 | 5e-06 | `-6.93%` | `39.59` / `49.35` | `47.56` | `0.575` | `BULLISH_HAMMER` | 4.31e-06 | `WATCH` | HOLD |
| `NEARUSDT` | 3.476 | 3.644071 | `-4.61%` | `77.48` / `81.59` | `51.99` | `0.722` | `BEARISH_ENGULFING` | 3.635896 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (82%) |
