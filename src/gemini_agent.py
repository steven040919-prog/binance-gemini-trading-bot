from __future__ import annotations

import json
import logging
from dataclasses import asdict, dataclass
from typing import Any

import requests

from src.market_scanner import TechnicalSnapshot
from src.state_manager import PositionState

logger = logging.getLogger(__name__)


@dataclass
class AIDecision:
    symbol: str
    action: str  # "BUY", "SELL", "HOLD"
    confidence: int  # 0..100
    allocation_pct: float
    stop_loss_pct: float
    take_profit_pct: float
    reasoning: str


@dataclass
class AIAnalysisResult:
    market_regime: str
    summary: str
    decisions: list[AIDecision]

    def to_dict(self) -> dict[str, Any]:
        return {
            "market_regime": self.market_regime,
            "summary": self.summary,
            "decisions": [asdict(d) for d in self.decisions],
        }


SYSTEM_INSTRUCTION = """Eres el motor de inteligencia artificial de un bot autonomo que ejecuta ESTRICTAMENTE la siguiente estrategia en temporalidad de 1 Hora (1h):

REGLAS OBLIGATORIAS DE LA ESTRATEGIA (EMA 200 + ESTOCASTICO 80/20 + VELAS MARTILLO / ENVOLVENTE):
1. CONDICION DE COMPRA (ALZA / LONG):
   - El precio actual DEBE estar POR ENCIMA de la EMA de 200 periodos (`above_ema_200 == true`, `current_price > ema_200`).
   - El oscilador Estocastico (`stoch_k` o `stoch_recent_min`) debe haber llegado a la zona de sobreventa (`<= 20`) durante el retroceso.
   - Debe haberse formado una vela de confirmacion alcista: **Vela Martillo Alcista (`BULLISH_HAMMER`)** o **Vela Envolvente Alcista (`BULLISH_ENGULFING`)** (`strategy_setup == "LONG_ENTRY"`).
   - El Stop-Loss se coloca exactamente en el ultimo bajo de la vela anterior (`prev_candle_low`).
   - El cierre de la compra se realiza cuando el Estocastico sube y alcanza `>= 80` (`EXIT_LONG_STOCH_80`).

2. CONDICION DE VENTA / BAJA (SHORT O CIERRE):
   - Si ya tenemos una posicion abierta y el Estocastico llega a `>= 80` (en compra) o `<= 20` (en corto), recomienda `SELL` con confianza >= 90 para cerrar la operativa en ganancia.
   - Si el grafico esta POR DEBAJO de la EMA de 200 periodos (`above_ema_200 == false`), el Estocastico sube a sobrecompra (`>= 80`) y forma una **Vela Martillo Invertido / Estrella Fugaz (`BEARISH_SHOOTING_STAR`)** o **Vela Envolvente Bajista (`BEARISH_ENGULFING`)** (`strategy_setup == "SHORT_ENTRY"`), senala `SELL` (con Stop-Loss en el ultimo alto de la vela anterior `prev_candle_high` y cierre cuando el Estocastico baje a `20`).

3. GESTION DE RIESGO:
   - Solo se arriesga el 1% del monto total de la cuenta (minimo $1 USD) por operacion, calculado sobre la distancia al Stop-Loss de la vela anterior.
   - Si un par NO cumple las condiciones de EMA 200 + Estocastico 20/80 + Vela Martillo/Envolvente, emite `HOLD`.

4. Responde SIEMPRE y UNICAMENTE con un objeto JSON valido con este esquema:
{
  "market_regime": "BULLISH | BEARISH | SIDEWAYS | HIGH_VOLATILITY",
  "summary": "Resumen ejecutivo en espanol evaluando EMA 200, Estocastico (20/80) y patrones de velas en 1H",
  "decisions": [
    {
      "symbol": "BTCUSDT",
      "action": "BUY | SELL | HOLD",
      "confidence": 88,
      "allocation_pct": 0.20,
      "stop_loss_pct": 0.02,
      "take_profit_pct": 0.05,
      "reasoning": "Precio sobre EMA 200 en 1H, Estocastico en 18 (sobreventa) y vela envolvente alcista confirmada. SL en bajo previo."
    }
  ]
}
"""


