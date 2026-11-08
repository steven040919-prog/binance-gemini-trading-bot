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
    allocation_pct: float  # Para BUY: 0.05..max_position_pct del capital total; Para SELL: 1.0 (100% de la posicion)
    stop_loss_pct: float  # % bajo el precio de entrada
    take_profit_pct: float  # % sobre el precio de entrada
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


SYSTEM_INSTRUCTION = """Eres un gestor cuantitativo autonomo de carteras de criptomonedas en Binance Spot.
Tu objetivo primordial es preservar el capital y capturar tendencias con alta probabilidad de exito (relacion Riesgo/Beneficio >= 1.8:1).

REGLAS ESTRICTAS DE OPERACION:
1. Solo operas en Spot contra USDT (sin apalancamiento, solo compras BUY y ventas SELL de posiciones existentes).
2. Prioriza compras (BUY) unicamente cuando:
   - El timeframe superior (1h `htf_trend`) sea BULLISH o NEUTRAL en recuperacion clara.
   - El RSI de 15m (`rsi_14`) no este en sobrecompra extrema (< 70) y muestre impulso alcista (MACD histograma positivo o girando al alza, precio sobre EMA 21 o rebotando en soporte con `volume_ratio` >= 1.0).
3. Recomienda vender (SELL) una posicion abierta cuando:
   - La estructura tecnica en 15m y 1h se vuelva BEARISH con perdida de EMAs clave, o el activo muestre agotamiento claro en sobrecompra extrema (RSI > 76 con divergencia/caida de volumen).
4. Si ninguna oportunidad es clara o el mercado general es bajista/peligroso, recomienda HOLD. No fuerces operaciones mediocres.
5. Responde SIEMPRE y UNICAMENTE con un objeto JSON valido que cumpla exactamente este esquema:
{
  "market_regime": "BULLISH | BEARISH | SIDEWAYS | HIGH_VOLATILITY",
  "summary": "Resumen ejecutivo en espanol del estado del mercado y la cartera",
  "decisions": [
    {
      "symbol": "BTCUSDT",
      "action": "BUY | SELL | HOLD",
      "confidence": 82,
      "allocation_pct": 0.20,
      "stop_loss_pct": 0.035,
      "take_profit_pct": 0.070,
      "reasoning": "Justificacion tecnica concisa en espanol"
    }
  ]
}
"""


class GeminiTradingAgent:
    """Agente de IA impulsado por Google Gemini para analisis cuantitativo y toma de decisiones."""

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
            "portfolio": {
                "usdt_free": round(usdt_free, 2),
                "total_equity_usdt": round(total_equity_usdt, 2),
                "daily_pnl_pct": round(daily_pnl_pct, 2),
                "open_positions_count": len(open_positions),
                "max_open_positions": max_open_positions,
                "max_position_pct": max_position_pct,
                "open_positions": positions_payload,
            },
            "risk_defaults": {
                "default_stop_loss_pct": default_sl_pct,
                "default_take_profit_pct": default_tp_pct,
            },
            "market_candidates": [s.to_dict() for s in snapshots],
            "recent_trades": recent_trades[-8:],
        }

        user_prompt = (
            "Analiza el siguiente estado de cartera y los indicadores tecnicos en tiempo real de Binance Spot. "
            "Emite tu decision estructurada en JSON:\n\n"
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
        # Intenta primero con el SDK oficial google-genai (Interactions API) y cae a REST directo si no esta instalado
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
                "temperature": 0.15,
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
        return "".join(part.get("text", "") for part in parts)

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
            alloc = max(0.05, min(max_position_pct, alloc)) if action == "BUY" else 1.0

            sl_pct = float(item.get("stop_loss_pct", default_sl_pct))
            sl_pct = max(0.01, min(0.15, sl_pct))

            tp_pct = float(item.get("take_profit_pct", default_tp_pct))
            tp_pct = max(0.02, min(0.35, tp_pct))

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
