# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T14:52:15Z`
- **Ciclo de ejecucion:** `#336`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de criptomonedas en temporalidad 1H mantiene un sesgo general bajista, con la mayoría de los activos cotizando por debajo de la EMA 200. Se identifican oportunidades institucionales bajo el Pilar S1 SHORT en Futuros USDT-M (ZECUSDT y HYPEUSDT) debido al rechazo bajista en la resistencia de la EMA 200 con sobrecompra en el estocástico y patrones de vela bajista. No hay posiciones abiertas actuales para ajuste.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.0775 | 0.077899 | `-0.51%` | `22.61` / `17.37` | `38.2` | `0.144` | `BULLISH_ENGULFING` | 0.073935 | `EXIT_SHORT_STOCH_20` | HOLD |
| `GRAMUSDT` | 1.129 | 1.137293 | `-0.73%` | `42.47` / `51.62` | `38.39` | `-0.02` | `BEARISH_ENGULFING` | 1.077066 | `WATCH` | HOLD |
| `BTCUSDT` | 69011.74 | 74095.705448 | `-6.86%` | `43.68` / `43.89` | `34.36` | `0.317` | `BULLISH_ENGULFING` | 67217.43476 | `WATCH` | HOLD |
| `ETHUSDT` | 1952.81 | 2115.567673 | `-7.69%` | `51.34` / `50.84` | `39.29` | `0.379` | `BEARISH_SHOOTING_STAR` | 1895.784692 | `WATCH` | HOLD |
| `MUBUSDT` | 781.44 | 763.195307 | `+2.39%` | `17.12` / `27.4` | `41.76` | `0.047` | `BEARISH_SHOOTING_STAR` | 752.834528 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INTCBUSDT` | 59.43 | 59.335541 | `+0.16%` | `20.54` / `32.52` | `36.63` | `-0.163` | `BEARISH_SHOOTING_STAR` | 57.507846 | `WATCH` | HOLD |
| `ZECUSDT` | 959.71 | 1097.784345 | `-12.58%` | `78.67` / `82.76` | `51.6` | `0.679` | `BEARISH_SHOOTING_STAR` | 1003.85666 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `DODOUSDT` | 0.0282 | 0.023743 | `+18.77%` | `64.07` / `69.54` | `57.77` | `0.579` | `NONE` | 0.0269028 | `WATCH` | HOLD |
| `SOLUSDT` | 80.93 | 85.765482 | `-5.64%` | `72.94` / `72.04` | `49.76` | `0.602` | `NONE` | 78.393448 | `WATCH` | HOLD |
| `NEARUSDT` | 3.554 | 3.631986 | `-2.15%` | `82.99` / `86.18` | `57.69` | `0.819` | `BULLISH_ENGULFING` | 3.390516 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 639.45 | 678.739466 | `-5.79%` | `52.79` / `50.89` | `40.62` | `0.412` | `BEARISH_SHOOTING_STAR` | 622.8243 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0342 | 1.107462 | `-6.62%` | `67.86` / `60.28` | `53.46` | `0.692` | `BULLISH_ENGULFING` | 0.98985184 | `WATCH` | HOLD |
| `INJUSDT` | 8.194 | 7.78312 | `+5.28%` | `91.9` / `92.99` | `76.4` | `1.116` | `NONE` | 7.817076 | `EXIT_LONG_STOCH_80` | HOLD |
| `PEPEUSDT` | 4.51e-06 | 5e-06 | `-6.96%` | `43.21` / `39.92` | `46.8` | `0.355` | `BEARISH_SHOOTING_STAR` | 4.3e-06 | `WATCH` | HOLD |
| `HYPEUSDT` | 74.0 | 75.241694 | `-1.65%` | `81.75` / `88.39` | `63.11` | `0.873` | `BEARISH_SHOOTING_STAR` | 77.404 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (82%) |
| `UNIUSDT` | 5.926 | 6.613378 | `-10.39%` | `56.69` / `47.56` | `48.34` | `0.56` | `BULLISH_HAMMER` | 5.653404 | `WATCH` | HOLD |
