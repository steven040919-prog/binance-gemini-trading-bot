from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv(dotenv_path: Path | None = None) -> bool:  # type: ignore[misc]
        if dotenv_path and dotenv_path.exists():
            for raw_line in dotenv_path.read_text(encoding="utf-8").splitlines():
                line = raw_line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip("'\""))
            return True
        return False

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def _env_bool(name: str, default: bool) -> bool:
    val = os.getenv(name)
    if val is None or val.strip() == "":
        return default
    return val.strip().lower() in ("1", "true", "yes", "on")


def _env_float(name: str, default: float) -> float:
    val = os.getenv(name)
    if val is None or val.strip() == "":
        return default
    return float(val.strip())


def _env_int(name: str, default: int) -> int:
    val = os.getenv(name)
    if val is None or val.strip() == "":
        return default
    return int(val.strip())


@dataclass(frozen=True)
class BotConfig:
    # Credenciales
    binance_api_key: str = field(default_factory=lambda: os.getenv("BINANCE_API_KEY", "").strip())
    binance_api_secret: str = field(default_factory=lambda: os.getenv("BINANCE_API_SECRET", "").strip())
    gemini_api_key: str = field(default_factory=lambda: os.getenv("GEMINI_API_KEY", "").strip())

    # Red / Proxy
    binance_proxy_url: str = field(default_factory=lambda: os.getenv("BINANCE_PROXY_URL", "").strip())

    # Modo de ejecucion (False = Cuenta Real Live por defecto)
    dry_run: bool = field(default_factory=lambda: _env_bool("DRY_RUN", False))
    gemini_model: str = field(default_factory=lambda: os.getenv("GEMINI_MODEL", "gemini-3.8-flash").strip() or "gemini-3.8-flash")

    # Mercado: "spot" (solo LONG) o "futures" (LONG y SHORT con EMA 200)
    trading_market: str = field(default_factory=lambda: os.getenv("TRADING_MARKET", "spot").strip().lower() or "spot")

    # Parametros de la Estrategia: EMA 200 + Estocastico (80/20) + Martillo/Envolvente en 1H
    kline_interval_primary: str = field(default_factory=lambda: os.getenv("KLINE_INTERVAL_PRIMARY", "1h").strip() or "1h")
    kline_interval_htf: str = field(default_factory=lambda: os.getenv("KLINE_INTERVAL_HTF", "4h").strip() or "4h")
    ema_trend_period: int = field(default_factory=lambda: _env_int("EMA_TREND_PERIOD", 200))
    stoch_k_period: int = field(default_factory=lambda: _env_int("STOCH_K_PERIOD", 14))
    stoch_smooth_k: int = field(default_factory=lambda: _env_int("STOCH_SMOOTH_K", 3))
    stoch_d_period: int = field(default_factory=lambda: _env_int("STOCH_D_PERIOD", 3))
    stoch_overbought: float = field(default_factory=lambda: _env_float("STOCH_OVERBOUGHT", 80.0))
    stoch_oversold: float = field(default_factory=lambda: _env_float("STOCH_OVERSOLD", 20.0))

    # Gestion de Riesgo del 1% del capital total (minimo $1 USD)
    quote_asset: str = field(default_factory=lambda: os.getenv("QUOTE_ASSET", "USDT").strip().upper() or "USDT")
    risk_per_trade_pct: float = field(default_factory=lambda: _env_float("RISK_PER_TRADE_PCT", 0.01))
    min_risk_usd: float = field(default_factory=lambda: _env_float("MIN_RISK_USD", 1.0))
    max_open_positions: int = field(default_factory=lambda: _env_int("MAX_OPEN_POSITIONS", 3))
    max_position_pct: float = field(default_factory=lambda: _env_float("MAX_POSITION_PCT", 0.85))
    min_order_usdt: float = field(default_factory=lambda: _env_float("MIN_ORDER_USDT", 5.5))
    min_usdt_reserve: float = field(default_factory=lambda: _env_float("MIN_USDT_RESERVE", 0.5))

    # Respaldo de Stop-Loss/Take-Profit si no hay vela previa
    stop_loss_pct: float = field(default_factory=lambda: _env_float("STOP_LOSS_PCT", 0.032))
    take_profit_pct: float = field(default_factory=lambda: _env_float("TAKE_PROFIT_PCT", 0.065))
    trailing_stop_pct: float = field(default_factory=lambda: _env_float("TRAILING_STOP_PCT", 0.025))
    trailing_activation_pct: float = field(default_factory=lambda: _env_float("TRAILING_ACTIVATION_PCT", 0.032))

    # Cortacircuitos diario
    max_daily_drawdown_pct: float = field(default_factory=lambda: _env_float("MAX_DAILY_DRAWDOWN_PCT", 0.050))

    # Escaneo dinamico
    top_candidates_limit: int = field(default_factory=lambda: _env_int("TOP_CANDIDATES_LIMIT", 16))
    min_24h_volume_usdt: float = field(default_factory=lambda: _env_float("MIN_24H_VOLUME_USDT", 8_000_000.0))
    min_ai_confidence: int = field(default_factory=lambda: _env_int("MIN_AI_CONFIDENCE", 70))

    # Rutas de persistencia en el repositorio
    data_dir: Path = field(default_factory=lambda: BASE_DIR / "data")
    state_file: Path = field(default_factory=lambda: BASE_DIR / "data" / "bot_state.json")
    history_file: Path = field(default_factory=lambda: BASE_DIR / "data" / "trade_history.json")
    report_file: Path = field(default_factory=lambda: BASE_DIR / "data" / "latest_report.md")

    def validate(self) -> None:
        missing = []
        if not self.binance_api_key and not self.dry_run:
            missing.append("BINANCE_API_KEY")
        if not self.binance_api_secret and not self.dry_run:
            missing.append("BINANCE_API_SECRET")
        if not self.gemini_api_key:
            missing.append("GEMINI_API_KEY")
        if missing:
            raise ValueError(
                f"Faltan variables de entorno obligatorias: {', '.join(missing)}. "
                "Configuralas en GitHub Secrets o en tu archivo .env local."
            )
        if not (0.001 <= self.risk_per_trade_pct <= 0.20):
            raise ValueError("RISK_PER_TRADE_PCT debe estar entre 0.001 (0.1%) y 0.20 (20%).")
