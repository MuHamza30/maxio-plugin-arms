from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ComponentCostDataRateTier(SdkBaseModel):
    starting_quantity: Optional[int] = UNSET
    ending_quantity: OptionalNullable[int] = UNSET
    quantity: Optional[str] = UNSET
    unit_price: Optional[str] = UNSET
    amount: Optional[str] = UNSET


class ComponentCostDataRateTierDict(TypedDict):
    starting_quantity: NotRequired[int]
    ending_quantity: NotRequired[int | None]
    quantity: NotRequired[str]
    unit_price: NotRequired[str]
    amount: NotRequired[str]
