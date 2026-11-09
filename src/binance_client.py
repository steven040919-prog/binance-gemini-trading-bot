from __future__ import annotations

import hashlib
import hmac
import logging
import time
from dataclasses import dataclass
from decimal import Decimal, ROUND_DOWN
from typing import Any
from urllib.parse import urlencode

import requests

logger = logging.getLogger(__name__)

# Endpoints publicos (data-api.binance.vision no tiene bloqueo geografico en GitHub Actions)
PUBLIC_ENDPOINTS = [
    "https://data-api.binance.vision",
    "https://api.binance.com",
    "https://api1.binance.com",
    "https://api2.binance.com",
    "https://api3.binance.com",
    "https://api4.binance.com",
]

# Endpoints autenticados para cuenta y ejecucion de ordenes Spot
PRIVATE_ENDPOINTS = [
    "https://api.binance.com",
    "https://api1.binance.com",
    "https://api2.binance.com",
    "https://api3.binance.com",
    "https://api4.binance.com",
]


class BinanceAPIError(RuntimeError):
    def __init__(self, status_code: int, code: int | None, message: str) -> None:
        super().__init__(f"Binance API Error (HTTP {status_code}, code={code}): {message}")
        self.status_code = status_code
        self.code = code
        self.message = message


@dataclass(frozen=True)
class SymbolFilters:
    symbol: str
    base_asset: str
    quote_asset: str
    status: str
    step_size: Decimal
    min_qty: Decimal
    max_qty: Decimal
    min_notional: Decimal
    tick_size: Decimal
    quote_order_qty_allowed: bool

    def round_quantity(self, quantity: float | Decimal) -> Decimal:
        qty = Decimal(str(quantity))
        if self.step_size <= 0:
            return qty
        steps = (qty / self.step_size).to_integral_value(rounding=ROUND_DOWN)
        return (steps * self.step_size).normalize()

    def format_quantity(self, quantity: float | Decimal) -> str:
        rounded = self.round_quantity(quantity)
        # Evita notacion cientifica
        return format(rounded, "f")


def normalize_proxy_list(raw_proxy: str) -> list[str]:
    """
    Convierte uno o varios proxies (separados por coma o salto de linea) al formato URL estandar.
    Soporta tanto 'http://user:pass@ip:port' / 'socks5://...' como el formato de Webshare 'ip:port:user:pass'.
    """
    if not raw_proxy or not raw_proxy.strip():
        return []
    proxies: list[str] = []
    for token in raw_proxy.replace("\n", ",").replace(";", ",").split(","):
        item = token.strip()
        if not item:
            continue
        if "://" in item:
            proxies.append(item)
            continue
        parts = item.split(":")
        if len(parts) == 4:
            ip, port, user, pwd = parts
            proxies.append(f"http://{user}:{pwd}@{ip}:{port}")
        elif len(parts) == 2:
            ip, port = parts
            proxies.append(f"http://{ip}:{port}")
        else:
            proxies.append(f"http://{item}")
    return proxies


