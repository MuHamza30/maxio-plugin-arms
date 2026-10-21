from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpdateProductPricePoint(SdkBaseModel):
    handle: Optional[str] = UNSET
    price_in_cents: Optional[int] = UNSET


class UpdateProductPricePointDict(TypedDict):
    handle: NotRequired[str]
    price_in_cents: NotRequired[int]
