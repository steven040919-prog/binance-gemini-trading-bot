from __future__ import annotations

import json
import logging
import os
import re
import time
from dataclasses import asdict, dataclass, field, is_dataclass
from datetime import datetime, timedelta, timezone
from typing import Any

import requests

from src.mt5_adaptive_scheduler import ensure_utc, utc_iso

logger = logging.getLogger(__name__)

VALID_ADAPTIVE_ACTIONS: tuple[str, ...] = (
    "ENTER_BUY",
    "ENTER_SELL",
    "WATCH_EXACT",
    "POSTPONE_WATCH",
    "INVALIDATE_WATCH",
    "HOLD",
)

# Model fallback chains aligned with src/gemini_agent.py plus resilient Flash fallbacks
DEFAULT_HIGH_PRIORITY_MODELS: tuple[str, ...] = (
    "gemini-4-hydrogen",
    "gemini-3.8-flash",
    "gemini-3.5-flash",
    "gemini-2.5-flash",
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
    "gemini-2.5-flash-lite",
)

DEFAULT_GENERAL_MODELS: tuple[str, ...] = (
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
    "gemini-2.5-flash-lite",
    "gemini-3.5-flash",
    "gemini-2.5-flash",
    "gemini-3.8-flash",
)

GEMINI_CADENCE_FEASIBILITY_NOTE: str = (
    "Gemini API Cadence & Quota Feasibility (MT5 Adaptive Bot):\n"
    "- Token budget per cycle (compact context + top signals + episodic memory): "
    "~1,800-3,200 input tokens + ~350-700 output tokens (~2,200-3,900 total tokens/call).\n"
    "- 30m base patrol + adaptive sniper wakes: 48 base calls + ~12-20 sniper wakes + ~4-8 post-mortems "
    "= ~64-76 RPD (peak 1-2 RPM, ~180k-280k tokens/day). Fits comfortably within Gemini Flash free tier "
    "(typically 10-15 RPM, 250k TPM, 250 RPD) with >3x daily headroom.\n"
    "- 15m base patrol + adaptive sniper wakes: 96 base calls + ~16-24 sniper wakes + ~4-8 post-mortems "
    "= ~116-128 RPD (peak 1-2 RPM, ~310k-460k tokens/day). Fits Flash free tier (~50% RPD utilization) "
    "and is negligible on Tier-1 pay-as-you-go (~$0.04-$0.15/day).\n"
    "- Recommendation: Use 30m base patrol with Flash-Lite on quiet patrols + Flash on READY/FORMING/SNIPER "
    "cycles. Exact sniper wakes deliver M5-M15 entry precision at ~55% of the RPD of a fixed 15m loop."
)


def estimate_gemini_quota_usage(
    base_interval_minutes: int = 30,
    avg_sniper_wakes_per_day: int = 16,
    avg_post_mortems_per_day: int = 6,
    avg_input_tokens_per_cycle: int = 2400,
    avg_output_tokens_per_cycle: int = 500,
) -> dict[str, Any]:
    """Estimate daily Gemini API request and token consumption for a given cadence."""
    interval = max(1, int(base_interval_minutes))
    base_calls_per_day = int(round((24 * 60) / interval))
    sniper_calls = max(0, int(avg_sniper_wakes_per_day))
    post_mortem_calls = max(0, int(avg_post_mortems_per_day))
    total_rpd = base_calls_per_day + sniper_calls + post_mortem_calls

    cycle_calls = base_calls_per_day + sniper_calls
    est_input_tokens_day = cycle_calls * avg_input_tokens_per_cycle + post_mortem_calls * 700
    est_output_tokens_day = cycle_calls * avg_output_tokens_per_cycle + post_mortem_calls * 120
    est_total_tokens_day = est_input_tokens_day + est_output_tokens_day

    fits_flash_free_tier = total_rpd <= 220  # conservative margin below 250 RPD
    fits_flash_lite_free_tier = total_rpd <= 900  # conservative margin below 1000 RPD

    return {
        "base_interval_minutes": interval,
        "base_calls_per_day": base_calls_per_day,
        "sniper_calls_per_day": sniper_calls,
        "post_mortem_calls_per_day": post_mortem_calls,
        "estimated_rpd": total_rpd,
        "estimated_peak_rpm": 2,
        "estimated_input_tokens_per_day": est_input_tokens_day,
        "estimated_output_tokens_per_day": est_output_tokens_day,
        "estimated_total_tokens_per_day": est_total_tokens_day,
        "fits_flash_free_tier": fits_flash_free_tier,
        "fits_flash_lite_free_tier": fits_flash_lite_free_tier,
    }


def _safe_int(val: Any, default: int) -> int:
    if val is None or isinstance(val, bool):
        return default
    try:
        return int(round(float(val)))
    except (TypeError, ValueError):
        return default


