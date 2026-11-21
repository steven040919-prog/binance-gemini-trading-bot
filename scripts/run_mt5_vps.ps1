<#
.SYNOPSIS
    Watchdog 24/7 de produccion para el Bot Adaptativo MetaTrader 5 (Exness) en Windows VPS.

.DESCRIPTION
    Supervisa la salud del terminal MetaTrader 5 (terminal64.exe), lanza el bot Python
    (src/mt5_bot.py), reinicia automaticamente ante cierres inesperados con backoff
    exponencial, rota los logs cuando superan el tamano maximo y soporta parada limpia
    mediante Ctrl+C o archivo centinela (logs/STOP_MT5_BOT).

.EXAMPLE
    .\scripts\run_mt5_vps.ps1 -AdaptiveAI -BaseIntervalMinutes 30

.EXAMPLE
    .\scripts\run_mt5_vps.ps1 -AdaptiveAI -DryRun -BaseIntervalMinutes 30
#>
[CmdletBinding()]
param(
    [string]$RepoRoot = "",
    [string]$PythonExe = "python",
    [string]$Mt5Path = "C:\Program Files\MetaTrader 5\terminal64.exe",
    [switch]$AdaptiveAI = $true,
    [int]$BaseIntervalMinutes = 30,
    [int]$IntervalSeconds = 300,
    [switch]$SeedHistory,
    [switch]$DryRun,
    [switch]$NoAutoStartMt5,
    [int]$Mt5StartupWaitSeconds = 15,
    [int]$InitialBackoffSeconds = 5,
    [int]$MaxBackoffSeconds = 300,
    [int]$HealthyRunResetSeconds = 300,
    [int]$MaxLogSizeMB = 10,
    [int]$MaxLogBackups = 5,
    [string]$StopFile = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Resolver raiz del repositorio
if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
    $ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
    $RepoRoot = (Resolve-Path (Join-Path $ScriptDir "..")).Path
} else {
    $RepoRoot = (Resolve-Path $RepoRoot).Path
}

$LogsDir = Join-Path $RepoRoot "logs"
if (-not (Test-Path $LogsDir)) {
    New-Item -ItemType Directory -Path $LogsDir -Force | Out-Null
}

if ([string]::IsNullOrWhiteSpace($StopFile)) {
    $StopFile = Join-Path $LogsDir "STOP_MT5_BOT"
}

$WatchdogLog = Join-Path $LogsDir "mt5_vps_watchdog.log"
$BotLog = Join-Path $LogsDir "mt5_bot.log"
$BotStdoutLog = Join-Path $LogsDir "mt5_bot_stdout.log"
$BotStderrLog = Join-Path $LogsDir "mt5_bot_stderr.log"
$PidFile = Join-Path $LogsDir "mt5_vps_watchdog.pid"
$BotScript = Join-Path $RepoRoot "src\mt5_bot.py"

$script:StopRequested = $false
$script:CurrentBotProcess = $null

function Write-WatchdogLog {
    param(
        [string]$Message,
        [ValidateSet("INFO", "WARN", "ERROR")]
        [string]$Level = "INFO"
    )
    $ts = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd HH:mm:ss 'UTC'")
    $line = "$ts | $($Level.PadRight(5)) | watchdog | $Message"
    Write-Host $line
    try {
        Add-Content -Path $WatchdogLog -Value $line -Encoding UTF8
    } catch {
        Write-Warning "No se pudo escribir en ${WatchdogLog}: $_"
    }
}