class GeminiTradingAgent:
    """Agente de IA impulsado por Google Gemini (gemini-3.8-flash) para la estrategia EMA 200 + Estocastico + Velas."""

    def __init__(self, api_key: str, model: str = "gemini-3.8-flash", timeout: int = 45) -> None:
        self.api_key = api_key.strip()
        self.model = model.strip() or "gemini-3.8-flash"
        self.timeout = timeout

    def analyze_market(
        self,
        usdt_free: float,
        total_equity_usdt: float,
        daily_pnl_pct: float,
        open_positions: dict[str, PositionState],
        snapshots: list[TechnicalSnapshot],
        recent_trades: list[dict[str, Any]],
        max_open_positions: int,
        max_position_pct: float,
        default_sl_pct: float,
        default_tp_pct: float,
    ) -> AIAnalysisResult:
        prices_map = {s.symbol: s.current_price for s in snapshots}
        positions_payload = []
        for sym, pos in open_positions.items():
            cur_price = prices_map.get(sym, pos.entry_price)
            positions_payload.append(
                {
                    "symbol": sym,
                    "quantity": pos.quantity,
                    "entry_price": pos.entry_price,
                    "current_price": cur_price,
                    "highest_price": pos.highest_price,
                    "unrealized_pnl_pct": round(pos.unrealized_pnl_pct(cur_price), 2),
                    "stop_loss_price": pos.stop_loss_price,
                    "take_profit_price": pos.take_profit_price,
                    "opened_at": pos.opened_at,
                }
            )

        prompt_payload = {
            "strategy_rules": {
                "timeframe": "1h",
                "trend_indicator": "EMA 200",
                "oscillator": "Stochastic (14,3,3) levels 20 / 80",
                "entry_patterns": ["BULLISH_HAMMER", "BULLISH_ENGULFING", "BEARISH_SHOOTING_STAR", "BEARISH_ENGULFING"],
                "risk_per_trade": "1% of total equity (min $1 USD) based on previous candle low/high stop-loss",
            },
            "portfolio": {
                "usdt_free": round(usdt_free, 2),
                "total_equity_usdt": round(total_equity_usdt, 2),
                "daily_pnl_pct": round(daily_pnl_pct, 2),
                "open_positions_count": len(open_positions),
                "max_open_positions": max_open_positions,
                "open_positions": positions_payload,
            },
            "market_candidates": [s.to_dict() for s in snapshots],
            "recent_trades": recent_trades[-8:],
        }

        user_prompt = (
            "Evalua los siguientes activos en temporalidad 1H aplicando estrictamente la estrategia "
            "EMA 200 + Estocastico (20/80) + Vela Martillo/Envolvente. Emite tu decision en JSON:\n\n"
            + json.dumps(prompt_payload, indent=2, ensure_ascii=False)
        )

        raw_text = self._call_gemini(user_prompt)
        return self._parse_response(
            raw_text=raw_text,
            max_position_pct=max_position_pct,
            default_sl_pct=default_sl_pct,
            default_tp_pct=default_tp_pct,
        )

    def _call_gemini(self, user_prompt: str) -> str:
        try:
            from google import genai

            client = genai.Client(api_key=self.api_key)
            interaction = client.interactions.create(
                model=self.model,
                input=user_prompt,
                system_instruction=SYSTEM_INSTRUCTION,
                response_mime_type="application/json",
            )
            if interaction and getattr(interaction, "output_text", None):
                return interaction.output_text
        except ImportError:
            logger.debug("SDK google-genai no disponible, usando llamada REST directa.")
        except Exception as exc:
            logger.warning("Fallo en SDK google-genai (%s), intentando llamada REST directa...", exc)

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent"
        payload = {
            "system_instruction": {"parts": [{"text": SYSTEM_INSTRUCTION}]},
            "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
            "generationConfig": {
                "temperature": 0.1,
                "responseMimeType": "application/json",
            },
        }
        resp = requests.post(
            url,
            params={"key": self.api_key},
            json=payload,
            timeout=self.timeout,
        )
        if resp.status_code >= 400:
            raise RuntimeError(f"Error en Gemini API (HTTP {resp.status_code}): {resp.text}")
        data = resp.json()
        candidates = data.get("candidates", [])
        if not candidates:
            raise RuntimeError(f"Gemini no devolvio candidatos: {data}")
        parts = candidates[0].get("content", {}).get("parts", [])
        return "".join(part.get("text", "") for part in parts if "text" in part)

    def _parse_response(
        self,
        raw_text: str,
        max_position_pct: float,
        default_sl_pct: float,
        default_tp_pct: float,
    ) -> AIAnalysisResult:
        cleaned = raw_text.strip()
        if cleaned.startswith("```"):
            lines = cleaned.splitlines()
            lines = [ln for ln in lines if not ln.strip().startswith("```")]
            cleaned = "\n".join(lines).strip()

        parsed = json.loads(cleaned)
        regime = str(parsed.get("market_regime", "SIDEWAYS")).upper()
        summary = str(parsed.get("summary", "Sin resumen disponible."))

        decisions: list[AIDecision] = []
        for item in parsed.get("decisions", []):
            sym = str(item.get("symbol", "")).upper().strip()
            action = str(item.get("action", "HOLD")).upper().strip()
            if not sym or action not in ("BUY", "SELL", "HOLD"):
                continue

            confidence = int(max(0, min(100, int(item.get("confidence", 50)))))
            alloc = float(item.get("allocation_pct", max_position_pct))
            alloc = max(0.01, min(max_position_pct, alloc)) if action == "BUY" else 1.0

            sl_pct = float(item.get("stop_loss_pct", default_sl_pct))
            sl_pct = max(0.002, min(0.15, sl_pct))

            tp_pct = float(item.get("take_profit_pct", default_tp_pct))
            tp_pct = max(0.005, min(0.35, tp_pct))

            reasoning = str(item.get("reasoning", "")).strip()
            decisions.append(
                AIDecision(
                    symbol=sym,
                    action=action,
                    confidence=confidence,
                    allocation_pct=alloc,
                    stop_loss_pct=sl_pct,
                    take_profit_pct=tp_pct,
                    reasoning=reasoning,
                )
            )

        return AIAnalysisResult(
            market_regime=regime,
            summary=summary,
            decisions=decisions,
        )
