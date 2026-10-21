from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UpdateCurrencyPrice(SdkBaseModel):
    id: int
    """ID of the currency price record being updated"""

    price: float
    """New price for the given currency"""


class UpdateCurrencyPriceDict(TypedDict):
    id: int
    price: float
