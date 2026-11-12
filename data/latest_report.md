# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T07:33:33Z`
- **Ciclo de ejecucion:** `#210`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un regimen claramente bajista, con la gran mayoria de los activos cotizando por debajo de sus respectivas EMA 200 y experimentando presiones vendedoras en 1H. Los indicadores de oscilacion (Estocastico < 20) muestran condiciones de sobreventa generalizadas, pero sin activarse las confluencias estrictas de los pilares LONG (P1-P4) debido a la falta de soporte estructural firme o pendientes alcistas validas en la EMA 200. Tampoco se cumplen las condiciones para entradas SHORT bajo el Pilar S1 en resistencia (dado que el precio esta lejos de testear la EMA 200 por debajo). Por lo tanto, no se ejecutan nuevas entradas en ningun activo y se mantiene la recomendacion de HOLD para proteger el capital.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.49e-06 | 5e-06 | `-10.08%` | `10.02` / `10.84` | `25.93` | `0.191` | `NONE` | 4.28e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73588.96 | 75419.489111 | `-2.43%` | `9.22` / `14.19` | `42.43` | `0.21` | `BULLISH_ENGULFING` | 71675.64704 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `ETHUSDT` | 2051.06 | 2163.774309 | `-5.21%` | `18.8` / `19.29` | `43.67` | `0.278` | `BULLISH_ENGULFING` | 1997.73244 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `SOLUSDT` | 82.94 | 87.79954 | `-5.53%` | `18.94` / `21.25` | `41.23` | `0.196` | `BULLISH_ENGULFING` | 80.78356 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `UNIUSDT` | 6.164 | 6.874405 | `-10.33%` | `12.07` / `16.72` | `33.18` | `0.189` | `NONE` | 5.9199848 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0452 | 1.135719 | `-7.97%` | `14.12` / `11.55` | `40.46` | `0.203` | `BULLISH_HAMMER` | 1.01775928 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.525 | 3.743946 | `-5.85%` | `6.33` / `5.81` | `37.71` | `0.162` | `NONE` | 3.38725 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.425 | 7.905428 | `-6.08%` | `7.82` / `11.32` | `31.32` | `0.158` | `NONE` | 7.121005 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.143 | 0.15899 | `-10.06%` | `5.16` / `5.58` | `29.91` | `0.182` | `NONE` | 0.1374384 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 674.59 | 691.223502 | `-2.41%` | `10.95` / `7.46` | `38.2` | `0.119` | `BULLISH_ENGULFING` | 657.05066 | `EXIT_SHORT_STOCH_20` | **HOLD** (78%) |
| `HYPEUSDT` | 71.49 | 76.83126 | `-6.95%` | `20.62` / `26.55` | `41.21` | `0.185` | `BULLISH_ENGULFING` | 69.28722 | `WATCH` | HOLD |
| `DOGEUSDT` | 0.06703 | 0.070743 | `-5.25%` | `18.74` / `21.08` | `37.64` | `0.188` | `BULLISH_ENGULFING` | 0.06528722 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1489 | 0.16401 | `-9.21%` | `3.74` / `5.08` | `27.99` | `0.148` | `NONE` | 0.14434146 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 165.02 | 189.374788 | `-12.86%` | `9.25` / `10.64` | `30.59` | `0.202` | `NONE` | 157.42908 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3952.03 | 4026.461985 | `-1.85%` | `12.81` / `16.25` | `25.38` | `0.071` | `NONE` | 3849.27722 | `EXIT_SHORT_STOCH_20` | HOLD |
| `OPGUSDT` | 0.1364 | 0.126237 | `+8.05%` | `22.49` / `15.89` | `51.4` | `0.382` | `BEARISH_SHOOTING_STAR` | 0.1301256 | `EXIT_SHORT_STOCH_20` | **HOLD** (80%) |
