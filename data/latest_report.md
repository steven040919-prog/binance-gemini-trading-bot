# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-13T13:54:30Z`
- **Ciclo de ejecucion:** `#330`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `0.00 USDT`
- **Liquidez Disponible:** `0.00 USDT`
- **Rendimiento Diario (UTC):** `+0.00%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado de criptomonedas se mantiene bajo presión bajista macro (mayoría de activos cotizando por debajo de la EMA 200 en temporalidad 1h). Se identifican dos oportunidades operativas clave de acuerdo a los pilares institucionales: ERAUSDT cumple con el Pilar 1 LONG (PULLBACK_DE_VALOR_SOBRE_EMA200) gracias a su soporte en la EMA 200 y giro alcista del estocástico con patrón de martillo, y HYPEUSDT cumple con el Pilar S1 SHORT en Futuros USDT-M (RECHAZO_BAJISTA_EN_RESISTENCIA_EMA200) con rechazo bajista en la EMA 200 y estocástico en zona de sobrecompra. No existen posiciones abiertas previas en el portafolio para realizar ajustes dinámicos de SL/TP.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ERAUSDT` | 0.0787 | 0.077948 | `+0.96%` | `19.47` / `12.2` | `40.41` | `0.241` | `BULLISH_HAMMER` | 0.0750798 | `P1_EMA200_PULLBACK` | **BUY** (88%) |
| `GRAMUSDT` | 1.13 | 1.137677 | `-0.67%` | `53.21` / `56.29` | `38.67` | `-0.064` | `BEARISH_ENGULFING` | 1.07802 | `WATCH` | HOLD |
| `BTCUSDT` | 69631.89 | 74141.952833 | `-6.08%` | `45.78` / `43.37` | `40.05` | `0.422` | `BEARISH_SHOOTING_STAR` | 67480.532908 | `WATCH` | HOLD |
| `ETHUSDT` | 1970.3 | 2117.223726 | `-6.94%` | `53.57` / `48.52` | `45.46` | `0.477` | `BEARISH_SHOOTING_STAR` | 1898.48814 | `WATCH` | HOLD |
| `NEARUSDT` | 3.579 | 3.6329 | `-1.48%` | `88.64` / `86.19` | `60.91` | `0.938` | `BULLISH_ENGULFING` | 3.414366 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 81.64 | 85.848581 | `-4.90%` | `75.07` / `69.33` | `56.15` | `0.754` | `BEARISH_SHOOTING_STAR` | 78.290016 | `WATCH` | HOLD |
| `DODOUSDT` | 0.02882 | 0.023697 | `+21.62%` | `73.62` / `71.16` | `63.01` | `0.765` | `NONE` | 0.02749428 | `WATCH` | HOLD |
| `ZECUSDT` | 968.65 | 1100.059011 | `-11.95%` | `84.85` / `83.88` | `55.06` | `0.817` | `BEARISH_SHOOTING_STAR` | 924.0921 | `EXIT_LONG_STOCH_80` | HOLD |
| `BNBUSDT` | 644.64 | 679.215399 | `-5.09%` | `52.77` / `48.66` | `46.2` | `0.52` | `BULLISH_ENGULFING` | 623.625424 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.57e-06 | 5e-06 | `-5.69%` | `43.21` / `36.21` | `53.83` | `0.757` | `BEARISH_SHOOTING_STAR` | 4.36e-06 | `WATCH` | HOLD |
| `XRPUSDT` | 1.0349 | 1.107642 | `-6.57%` | `61.57` / `57.98` | `53.85` | `0.714` | `BEARISH_ENGULFING` | 0.98942052 | `WATCH` | HOLD |
| `HYPEUSDT` | 74.1 | 75.266329 | `-1.55%` | `89.29` / `89.39` | `64.27` | `0.948` | `BEARISH_SHOOTING_STAR` | 77.5086 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (85%) |
| `INJUSDT` | 8.213 | 7.778679 | `+5.58%` | `93.46` / `92.65` | `76.74` | `1.29` | `NONE` | 7.835202 | `EXIT_LONG_STOCH_80` | HOLD |
| `UNIUSDT` | 5.976 | 6.625211 | `-9.80%` | `50.0` / `40.57` | `52.09` | `0.642` | `NONE` | 5.701104 | `WATCH` | HOLD |
| `SUIUSDT` | 0.8209 | 0.836024 | `-1.81%` | `87.92` / `87.13` | `63.69` | `0.974` | `NONE` | 0.7831386 | `EXIT_LONG_STOCH_80` | HOLD |
| `INITUSDT` | 0.11724 | 0.151701 | `-22.72%` | `35.99` / `46.26` | `43.52` | `0.451` | `BULLISH_HAMMER` | 0.11184696 | `WATCH` | HOLD |
