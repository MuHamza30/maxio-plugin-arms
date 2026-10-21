from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .create_offer_component import CreateOfferComponent, CreateOfferComponentDict


class CreateOffer(SdkBaseModel):
    name: str
    handle: str
    description: Optional[str] = UNSET
    product_id: int
    product_price_point_id: Optional[int] = UNSET
    components: Optional[list[CreateOfferComponent]] = UNSET
    coupons: Optional[list[str]] = UNSET


class CreateOfferDict(TypedDict):
    name: str
    handle: str
    description: NotRequired[str]
    product_id: int
    product_price_point_id: NotRequired[int]
    components: NotRequired[list[CreateOfferComponentDict]]
    coupons: NotRequired[list[str]]
