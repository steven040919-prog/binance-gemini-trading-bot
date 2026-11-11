# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T22:38:23Z`
- **Ciclo de ejecucion:** `#161`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un regimen bajista generalizado con la mayoria de los activos cotizando por debajo de la EMA 200. Se evalua y activa la entrada SHORT (S1_EMA200_RESISTANCE_REJECT) en BTCUSDT tras rechazo bajista en la zona de resistencia con patron BEARISH_ENGULFING. No hay posiciones abiertas previas para gestion dinamica.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.67e-06 | 5e-06 | `-7.50%` | `4.01` / `3.48` | `21.31` | `0.079` | `BEARISH_SHOOTING_STAR` | 4.46e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 986.0 | 1176.074934 | `-16.16%` | `49.01` / `54.88` | `39.9` | `0.353` | `BEARISH_SHOOTING_STAR` | 940.644 | `WATCH` | HOLD |
| `UNIUSDT` | 6.39 | 6.928086 | `-7.77%` | `40.23` / `53.5` | `34.84` | `0.15` | `NONE` | 6.16991 | `WATCH` | HOLD |
| `HYPEUSDT` | 72.13 | 77.277822 | `-6.66%` | `41.15` / `52.06` | `42.94` | `0.285` | `NONE` | 70.201176 | `WATCH` | HOLD |
| `ENAUSDT` | 0.1478 | 0.160553 | `-7.94%` | `9.35` / `15.47` | `35.37` | `-0.16` | `NONE` | 0.14245216 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1549 | 0.165365 | `-6.33%` | `7.44` / `14.87` | `33.2` | `-0.069` | `NONE` | 0.14962202 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06801 | 0.071072 | `-4.31%` | `39.84` / `49.05` | `43.37` | `0.275` | `BEARISH_ENGULFING` | 0.06624174 | `WATCH` | HOLD |
| `OPGUSDT` | 0.1355 | 0.125701 | `+7.80%` | `24.26` / `31.75` | `48.34` | `0.43` | `BEARISH_ENGULFING` | 0.129267 | `WATCH` | HOLD |
| `INJUSDT` | 7.796 | 7.955082 | `-2.00%` | `9.35` / `15.98` | `38.58` | `0.19` | `NONE` | 7.5498832 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74177.99 | 75572.435232 | `-1.85%` | `72.84` / `77.59` | `51.12` | `0.607` | `BEARISH_ENGULFING` | 76106.61774 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (88%) |
| `XAUTUSDT` | 3983.76 | 4031.866021 | `-1.19%` | `6.75` / `4.74` | `25.38` | `0.198` | `BULLISH_ENGULFING` | 3880.18224 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LINKUSDT` | 10.247 | 10.750779 | `-4.69%` | `30.36` / `47.43` | `38.35` | `-0.006` | `NONE` | 9.980578 | `WATCH` | HOLD |
| `WLDUSDT` | 0.3118 | 0.336247 | `-7.27%` | `31.0` / `38.81` | `43.97` | `0.256` | `BEARISH_ENGULFING` | 0.30190724 | `WATCH` | HOLD |
| `LTCUSDT` | 50.39 | 52.26142 | `-3.58%` | `24.23` / `37.37` | `38.22` | `-0.086` | `BEARISH_ENGULFING` | 49.07986 | `WATCH` | HOLD |
| `TAOUSDT` | 217.9 | 223.419004 | `-2.47%` | `17.97` / `33.03` | `41.77` | `0.14` | `NONE` | 212.2346 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 121.52 | 128.964986 | `-5.77%` | `16.22` / `28.74` | `36.3` | `-0.117` | `NONE` | 118.36048 | `EXIT_SHORT_STOCH_20` | HOLD |
