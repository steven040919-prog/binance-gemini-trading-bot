# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T03:04:23Z`
- **Ciclo de ejecucion:** `#180`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `-100.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen netamente bajista en temporalidad de 1H con la mayoría de los activos operando por debajo de la EMA 200. No obstante, se identifican oportunidades de alta probabilidad bajo los pilares institucionales: QNTUSDT activa con precisión milimétrica el Pilar 2 (Capitulación Institucional de Doble Sobreventa) con patrón de Martillo alcista y divergencia positiva; mientras que LINKUSDT y ADAUSDT configuran entradas en corto bajo el pilar M15 de pullback bajista en tendencia macro en contra de la EMA 200. Se gestionan los niveles estructurales con stop-loss basado en ATR y patrones de velas confirmados.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.6e-06 | 5e-06 | `-8.44%` | `16.67` / `12.95` | `26.95` | `0.195` | `BEARISH_SHOOTING_STAR` | 4.39e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.235 | 6.9073 | `-9.73%` | `16.28` / `12.22` | `33.98` | `0.166` | `BULLISH_ENGULFING` | 5.94819 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.572 | 3.754112 | `-4.85%` | `17.43` / `21.68` | `40.75` | `0.159` | `NONE` | 3.4342656 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0507 | 1.139872 | `-7.82%` | `23.2` / `27.67` | `41.9` | `0.154` | `BEARISH_SHOOTING_STAR` | 1.02329474 | `WATCH` | HOLD |
| `INJUSDT` | 7.498 | 7.929616 | `-5.44%` | `14.24` / `13.7` | `30.97` | `0.078` | `BULLISH_ENGULFING` | 7.153092 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1514 | 0.164695 | `-8.07%` | `11.03` / `8.92` | `31.03` | `0.108` | `BULLISH_ENGULFING` | 0.14488548 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1451 | 0.159909 | `-9.26%` | `16.08` / `18.73` | `32.19` | `0.116` | `BEARISH_SHOOTING_STAR` | 0.13900542 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 166.17 | 190.559605 | `-12.80%` | `10.11` / `9.52` | `28.22` | `0.072` | `BULLISH_HAMMER` | 158.52618 | `P2_EXTREME_CAPITULATION` | **BUY** (88%) |
| `LINKUSDT` | 10.167 | 10.738795 | `-5.32%` | `22.2` / `24.53` | `37.19` | `0.15` | `BEARISH_SHOOTING_STAR` | 10.486342 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (82%) |
| `OPGUSDT` | 0.1332 | 0.126088 | `+5.64%` | `4.32` / `5.5` | `45.49` | `0.271` | `BEARISH_SHOOTING_STAR` | 0.1270728 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 119.17 | 128.455719 | `-7.23%` | `12.6` / `14.14` | `32.82` | `0.092` | `NONE` | 114.618576 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3976.14 | 4029.139642 | `-1.32%` | `19.33` / `20.46` | `31.99` | `0.264` | `NONE` | 3872.76036 | `EXIT_SHORT_STOCH_20` | HOLD |
| `LTCUSDT` | 50.04 | 52.177012 | `-4.10%` | `22.86` / `27.04` | `37.15` | `0.113` | `BEARISH_SHOOTING_STAR` | 48.73896 | `WATCH` | HOLD |
| `TAOUSDT` | 215.8 | 223.246158 | `-3.34%` | `23.74` / `26.3` | `38.67` | `0.155` | `NONE` | 209.905 | `WATCH` | HOLD |
| `BTCUSDT` | 73860.0 | 75523.902729 | `-2.20%` | `28.39` / `33.64` | `46.69` | `0.343` | `BEARISH_SHOOTING_STAR` | 71939.64 | `WATCH` | HOLD |
| `ADAUSDT` | 0.1739 | 0.181302 | `-4.08%` | `20.88` / `23.32` | `39.47` | `0.159` | `BEARISH_SHOOTING_STAR` | 0.17931272 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (80%) |
