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
    action: str  # "BUY", "SELL", "ADJUST", "HOLD"
    confidence: int  # 0..100
    allocation_pct: float
    stop_loss_pct: float
    take_profit_pct: float
    reasoning: str
    new_stop_loss_price: float = 0.0
    new_take_profit_price: float = 0.0


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


SYSTEM_INSTRUCTION = """Eres el motor de inteligencia artificial de un bot autonomo que ejecuta la estrategia en temporalidad de 1 Hora (1h) y GESTIONA DINAMICAMENTE EL STOP-LOSS Y TAKE-PROFIT para dejar correr las ganancias:

REGLAS OBLIGATORIAS DE LA ESTRATEGIA (EMA 200 + ESTOCASTICO 80/20 + VELAS MARTILLO / ENVOLVENTE):
1. CONDICION DE COMPRA (ALZA / LONG):
   - El precio actual DEBE estar POR ENCIMA de la EMA de 200 periodos (`above_ema_200 == true`, `current_price > ema_200`).
   - El oscilador Estocastico (`stoch_k` o `stoch_recent_min`) debe haber llegado a la zona de sobreventa (`<= 20`) durante el retroceso.
   - Debe haberse formado una vela de confirmacion alcista: **Vela Martillo Alcista (`BULLISH_HAMMER`)** o **Vela Envolvente Alcista (`BULLISH_ENGULFING`)** (`strategy_setup == "LONG_ENTRY"`).
   - El Stop-Loss inicial se coloca exactamente en el ultimo bajo de la vela anterior (`prev_candle_low`).

2. DEJAR CORRER LAS GANANCIAS (MOVER STOP-LOSS Y TAKE-PROFIT CON `action: "ADJUST"`):
   - Cuando una posicion abierta (`open_positions`) va dando ganancias (`unrealized_pnl_pct > 0`):
     - Si la tendencia sigue fuerte (precio sobre EMA 200, sobre EMA 9/21 o rompiendo resistencias), **NO cierres prematuramente la operacion** aunque el Estocastico toque 80 si no hay vela de rechazo bajista.
     - En su lugar, emite `action: "ADJUST"` con:
       - `new_stop_loss_price`: Un nuevo Stop-Loss MAS ALTO que el actual (por ejemplo, en el ultimo bajo de la vela previa `prev_candle_low`, en la EMA 21, o asegurando al menos el 50%-70% de la ganancia flotante) para proteger las ganancias acumuladas.
       - `new_take_profit_price`: Un nuevo Take-Profit MAS ALTO que el precio actual (proyectando el siguiente nivel de resistencia o +3% a +6% adicional) para dejar correr la tendencia y maximizar beneficios.

3. CONDICION DE CIERRE (`action: "SELL"`):
   - Si tenemos una posicion abierta, el Estocastico ya esta en sobrecompra (`>= 80`) Y ADEMAS aparece agotamiento claro o una vela bajista (`BEARISH_SHOOTING_STAR` o `BEARISH_ENGULFING`) o perdida de estructura, recomienda `SELL` para cobrar toda la ganancia antes de la caida.

4. GESTION DE RIESGO:
   - Solo se arriesga el 1% del monto total de la cuenta (minimo $1 USD) por operacion al entrar.
   - Si un par sin posicion abierta NO cumple las condiciones de entrada, emite `HOLD`.

5. Responde SIEMPRE y UNICAMENTE con un objeto JSON valido con este esquema:
{
  "market_regime": "BULLISH | BEARISH | SIDEWAYS | HIGH_VOLATILITY",
  "summary": "Resumen ejecutivo en espanol evaluando EMA 200, Estocastico (20/80), patrones de velas y ajustes de SL/TP en posiciones ganadoras",
  "decisions": [
    {
      "symbol": "BTCUSDT",
      "action": "BUY | SELL | ADJUST | HOLD",
      "confidence": 88,
      "allocation_pct": 0.20,
      "stop_loss_pct": 0.02,
      "take_profit_pct": 0.05,
      "new_stop_loss_price": 0.0,
      "new_take_profit_price": 0.0,
      "reasoning": "Justificacion tecnica concisa en espanol"
    }
  ]
}
"""


