from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProductPricePointErrors(SdkBaseModel):
    price_point: Optional[str] = UNSET
    interval: Optional[list[str]] = UNSET
    interval_unit: Optional[list[str]] = UNSET
    name: Optional[list[str]] = UNSET
    price: Optional[list[str]] = UNSET
    price_in_cents: Optional[list[str]] = UNSET


class ProductPricePointErrorsDict(TypedDict):
    price_point: NotRequired[str]
    interval: NotRequired[list[str]]
    interval_unit: NotRequired[list[str]]
    name: NotRequired[list[str]]
    price: NotRequired[list[str]]
    price_in_cents: NotRequired[list[str]]
