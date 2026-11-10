from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime, timezone

from src.bot_engine import AutonomousTradingBot
from src.config import BotConfig


def is_local_pc_active(state_file_path, max_idle_minutes: float = 20.0) -> tuple[bool, float]:
    """
    Verifica si el bot local en la PC del usuario actualizo `data/bot_state.json` recientemente.
    Retorna (esta_activo, minutos_desde_ultima_actualizacion).
    """
    try:
        if not state_file_path.exists():
            return False, 9999.0
        raw = json.loads(state_file_path.read_text(encoding="utf-8"))
        updated_str = str(raw.get("updated_at", "")).strip()
        last_source = str(raw.get("last_runner_source", "")).strip()
        if not updated_str or last_source != "LOCAL_PC":
            return False, 9999.0
        dt = datetime.fromisoformat(updated_str.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        elapsed_min = (datetime.now(timezone.utc) - dt).total_seconds() / 60.0
        return (0.0 <= elapsed_min <= max_idle_minutes), round(elapsed_min, 1)
    except Exception:
        return False, 9999.0


def setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Bot Autonomo de Trading Spot en Binance impulsado por Google Gemini AI"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fuerza el modo simulacion sin enviar ordenes reales a Binance.",
    )
    parser.add_argument(
        "--loop",
        action="store_true",
        help="Ejecuta el bot en bucle continuo (para VPS/PC) en lugar de un ciclo unico de GitHub Actions.",
    )
    parser.add_argument(
        "--interval-minutes",
        type=int,
        default=15,
        help="Minutos de espera entre ciclos cuando se usa --loop (por defecto: 15).",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Activa logs detallados de depuracion.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    setup_logging(verbose=args.verbose)

    cfg = BotConfig()
    if args.dry_run:
        object.__setattr__(cfg, "dry_run", True)

    # Si corre como tarea programada en GitHub Actions y la PC local estuvo activa hace <= 20 min,
    # la nube queda en espera (Standby) y toma el control automaticamente en cuanto se apague la PC.
    if os.getenv("GITHUB_ACTIONS") == "true" and os.getenv("GITHUB_EVENT_NAME") == "schedule":
        pc_active, elapsed_min = is_local_pc_active(cfg.state_file, max_idle_minutes=20.0)
        if pc_active:
            logging.info(
                "MODO RESPALDO CLOUD: PC Local detectada activa (ultimo ciclo hace %.1f min). "
                "GitHub Actions permanece en Standby y tomara el control automaticamente cuando apagues la PC.",
                elapsed_min,
            )
            return 0
        logging.info(
            "MODO RESPALDO CLOUD ACTIVO: La PC Local lleva %.1f min sin reportar (>20 min). "
            "GitHub Actions asume el control automatico del Bot de Binance en la nube.",
            elapsed_min,
        )

    bot = AutonomousTradingBot(config=cfg)

    if not args.loop:
        result = bot.run_cycle()
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0

    logging.info("Modo bucle continuo activado (intervalo: %d minutos).", args.interval_minutes)
    while True:
        try:
            result = bot.run_cycle()
            print(json.dumps(result, indent=2, ensure_ascii=False))
        except Exception as exc:
            logging.exception("Error durante el ciclo del bot: %s", exc)
        time.sleep(max(1, args.interval_minutes) * 60)


if __name__ == "__main__":
    sys.exit(main())