class GeminiTradingAgent:
    """Agente de IA impulsado por Google Gemini (gemini-3.8-flash) con gestion dinamica de SL/TP."""

    def __init__(self, api_key: str, model: str = "gemini-3.8-flash", timeout: int = 90) -> None:
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
                    "locked_profit_pct": round(pos.locked_profit_pct(), 2),
                    "r_multiple": round(pos.r_multiple(cur_price), 2),
                    "stop_loss_price": pos.stop_loss_price,
                    "initial_stop_loss_price": pos.initial_stop_loss_price,
                    "take_profit_price": pos.take_profit_price,
                    "sl_adjustments_count": pos.sl_adjustments_count,
                    "opened_at": pos.opened_at,
                }
            )

        prompt_payload = {
            "strategy_rules": {
                "timeframe": "1h",
                "trend_indicator": "EMA 200",
                "oscillator": "Stochastic (14,3,3) levels 20 / 80",
                "entry_patterns": ["BULLISH_HAMMER", "BULLISH_ENGULFING", "BEARISH_SHOOTING_STAR", "BEARISH_ENGULFING"],
                "dynamic_profit_runner": "Move Stop-Loss and Take-Profit up on winning positions (action=ADJUST) to lock profits and let winners run",
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
            "Evalua los siguientes activos en temporalidad 1H aplicando la estrategia "
            "EMA 200 + Estocastico (20/80) + Vela Martillo/Envolvente, y ajusta dinamicamente "
            "el Stop-Loss y Take-Profit en las posiciones abiertas con ganancia para dejar correr "
            "las operaciones ganadoras. Emite tu decision en JSON:\n\n"
            + json.dumps(prompt_payload, indent=2, ensure_ascii=False)
        )

        try:
            raw_text = self._call_gemini(user_prompt)
            return self._parse_response(
                raw_text=raw_text,
                max_position_pct=max_position_pct,
                default_sl_pct=default_sl_pct,
                default_tp_pct=default_tp_pct,
            )
        except Exception as exc:
            logger.warning("Usando motor cuantitativo determinista de respaldo tras demora/error en Gemini API: %s", exc)
            return self._fallback_deterministic_analysis(
                snapshots=snapshots,
                open_positions=open_positions,
                max_position_pct=max_position_pct,
                default_sl_pct=default_sl_pct,
                default_tp_pct=default_tp_pct,
            )

    def _call_gemini(self, user_prompt: str) -> str:
        models_to_try = [self.model, "gemini-3.5-flash-lite", "gemini-3.1-flash-lite"]

        last_err: Exception | None = None
        for mdl in models_to_try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{mdl}:generateContent"
            payload = {
                "system_instruction": {"parts": [{"text": SYSTEM_INSTRUCTION}]},
                "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
                "generationConfig": {
                    "temperature": 0.1,
                    "responseMimeType": "application/json",
                },
            }
            try:
                resp = requests.post(
                    url,
                    params={"key": self.api_key},
                    json=payload,
                    timeout=50,
                )
                if resp.status_code >= 400:
                    last_err = RuntimeError(f"Error en Gemini API ({mdl}, HTTP {resp.status_code}): {resp.text[:250]}")
                    continue
                data = resp.json()
                candidates = data.get("candidates", [])
                if not candidates:
                    last_err = RuntimeError(f"Gemini ({mdl}) no devolvio candidatos.")
                    continue
                parts = candidates[0].get("content", {}).get("parts", [])
                text = "".join(part.get("text", "") for part in parts if "text" in part)
                if text.strip():
                    return text
            except Exception as exc:
                last_err = exc
                logger.warning("Intento con modelo %s fallo/excedio tiempo: %s", mdl, exc)

        if last_err:
            raise last_err
        raise RuntimeError("No se pudo obtener respuesta de Gemini API.")

    def _fallback_deterministic_analysis(
        self,
        snapshots: list[TechnicalSnapshot],
        open_positions: dict[str, PositionState],
        max_position_pct: float,
        default_sl_pct: float,
        default_tp_pct: float,
    ) -> AIAnalysisResult:
        bullish_count = sum(1 for s in snapshots if s.above_ema_200)
        regime = "BULLISH" if bullish_count >= len(snapshots) / 2 else "BEARISH"
        decisions: list[AIDecision] = []

        for s in snapshots:
            pos = open_positions.get(s.symbol)
            if pos is not None:
                pnl = pos.unrealized_pnl_pct(s.current_price)
                if s.stoch_k >= 80.0 and s.candle_pattern in ("BEARISH_SHOOTING_STAR", "BEARISH_ENGULFING"):
                    decisions.append(
                        AIDecision(
                            symbol=s.symbol,
                            action="SELL",
                            confidence=90,
                            allocation_pct=1.0,
                            stop_loss_pct=default_sl_pct,
                            take_profit_pct=default_tp_pct,
                            reasoning=f"Estocastico en sobrecompra ({s.stoch_k}) con vela bajista {s.candle_pattern}.",
                        )
                    )
                elif pnl > 1.0:
                    new_sl = max(pos.stop_loss_price, s.prev_candle_low, round(pos.entry_price + (s.current_price - pos.entry_price) * 0.65, 8))
                    new_tp = max(pos.take_profit_price, round(s.current_price * 1.04, 8))
                    decisions.append(
                        AIDecision(
                            symbol=s.symbol,
                            action="ADJUST",
                            confidence=85,
                            allocation_pct=max_position_pct,
                            stop_loss_pct=default_sl_pct,
                            take_profit_pct=default_tp_pct,
                            new_stop_loss_price=new_sl,
                            new_take_profit_price=new_tp,
                            reasoning="Posicion en ganancia: subiendo Stop-Loss y expandiendo Take-Profit para dejar correr la tendencia.",
                        )
                    )
                else:
                    decisions.append(
                        AIDecision(
                            symbol=s.symbol,
                            action="HOLD",
                            confidence=75,
                            allocation_pct=max_position_pct,
                            stop_loss_pct=default_sl_pct,
                            take_profit_pct=default_tp_pct,
                            reasoning="Manteniendo posicion abierta bajo vigilancia de SL y Estocastico.",
                        )
                    )
            elif s.strategy_setup == "LONG_ENTRY":
                decisions.append(
                    AIDecision(
                        symbol=s.symbol,
                        action="BUY",
                        confidence=88,
                        allocation_pct=max_position_pct,
                        stop_loss_pct=default_sl_pct,
                        take_profit_pct=default_tp_pct,
                        reasoning=f"Precio sobre EMA 200 ({s.ema_200}), Estocastico en sobreventa ({s.stoch_k}) y patron {s.candle_pattern}.",
                    )
                )
            else:
                decisions.append(
                    AIDecision(
                        symbol=s.symbol,
                        action="HOLD",
                        confidence=70,
                        allocation_pct=max_position_pct,
                        stop_loss_pct=default_sl_pct,
                        take_profit_pct=default_tp_pct,
                        reasoning=f"Esperando setup completo (EMA200={'Alcista' if s.above_ema_200 else 'Bajista'}, Stoch %K={s.stoch_k}, Vela={s.candle_pattern}).",
                    )
                )

        return AIAnalysisResult(
            market_regime=regime,
            summary=f"Evaluacion cuantitativa completada sobre {len(snapshots)} pares en 1H ({bullish_count} sobre EMA 200).",
            decisions=decisions,
        )

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
            if not sym or action not in ("BUY", "SELL", "ADJUST", "HOLD"):
                continue

            confidence = int(max(0, min(100, int(item.get("confidence", 50)))))
            alloc = float(item.get("allocation_pct", max_position_pct))
            alloc = max(0.01, min(max_position_pct, alloc)) if action == "BUY" else 1.0

            sl_pct = float(item.get("stop_loss_pct", default_sl_pct))
            sl_pct = max(0.002, min(0.15, sl_pct))

            tp_pct = float(item.get("take_profit_pct", default_tp_pct))
            tp_pct = max(0.005, min(0.35, tp_pct))

            new_sl = float(item.get("new_stop_loss_price") or 0.0)
            new_tp = float(item.get("new_take_profit_price") or 0.0)

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
                    new_stop_loss_price=max(0.0, new_sl),
                    new_take_profit_price=max(0.0, new_tp),
                )
            )

        return AIAnalysisResult(
            market_regime=regime,
            summary=summary,
            decisions=decisions,
        )
