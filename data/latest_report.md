# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T03:13:56Z`
- **Ciclo de ejecucion:** `#181`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `-100.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado cripto mantiene un régimen claramente bajista con la gran mayoría de los activos operando por debajo de la EMA 200 en temporalidad de 1H y pendientes negativas. Se identifican oportunidades de capitulación extrema y patrones de giro alcista en soportes clave (Pilar P2) como en ARBUSDT y QNTUSDT, activando órdenes LONG. Asimismo, activos como ETHUSDT, SOLUSDT y SUIUSDT presentan oportunidades en cortos bajo el Pilar M15_SCALPER_PULLBACK_SHORT. No hay posiciones abiertas previas que requieran ajuste dinámico de SL/TP en este ciclo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.59e-06 | 5e-06 | `-8.63%` | `16.05` / `12.75` | `26.54` | `0.183` | `BEARISH_SHOOTING_STAR` | 4.38e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73742.28 | 75522.731385 | `-2.36%` | `25.63` / `32.72` | `44.62` | `0.254` | `BEARISH_SHOOTING_STAR` | 71824.98072 | `WATCH` | HOLD |
| `ETHUSDT` | 2053.2 | 2169.576483 | `-5.36%` | `27.09` / `29.78` | `43.35` | `0.251` | `NONE` | 2106.5832 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (80%) |
| `UNIUSDT` | 6.21 | 6.907051 | `-10.09%` | `14.85` / `11.75` | `32.86` | `0.127` | `BULLISH_ENGULFING` | 5.92434 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.558 | 3.753972 | `-5.22%` | `15.79` / `21.13` | `39.39` | `0.121` | `NONE` | 3.4256236 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 83.19 | 88.079494 | `-5.55%` | `29.05` / `31.3` | `42.37` | `0.191` | `BEARISH_SHOOTING_STAR` | 85.683628 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (80%) |
| `XRPUSDT` | 1.0458 | 1.139823 | `-8.25%` | `19.1` / `26.3` | `38.87` | `0.004` | `BEARISH_SHOOTING_STAR` | 1.0186092 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.456 | 7.929198 | `-5.97%` | `12.21` / `13.02` | `29.65` | `0.034` | `BULLISH_ENGULFING` | 7.1390752 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1508 | 0.164689 | `-8.43%` | `9.59` / `8.44` | `30.03` | `0.076` | `BULLISH_ENGULFING` | 0.14481408 | `P2_EXTREME_CAPITULATION` | **BUY** (85%) |
| `ENAUSDT` | 0.144 | 0.159898 | `-9.94%` | `13.52` / `17.87` | `29.56` | `0.049` | `BEARISH_ENGULFING` | 0.1385432 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 678.69 | 692.030172 | `-1.93%` | `17.98` / `23.14` | `42.43` | `0.159` | `NONE` | 661.04406 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 165.68 | 190.554729 | `-13.05%` | `9.27` / `9.24` | `26.85` | `0.053` | `BULLISH_HAMMER` | 158.05872 | `P2_EXTREME_CAPITULATION` | **BUY** (84%) |
| `LINKUSDT` | 10.135 | 10.738477 | `-5.62%` | `20.34` / `23.91` | `34.94` | `0.096` | `BEARISH_SHOOTING_STAR` | 9.815436 | `WATCH` | HOLD |
| `AAVEUSDT` | 118.86 | 128.452634 | `-7.47%` | `11.2` / `13.67` | `31.19` | `0.061` | `BEARISH_SHOOTING_STAR` | 114.603236 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SUIUSDT` | 0.8188 | 0.853732 | `-4.09%` | `23.07` / `25.17` | `39.36` | `0.128` | `BEARISH_ENGULFING` | 0.84462368 | `M15_SCALPER_PULLBACK_SHORT` | HOLD |
| `XAUTUSDT` | 3975.48 | 4029.133074 | `-1.33%` | `18.99` / `20.34` | `31.45` | `0.258` | `BEARISH_SHOOTING_STAR` | 3872.11752 | `EXIT_SHORT_STOCH_20` | HOLD |
