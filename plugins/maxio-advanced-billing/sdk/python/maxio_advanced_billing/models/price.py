from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .unions.ending_quantity import EndingQuantity, EndingQuantityDict
from .unions.starting_quantity import StartingQuantity, StartingQuantityDict
from .unions.unit_price import UnitPrice, UnitPriceDict


class Price(SdkBaseModel):
    starting_quantity: StartingQuantity
    ending_quantity: OptionalNullable[EndingQuantity] = UNSET
    unit_price: UnitPrice
    """The price can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065"""


class PriceDict(TypedDict):
    starting_quantity: StartingQuantityDict
    ending_quantity: NotRequired[EndingQuantityDict | None]
    unit_price: UnitPriceDict