def _safe_float(val: Any, default: float | None = None) -> float | None:
    if val is None or isinstance(val, bool):
        return default
    try:
        out = float(val)
        return out
    except (TypeError, ValueError):
        return default


def _to_plain_dict(obj: Any) -> dict[str, Any]:
    """Convert dataclass, object with to_dict(), or dict into a plain dict."""
    if isinstance(obj, dict):
        return dict(obj)
    if hasattr(obj, "to_dict") and callable(obj.to_dict):
        res = obj.to_dict()
        if isinstance(res, dict):
            return res
    if is_dataclass(obj) and not isinstance(obj, type):
        return asdict(obj)
    return {}


def extract_json_object(raw_text: str) -> dict[str, Any]:
    """
    Robustly extract a JSON object from LLM output, handling markdown code fences,
    leading/trailing prose, and minor formatting artifacts.
    """
    if not raw_text or not raw_text.strip():
        raise ValueError("Empty LLM response")

    cleaned = raw_text.strip()

    # Strip markdown fences if present
    fence_match = re.search(r"```(?:json)?\s*([\s\S]*?)```", cleaned, flags=re.IGNORECASE)
    if fence_match:
        cleaned = fence_match.group(1).strip()

    # Direct parse fast path
    try:
        parsed = json.loads(cleaned)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        pass

    # Balanced brace scan to isolate the first valid JSON object inside surrounding prose
    start_idx = cleaned.find("{")
    if start_idx == -1:
        raise ValueError(f"No JSON object found in LLM response: {cleaned[:160]}")

    depth = 0
    in_string = False
    escape = False
    for idx in range(start_idx, len(cleaned)):
        ch = cleaned[idx]
        if escape:
            escape = False
            continue
        if ch == "\\" and in_string:
            escape = True
            continue
        if ch == '"':
            in_string = not in_string
            continue
        if in_string:
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                candidate = cleaned[start_idx : idx + 1]
                try:
                    parsed = json.loads(candidate)
                    if isinstance(parsed, dict):
                        return parsed
                except json.JSONDecodeError:
                    # Try removing trailing commas before } or ]
                    sanitized = re.sub(r",\s*([}\]])", r"\1", candidate)
                    parsed = json.loads(sanitized)
                    if isinstance(parsed, dict):
                        return parsed
                break

    raise ValueError(f"Unable to parse valid JSON object from LLM response: {cleaned[:160]}")


@dataclass
class SymbolAdaptiveDecision:
    """Structured AI decision for a single candidate or watched symbol."""

    symbol: str
    action: str  # ENTER_BUY | ENTER_SELL | WATCH_EXACT | POSTPONE_WATCH | INVALIDATE_WATCH | HOLD
    strategy_name: str = ""
    confidence_pct: int = 50
    wake_in_minutes: float | None = None
    wake_at_utc: str | None = None
    watch_hypothesis: str = ""
    trigger_condition: str = ""
    invalidation_condition: str = ""
    sl_adjustment: float | None = None
    tp_adjustment: float | None = None
    reasoning: str = ""
    lesson_note: str = ""

    def __post_init__(self) -> None:
        self.symbol = str(self.symbol).strip()
        action_up = str(self.action).strip().upper()
        self.action = action_up if action_up in VALID_ADAPTIVE_ACTIONS else "HOLD"
        self.strategy_name = str(self.strategy_name).strip()
        self.confidence_pct = max(0, min(100, _safe_int(self.confidence_pct, 50)))
        if self.wake_in_minutes is not None:
            self.wake_in_minutes = round(max(0.0, float(self.wake_in_minutes)), 2)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class AdaptiveCycleDecision:
    """Structured output of `MT5AdaptiveAIBrain.evaluate_market_cycle`."""

    market_summary: str
    decisions: dict[str, SymbolAdaptiveDecision] = field(default_factory=dict)
    model_used: str = "quant_local"
    priority_tier: str = "GENERAL"
    cycle_mode: str = "BASE_PATROL"
    timestamp_utc: str = ""
    fallback_used: bool = False
    raw_error: str = ""

    def get(self, symbol: str) -> SymbolAdaptiveDecision | None:
        if symbol in self.decisions:
            return self.decisions[symbol]
        sym_up = symbol.upper()
        for k, v in self.decisions.items():
            if k.upper() == sym_up:
                return v
        return None

    def to_dict(self) -> dict[str, Any]:
        return {
            "market_summary": self.market_summary,
            "model_used": self.model_used,
            "priority_tier": self.priority_tier,
            "cycle_mode": self.cycle_mode,
            "timestamp_utc": self.timestamp_utc,
            "fallback_used": self.fallback_used,
            "raw_error": self.raw_error,
            "decisions": {k: v.to_dict() for k, v in self.decisions.items()},
        }


