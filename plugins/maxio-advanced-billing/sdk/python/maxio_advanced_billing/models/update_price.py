from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.ending_quantity import EndingQuantity, EndingQuantityDict
from .unions.starting_quantity import StartingQuantity, StartingQuantityDict
from .unions.unit_price import UnitPrice, UnitPriceDict


class UpdatePrice(SdkBaseModel):
    id: Optional[int] = UNSET
    ending_quantity: Optional[EndingQuantity] = UNSET
    unit_price: Optional[UnitPrice] = UNSET
    """The price can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065"""

    destroy: Optional[bool] = Field(default=UNSET, alias="_destroy")
    starting_quantity: Optional[StartingQuantity] = UNSET


class UpdatePriceDict(TypedDict):
    id: NotRequired[int]
    ending_quantity: NotRequired[EndingQuantityDict]
    unit_price: NotRequired[UnitPriceDict]
    destroy: NotRequired[bool]
    starting_quantity: NotRequired[StartingQuantityDict]
