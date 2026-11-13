# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T09:53:05Z`
- **Ciclo de ejecucion:** `#305`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> Mercado predominantemente bajista en H1 con la gran mayoria de los activos cotizando por debajo de sus EMA 200 y registrando retrocesos significativos de 24h. Se identifica una oportunidad de entrada SHORT en BTCUSDT bajo la estrategia M15 Scalper Pullback Bajista. El resto de activos se mantienen en estado de observacion (HOLD) o en zona de salida por sobreventa de Estocastico (Stoch < 20). No existen posiciones abiertas en el portafolio para ajuste dinamico de SL/TP.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 68996.48 | 74399.855086 | `-7.26%` | `28.21` / `26.29` | `29.83` | `0.224` | `NONE` | 70820.11608 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (78%) |
| `ETHUSDT` | 1938.57 | 2126.458106 | `-8.84%` | `30.48` / `28.54` | `30.44` | `0.215` | `BULLISH_ENGULFING` | 1993.440252 | `M15_SCALPER_PULLBACK_SHORT` | **HOLD** (65%) |
| `BNBUSDT` | 636.55 | 681.245467 | `-6.56%` | `28.08` / `24.8` | `35.1` | `0.275` | `BULLISH_HAMMER` | 613.3859 | `WATCH` | **HOLD** (70%) |
| `UNIUSDT` | 5.773 | 6.668887 | `-13.43%` | `34.7` / `34.07` | `33.06` | `0.199` | `NONE` | 5.5647904 | `WATCH` | **HOLD** (75%) |
| `GRAMUSDT` | 1.151 | 1.138039 | `+1.14%` | `46.07` / `33.28` | `44.57` | `0.412` | `BULLISH_ENGULFING` | 1.102168 | `WATCH` | **HOLD** (72%) |
| `ONEUSDT` | 0.001468 | 0.001546 | `-5.03%` | `14.17` / `18.18` | `38.03` | `0.167` | `BEARISH_SHOOTING_STAR` | 0.00140047 | `EXIT_SHORT_STOCH_20` | **HOLD** (80%) |
| `AAVEUSDT` | 110.62 | 124.217995 | `-10.95%` | `30.27` / `31.71` | `31.93` | `0.148` | `NONE` | 107.607508 | `WATCH` | **HOLD** (70%) |
| `TRXUSDT` | 0.3113 | 0.317647 | `-2.00%` | `6.72` / `7.21` | `22.98` | `0.17` | `BULLISH_ENGULFING` | 0.3032062 | `EXIT_SHORT_STOCH_20` | **HOLD** (80%) |
| `ARBUSDT` | 0.1443 | 0.159974 | `-9.80%` | `35.87` / `36.4` | `36.17` | `0.189` | `BEARISH_ENGULFING` | 0.13899582 | `WATCH` | **HOLD** (75%) |
| `HBARUSDT` | 0.06211 | 0.066539 | `-6.66%` | `44.66` / `40.68` | `36.3` | `0.292` | `BEARISH_SHOOTING_STAR` | 0.06039756 | `WATCH` | **HOLD** (70%) |
| `TIAUSDT` | 0.4151 | 0.429346 | `-3.32%` | `37.37` / `38.3` | `46.03` | `0.334` | `BEARISH_ENGULFING` | 0.3960054 | `WATCH` | **HOLD** (68%) |
| `ZECUSDT` | 946.61 | 1113.38291 | `-14.98%` | `71.5` / `68.24` | `47.69` | `0.514` | `BEARISH_SHOOTING_STAR` | 903.06594 | `WATCH` | **HOLD** (70%) |
| `SOLUSDT` | 80.02 | 86.216538 | `-7.19%` | `47.61` / `44.35` | `41.16` | `0.359` | `BEARISH_SHOOTING_STAR` | 77.697532 | `WATCH` | **HOLD** (75%) |
| `NBISBUSDT` | 125.23 | 138.585089 | `-9.64%` | `18.82` / `19.82` | `32.56` | `0.122` | `BEARISH_SHOOTING_STAR` | 120.467134 | `EXIT_SHORT_STOCH_20` | **HOLD** (80%) |
| `ERAUSDT` | 0.0804 | 0.078152 | `+2.88%` | `35.94` / `34.78` | `40.44` | `0.292` | `BEARISH_ENGULFING` | 0.0767016 | `WATCH` | **HOLD** (70%) |
| `DODOUSDT` | 0.02881 | 0.023512 | `+22.53%` | `40.79` / `32.82` | `66.31` | `0.807` | `BULLISH_ENGULFING` | 0.02748474 | `WATCH` | **HOLD** (75%) |
