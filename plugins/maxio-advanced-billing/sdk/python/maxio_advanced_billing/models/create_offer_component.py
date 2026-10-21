from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateOfferComponent(SdkBaseModel):
    component_id: Optional[int] = UNSET
    price_point_id: Optional[int] = UNSET
    starting_quantity: Optional[int] = UNSET


class CreateOfferComponentDict(TypedDict):
    component_id: NotRequired[int]
    price_point_id: NotRequired[int]
    starting_quantity: NotRequired[int]
