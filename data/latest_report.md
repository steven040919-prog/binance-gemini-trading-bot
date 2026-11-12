# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T04:21:56Z`
- **Ciclo de ejecucion:** `#190`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> Evaluación general de mercado con sesgo bajista predominante y la EMA 200 actuando como resistencia generalizada. Destaca la oportunidad en OPGUSDT cumpliendo rigurosamente los parámetros institucionales del Pilar 1 (Pullback sobre EMA 200 con soporte dinámico, estocástico girando al alza y patrón de vela envolvente alcista). No existen posiciones abiertas vigentes para requerir ajustes, por lo que se prioriza la ejecución de la entrada LONG detectada.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.56e-06 | 5e-06 | `-9.09%` | `14.81` / `14.61` | `25.34` | `0.181` | `NONE` | 4.36e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73766.95 | 75494.04021 | `-2.29%` | `28.22` / `29.73` | `44.97` | `0.266` | `BEARISH_ENGULFING` | 71849.0093 | `WATCH` | HOLD |
| `ETHUSDT` | 2053.81 | 2168.008258 | `-5.27%` | `29.25` / `29.62` | `43.56` | `0.269` | `NONE` | 2000.41094 | `WATCH` | HOLD |
| `UNIUSDT` | 6.229 | 6.895817 | `-9.67%` | `21.88` / `16.95` | `34.01` | `0.187` | `BULLISH_HAMMER` | 5.942466 | `EXIT_SHORT_STOCH_20` | HOLD |
| `SOLUSDT` | 83.17 | 87.999737 | `-5.49%` | `30.87` / `31.54` | `42.1` | `0.166` | `BULLISH_HAMMER` | 81.00758 | `WATCH` | HOLD |
| `NEARUSDT` | 3.559 | 3.751765 | `-5.14%` | `11.58` / `16.84` | `39.46` | `0.137` | `BULLISH_HAMMER` | 3.4221294 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.00144 | 0.001547 | `-6.93%` | `4.59` / `5.95` | `29.95` | `0.087` | `NONE` | 0.00137376 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0457 | 1.138791 | `-8.17%` | `18.34` / `22.92` | `38.7` | `0.044` | `BEARISH_ENGULFING` | 1.0185118 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.556 | 7.923385 | `-4.64%` | `20.64` / `17.33` | `33.75` | `0.178` | `BULLISH_HAMMER` | 7.208424 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1499 | 0.164484 | `-8.87%` | `6.95` / `8.14` | `28.61` | `0.086` | `BEARISH_ENGULFING` | 0.14484324 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1436 | 0.159632 | `-10.04%` | `10.49` / `14.45` | `28.72` | `0.082` | `BEARISH_ENGULFING` | 0.1380868 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 678.08 | 691.684153 | `-1.97%` | `16.45` / `20.09` | `41.39` | `0.136` | `NONE` | 660.44992 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06722 | 0.07087 | `-5.15%` | `30.93` / `31.87` | `37.9` | `0.122` | `NONE` | 0.06547228 | `WATCH` | HOLD |
| `QNTUSDT` | 165.43 | 190.20332 | `-13.02%` | `11.73` / `9.71` | `26.6` | `0.097` | `BEARISH_SHOOTING_STAR` | 157.82022 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INTCBUSDT` | 60.84 | 59.191149 | `+2.79%` | `26.68` / `30.59` | `47.61` | `0.241` | `BEARISH_SHOOTING_STAR` | 58.649624 | `WATCH` | HOLD |
| `OPGUSDT` | 0.1341 | 0.126153 | `+6.30%` | `6.44` / `5.46` | `47.18` | `0.299` | `BULLISH_ENGULFING` | 0.1279314 | `P1_EMA200_PULLBACK` | **BUY** (89%) |
