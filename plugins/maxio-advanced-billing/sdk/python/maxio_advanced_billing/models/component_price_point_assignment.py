from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.price_point2 import PricePoint2, PricePoint2Dict


class ComponentPricePointAssignment(SdkBaseModel):
    component_id: Optional[int] = UNSET
    price_point: Optional[PricePoint2] = UNSET


class ComponentPricePointAssignmentDict(TypedDict):
    component_id: NotRequired[int]
    price_point: NotRequired[PricePoint2Dict]
