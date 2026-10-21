from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_currency_price import UpdateCurrencyPrice, UpdateCurrencyPriceDict


class UpdateCurrencyPricesRequest(SdkBaseModel):
    currency_prices: list[UpdateCurrencyPrice]


class UpdateCurrencyPricesRequestDict(TypedDict):
    currency_prices: list[UpdateCurrencyPriceDict]
