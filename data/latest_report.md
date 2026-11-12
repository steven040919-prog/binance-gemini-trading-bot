# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T02:25:45Z`
- **Ciclo de ejecucion:** `#176`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `-100.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen netamente bajista con todos los activos cotizando por debajo de la EMA 200 en temporalidad 1H. No se cumplen los requisitos estrictos para los Pilares LONG (P1-P4) ya que las tendencias principales son bajistas y los precios no muestran soporte estructural alcista confirmado. Tampoco se activa el pilar SHORT (S1) de rechazo en la EMA 200 con sobrecompra, ya que los osciladores estocásticos están mayormente deprimidos en zonas de sobreventa buscando salida o consolidación. Portfolio sin posiciones abiertas y sin operaciones válidas para ejecutar en este ciclo.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.58e-06 | 5e-06 | `-8.88%` | `12.35` / `8.68` | `24.03` | `0.157` | `BULLISH_HAMMER` | 4.37e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.174 | 6.911734 | `-10.67%` | `10.0` / `8.55` | `28.72` | `0.035` | `NONE` | 5.889996 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.607 | 3.753694 | `-3.91%` | `27.25` / `24.64` | `44.04` | `0.24` | `NONE` | 3.441078 | `WATCH` | HOLD |
| `INJUSDT` | 7.482 | 7.929966 | `-5.65%` | `11.87` / `11.54` | `28.29` | `0.048` | `BEARISH_ENGULFING` | 7.1426336 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1508 | 0.164787 | `-8.49%` | `6.68` / `7.38` | `27.69` | `0.029` | `NONE` | 0.14481408 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.145 | 0.159968 | `-9.36%` | `19.35` / `19.33` | `31.7` | `0.056` | `BEARISH_ENGULFING` | 0.13869 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 164.45 | 190.775938 | `-13.80%` | `5.69` / `9.68` | `24.67` | `-0.061` | `NONE` | 156.8853 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 118.63 | 128.574718 | `-7.73%` | `10.69` / `15.45` | `29.22` | `-0.027` | `NONE` | 114.514634 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3983.02 | 4029.867102 | `-1.16%` | `27.43` / `19.65` | `34.94` | `0.301` | `NONE` | 3879.46148 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73884.01 | 75519.363802 | `-2.17%` | `35.64` / `39.45` | `47.03` | `0.347` | `BEARISH_ENGULFING` | 71963.02574 | `WATCH` | **HOLD** (50%) |
| `LTCUSDT` | 50.07 | 52.199737 | `-4.08%` | `28.32` / `29.18` | `37.76` | `0.076` | `BEARISH_ENGULFING` | 48.698502 | `WATCH` | HOLD |
| `TAOUSDT` | 216.0 | 223.280958 | `-3.26%` | `28.06` / `25.4` | `38.64` | `0.128` | `BEARISH_SHOOTING_STAR` | 209.668 | `WATCH` | HOLD |
| `PAXGUSDT` | 3984.97 | 4035.474197 | `-1.25%` | `26.47` / `18.91` | `34.54` | `0.3` | `NONE` | 3881.36078 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2059.36 | 2170.295624 | `-5.11%` | `32.15` / `31.08` | `46.11` | `0.36` | `BEARISH_ENGULFING` | 2005.81664 | `WATCH` | HOLD |
| `ZECUSDT` | 998.57 | 1168.630245 | `-14.55%` | `56.41` / `42.92` | `46.9` | `0.7` | `BULLISH_HAMMER` | 952.63578 | `WATCH` | HOLD |
| `ONEUSDT` | 0.001473 | 0.00155 | `-4.94%` | `8.98` / `7.16` | `33.96` | `0.196` | `BULLISH_HAMMER` | 0.00140524 | `EXIT_SHORT_STOCH_20` | HOLD |
