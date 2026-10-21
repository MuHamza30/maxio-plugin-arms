from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.unit_price8 import UnitPrice8, UnitPrice8Dict


class CreateOrUpdateSegmentPrice(SdkBaseModel):
    starting_quantity: Optional[int] = UNSET
    ending_quantity: Optional[int] = UNSET
    unit_price: UnitPrice8
    """The price can contain up to 8 decimal places. e.g., 1.00 or 0.0012 or 0.00000065"""


class CreateOrUpdateSegmentPriceDict(TypedDict):
    starting_quantity: NotRequired[int]
    ending_quantity: NotRequired[int]
    unit_price: UnitPrice8Dict