function Invoke-LogRotation {
    param(
        [string]$FilePath,
        [int]$MaxSizeMB = 10,
        [int]$MaxBackups = 5
    )
    if (-not (Test-Path $FilePath)) {
        return
    }
    try {
        $item = Get-Item -Path $FilePath -ErrorAction Stop
        $maxBytes = [int64]$MaxSizeMB * 1MB
        if ($item.Length -lt $maxBytes) {
            return
        }

        # Eliminar el respaldo mas antiguo
        $oldest = "$FilePath.$MaxBackups"
        if (Test-Path $oldest) {
            Remove-Item -Path $oldest -Force -ErrorAction SilentlyContinue
        }

        # Desplazar respaldos existentes (.4 -> .5, ..., .1 -> .2)
        for ($i = $MaxBackups - 1; $i -ge 1; $i--) {
            $src = "$FilePath.$i"
            $dst = "$FilePath.$($i + 1)"
            if (Test-Path $src) {
                Move-Item -Path $src -Destination $dst -Force -ErrorAction SilentlyContinue
            }
        }

        # Rotar archivo actual a .1
        Move-Item -Path $FilePath -Destination "$FilePath.1" -Force -ErrorAction Stop
        New-Item -ItemType File -Path $FilePath -Force | Out-Null
    } catch {
        # Si otro proceso tiene el archivo abierto, omitir hasta el proximo ciclo
        Write-Warning "Rotacion omitida para ${FilePath}: $_"
    }
}

function Rotate-AllLogs {
    foreach ($logFile in @($WatchdogLog, $BotLog, $BotStdoutLog, $BotStderrLog)) {
        Invoke-LogRotation -FilePath $logFile -MaxSizeMB $MaxLogSizeMB -MaxBackups $MaxLogBackups
    }
}

function Test-Mt5TerminalRunning {
    $procs = Get-Process -Name "terminal64" -ErrorAction SilentlyContinue
    if ($null -eq $procs) {
        return $false
    }
    foreach ($p in @($procs)) {
        try {
            if (-not $p.HasExited -and $p.Responding) {
                return $true
            }
        } catch {
            # Algunos procesos elevados no exponen Responding; si existe, asumimos activo
            return $true
        }
    }
    return $false
}

function Ensure-Mt5TerminalHealthy {
    if (Test-Mt5TerminalRunning) {
        return $true
    }

    if ($NoAutoStartMt5) {
        Write-WatchdogLog "MetaTrader 5 (terminal64.exe) no esta en ejecucion y -NoAutoStartMt5 esta activo." "WARN"
        return $false
    }

    if (-not (Test-Path $Mt5Path)) {
        Write-WatchdogLog "No se encontro el ejecutable de MetaTrader 5 en '$Mt5Path'." "ERROR"
        return $false
    }

    Write-WatchdogLog "MetaTrader 5 no detectado. Iniciando terminal desde '$Mt5Path'..." "WARN"
    try {
        Start-Process -FilePath $Mt5Path -WorkingDirectory (Split-Path -Parent $Mt5Path) | Out-Null
        $waited = 0
        while ($waited -lt $Mt5StartupWaitSeconds) {
            if ($script:StopRequested -or (Test-Path $StopFile)) {
                return $false
            }
            Start-Sleep -Seconds 1
            $waited++
            if (Test-Mt5TerminalRunning) {
                Write-WatchdogLog "MetaTrader 5 iniciado correctamente (${waited}s). Esperando estabilizacion de conexion (5s)..." "INFO"
                Start-Sleep -Seconds 5
                return $true
            }
        }
        Write-WatchdogLog "MetaTrader 5 no respondio tras ${Mt5StartupWaitSeconds}s de espera." "WARN"
        return (Test-Mt5TerminalRunning)
    } catch {
        Write-WatchdogLog "Error al iniciar MetaTrader 5: $_" "ERROR"
        return $false
    }
}

function Stop-BotProcessGracefully {
    param(
        [System.Diagnostics.Process]$Process,
        [int]$TimeoutSeconds = 15
    )
    if ($null -eq $Process) {
        return
    }
    try {
        if ($Process.HasExited) {
            return
        }
        Write-WatchdogLog "Solicitando cierre limpio del proceso bot (PID=$($Process.Id))..." "INFO"
        try {
            $null = $Process.CloseMainWindow()
        } catch {
            # Proceso de consola sin ventana principal
        }
        if (-not $Process.WaitForExit($TimeoutSeconds * 1000)) {
            Write-WatchdogLog "El proceso bot (PID=$($Process.Id)) no termino en ${TimeoutSeconds}s; finalizando..." "WARN"
            Stop-Process -Id $Process.Id -Force -ErrorAction SilentlyContinue
            $Process.WaitForExit(5000) | Out-Null
        }
    } catch {
        Write-WatchdogLog "Error al detener proceso bot: $_" "WARN"
    }
}

