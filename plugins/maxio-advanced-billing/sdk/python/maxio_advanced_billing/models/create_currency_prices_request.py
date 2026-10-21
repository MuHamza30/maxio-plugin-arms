from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_currency_price import CreateCurrencyPrice, CreateCurrencyPriceDict


class CreateCurrencyPricesRequest(SdkBaseModel):
    currency_prices: list[CreateCurrencyPrice]


class CreateCurrencyPricesRequestDict(TypedDict):
    currency_prices: list[CreateCurrencyPriceDict]
