# Reporte Autonomo MetaTrader 5 (Exness) - Estrategia Cuantitativa 1H (LONG & SHORT)

- **Ultima actualizacion:** `2026-11-21 18:49:04 UTC` | **Ciclo:** `#25`
- **Cuenta Exness:** `478600800` (`Exness-MT5Real11`) | **Apalancamiento:** `1:200`
- **Balance:** `$580.68 USD` | **Equity:** `$580.68 USD` | **Margen Libre:** `$580.68 USD`
- **Nivel de Capital:** `Fase 5 (>= $400 USD) — B_FINAL_HYBRID_ADX (Max 3 posiciones, riesgo proporcional 1.00% / max 1.25%, veto SL >20%)`

## Lectura de Mercado y Asistencia Gemini AI
- **Modo IA del Ciclo:** `GENERAL` | **Modelo utilizado:** `quant_local`
- **Pulso Macro 360°:** Dolar: `USD_STRONG_BULLISH` (`6/1`) | Cripto (BTC/ETH): `CRYPTO_ALIGNED_BEARISH` | Wall Street: `WALL_STREET_BEARISH` | Sesion/Noticias: `NUEVA_YORK` (`ALERTA VOLATILIDAD/NOTICIAS`)
- **Candado Diario / Racha (`2026-11-21`):** `NORMAL` | PnL Cerrado Hoy: `$+0.00 USD` | Racha Perdidas: `0` (ultima: `N/A`) | Umbral IA: `60%` | Escala Riesgo: `1.00x` | Max Pos: `4`
> Sin eventos relevantes en este ciclo (0 llamadas API, event-driven).

## Posiciones Abiertas en Exness MT5
_No hay posiciones abiertas en este momento._

## Evaluaciones IA Post-Cierre y Bloqueos Activos (90 Minutos)
_Ningun simbolo bloqueado por IA en este momento._

### Ultimas Evaluaciones Post-Cierre (Manual / Positivo / Negativo)
- `2026-11-20 21:46 UTC` | **USDCHFm** (`#266640655`, `POSITIVE`, `$+0.54`) -> Prob. IA: **51%** -> **BLOQUEADO 30m** (Cierre reciente positivo con patrones de velas bajistas (Bearish Engulfing) y estocástico girando a la baja cerca de zona media. Rollover activo con spreads elevados y distancia superior a 2.5 ATR sobre EMA200 aconsejan esperar corrección profunda antes de reenganchar.)
- `2026-11-19 19:31 UTC` | **NZDUSDm** (`#265862768`, `POSITIVE`, `$+2.76`) -> Prob. IA: **52%** -> **BLOQUEADO 90m** (Cierre positivo reciente hace menos de 90 minutos. Aunque la estructura es bajista, el estocástico en zona de sobreventa (9.9) sugiere un posible rebote técnico a corto plazo. Se recomienda esperar a que el estocástico gire al alza o el precio se acerque a la EMA200.)
- `2026-11-19 17:35 UTC` | **ETHUSDm** (`#265796844`, `POSITIVE`, `$+1.98`) -> Prob. IA: **75%** -> **HABILITADO (>=60%)** (4H BEARISH a favor; estructura 1H alineada; MACD a favor; cierre POSITIVO reciente (2m); BTC+ETH alineados)
- `2026-11-19 15:44 UTC` | **EURUSDm** (`#265702458`, `POSITIVE`, `$+0.42`) -> Prob. IA: **64%** -> **HABILITADO (>=60%)** (4H BEARISH a favor; estructura 1H alineada; tendencia 1H sobre-extendida (-5.7x ATR); MACD a favor; espacio bajista en Estocastico; cierre POSITIVO reciente (1m); bloque USD alineado)
- `2026-11-19 15:05 UTC` | **US500m** (`#265657478`, `POSITIVE`, `$+0.57`) -> Prob. IA: **49%** -> **BLOQUEADO 90m** (Cierre positivo reciente y alta volatilidad en índices. Se requiere esperar el periodo de enfriamiento de 90 minutos para evitar trampas de mercado.)
- `2026-11-19 10:08 UTC` | **USTECm** (`#265519450`, `NEGATIVE`, `$-4.54`) -> Prob. IA: **45%** -> **BLOQUEADO 90m** (Cierre NEGATIVO reciente hace apenas un minuto con patrón de velas alcista (BULLISH_ENGULFING) y tendencia de 4H neutral, lo que sugiere evitar la reentrada inmediata.)

