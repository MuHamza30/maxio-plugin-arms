from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .currency_overage_prices import CurrencyOveragePrices, CurrencyOveragePricesDict


class ComponentPricePointCurrencyOverageResponse(SdkBaseModel):
    price_point: CurrencyOveragePrices
    """Extends a component price point with currency overage prices."""


class ComponentPricePointCurrencyOverageResponseDict(TypedDict):
    price_point: CurrencyOveragePricesDict
