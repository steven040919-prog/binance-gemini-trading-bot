# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-12T07:43:13Z`
- **Ciclo de ejecucion:** `#211`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado se encuentra en un régimen netamente bajista en temporalidad 1H, con la gran mayoría de los activos cotizando por debajo de la EMA 200 y con pendientes negativas pronunciadas. No se cumplen los requisitos estrictos de los Pilares LONG (P1-P4) debido a la ausencia de tendencias alcistas y giros válidos en sobreventa con suficiente confirmación estructural. En cuanto al Pilar SHORT (S1) en Futuros USDT-M y la gestión dinámica de posiciones, los activos evaluados no muestran actualmente un retroceso claro hacia la resistencia de la EMA 200 combinada con sobrecompra en el estocástico para ejecutar nuevas entradas cortas, ni existen posiciones abiertas con ganancias que requieran ajustes de SL/TP (acción ADJUST). Por lo tanto, se emite una postura de espera (HOLD) general para preservar capital.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `PEPEUSDT` | 4.46e-06 | 5e-06 | `-10.68%` | `8.13` / `10.21` | `22.35` | `0.157` | `BEARISH_SHOOTING_STAR` | 4.25e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 73588.0 | 75419.479559 | `-2.43%` | `9.2` / `14.18` | `42.4` | `0.209` | `BULLISH_ENGULFING` | 71674.712 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `ETHUSDT` | 2048.75 | 2163.751324 | `-5.31%` | `17.46` / `18.84` | `42.2` | `0.24` | `NONE` | 1995.4825 | `EXIT_SHORT_STOCH_20` | **HOLD** (75%) |
| `SOLUSDT` | 82.83 | 87.798445 | `-5.66%` | `17.81` / `20.87` | `39.82` | `0.167` | `BEARISH_SHOOTING_STAR` | 80.67642 | `EXIT_SHORT_STOCH_20` | HOLD |
| `UNIUSDT` | 6.157 | 6.874336 | `-10.43%` | `11.64` / `16.58` | `32.53` | `0.18` | `NONE` | 5.9202074 | `EXIT_SHORT_STOCH_20` | HOLD |
| `NEARUSDT` | 3.512 | 3.743817 | `-6.19%` | `4.67` / `5.26` | `35.64` | `0.133` | `BEARISH_SHOOTING_STAR` | 3.38764 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XRPUSDT` | 1.0434 | 1.135702 | `-8.13%` | `12.31` / `10.94` | `38.58` | `0.162` | `BULLISH_HAMMER` | 1.0162716 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INJUSDT` | 7.408 | 7.905259 | `-6.29%` | `6.9` / `11.01` | `30.74` | `0.14` | `NONE` | 7.1200912 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BNBUSDT` | 673.85 | 691.216138 | `-2.51%` | `9.57` / `7.0` | `36.39` | `0.085` | `NONE` | 656.3299 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ENAUSDT` | 0.1425 | 0.158985 | `-10.37%` | `3.7` / `5.09` | `27.15` | `0.156` | `BEARISH_SHOOTING_STAR` | 0.1374255 | `EXIT_SHORT_STOCH_20` | HOLD |
| `HYPEUSDT` | 71.31 | 76.829468 | `-7.18%` | `18.88` / `25.97` | `39.11` | `0.139` | `NONE` | 69.29118 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ARBUSDT` | 0.1488 | 0.164009 | `-9.27%` | `3.44` / `4.98` | `27.83` | `0.143` | `NONE` | 0.14431456 | `EXIT_SHORT_STOCH_20` | HOLD |
| `DOGEUSDT` | 0.06694 | 0.070742 | `-5.37%` | `17.66` / `20.72` | `36.01` | `0.162` | `BEARISH_SHOOTING_STAR` | 0.06519956 | `EXIT_SHORT_STOCH_20` | HOLD |
| `QNTUSDT` | 164.76 | 189.372201 | `-13.00%` | `8.74` / `10.47` | `29.76` | `0.193` | `NONE` | 157.18104 | `EXIT_SHORT_STOCH_20` | HOLD |
| `XAUTUSDT` | 3953.5 | 4026.476612 | `-1.81%` | `13.9` / `16.62` | `25.79` | `0.086` | `NONE` | 3850.709 | `EXIT_SHORT_STOCH_20` | HOLD |
| `AAVEUSDT` | 117.01 | 128.02744 | `-8.61%` | `5.67` / `6.29` | `25.89` | `0.101` | `NONE` | 113.50475 | `EXIT_SHORT_STOCH_20` | HOLD |