function Test-ExistingWatchdog {
    if (-not (Test-Path $PidFile)) {
        return $false
    }
    try {
        $existingPidText = (Get-Content -Path $PidFile -ErrorAction Stop | Select-Object -First 1).Trim()
        if ($existingPidText -match '^\d+$') {
            $existingPid = [int]$existingPidText
            if ($existingPid -ne $PID) {
                $existingProc = Get-Process -Id $existingPid -ErrorAction SilentlyContinue
                if ($null -ne $existingProc -and -not $existingProc.HasExited) {
                    return $true
                }
            }
        }
    } catch {
        # PID file invalido o corrupto; continuar
    }
    return $false
}

function Build-BotArguments {
    $argsList = [System.Collections.Generic.List[string]]::new()
    $argsList.Add($BotScript)
    $argsList.Add("--loop")
    if ($AdaptiveAI) {
        $argsList.Add("--adaptive-ai")
        $argsList.Add("--base-interval-minutes")
        $argsList.Add([string]([Math]::Max(5, $BaseIntervalMinutes)))
    } else {
        $argsList.Add("--interval")
        $argsList.Add([string]([Math]::Max(30, $IntervalSeconds)))
    }
    if ($SeedHistory) {
        $argsList.Add("--seed-history")
    }
    if ($DryRun) {
        $argsList.Add("--dry-run")
    }
    return $argsList
}

# Verificar archivo principal del bot
if (-not (Test-Path $BotScript)) {
    Write-Error "No se encontro el script del bot en '$BotScript'."
    exit 1
}

# Evitar instancias duplicadas del watchdog
if (Test-ExistingWatchdog) {
    Write-WatchdogLog "Ya existe una instancia activa del watchdog registrada en '$PidFile'. Abortando duplicado." "WARN"
    exit 0
}

Set-Content -Path $PidFile -Value $PID -Encoding ASCII

# Registrar manejador de Ctrl+C para parada limpia
$cancelHandler = [ConsoleCancelEventHandler]{
    param($sender, $e)
    $e.Cancel = $true
    $script:StopRequested = $true
}
[Console]::add_CancelKeyPress($cancelHandler)

$backoffSeconds = [Math]::Max(1, $InitialBackoffSeconds)
$restartCount = 0

Write-WatchdogLog "=== Watchdog MT5 VPS iniciado (PID=$PID, Repo='$RepoRoot') ===" "INFO"
Write-WatchdogLog "Configuracion: AdaptiveAI=$AdaptiveAI, BaseIntervalMinutes=$BaseIntervalMinutes, DryRun=$DryRun, SeedHistory=$SeedHistory, StopFile='$StopFile'" "INFO"