ADAPTIVE_CYCLE_SYSTEM_INSTRUCTION = """Eres el cerebro cuantitativo adaptativo de un bot autonomo de trading en MetaTrader 5 (Exness: Forex, Metales, Indices y Cripto).
Tu funcion en cada ciclo (BASE_PATROL o SNIPER_WATCH) es analizar:
1. `strategy_signals`: senales multi-estrategia con `setup_stage` (`READY`, `FORMING`, `NONE`), `score`, `direction`, `regime`, `forming_hint`, `invalidation_level`.
2. `memory_context`: estadisticas historicas + en vivo (prior + live Bayesian) y lecciones recientes aprendidas de operaciones cerradas.
3. `active_watches`: hipotesis sniper activas que despertaron en este instante (`hypothesis`, `trigger_condition`, `invalidation_condition`, `postpone_count`, `max_postpones`).
4. `market_context` y `open_positions`: contexto macro, sesion, spreads, riesgo diario y exposicion actual.

Reglas estrictas de decision por simbolo:
- `ENTER_BUY` / `ENTER_SELL`: SOLO cuando el setup esta confirmado (`READY` o trigger sniper cumplido), alineado con regimen/macro/memoria y con `confidence_pct >= 62`.
- `WATCH_EXACT`: Cuando un setup esta `FORMING` (aun no listo pero muy cerca de gatillarse en los proximos 2 a 25 minutos). DEBES especificar `wake_in_minutes` (entre `min_wake_minutes` y `max_wake_minutes`), `watch_hypothesis`, `trigger_condition` e `invalidation_condition`.
- `POSTPONE_WATCH`: SOLO para simbolos que ya tienen un watch activo cuyo escenario sigue valido pero requiere unos minutos adicionales de confirmacion (respeta `postpone_count < max_postpones`). Especifica `wake_in_minutes`.
- `INVALIDATE_WATCH`: Para un watch activo cuya condicion de invalidacion se rompio, perdio momentum o ya no tiene ventaja. Incluye `lesson_note` breve.
- `HOLD`: Sin ventaja clara o esperar al siguiente ciclo base.

Responde SIEMPRE y UNICAMENTE en JSON valido con este esquema exacto:
{
  "market_summary": "Resumen conciso en espanol del estado de mercado y prioridades del ciclo",
  "decisions": [
    {
      "symbol": "EURUSDm",
      "action": "ENTER_BUY | ENTER_SELL | WATCH_EXACT | POSTPONE_WATCH | INVALIDATE_WATCH | HOLD",
      "strategy_name": "TrendPullbackEMA",
      "confidence_pct": 74,
      "wake_in_minutes": 8,
      "wake_at_utc": null,
      "watch_hypothesis": "Pullback acercandose a EMA50 con RSI saliendo de sobreventa",
      "trigger_condition": "Cierre M15 alcista sobre 1.0845 con spread < 16",
      "invalidation_condition": "Ruptura bajista bajo 1.0810",
      "sl_adjustment": null,
      "tp_adjustment": null,
      "reasoning": "Justificacion tecnica y de memoria concisa en espanol",
      "lesson_note": ""
    }
  ]
}
"""

POST_MORTEM_SYSTEM_INSTRUCTION = """Eres el auditor post-mortem de un bot cuantitativo en MetaTrader 5.
Dado el resultado de una operacion cerrada (`trade_outcome`) y su contexto de mercado (`market_context`), extrae UNA sola leccion operativa concreta, reutilizable y accionable (maximo 220 caracteres, en espanol) para futuras decisiones.
Evita frases genericas; menciona la estrategia, regimen/sesion o condicion tecnica concreta que ayudo o perjudico.
Responde UNICAMENTE en JSON valido:
{"lesson": "Leccion concisa y reutilizable aqui"}
"""


