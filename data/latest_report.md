# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T05:37:22Z`
- **Ciclo de ejecucion:** `#109`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El régimen de mercado general es predominantemente BAJISTA (BEARISH), con la gran mayoría de los activos cotizando por debajo de su EMA 200 en temporalidad de 1H y presiones bajistas en marcos temporales superiores. Tras analizar de forma exhaustiva los 4 Pilares de entrada LONG y el Pilar S1 de SHORT, ningún activo cumple con la confluencia cuantitativa requerida (entry_pillar es NONE para todos los candidatos). Dado que no existen posiciones abiertas en el portafolio para realizar un ajuste dinámico de Stop-Loss/Take-Profit, la decisión óptima de gestión de riesgo es mantenerse al margen en HOLD a la espera de confirmaciones técnicas válidas.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 1013.91 | 1213.0184 | `-16.41%` | `15.37` / `14.39` | `30.88` | `0.267` | `BEARISH_ENGULFING` | 967.27014 | `EXIT_SHORT_STOCH_20` | **HOLD** (90%) |
| `UNIUSDT` | 6.652 | 6.998641 | `-4.95%` | `13.92` / `14.33` | `37.54` | `0.274` | `BEARISH_ENGULFING` | 6.4164752 | `EXIT_SHORT_STOCH_20` | **HOLD** (88%) |
| `QNTUSDT` | 180.4 | 193.969441 | `-7.00%` | `47.17` / `44.43` | `34.46` | `0.297` | `BEARISH_SHOOTING_STAR` | 174.48056 | `WATCH` | HOLD |
| `TRXUSDT` | 0.3178 | 0.318516 | `-0.22%` | `15.23` / `11.09` | `45.44` | `0.327` | `BULLISH_HAMMER` | 0.3095372 | `EXIT_SHORT_STOCH_20` | **HOLD** (80%) |
| `BTCUSDT` | 73818.16 | 75814.183747 | `-2.63%` | `59.68` / `50.36` | `47.05` | `0.551` | `BULLISH_HAMMER` | 71898.88784 | `WATCH` | **HOLD** (85%) |
| `ETHUSDT` | 2067.98 | 2192.681932 | `-5.69%` | `73.78` / `62.19` | `47.16` | `0.611` | `NONE` | 2014.21252 | `WATCH` | **HOLD** (85%) |
| `ONEUSDT` | 0.001804 | 0.001553 | `+16.17%` | `29.4` / `42.23` | `53.23` | `0.435` | `BULLISH_HAMMER` | 0.00172102 | `WATCH` | **HOLD** (82%) |
| `SOLUSDT` | 83.13 | 89.057085 | `-6.66%` | `51.99` / `49.85` | `40.47` | `0.43` | `NONE` | 80.96862 | `WATCH` | **HOLD** (85%) |
| `XRPUSDT` | 1.0586 | 1.159229 | `-8.68%` | `57.51` / `54.04` | `42.54` | `0.447` | `BEARISH_ENGULFING` | 1.02789284 | `WATCH` | **HOLD** (85%) |
| `RLUSDUSDT` | 1.0012 | 1.001199 | `+0.00%` | `75.4` / `79.37` | `54.62` | `0.686` | `BEARISH_SHOOTING_STAR` | 0.9751688 | `WATCH` | HOLD |
| `NEARUSDT` | 3.647 | 3.768965 | `-3.24%` | `70.35` / `70.73` | `53.27` | `0.658` | `BEARISH_ENGULFING` | 3.5046846 | `WATCH` | **HOLD** (85%) |
| `BNBUSDT` | 681.05 | 693.453133 | `-1.79%` | `63.02` / `58.3` | `47.0` | `0.521` | `BEARISH_ENGULFING` | 663.3427 | `WATCH` | **HOLD** (85%) |
| `PEPEUSDT` | 5.33e-06 | 5e-06 | `+5.20%` | `49.91` / `53.45` | `52.07` | `0.509` | `BULLISH_HAMMER` | 5.08e-06 | `WATCH` | HOLD |
| `HYPEUSDT` | 72.06 | 78.109391 | `-7.74%` | `48.68` / `41.92` | `41.24` | `0.414` | `MORNING_STAR` | 70.041444 | `WATCH` | HOLD |
| `DOGEUSDT` | 0.06817 | 0.071543 | `-4.72%` | `57.24` / `53.82` | `43.63` | `0.481` | `BEARISH_ENGULFING` | 0.06639758 | `WATCH` | HOLD |
| `ARBUSDT` | 0.1634 | 0.166236 | `-1.71%` | `62.37` / `69.23` | `46.53` | `0.624` | `NONE` | 0.15681368 | `WATCH` | HOLD |
