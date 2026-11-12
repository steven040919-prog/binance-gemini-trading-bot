# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T02:44:58Z`
- **Ciclo de ejecucion:** `#178`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `-100.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra bajo un régimen bajista generalizado con la mayoría de los activos cotizando por debajo de la EMA 200 y con pendientes negativas. No se activan entradas LONG debido a que las condiciones de los pilares principales (P1-P4) no se cumplen plenamente o no hay señales de capitulación extrema simultánea con volumen. Se identifican oportunidades bajistas bajo los criterios de Futuros USDT-M (Pilar S1 y Scalper M15), destacando a NEARUSDT y TAOUSDT con configuraciones de continuación bajista. No hay posiciones abiertas actuales para ajustar.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.6e-06 | 5e-06 | `-8.48%` | `13.58` / `9.09` | `26.29` | `0.179` | `BULLISH_HAMMER` | 4.39e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.205 | 6.912042 | `-10.23%` | `11.77` / `9.14` | `31.49` | `0.08` | `NONE` | 5.91957 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.575 | 3.753376 | `-4.75%` | `23.51` / `23.39` | `40.86` | `0.143` | `NONE` | 3.73945 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (78%) |
| `XRPUSDT` | 1.0514 | 1.140802 | `-7.84%` | `29.65` / `29.5` | `42.44` | `0.143` | `BEARISH_ENGULFING` | 1.02243836 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1516 | 0.164795 | `-8.01%` | `8.6` / `8.02` | `30.82` | `0.072` | `NONE` | 0.1446972 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.516 | 7.930304 | `-5.22%` | `13.51` / `12.08` | `30.85` | `0.082` | `BEARISH_ENGULFING` | 7.170264 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1453 | 0.159971 | `-9.17%` | `20.05` / `19.56` | `33.05` | `0.076` | `BEARISH_ENGULFING` | 0.1386786 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 165.5 | 190.786386 | `-13.25%` | `7.49` / `10.28` | `26.18` | `-0.023` | `BULLISH_HAMMER` | 157.887 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 118.86 | 128.577006 | `-7.56%` | `11.73` / `15.8` | `30.76` | `-0.004` | `NONE` | 114.508148 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3970.14 | 4029.738943 | `-1.48%` | `21.43` / `17.65` | `29.17` | `0.192` | `NONE` | 3866.91636 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LTCUSDT` | 50.06 | 52.199638 | `-4.10%` | `28.17` / `29.13` | `37.55` | `0.071` | `BEARISH_ENGULFING` | 48.698716 | `WATCH` | HOLD |
| `TAOUSDT` | 215.8 | 223.278968 | `-3.35%` | `27.58` / `25.24` | `38.16` | `0.112` | `BEARISH_SHOOTING_STAR` | 223.86976 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (76%) |
| `BTCUSDT` | 73876.65 | 75519.290568 | `-2.18%` | `35.46` / `39.39` | `46.91` | `0.341` | `BEARISH_ENGULFING` | 71955.8571 | `WATCH` | HOLD |
| `PAXGUSDT` | 3971.37 | 4035.338874 | `-1.59%` | `20.08` / `16.78` | `28.15` | `0.186` | `NONE` | 3868.11438 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 993.91 | 1168.583877 | `-14.95%` | `54.29` / `42.21` | `45.38` | `0.607` | `BULLISH_HAMMER` | 948.19014 | `WATCH` | HOLD |
| `ETHUSDT` | 2058.81 | 2170.290152 | `-5.14%` | `31.88` / `30.99` | `45.83` | `0.348` | `BEARISH_ENGULFING` | 2005.28094 | `WATCH` | HOLD |
