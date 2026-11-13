# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T15:01:50Z`
- **Ciclo de ejecucion:** `#337`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado cripto mantiene un sesgo bajista generalizado en temporalidad de 1 hora, con la mayoria de los activos cotizando por debajo de la EMA 200. Se evaluan oportunidades institucionales bajo los pilares de corto y rebotes tecnicos. ZECUSDT y HYPEUSDT activan el Pilar S1 (Rechazo Bajista en Resistencia EMA 200) mostrando patrones de velas envolventes y estocastico en zona de distribucion ideal para cortos en Futuros USDT-M. No existen posiciones abiertas vigentes para ajuste dinamico de SL/TP, priorizando la conservacion de capital y entradas de alta probabilidad.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.0772 | 0.077869 | `-0.86%` | `22.61` / `21.43` | `37.65` | `0.148` | `NONE` | 0.0736488 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.13 | 1.13723 | `-0.64%` | `29.63` / `41.98` | `38.67` | `0.068` | `NONE` | 1.078066 | `WATCH` | HOLD |
| `BTCUSDT` | 68914.96 | 74020.657605 | `-6.90%` | `43.16` / `44.01` | `33.59` | `0.317` | `BEARISH_ENGULFING` | 67123.17104 | `WATCH` | HOLD |
| `ETHUSDT` | 1946.3 | 2113.446881 | `-7.91%` | `48.66` / `50.86` | `37.32` | `0.354` | `BEARISH_ENGULFING` | 1895.02694 | `WATCH` | HOLD |
| `MUBUSDT` | 773.06 | 762.845189 | `+1.34%` | `8.9` / `17.39` | `37.71` | `-0.014` | `BEARISH_ENGULFING` | 747.735872 | `EXIT_SHORT_STOCH_20` | HOLD |
| `INTCBUSDT` | 58.72 | 59.289341 | `-0.96%` | `11.92` / `22.7` | `32.91` | `-0.136` | `BEARISH_ENGULFING` | 56.892352 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ZECUSDT` | 949.81 | 1095.420587 | `-13.29%` | `69.46` / `77.44` | `47.86` | `0.546` | `BEARISH_ENGULFING` | 993.50126 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (82%) |
| `DODOUSDT` | 0.02812 | 0.023789 | `+18.20%` | `52.68` / `62.76` | `57.08` | `0.549` | `NONE` | 0.02682648 | `WATCH` | HOLD |
| `SOLUSDT` | 80.51 | 85.697448 | `-6.05%` | `67.86` / `71.36` | `46.26` | `0.518` | `NONE` | 78.390638 | `WATCH` | HOLD |
| `NEARUSDT` | 3.542 | 3.629635 | `-2.41%` | `78.88` / `83.65` | `56.18` | `0.755` | `NONE` | 3.379068 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 637.13 | 678.179945 | `-6.05%` | `50.87` / `51.65` | `38.46` | `0.374` | `BEARISH_ENGULFING` | 620.56462 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0309 | 1.106373 | `-6.82%` | `75.86` / `67.9` | `50.72` | `0.612` | `BEARISH_ENGULFING` | 0.99034604 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.49e-06 | 5e-06 | `-7.28%` | `37.04` / `40.74` | `44.63` | `0.196` | `BEARISH_ENGULFING` | 4.28e-06 | `WATCH` | HOLD |
| `INJUSDT` | 8.126 | 7.782764 | `+4.41%` | `89.39` / `91.17` | `72.36` | `0.973` | `NONE` | 7.752204 | `EXIT_LONG_STOCH_80` | HOLD |
| `HYPEUSDT` | 73.56 | 75.188423 | `-2.17%` | `72.72` / `81.19` | `58.85` | `0.748` | `BEARISH_ENGULFING` | 76.94376 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (78%) |
| `UNIUSDT` | 5.889 | 6.603314 | `-10.82%` | `62.96` / `55.8` | `45.62` | `0.504` | `NONE` | 5.618106 | `WATCH` | HOLD |