## Escaneo en Vivo MetaTrader 5 (1H - Forex, Indices y Cripto compatibles con tu margen)
| Simbolo | Bid / Ask | Spread | Margen (0.01) | EMA 200 | Dist (ATR) | Stoch (%K/%D) | RSI(14) | BB %B | Patron 1H | Pilar / Setup |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `EURUSDm` | 1.09668 | `20` | `$5.48` | 1.10302 | `-5.25x` | `26.39`/`32.87` | `44.32` | `0.26` | `BEARISH_ENGULFING` | **`WATCH`** |
| `GBPUSDm` | 1.30859 | `38` | `$6.54` | 1.32033 | `-8.72x` | `8.75`/`14.11` | `35.22` | `-0.031` | `NONE` | **`WATCH`** |
| `USDJPYm` | 158.538 | `18` | `$5.00` | 159.2 | `-3.08x` | `19.53`/`26.75` | `30.95` | `0.086` | `BEARISH_ENGULFING` | **`WATCH`** |
| `AUDUSDm` | 0.66189 | `9` | `$3.31` | 0.67552 | `-10.52x` | `9.4`/`9.25` | `25.33` | `-0.055` | `NONE` | **`WATCH`** |
| `NZDUSDm` | 0.54706 | `14` | `$2.74` | 0.55236 | `-6.09x` | `8.69`/`8.24` | `30.53` | `-0.095` | `BULLISH_HAMMER` | **`WATCH`** |
| `USDCADm` | 1.43417 | `18` | `$5.00` | 1.42657 | `+5.68x` | `87.3`/`83.11` | `63.16` | `1.1` | `BULLISH_ENGULFING` | **`WATCH`** |
| `USDCHFm` | 0.83999 | `13` | `$5.00` | 0.83713 | `+2.16x` | `33.81`/`35.62` | `41.47` | `0.251` | `BEARISH_ENGULFING` | **`WATCH`** |
| `EURGBPm` | 0.83801 | `19` | `$5.48` | 0.83535 | `+4.42x` | `83.75`/`76.89` | `61.41` | `0.87` | `BULLISH_ENGULFING` | **`WATCH`** |
| `EURJPYm` | 173.866 | `100` | `$5.48` | 175.605 | `-6.96x` | `12.28`/`19.42` | `28.08` | `0.022` | `BULLISH_HAMMER` | **`WATCH`** |
| `US500m` | 6957.93 | `40` | `$4.87` | 7391.88 | `-8.64x` | `11.68`/`11.7` | `21.18` | `-0.158` | `BEARISH_ENGULFING` | **`WATCH`** |
| `USTECm` | 25250.95 | `112` | `$6.31` | 27315.78 | `-7.93x` | `10.57`/`10.69` | `20.27` | `-0.113` | `BEARISH_ENGULFING` | **`WATCH`** |
| `BTCUSDm` | 59989.41 | `640` | `$3.00` | 64039.94 | `-4.53x` | `83.16`/`85.28` | `56.28` | `0.796` | `BEARISH_SHOOTING_STAR` | **`WATCH`** |
| `ETHUSDm` | 1678.84 | `100` | `$0.84` | 1801.99 | `-4.44x` | `81.38`/`83.65` | `55.86` | `0.782` | `BULLISH_HAMMER` | **`WATCH`** |
| `XAUUSDm` | 3540.063 | `240` | `$17.70` | 3808.485 | `-9.51x` | `27.59`/`28.29` | `29.27` | `0.108` | `BULLISH_HAMMER` | **`WATCH`** |
