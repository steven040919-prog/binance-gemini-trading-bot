# Reporte Autonomo - Estrategia EMA 200 + Estocastico (80/20) + SL/TP Dinamico (1H)

- **Ultima actualizacion (UTC):** `2026-11-08T23:48:05Z`
- **Ciclo de ejecucion:** `#1`
- **Modo:** `SIMULACION / CARTERA VIRTUAL`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `1000.00 USDT`
- **Liquidez Disponible:** `844.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado global opera mayoritariamente bajo la EMA de 200 en temporalidad de 1H con sesgo bajista general. ONEUSDT es el unico activo que cumple todas las condiciones de la estrategia alcista al cotizar por encima de la EMA de 200, mostrar estocastico en zona de sobreventa con retroceso y presentar una vela envolvente alcista confirmada (BULLISH_ENGULFING). Los demas pares se mantienen en observacion (HOLD) por no cumplir con la condicion estructural de la EMA de 200 o carecer de patron de entrada valido.

## Posiciones Abiertas (Con Stop-Loss y Take-Profit Dinamicos)
| Par | Entrada | Precio Actual | PnL Actual | SL Inicial | SL Actual (Dinamico) | Ganancia Asegurada | TP Actual (Dinamico) | Ajustes |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ONEUSDT` | 0.001708 | 0.001716 | **+0.47%** | 0.001606 | **0.001606** | `-5.97%` | **0.00191296** | 0 |

## Operaciones y Ajustes de SL/TP en este Ciclo
- **BUY `ONEUSDT`** @ `0.001708` (156.0 USDT) — _Estrategia EMA200+Stoch (BULLISH_ENGULFING, Stoch %K=14.82, Riesgo ~$10.0 USD / 1%): Cumple estrictamente la estrategia: precio actual por encima de la EMA 200, estocastico k en zona de sobreventa (14.82) tras retroceso, y formacion de patron de vela Envolvente Alcista. Stop-loss inicial fijado en el bajo de la vela previa (0.001606)._

## Escaneo 1H: EMA 200 + Estocastico (20/80) + Patrones de Vela
| Par | Precio | EMA 200 | Posicion EMA | Estocastico (%K / %D) | Patron de Vela (1H) | SL Vela Previa | Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ONEUSDT` | 0.001716 | 0.001481 | SOBRE EMA 200 (Alza) | `14.82` / `10.2` | `BULLISH_ENGULFING` | 0.001606 | `LONG_ENTRY` | **BUY** (88%) |
| `ETHUSDT` | 2133.46 | 2268.544006 | BAJO EMA 200 (Baja) | `37.58` / `30.55` | `BULLISH_HAMMER` | 2228.26 | `WATCH` | **HOLD** (50%) |
| `BTCUSDT` | 74904.45 | 77125.157679 | BAJO EMA 200 (Baja) | `36.9` / `30.05` | `BEARISH_SHOOTING_STAR` | 75785.53 | `WATCH` | **HOLD** (50%) |
| `ZECUSDT` | 1212.49 | 1266.80987 | BAJO EMA 200 (Baja) | `25.78` / `23.59` | `BULLISH_ENGULFING` | 1248.52 | `WATCH` | **HOLD** (50%) |
| `XRPUSDT` | 1.1145 | 1.218994 | BAJO EMA 200 (Baja) | `23.88` / `21.35` | `BEARISH_SHOOTING_STAR` | 1.1543 | `WATCH` | **HOLD** (50%) |
| `BMTUSDT` | 0.02518 | 0.024835 | SOBRE EMA 200 (Alza) | `28.1` / `19.22` | `NONE` | 0.02354 | `EXIT_SHORT_STOCH_20` | **HOLD** (60%) |
| `SOLUSDT` | 86.78 | 92.262211 | BAJO EMA 200 (Baja) | `26.79` / `27.27` | `BEARISH_SHOOTING_STAR` | 89.22 | `WATCH` | **HOLD** (50%) |
| `NEARUSDT` | 3.592 | 3.895469 | BAJO EMA 200 (Baja) | `33.56` / `28.74` | `BEARISH_SHOOTING_STAR` | 3.689 | `WATCH` | **HOLD** (50%) |
| `UNIUSDT` | 6.804 | 7.096732 | BAJO EMA 200 (Baja) | `27.84` / `24.56` | `BEARISH_SHOOTING_STAR` | 6.98 | `WATCH` | **HOLD** (50%) |
| `ENAUSDT` | 0.1489 | 0.170159 | BAJO EMA 200 (Baja) | `33.05` / `36.65` | `BEARISH_SHOOTING_STAR` | 0.154 | `WATCH` | **HOLD** (50%) |
| `BNBUSDT` | 685.7 | 703.957759 | BAJO EMA 200 (Baja) | `22.45` / `21.51` | `BEARISH_SHOOTING_STAR` | 697.43 | `WATCH` | **HOLD** (50%) |
| `WLDUSDT` | 0.3116 | 0.359285 | BAJO EMA 200 (Baja) | `26.86` / `24.14` | `BEARISH_SHOOTING_STAR` | 0.3226 | `WATCH` | **HOLD** (50%) |
