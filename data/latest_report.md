# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T10:20:06Z`
- **Ciclo de ejecucion:** `#127`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> Evaluación institucional de mercado 1H. El régimen general se mantiene BEARISH con el grueso de activos cotizando por debajo de la EMA 200 y con baja volatilidad direccional en el portafolio actual. No se cumplen los requisitos estrictos de los Pilares LONG (P1-P4) ni del Pilar SHORT (S1) ya que las condiciones simultáneas de sobreventa/sobrecompra extrema, giros de estocástico y patrones de vela confirmados no se alinean en este ciclo horario. Las posiciones abiertas en el portfolio se encuentran vacías, por lo que no se requieren ajustes dinámicos de SL/TP (action: ADJUST). Se prioriza la preservación de capital y se emite HOLD en los principales pares evaluados.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 987.24 | 1202.736481 | `-17.92%` | `15.83` / `17.11` | `33.87` | `0.185` | `NONE` | 941.82696 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001558 | 0.001557 | `+0.07%` | `5.88` / `7.11` | `38.29` | `0.02` | `NONE` | 0.00148633 | `EXIT_SHORT_STOCH_20` | HOLD |
| `PEPEUSDT` | 5.04e-06 | 5e-06 | `-0.52%` | `11.15` / `13.24` | `35.79` | `-0.005` | `BULLISH_HAMMER` | 4.81e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.423 | 6.975531 | `-7.92%` | `11.36` / `11.32` | `29.56` | `0.079` | `BULLISH_HAMMER` | 6.1293256 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INITUSDT` | 0.20626 | 0.17164 | `+20.17%` | `16.93` / `18.43` | `43.43` | `0.029` | `BEARISH_ENGULFING` | 0.19677204 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1586 | 0.166147 | `-4.54%` | `15.8` / `19.51` | `37.66` | `0.284` | `BULLISH_HAMMER` | 0.15325168 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 177.53 | 193.524619 | `-8.26%` | `15.54` / `21.96` | `34.41` | `0.01` | `NONE` | 172.672762 | `EXIT_SHORT_STOCH_20` | HOLD |
| `TRXUSDT` | 0.3178 | 0.31808 | `-0.09%` | `25.64` / `23.93` | `47.19` | `0.457` | `BULLISH_ENGULFING` | 0.3095372 | `WATCH` | HOLD |
| `BTCUSDT` | 73782.53 | 75731.449398 | `-2.57%` | `57.47` / `66.75` | `47.43` | `0.64` | `BULLISH_HAMMER` | 71864.18422 | `WATCH` | **HOLD** (75%) |
| `CYBERUSDT` | 0.266 | 0.281153 | `-5.39%` | `6.51` / `5.78` | `43.04` | `0.246` | `NONE` | 0.253764 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2056.46 | 2186.653719 | `-5.95%` | `52.67` / `64.98` | `43.67` | `0.583` | `BULLISH_HAMMER` | 2002.99204 | `WATCH` | HOLD |
| `ERAUSDT` | 0.0862 | 0.073411 | `+17.42%` | `42.49` / `45.02` | `60.21` | `0.804` | `BULLISH_ENGULFING` | 0.0822348 | `WATCH` | HOLD |
| `SOLUSDT` | 83.51 | 88.799474 | `-5.96%` | `60.3` / `55.08` | `47.54` | `0.776` | `BULLISH_ENGULFING` | 81.33874 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0575 | 1.154665 | `-8.42%` | `50.69` / `46.93` | `43.64` | `0.522` | `BULLISH_ENGULFING` | 1.030005 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.214 | 1.111517 | `+9.22%` | `89.13` / `84.17` | `78.56` | `1.196` | `NONE` | 1.158156 | `EXIT_LONG_STOCH_80` | HOLD |
| `RLUSDUSDT` | 1.0009 | 1.001199 | `-0.03%` | `26.67` / `39.68` | `38.24` | `0.182` | `NONE` | 0.9748766 | `WATCH` | HOLD |
