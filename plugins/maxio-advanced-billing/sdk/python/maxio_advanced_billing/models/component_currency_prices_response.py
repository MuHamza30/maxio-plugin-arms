from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .component_currency_price import ComponentCurrencyPrice, ComponentCurrencyPriceDict


class ComponentCurrencyPricesResponse(SdkBaseModel):
    currency_prices: list[ComponentCurrencyPrice]


class ComponentCurrencyPricesResponseDict(TypedDict):
    currency_prices: list[ComponentCurrencyPriceDict]