class BinanceSpotClient:
    """Cliente ligero y resiliente para Binance Spot API con soporte de Proxy Europeo y Failover."""

    def __init__(
        self,
        api_key: str = "",
        api_secret: str = "",
        proxy_url: str = "",
        timeout: int = 15,
    ) -> None:
        self.api_key = api_key.strip()
        self.api_secret = api_secret.strip()
        self.timeout = timeout
        self.time_offset_ms: int = 0
        self._symbol_filters_cache: dict[str, SymbolFilters] = {}
        self.proxy_candidates: list[str] = normalize_proxy_list(proxy_url)

        self.session = requests.Session()
        if self.api_key:
            self.session.headers.update({"X-MBX-APIKEY": self.api_key})
        if self.proxy_candidates:
            logger.info("Configurados %d proxy(s) para endpoints autenticados de Binance.", len(self.proxy_candidates))

    def sync_time(self) -> int:
        """Sincroniza el reloj local con el servidor de Binance para evitar errores -1021."""
        data = self._request("GET", "/api/v3/time", signed=False)
        server_time = int(data["serverTime"])
        local_time = int(time.time() * 1000)
        self.time_offset_ms = server_time - local_time
        logger.debug("Desfase de tiempo con Binance: %d ms", self.time_offset_ms)
        return self.time_offset_ms

    def _sign_params(self, params: dict[str, Any]) -> str:
        query = urlencode(params, doseq=True)
        signature = hmac.new(
            self.api_secret.encode("utf-8"),
            query.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
        return f"{query}&signature={signature}"

    def _request(
        self,
        method: str,
        path: str,
        params: dict[str, Any] | None = None,
        signed: bool = False,
    ) -> Any:
        endpoints = PRIVATE_ENDPOINTS if signed else PUBLIC_ENDPOINTS
        req_params = dict(params or {})

        if signed:
            if not self.api_key or not self.api_secret:
                raise ValueError("Se requieren BINANCE_API_KEY y BINANCE_API_SECRET para llamadas firmadas.")
            req_params.setdefault("recvWindow", 10000)
            req_params["timestamp"] = int(time.time() * 1000) + self.time_offset_ms
            query_string = self._sign_params(req_params)
        else:
            query_string = urlencode(req_params, doseq=True) if req_params else ""

        last_error: Exception | None = None

        if signed and self.proxy_candidates:
            proxy_chain: list[dict[str, str] | None] = [
                {"http": p, "https": p} for p in self.proxy_candidates
            ] + [None]
        elif self.proxy_candidates:
            proxy_chain = [None] + [{"http": p, "https": p} for p in self.proxy_candidates]
        else:
            proxy_chain = [None]

        for proxies in proxy_chain:
            for base_url in endpoints:
                url = f"{base_url}{path}"
                if query_string:
                    url = f"{url}?{query_string}"

                try:
                    resp = self.session.request(
                        method=method,
                        url=url,
                        timeout=self.timeout,
                        proxies=proxies,
                    )
                except requests.RequestException as exc:
                    last_error = exc
                    logger.warning("Fallo de conexion en %s%s: %s. Probando siguiente ruta...", base_url, path, exc)
                    continue

                if resp.status_code == 451:
                    geo_msg = (
                        "Binance bloqueo la solicitud por ubicacion geografica (HTTP 451 - IP de EE.UU. en GitHub Actions). "
                        "Configura el secret BINANCE_PROXY_URL con un proxy fuera de EE.UU."
                    )
                    last_error = BinanceAPIError(451, -451, geo_msg)
                    logger.warning("HTTP 451 en %s. Probando siguiente ruta...", base_url)
                    continue

                if resp.status_code >= 400:
                    try:
                        err_payload = resp.json()
                        err_code = err_payload.get("code")
                        err_msg = err_payload.get("msg", resp.text)
                    except ValueError:
                        err_code = None
                        err_msg = resp.text

                    # Si es desfase de reloj (-1021), sincronizamos y reintentamos una vez
                    if signed and err_code == -1021:
                        logger.info("Re-sincronizando reloj con Binance tras error -1021...")
                        self.sync_time()
                        req_params["timestamp"] = int(time.time() * 1000) + self.time_offset_ms
                        retry_qs = self._sign_params(req_params)
                        retry_url = f"{base_url}{path}?{retry_qs}"
                        retry_resp = self.session.request(
                            method=method,
                            url=retry_url,
                            timeout=self.timeout,
                            proxies=proxies,
                        )
                        if retry_resp.status_code < 400:
                            return retry_resp.json()

                    raise BinanceAPIError(resp.status_code, err_code, err_msg)

                return resp.json()

        if last_error:
            raise last_error
        raise RuntimeError(f"No se pudo completar la solicitud a Binance para {path}")

    # =========================================================================
    # DATOS DE MERCADO PUBLICOS
    # =========================================================================
    def get_24h_tickers(self) -> list[dict[str, Any]]:
        """Obtiene estadisticas de 24h de todos los pares en Binance Spot."""
        return self._request("GET", "/api/v3/ticker/24hr", signed=False)

    def get_ticker_price(self, symbol: str) -> float:
        """Obtiene el ultimo precio de un par especifico."""
        data = self._request("GET", "/api/v3/ticker/price", params={"symbol": symbol}, signed=False)
        return float(data["price"])

    def get_all_prices(self) -> dict[str, float]:
        """Retorna un diccionario {symbol: price} para todos los pares."""
        rows = self._request("GET", "/api/v3/ticker/price", signed=False)
        return {row["symbol"]: float(row["price"]) for row in rows}

    def get_klines(self, symbol: str, interval: str = "15m", limit: int = 100) -> list[dict[str, float]]:
        """Obtiene velas OHLCV formateadas para calculo de indicadores tecnicos."""
        raw = self._request(
            "GET",
            "/api/v3/klines",
            params={"symbol": symbol, "interval": interval, "limit": limit},
            signed=False,
        )
        candles: list[dict[str, float]] = []
        for item in raw:
            candles.append(
                {
                    "open_time": float(item[0]),
                    "open": float(item[1]),
                    "high": float(item[2]),
                    "low": float(item[3]),
                    "close": float(item[4]),
                    "volume": float(item[5]),
                    "close_time": float(item[6]),
                    "quote_volume": float(item[7]),
                    "trades": float(item[8]),
                }
            )
        return candles

    def get_exchange_filters(self, symbols: list[str] | None = None) -> dict[str, SymbolFilters]:
        """Obtiene y cachea las reglas LOT_SIZE y NOTIONAL de los pares solicitados."""
        missing = [s for s in (symbols or []) if s not in self._symbol_filters_cache]
        if symbols and not missing:
            return {s: self._symbol_filters_cache[s] for s in symbols}

        params: dict[str, Any] = {}
        if symbols and len(missing) <= 20:
            import json
            params["symbols"] = json.dumps(missing, separators=(",", ":"))

        data = self._request("GET", "/api/v3/exchangeInfo", params=params, signed=False)
        for sym_info in data.get("symbols", []):
            sym = sym_info["symbol"]
            step_size = Decimal("0.00000001")
            min_qty = Decimal("0.00000001")
            max_qty = Decimal("9000000000")
            min_notional = Decimal("5.0")
            tick_size = Decimal("0.00000001")

            for f in sym_info.get("filters", []):
                ftype = f.get("filterType")
                if ftype == "LOT_SIZE":
                    step_size = Decimal(str(f.get("stepSize", "0.00000001")))
                    min_qty = Decimal(str(f.get("minQty", "0.00000001")))
                    max_qty = Decimal(str(f.get("maxQty", "9000000000")))
                elif ftype in ("NOTIONAL", "MIN_NOTIONAL"):
                    min_notional = Decimal(str(f.get("minNotional", "5.0")))
                elif ftype == "PRICE_FILTER":
                    tick_size = Decimal(str(f.get("tickSize", "0.00000001")))

            self._symbol_filters_cache[sym] = SymbolFilters(
                symbol=sym,
                base_asset=sym_info.get("baseAsset", ""),
                quote_asset=sym_info.get("quoteAsset", ""),
                status=sym_info.get("status", "TRADING"),
                step_size=step_size,
                min_qty=min_qty,
                max_qty=max_qty,
                min_notional=min_notional,
                tick_size=tick_size,
                quote_order_qty_allowed=bool(sym_info.get("quoteOrderQtyMarketAllowed", True)),
            )

        if symbols:
            return {s: self._symbol_filters_cache[s] for s in symbols if s in self._symbol_filters_cache}
        return dict(self._symbol_filters_cache)

    # =========================================================================
    # ENDPOINTS PRIVADOS DE CUENTA Y ORDENES SPOT
    # =========================================================================
    def get_account_balances(self) -> dict[str, float]:
        """Retorna los saldos libres (free) mayores a 0 en la cuenta Spot."""
        self.sync_time()
        account = self._request("GET", "/api/v3/account", signed=True)
        balances: dict[str, float] = {}
        for item in account.get("balances", []):
            free_amt = float(item.get("free", 0.0))
            if free_amt > 0:
                balances[item["asset"]] = free_amt
        return balances

    def place_market_buy_usdt(
        self,
        symbol: str,
        usdt_amount: float,
        dry_run: bool = False,
    ) -> dict[str, Any]:
        """Ejecuta una compra Spot a precio de mercado gastando `usdt_amount` en USDT."""
        filters_map = self.get_exchange_filters([symbol])
        sym_filter = filters_map.get(symbol)
        current_price = self.get_ticker_price(symbol)

        if sym_filter and Decimal(str(usdt_amount)) < sym_filter.min_notional:
            raise ValueError(
                f"El monto de compra ({usdt_amount:.2f} USDT) es menor al minimo permitido "
                f"por Binance para {symbol} ({sym_filter.min_notional} USDT)."
            )

        if dry_run:
            est_qty = usdt_amount / current_price
            if sym_filter:
                est_qty = float(sym_filter.round_quantity(est_qty))
            return {
                "symbol": symbol,
                "side": "BUY",
                "type": "MARKET",
                "status": "FILLED_DRY_RUN",
                "executedQty": str(est_qty),
                "cummulativeQuoteQty": f"{usdt_amount:.2f}",
                "avgPrice": current_price,
                "transactTime": int(time.time() * 1000),
            }

        params: dict[str, Any] = {
            "symbol": symbol,
            "side": "BUY",
            "type": "MARKET",
        }
        if sym_filter is None or sym_filter.quote_order_qty_allowed:
            params["quoteOrderQty"] = f"{usdt_amount:.2f}"
        else:
            raw_qty = usdt_amount / current_price
            params["quantity"] = sym_filter.format_quantity(raw_qty)

        order = self._request("POST", "/api/v3/order", params=params, signed=True)
        exec_qty = float(order.get("executedQty", 0.0))
        quote_qty = float(order.get("cummulativeQuoteQty", 0.0))
        order["avgPrice"] = (quote_qty / exec_qty) if exec_qty > 0 else current_price
        return order

    def place_market_sell_quantity(
        self,
        symbol: str,
        quantity: float,
        dry_run: bool = False,
    ) -> dict[str, Any]:
        """Ejecuta una venta Spot a precio de mercado ajustando la cantidad al LOT_SIZE exacto."""
        filters_map = self.get_exchange_filters([symbol])
        sym_filter = filters_map.get(symbol)
        current_price = self.get_ticker_price(symbol)

        if sym_filter:
            formatted_qty = sym_filter.format_quantity(quantity)
            rounded_qty = float(formatted_qty)
            if Decimal(formatted_qty) < sym_filter.min_qty:
                raise ValueError(
                    f"La cantidad a vender de {symbol} ({formatted_qty}) es menor a minQty ({sym_filter.min_qty})."
                )
            notional = Decimal(formatted_qty) * Decimal(str(current_price))
            if notional < sym_filter.min_notional:
                raise ValueError(
                    f"El valor nocional de venta de {symbol} ({float(notional):.2f} USDT) es menor a "
                    f"minNotional ({sym_filter.min_notional} USDT)."
                )
        else:
            rounded_qty = quantity
            formatted_qty = f"{quantity:.6f}"

        if dry_run:
            quote_total = rounded_qty * current_price
            return {
                "symbol": symbol,
                "side": "SELL",
                "type": "MARKET",
                "status": "FILLED_DRY_RUN",
                "executedQty": formatted_qty,
                "cummulativeQuoteQty": f"{quote_total:.2f}",
                "avgPrice": current_price,
                "transactTime": int(time.time() * 1000),
            }

        params = {
            "symbol": symbol,
            "side": "SELL",
            "type": "MARKET",
            "quantity": formatted_qty,
        }
        order = self._request("POST", "/api/v3/order", params=params, signed=True)
        exec_qty = float(order.get("executedQty", 0.0))
        quote_qty = float(order.get("cummulativeQuoteQty", 0.0))
        order["avgPrice"] = (quote_qty / exec_qty) if exec_qty > 0 else current_price
        return order
