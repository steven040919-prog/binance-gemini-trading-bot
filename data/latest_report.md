# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T02:35:20Z`
- **Ciclo de ejecucion:** `#177`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `-100.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen bajista generalizado en temporalidad de 1H, con la mayoría de los activos cotizando por debajo de sus respectivas EMA 200 y con un sentimiento de compresión y capitulación leve. No se activan nuevas entradas LONG en los pilares principales (P1-P4) debido a que la tendencia macro es bajista y las condiciones de confirmación no se cumplen al 100%. Se identifican oportunidades de entrada SHORT en Futuros USDT-M mediante el Pilar S1 y M15 Scalper (como en XAUTUSDT y PAXGUSDT). No hay posiciones abiertas actuales para aplicar gestión dinámica.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.58e-06 | 5e-06 | `-8.88%` | `12.35` / `8.68` | `24.03` | `0.157` | `BULLISH_HAMMER` | 4.37e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.193 | 6.911923 | `-10.40%` | `11.09` / `8.91` | `30.44` | `0.062` | `NONE` | 5.908122 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.602 | 3.753645 | `-4.04%` | `26.67` / `24.45` | `43.43` | `0.224` | `NONE` | 3.4381668 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1515 | 0.164794 | `-8.07%` | `8.36` / `7.94` | `30.44` | `0.067` | `NONE` | 0.1447308 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.524 | 7.930384 | `-5.12%` | `13.9` / `12.21` | `31.42` | `0.09` | `BEARISH_ENGULFING` | 7.177896 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1454 | 0.159972 | `-9.11%` | `20.28` / `19.64` | `33.49` | `0.082` | `BEARISH_ENGULFING` | 0.1387116 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 165.37 | 190.785092 | `-13.32%` | `7.27` / `10.2` | `25.78` | `-0.028` | `BULLISH_HAMMER` | 157.76298 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3976.31 | 4029.800336 | `-1.33%` | `24.3` / `18.61` | `31.24` | `0.243` | `NONE` | 4079.69406 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (82%) |
| `AAVEUSDT` | 118.85 | 128.576907 | `-7.57%` | `11.68` / `15.78` | `30.69` | `-0.005` | `NONE` | 114.50843 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73878.01 | 75519.304101 | `-2.17%` | `35.5` / `39.41` | `46.93` | `0.342` | `BEARISH_ENGULFING` | 71957.18174 | `WATCH` | HOLD |
| `LTCUSDT` | 50.05 | 52.199538 | `-4.12%` | `28.02` / `29.08` | `37.33` | `0.067` | `BEARISH_ENGULFING` | 48.69893 | `WATCH` | HOLD |
| `TAOUSDT` | 216.1 | 223.281953 | `-3.22%` | `28.3` / `25.48` | `38.88` | `0.135` | `BEARISH_SHOOTING_STAR` | 209.6653 | `WATCH` | HOLD |
| `PAXGUSDT` | 3977.6 | 4035.400864 | `-1.43%` | `23.01` / `17.76` | `30.23` | `0.237` | `NONE` | 4081.0176 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (80%) |
| `ETHUSDT` | 2059.2 | 2170.294032 | `-5.12%` | `32.07` / `31.06` | `46.03` | `0.356` | `BEARISH_ENGULFING` | 2005.6608 | `WATCH` | HOLD |
| `ZECUSDT` | 995.4 | 1168.598703 | `-14.82%` | `54.97` / `42.44` | `45.88` | `0.637` | `BULLISH_HAMMER` | 949.6116 | `WATCH` | HOLD |
| `ONEUSDT` | 0.00149 | 0.00155 | `-3.85%` | `12.47` / `8.32` | `37.36` | `0.278` | `BULLISH_HAMMER` | 0.00142146 | `EXIT_SHORT_STOCH_20` | HOLD |
