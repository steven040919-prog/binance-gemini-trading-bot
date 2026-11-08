# Bot Autónomo de Trading Spot en Binance + Google Gemini AI (24/7 en GitHub)

Este proyecto implementa un **bot autónomo cuantitativo para Binance Spot** impulsado por **Google Gemini AI**, diseñado para ejecutarse automáticamente **24/7 mediante GitHub Actions** sin intervención humana y con **reglas estrictas de gestión de riesgo**.

---

## Características Principales

1. **Escaneo Dinámico de Mercado (`USDT` Spot):**
   - Analiza automáticamente los pares de mayor liquidez y movimiento en Binance Spot, descartando stablecoins, tokens apalancados y pares sin liquidez.
   - Calcula indicadores técnicos multi-temporalidad (`15m` y `1h`): **RSI (14)**, **EMA (9, 21, 50)**, **MACD (12, 26, 9)**, **Bandas de Bollinger (%B)**, **ATR (%)**, **Ratio de Volumen** y **Soportes/Resistencias**.
2. **Cerebro Cuantitativo con Google Gemini AI:**
   - Evalúa el estado real de tu cartera, posiciones abiertas, PnL diario e indicadores técnicos para emitir decisiones estructuradas (`BUY`, `SELL`, `HOLD`) con nivel de confianza.
3. **Doble Capa de Seguridad (Guardarraíles Deterministas):**
   - **Stop-Loss Estricto (`3.5%` por defecto):** Cierra automáticamente cualquier posición que caiga por debajo del límite permitido, antes incluso de consultar a la IA.
   - **Take-Profit (`7.0%`) y Trailing Stop (`2.5%`):** Asegura ganancias automáticamente cuando el precio sube y retrocede desde su máximo.
   - **Límite por Operación (`MAX_POSITION_PCT = 25%`) y Máximo de Posiciones (`MAX_OPEN_POSITIONS = 3`):** Impide concentrar toda la cuenta en una sola moneda.
   - **Cortacircuitos Diario (`MAX_DAILY_DRAWDOWN_PCT = 6%`):** Si el capital diario retrocede más del límite, bloquea nuevas compras por el resto del día UTC.
4. **Persistencia y Reporte en Vivo en el Repositorio:**
   - Guarda el estado en [`data/bot_state.json`](data/bot_state.json), el historial de operaciones en [`data/trade_history.json`](data/trade_history.json) y actualiza un tablero visual en [`data/latest_report.md`](data/latest_report.md) en cada ciclo.

---

## Cómo Desplegarlo 24/7 en tu Repositorio de GitHub

### Paso 1: Crear tus API Keys de Binance con Seguridad
1. Entra a **Binance -> Gestión de API (API Management)** y crea una clave API.
2. Marca **únicamente**:
   - `Enable Reading` (Lectura)
   - `Enable Spot & Margin Trading` (Trading Spot)
3. **NUNCA actives `Enable Withdrawals` (Retiros).** Así nadie puede retirar fondos con la API key.

### Paso 2: Obtener tu API Key de Google Gemini
1. Entra a [Google AI Studio](https://aistudio.google.com/apikey) y genera tu `GEMINI_API_KEY`.

### Paso 3: Configurar los Secrets en tu Repositorio de GitHub
En tu repositorio de GitHub (recomendado que sea **Privado** o con Secrets protegidos), ve a:
**`Settings` -> `Secrets and variables` -> `Actions` -> `New repository secret`** y agrega:

| Nombre del Secret | Descripción | Obligatorio |
| :--- | :--- | :---: |
| `BINANCE_API_KEY` | Tu API Key de Binance Spot | Sí |
| `BINANCE_API_SECRET` | Tu Secret Key de Binance Spot | Sí |
| `GEMINI_API_KEY` | Tu API Key de Google Gemini | Sí |
| `BINANCE_PROXY_URL` | Proxy HTTP/SOCKS5 fuera de EE.UU. (ej. `http://user:pass@ip:port`) | Recomendado en GitHub Actions* |

> **Nota importante sobre `BINANCE_PROXY_URL` en GitHub Actions:**
> Los servidores gratuitos de GitHub Actions (`ubuntu-latest`) están alojados en centros de datos de EE.UU. Mientras que los datos públicos de mercado se leen sin bloqueo desde `https://data-api.binance.vision`, Binance suele devolver `HTTP 451` para órdenes privadas desde IPs de EE.UU. Configurar `BINANCE_PROXY_URL` con un proxy en Europa, Latinoamérica o Asia (o asociar esa IP estática en las restricciones de IP de tu API Key de Binance) garantiza que las órdenes se ejecuten sin bloqueo 24/7.

### Paso 4: Subir el Proyecto a GitHub y Activar GitHub Actions
Ejecuta en la terminal dentro de esta carpeta:
```bash
git init
git add .
git commit -m "feat: inicializar bot autonomo Binance + Gemini AI"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
git push -u origin main
```

Luego en GitHub:
1. Ve a la pestaña **`Actions`**.
2. Selecciona **Binance + Gemini AI Autonomous Trading Bot (24/7)**.
3. Haz clic en **`Run workflow`** para disparar el primer ciclo inmediatamente (a partir de ahí se ejecutará solo cada 15 minutos 24/7).
4. Revisa el archivo [`data/latest_report.md`](data/latest_report.md) en tu repositorio para ver el panel actualizado tras cada ciclo.

---

## Ejecución Local (Opcional)

1. Copia `.env.example` a `.env` y rellena tus claves:
   ```bash
   cp .env.example .env
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta un ciclo en modo simulación (`--dry-run`) o en bucle continuo (`--loop`):
   ```bash
   # Probar un ciclo en modo simulacion
   python main.py --dry-run

   # Ejecutar en bucle continuo cada 15 minutos en tu PC o VPS
   python main.py --loop --interval-minutes 15
   ```
