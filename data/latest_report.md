# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T05:10:28Z`
- **Ciclo de ejecucion:** `#195`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global opera bajo un régimen bajista claro en temporalidad de 1H con todos los activos cotizando por debajo de la EMA 200 y con pendientes negativas. Se identifican múltiples condiciones de sobreventa extrema en el estocástico. Destaca el activo INJUSDT cumpliendo con los criterios de la arquitectura para el Pilar SHORT (S1/M15_SCALPER_PULLBACK_SHORT) con un patrón de giro bajista (BEARISH_SHOOTING_STAR) bajo la resistencia dinámica, por lo que se emite una orden de venta en corto. Para el resto de los activos evaluados en zonas de soporte con patrones de giro alcista, se mantiene la vigilancia o la salida de cortos previos, sin aperturas de posiciones LONG dado que la tendencia macro es bajista.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 73664.14 | 75468.998063 | `-2.39%` | `22.24` / `25.6` | `43.18` | `0.196` | `BEARISH_ENGULFING` | 71748.87236 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.58e-06 | 5e-06 | `-8.52%` | `13.87` / `14.7` | `27.01` | `0.233` | `BULLISH_HAMMER` | 4.37e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2048.4 | 2166.756204 | `-5.46%` | `22.85` / `26.18` | `41.19` | `0.185` | `NONE` | 1995.1416 | `WATCH` | HOLD |
| `UNIUSDT` | 6.239 | 6.889925 | `-9.45%` | `23.31` / `20.62` | `35.26` | `0.223` | `BULLISH_HAMMER` | 5.9943608 | `WATCH` | HOLD |
| `SOLUSDT` | 83.0 | 87.943357 | `-5.62%` | `26.41` / `29.11` | `40.68` | `0.137` | `NONE` | 80.842 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001451 | 0.001546 | `-6.16%` | `10.46` / `8.09` | `31.51` | `0.176` | `BULLISH_HAMMER` | 0.00138425 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.547 | 3.748441 | `-5.37%` | `7.84` / `11.46` | `38.37` | `0.133` | `BULLISH_HAMMER` | 3.4234618 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0433 | 1.138157 | `-8.33%` | `10.97` / `16.5` | `37.23` | `0.044` | `NONE` | 1.0161742 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.505 | 7.918193 | `-5.22%` | `18.46` / `18.43` | `31.6` | `0.151` | `BEARISH_SHOOTING_STAR` | 7.85023 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (85%) |
| `BNBUSDT` | 675.66 | 691.633913 | `-2.31%` | `6.09` / `12.61` | `37.56` | `0.028` | `NONE` | 658.09284 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1439 | 0.159419 | `-9.73%` | `8.84` / `11.18` | `29.34` | `0.143` | `NONE` | 0.1384513 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1514 | 0.16434 | `-7.87%` | `7.91` / `8.39` | `33.73` | `0.201` | `NONE` | 0.145158 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06714 | 0.070838 | `-5.22%` | `26.65` / `29.44` | `37.06` | `0.132` | `NONE` | 0.06539436 | `WATCH` | HOLD |
| `QNTUSDT` | 166.74 | 189.925897 | `-12.21%` | `14.68` / `12.38` | `30.27` | `0.186` | `BULLISH_HAMMER` | 159.06996 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LINKUSDT` | 10.083 | 10.721036 | `-5.95%` | `14.51` / `17.41` | `32.22` | `0.108` | `NONE` | 9.820842 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3972.9 | 4027.973278 | `-1.37%` | `20.07` / `18.74` | `32.49` | `0.274` | `BEARISH_ENGULFING` | 3869.6046 | `EXIT_SHORT_STOCH_20` | HOLD |
