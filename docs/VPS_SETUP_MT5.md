# Guia de Despliegue 24/7 en Windows VPS — Bot Adaptativo MetaTrader 5 (Exness)

Esta guia resume los pasos exactos para poner en marcha el bot adaptativo de MetaTrader 5 con aprendizaje historico de 2 años y watchdog 24/7 en un VPS Windows.

---

## 1. Requisitos del VPS Windows

- **Sistema operativo:** Windows Server 2019/2022 o Windows 10/11 (64 bits).
- **Python:** 3.10 o superior (marcar *"Add Python to PATH"* durante la instalacion).
- **MetaTrader 5 (Exness):** instalado en la ruta estandar `C:\Program Files\MetaTrader 5\terminal64.exe` (o anotar la ruta personalizada para pasarla con `-Mt5Path`).
- **Conexion estable** y politica de energia configurada en *Alto rendimiento / Nunca suspender*.

---

## 2. Instalar dependencias Python

Abrir PowerShell en la carpeta del repositorio (ej. `C:\Bots\Crypto`):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install MetaTrader5 numpy
```

Verificar que el paquete `MetaTrader5` importe sin errores:

```powershell
python -c "import MetaTrader5 as mt5; print('MT5 Python OK:', mt5.__version__)"
```

---

## 3. Configurar variables de entorno (`.env`)

Copiar la plantilla `.env.example` a `.env` (nunca subir `.env` al repositorio):

```powershell
Copy-Item .env.example .env
notepad .env
```

Variables clave para el bot MT5:

```dotenv
# Obligatoria para el cerebro adaptativo Gemini AI
GEMINI_API_KEY=tu_clave_real_de_gemini

# Modelo Gemini preferido (el bot cuenta con cadena de fallback automatica)
GEMINI_MODEL=gemini-3.8-flash