try {
    while (-not $script:StopRequested) {
        if (Test-Path $StopFile) {
            Write-WatchdogLog "Archivo centinela de parada detectado ('$StopFile'). Finalizando watchdog limpiamente." "INFO"
            break
        }

        Rotate-AllLogs

        # Verificar salud de MetaTrader 5 antes de arrancar el bot
        $mt5Ready = Ensure-Mt5TerminalHealthy
        if (-not $mt5Ready) {
            Write-WatchdogLog "MT5 no disponible. Reintentando en ${backoffSeconds}s..." "WARN"
            for ($s = 0; $s -lt $backoffSeconds; $s++) {
                if ($script:StopRequested -or (Test-Path $StopFile)) { break }
                Start-Sleep -Seconds 1
            }
            $backoffSeconds = [Math]::Min($MaxBackoffSeconds, $backoffSeconds * 2)
            continue
        }

        $botArgs = Build-BotArguments
        # --seed-history solo se ejecuta en el primer arranque exitoso para evitar re-sembrar en cada reinicio
        $seedUsedThisLaunch = $SeedHistory.IsPresent
        Write-WatchdogLog "Lanzando bot: $PythonExe $($botArgs -join ' ')" "INFO"

        $startTime = Get-Date
        $proc = $null
        try {
            $proc = Start-Process `
                -FilePath $PythonExe `
                -ArgumentList $botArgs `
                -WorkingDirectory $RepoRoot `
                -NoNewWindow `
                -RedirectStandardOutput $BotStdoutLog `
                -RedirectStandardError $BotStderrLog `
                -PassThru
            $script:CurrentBotProcess = $proc
            Write-WatchdogLog "Bot iniciado con PID=$($proc.Id)." "INFO"
        } catch {
            Write-WatchdogLog "No se pudo lanzar el proceso Python ('$PythonExe'): $_" "ERROR"
            $backoffSeconds = [Math]::Min($MaxBackoffSeconds, $backoffSeconds * 2)
            Start-Sleep -Seconds $backoffSeconds
            continue
        }

        $lastMaintenance = Get-Date
        while (-not $proc.HasExited) {
            if ($script:StopRequested -or (Test-Path $StopFile)) {
                Write-WatchdogLog "Senal de parada recibida mientras el bot esta activo." "INFO"
                Stop-BotProcessGracefully -Process $proc
                break
            }

            # Mantenimiento periodico cada 60s: rotacion de logs y chequeo de salud MT5
            if (((Get-Date) - $lastMaintenance).TotalSeconds -ge 60) {
                $lastMaintenance = Get-Date
                Rotate-AllLogs
                if (-not (Test-Mt5TerminalRunning)) {
                    Write-WatchdogLog "MetaTrader 5 se cerro mientras el bot estaba corriendo. Intentando recuperacion de MT5..." "WARN"
                    Ensure-Mt5TerminalHealthy | Out-Null
                }
            }

            Start-Sleep -Seconds 2
        }

        $script:CurrentBotProcess = $null
        $elapsedSeconds = [int]((Get-Date) - $startTime).TotalSeconds

        if ($script:StopRequested -or (Test-Path $StopFile)) {
            break
        }

        $exitCode = $proc.ExitCode
        if ($exitCode -eq 0) {
            Write-WatchdogLog "El bot finalizo limpiamente con codigo 0 tras ${elapsedSeconds}s. Saliendo del watchdog." "INFO"
            break
        }

        if ($seedUsedThisLaunch -and $elapsedSeconds -ge $HealthyRunResetSeconds) {
            $SeedHistory = $false
        }

        $restartCount++
        if ($elapsedSeconds -ge $HealthyRunResetSeconds) {
            $backoffSeconds = [Math]::Max(1, $InitialBackoffSeconds)
        }

        Write-WatchdogLog "El bot termino inesperadamente (ExitCode=$exitCode, Duracion=${elapsedSeconds}s, Reinicio=#$restartCount). Esperando ${backoffSeconds}s antes de reiniciar..." "ERROR"

        for ($s = 0; $s -lt $backoffSeconds; $s++) {
            if ($script:StopRequested -or (Test-Path $StopFile)) { break }
            Start-Sleep -Seconds 1
        }
        $backoffSeconds = [Math]::Min($MaxBackoffSeconds, $backoffSeconds * 2)
    }
} finally {
    if ($null -ne $script:CurrentBotProcess) {
        Stop-BotProcessGracefully -Process $script:CurrentBotProcess
    }
    try {
        [Console]::remove_CancelKeyPress($cancelHandler)
    } catch {
        # Ignorar al cerrar
    }
    if (Test-Path $PidFile) {
        Remove-Item -Path $PidFile -Force -ErrorAction SilentlyContinue
    }
    Write-WatchdogLog "=== Watchdog MT5 VPS detenido correctamente ===" "INFO"
}

exit 0
