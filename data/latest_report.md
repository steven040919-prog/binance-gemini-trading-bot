# Reporte Autonomo - Estrategia Dual Spot + Futuros (EMA 200 + Estocastico + Pilares Cuantitativos 1H)

- **Ultima actualizacion (UTC):** `2026-11-11T16:09:11Z`
- **Ciclo de ejecucion:** `#134`
- **Modo:** `CUENTA REAL DUAL (SPOT + FUTUROS USDT-M)`
- **Temporalidad:** `1h` | **Riesgo Inicial:** `1.0% (min $1.00 USD)`
- **Capital Total Estimado:** `14.00 USDT`
- **Liquidez Disponible:** `14.00 USDT`
- **Rendimiento Diario (UTC):** `-0.01%`
- **Regimen de Mercado (Gemini 3.8 Flash):** `BEARISH`

## Lectura de Mercado de Gemini AI
> El mercado muestra una tendencia bajista predominante con la mayoría de los activos operando por debajo de la EMA 200. Se identifica una oportunidad de entrada SHORT en NEARUSDT bajo el Pilar S1 (Rechazo en EMA 200) debido a la confluencia de sobrecompra estocástica y patrón de vela bajista. ONEUSDT presenta una señal de compra bajo el Pilar P1 (Pullback EMA 200) con patrón de martillo alcista. No hay posiciones abiertas actualmente, por lo que no se requieren ajustes dinámicos.

## Posiciones Abiertas (LONG Spot/Futuros & SHORT Futuros con SL/TP Dinamicos)
_No hay posiciones abiertas en este momento._

## Operaciones y Ajustes de SL/TP en este Ciclo
_Ninguna orden o ajuste ejecutado en este ciclo._

## Escaneo Cuantitativo 1H (Pilares LONG P1-P4 + Pilar SHORT S1 en Futuros USDT-M)
| Par | Precio | EMA 200 | Dist EMA | Estocastico (%K / %D) | RSI(14) | BB %B | Vela (1H) | SL (ATR) | Pilar / Setup | Decision IA |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `ZECUSDT` | 995.17 | 1189.495183 | `-16.34%` | `29.46` / `27.15` | `41.06` | `0.393` | `BEARISH_SHOOTING_STAR` | 949.39218 | `WATCH` | HOLD |
| `PEPEUSDT` | 4.97e-06 | 5e-06 | `-1.87%` | `8.1` / `7.96` | `35.15` | `0.203` | `BEARISH_SHOOTING_STAR` | 4.74e-06 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ONEUSDT` | 0.001586 | 0.001557 | `+1.89%` | `15.6` / `11.77` | `42.28` | `0.302` | `BULLISH_HAMMER` | 0.00151304 | `P1_EMA200_PULLBACK` | **BUY** (79%) |
| `TRXUSDT` | 0.3165 | 0.317499 | `-0.31%` | `14.44` / `19.54` | `31.05` | `-0.13` | `NONE` | 0.308271 | `EXIT_SHORT_STOCH_20` | HOLD |
| `BTCUSDT` | 74064.03 | 75630.901535 | `-2.07%` | `53.79` / `54.44` | `52.55` | `0.886` | `NONE` | 72138.36522 | `WATCH` | HOLD |
| `XAUTUSDT` | 3997.42 | 4035.054663 | `-0.93%` | `6.79` / `13.13` | `26.29` | `-0.053` | `BULLISH_HAMMER` | 3893.48708 | `EXIT_SHORT_STOCH_20` | HOLD |
| `ETHUSDT` | 2073.91 | 2179.787546 | `-4.86%` | `56.0` / `49.15` | `53.39` | `0.981` | `BULLISH_HAMMER` | 2014.120914 | `WATCH` | HOLD |
| `PAXGUSDT` | 4000.34 | 4040.688586 | `-1.00%` | `7.42` / `13.67` | `26.4` | `-0.056` | `NONE` | 3896.33116 | `EXIT_SHORT_STOCH_20` | HOLD |
| `MUBUSDT` | 813.9 | 751.304788 | `+8.33%` | `94.88` / `94.15` | `76.91` | `1.017` | `NONE` | 776.4606 | `EXIT_LONG_STOCH_80` | HOLD |
| `SOLUSDT` | 84.7 | 88.543388 | `-4.34%` | `76.7` / `80.66` | `56.57` | `0.966` | `BULLISH_ENGULFING` | 81.99988 | `EXIT_LONG_STOCH_80` | HOLD |
| `NEARUSDT` | 3.754 | 3.770642 | `-0.44%` | `72.36` / `75.77` | `58.6` | `0.817` | `BEARISH_SHOOTING_STAR` | 3.926684 | `S1_EMA200_RESISTANCE_REJECT` | **SHORT** (82%) |
| `SNXXBUSDT` | 4.51 | 4.165363 | `+8.27%` | `94.42` / `92.21` | `74.72` | `1.005` | `NONE` | 4.30254 | `EXIT_LONG_STOCH_80` | HOLD |
| `XRPUSDT` | 1.0701 | 1.149388 | `-6.90%` | `65.34` / `62.38` | `54.06` | `1.055` | `BULLISH_ENGULFING` | 1.03258212 | `WATCH` | HOLD |
| `UNIUSDT` | 6.54 | 6.954133 | `-5.96%` | `35.8` / `31.05` | `44.13` | `0.447` | `NONE` | 6.23916 | `WATCH` | HOLD |
| `RLUSDUSDT` | 1.0009 | 1.001189 | `-0.03%` | `33.33` / `34.92` | `42.18` | `0.21` | `BEARISH_SHOOTING_STAR` | 0.9748766 | `WATCH` | HOLD |
| `GRAMUSDT` | 1.177 | 1.116105 | `+5.46%` | `50.72` / `67.73` | `54.73` | `0.569` | `NONE` | 1.122858 | `WATCH` | HOLD |
