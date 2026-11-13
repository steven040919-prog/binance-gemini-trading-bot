# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T18:11:00Z`
- **Ciclo de ejecucion:** `#357`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado general muestra una estructura macro bajista con la mayoria de activos cotizando por debajo de la EMA 200 de 1H. Se han detectado dos oportunidades de venta en corto (SHORT) bajo los pilares institucionales de Futuros USDT-M: SOXSBUSDT mediante el Pilar S1 (Rechazo de Resistencia EMA 200) y XRPUSDT via el Pilar Scalper M15 Pullback Bajista. No hay posiciones abiertas actualmente que requieran ajuste dinamico de Trailing Stop.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.0752 | 0.077805 | `-3.35%` | `8.74` / `10.46` | `34.85` | `0.148` | `BEARISH_SHOOTING_STAR` | 0.0717408 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
| `UNIUSDT` | 5.761 | 6.58424 | `-12.50%` | `31.59` / `38.26` | `37.98` | `0.321` | `NONE` | 5.515365 | `WATCH` | **HOLD** (50%) |
| `BTCUSDT` | 68888.57 | 73870.019451 | `-6.74%` | `47.56` / `43.77` | `35.41` | `0.371` | `BULLISH_ENGULFING` | 67033.774028 | `WATCH` | **HOLD** (55%) |
| `GRAMUSDT` | 1.122 | 1.137213 | `-1.34%` | `19.64` / `23.53` | `37.13` | `0.072` | `BEARISH_ENGULFING` | 1.0823204 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
| `MUBUSDT` | 761.98 | 763.359782 | `-0.18%` | `18.56` / `14.68` | `35.13` | `0.095` | `BULLISH_ENGULFING` | 729.154976 | `EXIT_SHORT_STOCH_20` | **HOLD** (50%) |
| `ETHUSDT` | 1939.11 | 2108.417949 | `-8.03%` | `41.49` / `38.66` | `38.01` | `0.375` | `BULLISH_ENGULFING` | 1875.093936 | `WATCH` | **HOLD** (55%) |
| `BARDUSDT` | 0.1499 | 0.109204 | `+37.27%` | `46.93` / `57.42` | `57.84` | `0.568` | `BULLISH_HAMMER` | 0.1430046 | `WATCH` | **HOLD** (50%) |
| `SOLUSDT` | 80.1 | 85.550902 | `-6.37%` | `43.44` / `45.67` | `44.63` | `0.477` | `NONE` | 77.33556 | `WATCH` | **HOLD** (50%) |
| `ZECUSDT` | 945.35 | 1090.545661 | `-13.31%` | `58.33` / `60.23` | `46.19` | `0.49` | `NONE` | 901.8639 | `WATCH` | **HOLD** (50%) |
| `BNBUSDT` | 635.01 | 677.0889 | `-6.21%` | `39.37` / `37.99` | `39.45` | `0.393` | `NONE` | 616.138794 | `WATCH` | **HOLD** (50%) |
| `SOXSBUSDT` | 52.48 | 55.519821 | `-5.48%` | `76.53` / `82.47` | `66.63` | `0.9` | `BEARISH_SHOOTING_STAR` | 54.89408 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (84%) |
| `XRPUSDT` | 1.0222 | 1.103999 | `-7.41%` | `45.08` / `49.27` | `45.87` | `0.46` | `BEARISH_SHOOTING_STAR` | 1.05414612 | `M15_SCALPER_PULLBACK_SHORT` | **SHORT** (76%) |
| `NEARUSDT` | 3.491 | 3.624958 | `-3.70%` | `62.3` / `65.09` | `50.31` | `0.566` | `BEARISH_SHOOTING_STAR` | 3.330414 | `WATCH` | **HOLD** (50%) |
| `INJUSDT` | 8.088 | 7.797784 | `+3.72%` | `84.44` / `87.42` | `68.42` | `0.797` | `NONE` | 7.715952 | `EXIT_LONG_STOCH_80` | **HOLD** (50%) |
| `PEPEUSDT` | 4.48e-06 | 5e-06 | `-7.37%` | `25.0` / `25.46` | `45.34` | `0.235` | `BULLISH_ENGULFING` | 4.27e-06 | `WATCH` | **HOLD** (50%) |
| `ENAUSDT` | 0.1357 | 0.151924 | `-10.68%` | `35.96` / `42.19` | `41.19` | `0.299` | `NONE` | 0.1294578 | `WATCH` | **HOLD** (50%) |
