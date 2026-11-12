# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T22:00:53Z`
- **Ciclo de ejecucion:** `#269`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un regimen claramente bajista (Bearish) en temporalidad 1H, con la gran mayoria de los activos cotizando por debajo de la EMA 200 y con pendientes negativas pronunciadas. Las condiciones de sobreventa generalizadas dominan el estocastico y el RSI, pero sin activarse las confluencias institucionales optimas para entradas LONG (P1 a P4). En el apartado de Futuros USDT-M, se evalua el Pilar S1 y patrones bajistas de alta frecuencia, observando que activos como NBISBUSDT muestran configuraciones de scalping bajista (M15_SCALPER_PULLBACK_SHORT), sin embargo, al no haber posiciones abiertas previas, la cartera se mantiene en modo de observacion (HOLD) esperando quiebres de soporte o formaciones de mayor confluencia para proteger el capital.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 71525.51 | 75029.460944 | `-4.67%` | `10.51` / `12.7` | `25.39` | `0.201` | `NONE` | 69665.84674 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `ZECUSDT` | 941.89 | 1134.605073 | `-16.99%` | `23.15` / `27.54` | `34.59` | `0.111` | `NONE` | 899.44495 | `WATCH` | HOLD |
| `NBISBUSDT` | 129.25 | 140.739539 | `-8.16%` | `22.72` / `21.56` | `34.09` | `0.283` | `BEARISH_SHOOTING_STAR` | 135.1955 | `M15_SCALPER_PULLBACK_SHORT` | **HOLD** (70%) |
| `SOLUSDT` | 81.35 | 87.032288 | `-6.53%` | `29.39` / `32.28` | `34.73` | `0.223` | `NONE` | 79.2349 | `WATCH` | HOLD |
| `NEARUSDT` | 3.397 | 3.693627 | `-8.03%` | `37.82` / `40.87` | `34.38` | `0.243` | `BEARISH_ENGULFING` | 3.291693 | `WATCH` | HOLD |
| `UNIUSDT` | 6.0 | 6.764893 | `-11.31%` | `30.16` / `33.09` | `30.6` | `0.215` | `NONE` | 5.8356 | `WATCH` | HOLD |
| `BNBUSDT` | 654.06 | 686.850884 | `-4.77%` | `17.52` / `18.82` | `25.47` | `0.246` | `BEARISH_SHOOTING_STAR` | 637.05444 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3876.02 | 4009.693218 | `-3.33%` | `22.58` / `22.39` | `28.49` | `0.265` | `NONE` | 3775.24348 | `WATCH` | HOLD |
| `ENAUSDT` | 0.1402 | 0.156311 | `-10.31%` | `57.04` / `51.93` | `34.91` | `0.396` | `BEARISH_SHOOTING_STAR` | 0.13460144 | `WATCH` | HOLD |
| `AAVEUSDT` | 113.86 | 125.898277 | `-9.56%` | `49.44` / `45.01` | `35.25` | `0.367` | `BEARISH_SHOOTING_STAR` | 110.336272 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.14 | 1.138313 | `+0.15%` | `12.98` / `10.35` | `37.38` | `0.125` | `BEARISH_SHOOTING_STAR` | 1.08756 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ERAUSDT` | 0.0807 | 0.077768 | `+3.77%` | `2.17` / `5.03` | `37.24` | `0.057` | `NONE` | 0.0769878 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AVAXUSDT` | 8.312 | 8.441541 | `-1.53%` | `18.78` / `20.3` | `38.14` | `0.231` | `BEARISH_ENGULFING` | 8.0955376 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 163.45 | 185.964865 | `-12.11%` | `37.84` / `31.09` | `38.82` | `0.421` | `BULLISH_ENGULFING` | 157.22568 | `WATCH` | HOLD |
| `INJUSDT` | 7.423 | 7.840458 | `-5.32%` | `47.98` / `47.28` | `41.99` | `0.436` | `BEARISH_SHOOTING_STAR` | 7.1712176 | `WATCH` | HOLD |
| `PAXGUSDT` | 3877.18 | 4014.219787 | `-3.41%` | `21.98` / `22.56` | `27.28` | `0.257` | `NONE` | 3776.37332 | `WATCH` | HOLD |
