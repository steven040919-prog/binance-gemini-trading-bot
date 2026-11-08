from __future__ import annotations

import argparse
import json
import logging
import sys
import time

from src.bot_engine import AutonomousTradingBot
from src.config import BotConfig


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
