# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T09:30:59Z`
- **Ciclo de ejecucion:** `#222`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado presenta una tendencia bajista generalizada en H1 con todos los activos cotizando por debajo de la EMA 200 y con pendientes negativas. Múltiples pares muestran condiciones de sobreventa en el Estocástico y RSI, pero ninguno cumple de forma estricta los criterios confluentes de los Pilares LONG (P1-P4) ni del Pilar SHORT S1 (el cual requiere un retesteo a la EMA 200 en zona de sobrecompra >= 80). No existen posiciones abiertas en el portafolio para realizar ajustes dinámicos de SL/TP. Se preserva el capital a la espera de confirmaciones institucionales válidas.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTCUSDT` | 73452.74 | 75394.86601 | `-2.58%` | `14.05` / `12.49` | `40.22` | `0.155` | `NONE` | 71542.96876 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `PEPEUSDT` | 4.43e-06 | 5e-06 | `-11.08%` | `6.88` / `6.89` | `21.26` | `0.179` | `BEARISH_SHOOTING_STAR` | 4.23e-06 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `ETHUSDT` | 2047.09 | 2162.249406 | `-5.33%` | `26.51` / `23.05` | `41.65` | `0.227` | `BULLISH_HAMMER` | 1993.86566 | `WATCH` | **HOLD** (0%) |
| `SOLUSDT` | 83.04 | 87.716649 | `-5.33%` | `27.08` / `23.1` | `42.63` | `0.269` | `BULLISH_HAMMER` | 80.88096 | `WATCH` | **HOLD** (0%) |
| `NEARUSDT` | 3.496 | 3.737409 | `-6.46%` | `6.53` / `4.59` | `36.61` | `0.181` | `NONE` | 3.3500224 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `XRPUSDT` | 1.0473 | 1.134249 | `-7.67%` | `26.55` / `19.64` | `42.87` | `0.306` | `BULLISH_HAMMER` | 1.0200702 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `UNIUSDT` | 6.166 | 6.86462 | `-10.18%` | `10.38` / `9.84` | `33.88` | `0.254` | `BULLISH_HAMMER` | 5.9100872 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `BNBUSDT` | 671.54 | 691.104843 | `-2.83%` | `13.19` / `12.07` | `33.38` | `0.079` | `BULLISH_HAMMER` | 654.07996 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `ENAUSDT` | 0.1417 | 0.158604 | `-10.66%` | `4.04` / `2.91` | `26.87` | `0.191` | `NONE` | 0.13660568 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `ARBUSDT` | 0.1488 | 0.163767 | `-9.14%` | `5.31` / `4.52` | `29.0` | `0.209` | `NONE` | 0.1438336 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `INJUSDT` | 7.407 | 7.8958 | `-6.19%` | `7.21` / `7.62` | `31.08` | `0.208` | `BEARISH_SHOOTING_STAR` | 7.1120876 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `QNTUSDT` | 163.85 | 188.859567 | `-13.24%` | `10.32` / `9.96` | `29.96` | `0.216` | `NONE` | 156.83708 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `DOGEUSDT` | 0.06708 | 0.070685 | `-5.10%` | `25.31` / `21.51` | `39.32` | `0.26` | `BULLISH_ENGULFING` | 0.06533592 | `WATCH` | **HOLD** (0%) |
| `XAUTUSDT` | 3933.91 | 4024.607702 | `-2.25%` | `12.44` / `13.33` | `25.56` | `-0.048` | `NONE` | 3831.62834 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
| `HYPEUSDT` | 71.52 | 76.722855 | `-6.78%` | `27.43` / `22.82` | `42.29` | `0.253` | `BULLISH_ENGULFING` | 69.606688 | `WATCH` | **HOLD** (0%) |
| `AAVEUSDT` | 117.0 | 127.872227 | `-8.50%` | `9.28` / `8.21` | `26.92` | `0.171` | `BULLISH_HAMMER` | 113.712 | `EXIT_SHORT_STOCH_20` | **HOLD** (0%) |