# false para operar en vivo; true para simulacion sin ordenes reales
DRY_RUN=false
```

> [!TIP]
> Si solo vas a operar MetaTrader 5 en este VPS, no es necesario configurar claves de Binance.

---

## 4. Configurar el terminal MetaTrader 5 (Exness)

1. Abrir **MetaTrader 5** e iniciar sesion en tu cuenta **Exness** (Demo o Real) marcando **Guardar contraseña**.
2. Activar **Trading algoritmico** (boton verde *Algo Trading* en la barra superior).
3. Ir a **Herramientas → Opciones → Asesores Expertos**:
   - Marcar **Permitir trading algoritmico**.
   - Desmarcar *"Desactivar el trading algoritmico cuando se cambie de cuenta/perfil"* si no deseas pausas accidentales.
4. Ir a **Herramientas → Opciones → Graficos**:
   - Configurar **Max. barras en historial** y **Max. barras en grafico** en `Ilimitado` (necesario para descargar los 2 años completos de velas).
5. En **Observacion del Mercado** (`Ctrl+M`), asegurarte de mostrar todos los simbolos operados por el bot (`EURUSDm`, `GBPUSDm`, `USDJPYm`, `AUDUSDm`, `NZDUSDm`, `USDCADm`, `USDCHFm`, `EURGBPm`, `EURJPYm`, `US500m`, `USTECm`, `BTCUSDm`, `ETHUSDm`, `XAUUSDm`).

---

## 5. Sembrar el estudio historico de 2 años (`strategy_priors`)

Con MetaTrader 5 abierto y conectado a Exness, ejecuta el estudio historico de 2 años para evaluar todas las estrategias (IS Año 1 vs OOS Año 2) y poblar la base de conocimiento SQLite (`data/mt5_learning.db`):

```powershell
.\.venv\Scripts\Activate.ps1
python scripts/run_mt5_2yr_study.py
```

Tambien puedes ejecutar la siembra directamente desde el bot antes de entrar en produccion:

```powershell
python src/mt5_bot.py --adaptive-ai --seed-history --dry-run
```

Esto crea/actualiza `data/mt5_learning.db` con las estadisticas iniciales (*priors* bayesianos) por `(simbolo, estrategia, regimen, sesion)`.

---

## 6. Validacion rapida en simulacion (`--dry-run`)

Antes de activar dinero real, ejecuta 1 o 2 ciclos en modo simulacion para confirmar conexion IPC con MT5, lectura de simbolos, llamadas a Gemini AI y escritura en `data/mt5_learning.db`:

```powershell
.\scripts\run_mt5_vps.ps1 -PythonExe ".\.venv\Scripts\python.exe" -AdaptiveAI -BaseIntervalMinutes 15 -DryRun
```

Presiona `Ctrl+C` cuando confirmes que los ciclos corren sin errores.

---

## 7. Ejecucion 24/7 con el Watchdog y Programador de Tareas

### Ejecucion manual en consola PowerShell

```powershell
.\scripts\run_mt5_vps.ps1 -PythonExe ".\.venv\Scripts\python.exe" -AdaptiveAI -BaseIntervalMinutes 15
```

Parametros principales de `scripts/run_mt5_vps.ps1`:
- `-AdaptiveAI`: activa el motor multi-estrategia + cerebro adaptativo + despertares exactos (*sniper wake*).
- `-BaseIntervalMinutes 15`: cadencia base de patrullaje (15 o 30 minutos).
- `-Mt5Path "..."`: ruta alternativa a `terminal64.exe` si no esta en `C:\Program Files\MetaTrader 5\terminal64.exe`.
- `-DryRun`: modo simulacion.
- `-MaxLogSizeMB 10 -MaxLogBackups 5`: rotacion automatica de logs.

### Auto-arranque tras reinicio del VPS (Windows Task Scheduler)

1. Abrir **Programador de tareas** (`taskschd.msc`) → **Crear tarea...**.
2. **Pestaña General:**
   - Nombre: `MT5_Adaptive_Bot_Watchdog`
   - Seleccionar **Ejecutar solo cuando el usuario haya iniciado sesion** *(MetaTrader 5 requiere sesion interactiva de escritorio en Windows; configura auto-login del VPS si se reinicia automaticamente)*.
   - Marcar **Ejecutar con los privilegios mas altos**.
3. **Pestaña Desencadenadores:**
   - Nuevo → **Al iniciar sesion** (retrasar tarea `30 segundos` para dar tiempo a la red).
4. **Pestaña Acciones:**
   - Programa/script: `powershell.exe`
   - Argumentos:
     ```text
     -NoProfile -ExecutionPolicy Bypass -File "C:\Bots\Crypto\scripts\run_mt5_vps.ps1" -PythonExe "C:\Bots\Crypto\.venv\Scripts\python.exe" -AdaptiveAI -BaseIntervalMinutes 15
     ```
   - Iniciar en: `C:\Bots\Crypto`
5. **Pestaña Configuracion:**
   - Desmarcar *"Detener la tarea si se ejecuta durante mas de..."*.
   - Si la tarea ya esta en ejecucion: **No iniciar una nueva instancia**.

---

## 8. Monitoreo y parada limpia

- **Reporte en vivo:** `data/mt5_latest_report.md`
- **Base de aprendizaje SQLite:** `data/mt5_learning.db`
- **Logs del watchdog:** `logs/mt5_vps_watchdog.log`
- **Logs del bot:** `logs/mt5_bot.log`, `logs/mt5_bot_stdout.log`, `logs/mt5_bot_stderr.log`

Para **detener el bot de forma limpia** (sin matar procesos a la fuerza) desde otra terminal PowerShell:

```powershell
New-Item -ItemType File -Path ".\logs\STOP_MT5_BOT" -Force
```

El watchdog detectara el archivo `logs/STOP_MT5_BOT` en menos de 2 segundos, cerrara limpiamente el bot y finalizara. Antes de volver a arrancar el bot, elimina el archivo centinela:

```powershell
Remove-Item ".\logs\STOP_MT5_BOT" -Force
```
