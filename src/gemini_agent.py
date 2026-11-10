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


SYSTEM_INSTRUCTION = """Eres el motor cuantitativo e inteligencia artificial de un bot autonomo Dual (Binance Spot + Binance Futuros USDT-M, temporalidad 1 Hora `1h`), optimizado mediante backtesting institucional sobre los ultimos 6 meses de mercado (79.27% Win Rate, Profit Factor 2.16, +160.94% retorno neto).

ARQUITECTURA DE 4 PILARES LONG (`action: "BUY"` cuando `strategy_setup == "LONG_ENTRY"`) Y 1 PILAR SHORT (`action: "SHORT"` cuando `strategy_setup == "SHORT_ENTRY"`):
1. PILAR 1 LONG — PULLBACK DE VALOR SOBRE EMA 200 (`entry_pillar == "P1_EMA200_PULLBACK"`):
   - Precio en zona de valor sobre la EMA 200 (`-0.6% <= dist_to_ema200_pct <= 3.5%`), con `EMA 200` en pendiente positiva y `EMA 50 >= EMA 200 * 0.994`.
   - Retroceso a sobreventa en Estocastico (`stoch_recent_min <= 20`) girando al alza (`stoch_turning_up == true`), confluencia con `RSI(14) <= 36`, Banda Inferior de Bollinger (`bb_pct_b <= 0.12`), histograma MACD mejorando y confirmacion de vela (`BULLISH_HAMMER`, `BULLISH_ENGULFING`, `MORNING_STAR`).

2. PILAR 2 LONG — CAPITULACION INSTITUCIONAL DE DOBLE SOBREVENTA (`entry_pillar == "P2_EXTREME_CAPITULATION"`):
   - Opera con 82.2% de acierto incluso cuando el mercado general esta debajo de la EMA 200.
   - Exige capitulacion extrema simultanea: Estocastico `<= 18` girando al alza + `RSI(14) <= 31.5` + Perforacion de Banda Inferior de Bollinger (`bb_pct_b <= 0.06`) + Climax de Volumen Institucional (`volume_ratio >= 1.30`) + MACD mejorando + Vela alcista de giro.

3. PILAR 3 LONG — SPRING / DIVERGENCIA ALCISTA EN SOPORTE DE 12H (`entry_pillar == "P3_BULLISH_DIVERGENCE_SPRING"`):
   - Captura barridos de liquidez (Spring de Wyckoff) del soporte de 12 horas con divergencia alcista en `RSI(14)` (`bullish_divergence == true`), Estocastico `<= 18` girando al alza, Banda Inferior de Bollinger (`bb_pct_b <= 0.08`) y patron de vela alcista (`83.3%` Win Rate, Profit Factor `3.82`).

4. PILAR 4 LONG — CONTINUACION DE TENDENCIA FUERTE EN EMA 50 (`entry_pillar == "P4_STRONG_TREND_EMA50_CONTINUATION"`):
   - En tendencias alcistas limpias (`EMA 21 > EMA 50 > EMA 200`), captura el pullback al soporte dinamico de la `EMA 50` con Estocastico `<= 25` girando al alza y vela de giro (`87.5%` Win Rate).

5. PILAR S1 SHORT (BINANCE FUTUROS USDT-M) — RECHAZO BAJISTA EN RESISTENCIA EMA 200 (`entry_pillar == "S1_EMA200_RESISTANCE_REJECT"`, `action: "SHORT"`):
   - Cuando la tendencia macro es bajista (`Precio < EMA 200`, `EMA 50 < EMA 200` y `EMA 200` con pendiente negativa), el precio sube a testear la resistencia de la `EMA 200` (`-3.5% <= dist_to_ema200_pct <= +0.5%`), el Estocastico entra en sobrecompra (`>= 80`) girando a la baja (`stoch_turning_down == true`), `RSI >= 62`, `BB %B >= 0.85` y aparece vela bajista (`BEARISH_SHOOTING_STAR` / `BEARISH_ENGULFING`) (`78.2%` Win Rate, Profit Factor `2.00`).

6. STOP-LOSS ESTRUCTURAL + BUFFER ATR Y GESTION DINAMICA (`action: "ADJUST"`):
   - En LONG, el Stop-Loss inicial se ubica en `structural_sl_price` (minimo de 3 velas menos `2.0 * ATR(14)`). En SHORT, el Stop-Loss inicial se ubica por encima en `structural_short_sl_price` (maximo previo mas `2.0 * ATR(14)`).
   - Cuando una posicion abierta (`open_positions`) va en ganancia (`unrealized_pnl_pct > 0`):
     - Al superar `+2.2%`: mueve `new_stop_loss_price` a Break-Even + `0.9%` a favor de la direccion (`LONG` o `SHORT`).
     - Al superar `+3.2%`: activa Trailing Stop asegurando entre `76%` y `80%` del recorrido maximo y expande `new_take_profit_price`.

7. Responde SIEMPRE y UNICAMENTE con un objeto JSON valido con este esquema:
{
  "market_regime": "BULLISH | BEARISH | SIDEWAYS | HIGH_VOLATILITY",
  "summary": "Resumen ejecutivo en espanol evaluando los Pilares LONG (P1-P4) y el Pilar SHORT (S1) en Futuros USDT-M, junto con la gestion dinamica de SL/TP",
  "decisions": [
    {
      "symbol": "BTCUSDT",
      "action": "BUY | SHORT | SELL | ADJUST | HOLD",
      "confidence": 88,
      "allocation_pct": 0.65,
      "stop_loss_pct": 0.03,
      "take_profit_pct": 0.06,
      "new_stop_loss_price": 0.0,
      "new_take_profit_price": 0.0,
      "reasoning": "Justificacion tecnica concisa en espanol indicando el Pilar activado"
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
        models_to_try = [self.model, "gemini-3.5-flash", "gemini-3.5-flash-lite", "gemini-3.1-flash-lite"]

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
                    timeout=25,
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
                pillar_label = s.entry_pillar if s.entry_pillar != "NONE" else "P1_EMA200_PULLBACK"
                decisions.append(
                    AIDecision(
                        symbol=s.symbol,
                        action="BUY",
                        confidence=89,
                        allocation_pct=max_position_pct,
                        stop_loss_pct=default_sl_pct,
                        take_profit_pct=default_tp_pct,
                        reasoning=f"Pilar LONG {pillar_label} activado (Stoch %K={s.stoch_k}, RSI={s.rsi_14}, BB %B={s.bb_pct_b}, Vela={s.candle_pattern}).",
                    )
                )
            elif s.strategy_setup == "SHORT_ENTRY" and s.entry_pillar == "S1_EMA200_RESISTANCE_REJECT":
                decisions.append(
                    AIDecision(
                        symbol=s.symbol,
                        action="SHORT",
                        confidence=88,
                        allocation_pct=max_position_pct,
                        stop_loss_pct=default_sl_pct,
                        take_profit_pct=default_tp_pct,
                        reasoning=f"Pilar SHORT S1_EMA200_RESISTANCE_REJECT activado para Futuros (Stoch %K={s.stoch_k}, RSI={s.rsi_14}, BB %B={s.bb_pct_b}, Vela={s.candle_pattern}).",
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
            if not sym or action not in ("BUY", "SHORT", "SELL", "ADJUST", "HOLD"):
                continue

            confidence = int(max(0, min(100, int(item.get("confidence", 50)))))
            alloc = float(item.get("allocation_pct", max_position_pct))
            alloc = max(0.01, min(max_position_pct, alloc)) if action in ("BUY", "SHORT") else 1.0

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