class MT5AdaptiveAIBrain:
    """
    Gemini-powered adaptive reasoning brain for the MT5 bot.
    Reuses the lightweight REST pattern from `src/gemini_agent.py` with:
    - Model fallback chains (high-priority vs general/lite)
    - HTTP 429 / 503 cooldown & Retry-After handling
    - Robust JSON extraction and strict schema normalization
    - Deterministic local fallback when offline or rate-limited
    """

    def __init__(
        self,
        api_key: str | None = None,
        model: str | None = None,
        timeout: int = 20,
        max_retries: int = 1,
        cooldown_seconds: float = 900.0,
        high_priority_models: list[str] | tuple[str, ...] | None = None,
        general_models: list[str] | tuple[str, ...] | None = None,
    ) -> None:
        raw_key = os.getenv("GEMINI_API_KEY", "") if api_key is None else api_key
        raw_model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash") if model is None else model
        self.api_key: str = str(raw_key).strip()
        self.model: str = str(raw_model).strip() or "gemini-3.8-flash"
        self.timeout: int = max(5, int(timeout))
        self.max_retries: int = max(0, int(max_retries))
        self.cooldown_seconds: float = max(30.0, float(cooldown_seconds))

        self._high_priority_models: tuple[str, ...] = (
            tuple(high_priority_models) if high_priority_models else DEFAULT_HIGH_PRIORITY_MODELS
        )
        self._general_models: tuple[str, ...] = (
            tuple(general_models) if general_models else DEFAULT_GENERAL_MODELS
        )

        self._model_cooldown_until: dict[str, float] = {}
        self.last_model_used: str = ""
        self.last_latency_ms: int = 0
        self.calls_total: int = 0
        self.calls_429: int = 0
        self.calls_fallback: int = 0

    def _get_models_for_priority(self, high_priority: bool = True) -> list[str]:
        if high_priority:
            raw_order = [self.model, *self._high_priority_models]
        else:
            raw_order = [*self._general_models, self.model]
        return list(dict.fromkeys(m.strip() for m in raw_order if m and m.strip()))

    def _call_gemini(
        self,
        user_prompt: str,
        system_instruction: str,
        high_priority: bool = True,
        temperature: float = 0.1,
        trigger_reason: str = "ADAPTIVE_CYCLE",
    ) -> str:
        if not self.api_key:
            raise RuntimeError("GEMINI_API_KEY is not configured")

        models_to_try = self._get_models_for_priority(high_priority=high_priority)
        now = time.time()
        available_models = [m for m in models_to_try if self._model_cooldown_until.get(m, 0.0) <= now]
        self.last_model_used = ""
        if not available_models:
            raise RuntimeError("All Gemini models are currently in cooldown")

        tier_label = "ALTA_PRIORIDAD" if high_priority else "GENERAL"
        call_start = time.perf_counter()
        last_err: Exception | None = None
        self.calls_total += 1

        for mdl in available_models:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{mdl}:generateContent"
            payload = {
                "system_instruction": {"parts": [{"text": system_instruction}]},
                "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
                "generationConfig": {
                    "temperature": temperature,
                    "responseMimeType": "application/json",
                },
            }
            req_timeout = max(self.timeout, 18) if mdl == "gemini-4-hydrogen" else self.timeout

            for attempt in range(self.max_retries + 1):
                try:
                    resp = requests.post(
                        url,
                        params={"key": self.api_key},
                        json=payload,
                        timeout=req_timeout,
                    )
                    if resp.status_code == 429:
                        self.calls_429 += 1
                        retry_after = _safe_float(resp.headers.get("Retry-After"))
                        cooldown = min(max(retry_after or self.cooldown_seconds, 60.0), 3600.0)
                        self._model_cooldown_until[mdl] = time.time() + cooldown
                        logger.warning("Gemini model %s rate-limited (HTTP 429); cooldown %.0fs.", mdl, cooldown)
                        last_err = RuntimeError(f"Gemini HTTP 429 ({mdl}): {resp.text[:200]}")
                        break
                    if resp.status_code == 503:
                        self._model_cooldown_until[mdl] = time.time() + self.cooldown_seconds
                        logger.warning("Gemini model %s unavailable (HTTP 503); cooldown %.0fs.", mdl, self.cooldown_seconds)
                        last_err = RuntimeError(f"Gemini HTTP 503 ({mdl}): {resp.text[:200]}")
                        break
                    if resp.status_code >= 500:
                        last_err = RuntimeError(f"Gemini HTTP {resp.status_code} ({mdl}): {resp.text[:200]}")
                        if attempt < self.max_retries:
                            time.sleep(0.5 * (attempt + 1))
                            continue
                        break
                    if resp.status_code >= 400:
                        last_err = RuntimeError(f"Gemini HTTP {resp.status_code} ({mdl}): {resp.text[:200]}")
                        break

                    data = resp.json()
                    candidates = data.get("candidates", [])
                    if not candidates:
                        last_err = RuntimeError(f"Gemini ({mdl}) returned no candidates")
                        break
                    parts = candidates[0].get("content", {}).get("parts", [])
                    text = "".join(str(part.get("text", "")) for part in parts if isinstance(part, dict) and "text" in part)
                    if text.strip():
                        self._model_cooldown_until.pop(mdl, None)
                        self.last_model_used = mdl
                        self.last_latency_ms = int(round((time.perf_counter() - call_start) * 1000.0))
                        logger.info(
                            "MT5AdaptiveAIBrain OK | model=%s | tier=%s | latency_ms=%d | trigger=%s",
                            mdl,
                            tier_label,
                            self.last_latency_ms,
                            trigger_reason,
                        )
                        return text
                    last_err = RuntimeError(f"Gemini ({mdl}) returned empty text")
                    break
                except requests.exceptions.Timeout as exc:
                    last_err = exc
                    self._model_cooldown_until[mdl] = time.time() + self.cooldown_seconds
                    logger.warning("Gemini model %s timed out (%ss); cooldown %.0fs.", mdl, req_timeout, self.cooldown_seconds)
                    break
                except Exception as exc:
                    last_err = exc
                    if attempt < self.max_retries:
                        time.sleep(0.5 * (attempt + 1))
                        continue
                    logger.warning("Gemini model %s failed: %s", mdl, exc)
                    break

        if last_err is not None:
            raise last_err
        raise RuntimeError("No Gemini model succeeded")

    def evaluate_market_cycle(
        self,
        market_context: dict[str, Any] | None,
        strategy_signals: list[Any],
        memory_context: dict[str, Any] | None,
        active_watches: list[Any],
        open_positions: list[Any],
        *,
        cycle_mode: str = "BASE_PATROL",
        high_priority: bool | None = None,
        now_utc: datetime | None = None,
        min_wake_minutes: float = 1.0,
        max_wake_minutes: float = 30.0,
    ) -> AdaptiveCycleDecision:
        """
        Evaluate candidate strategy signals, active sniper watches, memory context, and
        open positions to emit strict per-symbol adaptive decisions.
        """
        now = ensure_utc(now_utc)
        now_iso = utc_iso(now) or ""
        mode_up = str(cycle_mode or "BASE_PATROL").strip().upper()
        if mode_up not in ("BASE_PATROL", "SNIPER_WATCH"):
            mode_up = "BASE_PATROL"

        norm_signals = [d for d in (_to_plain_dict(s) for s in (strategy_signals or [])) if d.get("symbol")]
        norm_watches = [d for d in (_to_plain_dict(w) for w in (active_watches or [])) if d.get("symbol")]
        norm_positions = [_to_plain_dict(p) for p in (open_positions or []) if _to_plain_dict(p)]

        has_actionable = any(
            str(s.get("setup_stage", "")).upper() in ("READY", "FORMING") for s in norm_signals
        )
        use_high_priority = (
            high_priority
            if high_priority is not None
            else (mode_up == "SNIPER_WATCH" or has_actionable or bool(norm_watches))
        )
        priority_tier = "ALTA_PRIORIDAD" if use_high_priority else "GENERAL"

        if not norm_signals and not norm_watches:
            return AdaptiveCycleDecision(
                market_summary="Sin senales candidatas ni watches activos en este ciclo.",
                decisions={},
                model_used="quant_local",
                priority_tier=priority_tier,
                cycle_mode=mode_up,
                timestamp_utc=now_iso,
                fallback_used=False,
            )

        if not self.api_key:
            self.calls_fallback += 1
            return self._deterministic_fallback_cycle(
                market_context=market_context,
                signals=norm_signals,
                watches=norm_watches,
                cycle_mode=mode_up,
                priority_tier=priority_tier,
                now=now,
                min_wake_minutes=min_wake_minutes,
                max_wake_minutes=max_wake_minutes,
                reason="GEMINI_API_KEY no configurada; usando motor determinista.",
            )

        payload = {
            "now_utc": now_iso,
            "cycle_mode": mode_up,
            "wake_bounds_minutes": {
                "min_wake_minutes": round(float(min_wake_minutes), 2),
                "max_wake_minutes": round(float(max_wake_minutes), 2),
            },
            "market_context": market_context or {},
            "strategy_signals": norm_signals[:20],
            "active_watches": norm_watches[:10],
            "open_positions": norm_positions[:10],
            "memory_context": memory_context or {},
        }
        user_prompt = (
            "Evalua este ciclo de MetaTrader 5 y devuelve decisiones estrictas en JSON para cada simbolo relevante:\n\n"
            + json.dumps(payload, ensure_ascii=False)
        )

        try:
            raw_text = self._call_gemini(
                user_prompt=user_prompt,
                system_instruction=ADAPTIVE_CYCLE_SYSTEM_INSTRUCTION,
                high_priority=use_high_priority,
                temperature=0.1,
                trigger_reason=mode_up,
            )
            parsed = extract_json_object(raw_text)
            return self._parse_adaptive_cycle_response(
                parsed=parsed,
                signals=norm_signals,
                watches=norm_watches,
                cycle_mode=mode_up,
                priority_tier=priority_tier,
                model_used=self.last_model_used or "quant_local",
                now=now,
                min_wake_minutes=min_wake_minutes,
                max_wake_minutes=max_wake_minutes,
            )
        except Exception as exc:
            self.calls_fallback += 1
            logger.warning("MT5AdaptiveAIBrain falling back to deterministic logic: %s", exc)
            return self._deterministic_fallback_cycle(
                market_context=market_context,
                signals=norm_signals,
                watches=norm_watches,
                cycle_mode=mode_up,
                priority_tier=priority_tier,
                now=now,
                min_wake_minutes=min_wake_minutes,
                max_wake_minutes=max_wake_minutes,
                reason=f"Respaldo determinista activo tras fallo Gemini: {exc}",
                raw_error=str(exc),
            )

    def _resolve_wake_timing(
        self,
        action: str,
        raw_wake_mins: Any,
        raw_wake_at: Any,
        now: datetime,
        min_wake_minutes: float,
        max_wake_minutes: float,
    ) -> tuple[float | None, str | None]:
        if action not in ("WATCH_EXACT", "POSTPONE_WATCH"):
            return None, None

        min_m = max(1.0, float(min_wake_minutes))
        max_m = max(min_m, float(max_wake_minutes))
        mins = _safe_float(raw_wake_mins)

        if mins is None and raw_wake_at:
            try:
                target_dt = ensure_utc(str(raw_wake_at))
                mins = (target_dt - now).total_seconds() / 60.0
            except Exception:
                mins = None

        if mins is None:
            mins = min(10.0, max_m / 2.0)

        clamped_mins = round(max(min_m, min(max_m, mins)), 2)
        wake_dt = now + timedelta(minutes=clamped_mins)
        return clamped_mins, utc_iso(wake_dt)

    def _parse_adaptive_cycle_response(
        self,
        parsed: dict[str, Any],
        signals: list[dict[str, Any]],
        watches: list[dict[str, Any]],
        cycle_mode: str,
        priority_tier: str,
        model_used: str,
        now: datetime,
        min_wake_minutes: float,
        max_wake_minutes: float,
    ) -> AdaptiveCycleDecision:
        summary = str(parsed.get("market_summary", "")).strip() or "Evaluacion adaptativa completada."
        raw_decisions = parsed.get("decisions", [])
        if isinstance(raw_decisions, dict):
            raw_list = [{"symbol": k, **(v if isinstance(v, dict) else {})} for k, v in raw_decisions.items()]
        elif isinstance(raw_decisions, list):
            raw_list = [item for item in raw_decisions if isinstance(item, dict)]
        else:
            raw_list = []

        # Preserve canonical casing from input signals/watches (e.g., EURUSDm)
        canonical_symbols: dict[str, str] = {}
        for row in signals + watches:
            sym = str(row.get("symbol", "")).strip()
            if sym:
                canonical_symbols[sym.upper()] = sym

        watch_by_sym_up = {str(w.get("symbol", "")).strip().upper(): w for w in watches}
        decisions: dict[str, SymbolAdaptiveDecision] = {}

        for item in raw_list:
            raw_sym = str(item.get("symbol", "")).strip()
            if not raw_sym:
                continue
            sym = canonical_symbols.get(raw_sym.upper(), raw_sym)
            action = str(item.get("action", "HOLD")).strip().upper()
            if action not in VALID_ADAPTIVE_ACTIONS:
                action = "HOLD"

            # Guardrail: POSTPONE_WATCH / INVALIDATE_WATCH only valid if symbol has an active watch
            if action in ("POSTPONE_WATCH", "INVALIDATE_WATCH") and sym.upper() not in watch_by_sym_up:
                action = "WATCH_EXACT" if action == "POSTPONE_WATCH" else "HOLD"

            wake_mins, wake_iso = self._resolve_wake_timing(
                action=action,
                raw_wake_mins=item.get("wake_in_minutes"),
                raw_wake_at=item.get("wake_at_utc"),
                now=now,
                min_wake_minutes=min_wake_minutes,
                max_wake_minutes=max_wake_minutes,
            )

            decisions[sym] = SymbolAdaptiveDecision(
                symbol=sym,
                action=action,
                strategy_name=str(item.get("strategy_name", "")).strip(),
                confidence_pct=max(0, min(100, _safe_int(item.get("confidence_pct", 50), 50))),
                wake_in_minutes=wake_mins,
                wake_at_utc=wake_iso,
                watch_hypothesis=str(item.get("watch_hypothesis", "")).strip(),
                trigger_condition=str(item.get("trigger_condition", "")).strip(),
                invalidation_condition=str(item.get("invalidation_condition", "")).strip(),
                sl_adjustment=_safe_float(item.get("sl_adjustment")),
                tp_adjustment=_safe_float(item.get("tp_adjustment")),
                reasoning=str(item.get("reasoning", "")).strip(),
                lesson_note=str(item.get("lesson_note", "")).strip(),
            )

        # Ensure any active watch omitted by the LLM gets a safe deterministic decision
        if watches:
            fallback = self._deterministic_fallback_cycle(
                market_context=None,
                signals=signals,
                watches=watches,
                cycle_mode=cycle_mode,
                priority_tier=priority_tier,
                now=now,
                min_wake_minutes=min_wake_minutes,
                max_wake_minutes=max_wake_minutes,
                reason="",
            )
            for w in watches:
                sym = str(w.get("symbol", "")).strip()
                if sym and sym not in decisions and sym in fallback.decisions:
                    decisions[sym] = fallback.decisions[sym]

        return AdaptiveCycleDecision(
            market_summary=summary,
            decisions=decisions,
            model_used=model_used,
            priority_tier=priority_tier,
            cycle_mode=cycle_mode,
            timestamp_utc=utc_iso(now) or "",
            fallback_used=False,
        )

    def _deterministic_fallback_cycle(
        self,
        market_context: dict[str, Any] | None,
        signals: list[dict[str, Any]],
        watches: list[dict[str, Any]],
        cycle_mode: str,
        priority_tier: str,
        now: datetime,
        min_wake_minutes: float,
        max_wake_minutes: float,
        reason: str,
        raw_error: str = "",
    ) -> AdaptiveCycleDecision:
        """Safe rule-based fallback so the adaptive loop never stalls on API outages."""
        best_signal_by_sym: dict[str, dict[str, Any]] = {}
        for sig in signals:
            sym = str(sig.get("symbol", "")).strip()
            if not sym:
                continue
            prev = best_signal_by_sym.get(sym)
            sig_score = float(sig.get("score", 0.0) or 0.0)
            prev_score = float(prev.get("score", -1.0) or -1.0) if prev else -1.0
            if prev is None or sig_score > prev_score:
                best_signal_by_sym[sym] = sig

        watch_by_sym = {str(w.get("symbol", "")).strip(): w for w in watches if w.get("symbol")}
        all_symbols = list(dict.fromkeys([*watch_by_sym.keys(), *best_signal_by_sym.keys()]))
        decisions: dict[str, SymbolAdaptiveDecision] = {}

        for sym in all_symbols:
            sig = best_signal_by_sym.get(sym)
            watch = watch_by_sym.get(sym)

            stage = str((sig or {}).get("setup_stage", "NONE")).strip().upper()
            direction = str((sig or {}).get("direction", "NONE")).strip().upper()
            score = max(0, min(100, _safe_int((sig or {}).get("score", 50), 50)))
            strategy_name = str(
                (sig or {}).get("strategy_name") or (watch or {}).get("strategy_name") or ""
            ).strip()
            forming_hint = str((sig or {}).get("forming_hint", "")).strip()
            inv_level = (sig or {}).get("invalidation_level")
            inv_str = f"Invalidacion en nivel {inv_level}" if inv_level is not None else ""

            if stage == "READY" and direction in ("BUY", "SELL") and score >= 65:
                action = "ENTER_BUY" if direction == "BUY" else "ENTER_SELL"
                decisions[sym] = SymbolAdaptiveDecision(
                    symbol=sym,
                    action=action,
                    strategy_name=strategy_name,
                    confidence_pct=score,
                    reasoning=f"Fallback determinista: senal READY ({strategy_name}, score={score}).",
                )
            elif stage == "FORMING" and score >= 50:
                if watch is not None:
                    postpone_cnt = int(watch.get("postpone_count", 0) or 0)
                    max_postpones = int(watch.get("max_postpones", 3) or 3)
                    if postpone_cnt + 1 >= max_postpones:
                        decisions[sym] = SymbolAdaptiveDecision(
                            symbol=sym,
                            action="INVALIDATE_WATCH",
                            strategy_name=strategy_name,
                            confidence_pct=score,
                            reasoning="Fallback determinista: watch agotado por limite de posposiciones.",
                            lesson_note=f"Setup {strategy_name} en {sym} no confirmo a tiempo.",
                        )
                    else:
                        wake_m, wake_iso = self._resolve_wake_timing(
                            "POSTPONE_WATCH", 8.0, None, now, min_wake_minutes, max_wake_minutes
                        )
                        decisions[sym] = SymbolAdaptiveDecision(
                            symbol=sym,
                            action="POSTPONE_WATCH",
                            strategy_name=strategy_name,
                            confidence_pct=score,
                            wake_in_minutes=wake_m,
                            wake_at_utc=wake_iso,
                            watch_hypothesis=forming_hint or str(watch.get("hypothesis", "")),
                            trigger_condition=str(watch.get("trigger_condition", "Confirmacion de vela de entrada")),
                            invalidation_condition=inv_str or str(watch.get("invalidation_condition", "")),
                            reasoning=f"Fallback determinista: setup aun FORMING (score={score}), posponiendo watch.",
                        )
                else:
                    wake_m, wake_iso = self._resolve_wake_timing(
                        "WATCH_EXACT", 8.0, None, now, min_wake_minutes, max_wake_minutes
                    )
                    decisions[sym] = SymbolAdaptiveDecision(
                        symbol=sym,
                        action="WATCH_EXACT",
                        strategy_name=strategy_name,
                        confidence_pct=score,
                        wake_in_minutes=wake_m,
                        wake_at_utc=wake_iso,
                        watch_hypothesis=forming_hint or f"Setup {strategy_name} en formacion",
                        trigger_condition=f"Confirmacion {direction or 'direccional'} en cierre de vela",
                        invalidation_condition=inv_str or "Perdida de estructura tecnica",
                        reasoning=f"Fallback determinista: programando sniper watch para setup FORMING (score={score}).",
                    )
            elif watch is not None:
                decisions[sym] = SymbolAdaptiveDecision(
                    symbol=sym,
                    action="INVALIDATE_WATCH",
                    strategy_name=strategy_name,
                    confidence_pct=min(score, 45),
                    reasoning="Fallback determinista: el setup vigilado perdio vigencia.",
                    lesson_note=f"Watch en {sym} ({strategy_name}) invalidado al perder estructura.",
                )
            else:
                decisions[sym] = SymbolAdaptiveDecision(
                    symbol=sym,
                    action="HOLD",
                    strategy_name=strategy_name,
                    confidence_pct=score,
                    reasoning="Fallback determinista: sin ventaja clara, esperar siguiente ciclo base.",
                )

        return AdaptiveCycleDecision(
            market_summary=reason or "Evaluacion determinista local completada.",
            decisions=decisions,
            model_used="quant_local",
            priority_tier=priority_tier,
            cycle_mode=cycle_mode,
            timestamp_utc=utc_iso(now) or "",
            fallback_used=True,
            raw_error=raw_error,
        )

    def generate_post_mortem_lesson(
        self,
        trade_outcome: dict[str, Any] | Any,
        market_context: dict[str, Any] | None = None,
    ) -> str:
        """
        Extract a concise, reusable lesson after a trade closes.
        Falls back to a structured deterministic lesson if Gemini is unavailable.
        """
        outcome = _to_plain_dict(trade_outcome)
        sym = str(outcome.get("symbol", "UNKNOWN")).strip()
        strategy = str(outcome.get("strategy_name", "UNKNOWN")).strip()
        direction = str(outcome.get("direction", "")).strip().upper()
        regime = str(outcome.get("regime", "")).strip().upper()
        session = str(outcome.get("session", "")).strip()
        pnl = _safe_float(outcome.get("pnl_usd", outcome.get("profit_usd")), 0.0) or 0.0
        r_mult = _safe_float(outcome.get("r_multiple"))
        close_reason = str(outcome.get("close_reason", outcome.get("exit_reason", ""))).strip()

        def _deterministic_lesson() -> str:
            outcome_tag = "ganadora" if pnl > 0 else ("perdedora" if pnl < 0 else "en break-even")
            r_str = f" ({r_mult:+.2f}R)" if r_mult is not None else ""
            ctx_parts = [p for p in (regime, session, close_reason) if p]
            ctx_str = f" en {'/'.join(ctx_parts)}" if ctx_parts else ""
            if pnl > 0:
                return (
                    f"{sym} {direction} con {strategy} fue {outcome_tag}{r_str}{ctx_str}: "
                    "mantener disciplina de entrada alineada con regimen."
                )[:240]
            return (
                f"{sym} {direction} con {strategy} fue {outcome_tag}{r_str}{ctx_str}: "
                "exigir mayor confirmacion de momentum y evitar entradas contra estructura."
            )[:240]

        if not self.api_key:
            return _deterministic_lesson()

        payload = {
            "trade_outcome": outcome,
            "market_context": market_context or {},
        }
        user_prompt = (
            "Analiza esta operacion cerrada y extrae una sola leccion operativa concisa y reutilizable:\n\n"
            + json.dumps(payload, ensure_ascii=False)
        )

        try:
            raw_text = self._call_gemini(
                user_prompt=user_prompt,
                system_instruction=POST_MORTEM_SYSTEM_INSTRUCTION,
                high_priority=False,
                temperature=0.15,
                trigger_reason="POST_MORTEM",
            )
            parsed = extract_json_object(raw_text)
            lesson = str(parsed.get("lesson", "")).strip()
            if lesson:
                return lesson[:280]
        except Exception as exc:
            logger.warning("Post-mortem Gemini call failed (%s); using deterministic lesson.", exc)

        return _deterministic_lesson()

    def get_quota_telemetry(self) -> dict[str, Any]:
        now = time.time()
        active_cooldowns = {
            mdl: round(until - now, 1)
            for mdl, until in self._model_cooldown_until.items()
            if until > now
        }
        return {
            "calls_total": self.calls_total,
            "calls_429": self.calls_429,
            "calls_fallback": self.calls_fallback,
            "last_model_used": self.last_model_used or "quant_local",
            "last_latency_ms": self.last_latency_ms,
            "active_model_cooldowns_sec": active_cooldowns,
        }

    @staticmethod
    def estimate_quota_usage(
        base_interval_minutes: int = 30,
        avg_sniper_wakes_per_day: int = 16,
        avg_post_mortems_per_day: int = 6,
    ) -> dict[str, Any]:
        return estimate_gemini_quota_usage(
            base_interval_minutes=base_interval_minutes,
            avg_sniper_wakes_per_day=avg_sniper_wakes_per_day,
            avg_post_mortems_per_day=avg_post_mortems_per_day,
        )
