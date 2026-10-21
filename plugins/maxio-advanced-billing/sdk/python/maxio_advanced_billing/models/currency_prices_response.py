from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .currency_price import CurrencyPrice, CurrencyPriceDict


class CurrencyPricesResponse(SdkBaseModel):
    currency_prices: list[CurrencyPrice]


class CurrencyPricesResponseDict(TypedDict):
    currency_prices: list[CurrencyPriceDict]
