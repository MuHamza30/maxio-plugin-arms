from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ComponentPrice(SdkBaseModel):
    id: Optional[int] = UNSET
    component_id: Optional[int] = UNSET
    starting_quantity: Optional[int] = UNSET
    ending_quantity: OptionalNullable[int] = UNSET
    unit_price: Optional[str] = UNSET
    price_point_id: Optional[int] = UNSET
    formatted_unit_price: Optional[str] = UNSET
    segment_id: OptionalNullable[int] = UNSET


class ComponentPriceDict(TypedDict):
    id: NotRequired[int]
    component_id: NotRequired[int]
    starting_quantity: NotRequired[int]
    ending_quantity: NotRequired[int | None]
    unit_price: NotRequired[str]
    price_point_id: NotRequired[int]
    formatted_unit_price: NotRequired[str]
    segment_id: NotRequired[int | None]
