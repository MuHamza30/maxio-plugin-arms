from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Price1(SdkBaseModel):
    starting_quantity: Optional[int] = UNSET
    ending_quantity: OptionalNullable[int] = UNSET
    unit_price: Optional[str] = UNSET


class Price1Dict(TypedDict):
    starting_quantity: NotRequired[int]
    ending_quantity: NotRequired[int | None]
    unit_price: NotRequired[str]
