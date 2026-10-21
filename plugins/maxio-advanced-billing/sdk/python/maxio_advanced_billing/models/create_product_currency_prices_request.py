from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_product_currency_price import CreateProductCurrencyPrice, CreateProductCurrencyPriceDict


class CreateProductCurrencyPricesRequest(SdkBaseModel):
    currency_prices: list[CreateProductCurrencyPrice]


class CreateProductCurrencyPricesRequestDict(TypedDict):
    currency_prices: list[CreateProductCurrencyPriceDict]
