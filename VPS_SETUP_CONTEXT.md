# Contexto de Despliegue en VPS e Instrucciones para Antigravity

Este archivo resume las decisiones, la arquitectura y las instrucciones acordadas para instalar y operar el bot en el **VPS Windows** y mantener respaldos versionados.

---

## 1. Resumen del Proyecto
- **Motor activo:** `src/mt5_bot.py` en **Modo Adaptativo IA (`--adaptive-ai`)** para **Exness MetaTrader 5** (multi-estrategia + aprendizaje en SQLite `data/mt5_learning.db` + agente Gemini en `src/gemini_agent.py` + `src/mt5_ai_brain.py` + `src/mt5_adaptive_scheduler.py`).
- **Importante:** En el VPS usar **únicamente el modo adaptativo (`--adaptive-ai`)**, NO el modo clásico (`--interval 300`).
- **Inicio en Windows:** `start_mt5_bot.bat` ejecuta:
  ```bat
  python src/mt5_bot.py --loop --adaptive-ai --seed-history
  ```
- **Dependencias:** `requirements.txt` (`requests`, `PySocks`, `python-dotenv`, `pytest`) + la librería oficial `MetaTrader5`.

---

## 2. Entorno del VPS Elegido
- **Proveedor / Plan:** VPS-Mart Basic (4 CPU Cores, 8 GB RAM, 140 GB SSD, 1 IPv4 dedicada).
- **Sistema Operativo:** Windows Server 2025 x64.
- **Nota operativa:** No usar MQL5 VPS (no soporta Python). Cerrar Antigravity cuando no se esté editando código para dejar libre la RAM del servidor.

---

## 3. Guía de Instalación en el VPS (cuando se abra este proyecto en el VPS)
Si el usuario te pide **"instala y deja corriendo el bot en el VPS"**, sigue estos pasos:

1. **Verificar / Instalar Python 3.10+ (64 bits):**
   - Comprobar con `python --version`. Si falta, instalar Python 64 bits marcado con *Add to PATH*.
2. **Instalar dependencias:**
   ```powershell
   pip install -r requirements.txt
   pip install MetaTrader5
   ```
3. **Verificar MetaTrader 5 (Exness):**
   - El usuario debe haber descargado e iniciado sesión manualmente en el terminal **MetaTrader 5 de Exness** dentro del VPS (con trading algorítmico habilitado).
   - Comprobar desde Python que `MetaTrader5.initialize()` conecta correctamente con el terminal abierto.
4. **Configurar `.env`:**
   - El archivo `.env` **no** está incluido en GitHub ni en los respaldos `.zip` de Google Drive por seguridad.
   - El usuario debe copiar su `.env` local al VPS (o crearlo usando `.env.example` como base y rellenando su `GEMINI_API_KEY` y demás variables de MT5/estrategia).
5. **Arranque y ejecución 24/7:**
   - Actualizar la ruta en `start_mt5_bot.bat` si el proyecto se ubicó en una carpeta distinta a `c:\Users\CINDEA\Documents\Crypto`.
   - Probar ejecución inicial y, si el usuario lo desea, configurar una tarea en el **Programador de Tareas de Windows** (Task Scheduler) para que el bot arranque automáticamente si el VPS se reinicia.

---

## 4. Política Obligatoria de Respaldos y Versiones
Cada vez que se realicen cambios en el código del bot:
1. **GitHub (`origin/main` + tag):**
   - Hacer `git add`, `git commit` con mensaje claro y crear un nuevo tag secuencial (`v1.0.2`, `v1.0.3`, etc.).
   - Ejecutar `git push origin main --tags` hacia `https://github.com/steven040919-prog/binance-gemini-trading-bot.git`.
2. **Google Drive (`Backups_MT5_Bot`):**
   - Generar un `.zip` limpio de esa versión con `git archive --format=zip --output=mt5-bot-vX.Y.Z-YYYY-MM-DD.zip vX.Y.Z` (excluye `.env` por seguridad).
   - Subirlo a la carpeta de Google Drive **Backups_MT5_Bot** (ID: `1WRNaUJ0E18MhCtMvItE86UJZkR1lCdC2`).

---

## 5. Historial de Versiones
- **v1.0.0 (2026-11-21):** Respaldo inicial completo del bot MT5 Exness + agente Gemini (`3ef6ef4`).
- **v1.0.1 (2026-11-22):** Agregado `VPS_SETUP_CONTEXT.md` con contexto del proyecto, guía de instalación en VPS y política de respaldos.
- **v1.0.2 (2026-11-22):** Configurado arranque exclusivo en Modo Adaptativo (`--adaptive-ai --seed-history`) e incluidos los últimos cambios y `tests/test_mt5_adaptive_bot.py`.
- **v1.0.3 (2026-11-23):** Agregada tercera estrategia `SUPERVISED_M15_SCALPER` (`src/mt5_scalper_profiles.py`, `src/mt5_strategies.py`, `src/mt5_bot.py`) con perfiles personalizados para los 14 activos, ventana horaria estricta 08:00-23:00 hora local (UTC-6) para nuevas entradas con gestión 24/7 de posiciones abiertas, lanzador `start_mt5_scalper.bat` y 16 pruebas en `tests/test_mt5_supervised_scalper.py`.
