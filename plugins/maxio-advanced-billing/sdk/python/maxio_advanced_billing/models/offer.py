from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .offer_discount import OfferDiscount, OfferDiscountDict
from .offer_item import OfferItem, OfferItemDict
from .offer_signup_page import OfferSignupPage, OfferSignupPageDict


class Offer(SdkBaseModel):
    id: Optional[int] = UNSET
    site_id: Optional[int] = UNSET
    product_family_id: Optional[int] = UNSET
    product_id: Optional[int] = UNSET
    product_price_point_id: Optional[int] = UNSET
    product_revisable_number: Optional[int] = UNSET
    name: Optional[str] = UNSET
    handle: Optional[str] = UNSET
    description: OptionalNullable[str] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    updated_at: Optional[RFC3339DateTime] = UNSET
    archived_at: OptionalNullable[RFC3339DateTime] = UNSET
    offer_items: Optional[list[OfferItem]] = UNSET
    offer_discounts: Optional[list[OfferDiscount]] = UNSET
    product_family_name: Optional[str] = UNSET
    product_name: Optional[str] = UNSET
    product_price_point_name: Optional[str] = UNSET
    product_price_in_cents: Optional[int] = UNSET
    offer_signup_pages: Optional[list[OfferSignupPage]] = UNSET


class OfferDict(TypedDict):
    id: NotRequired[int]
    site_id: NotRequired[int]
    product_family_id: NotRequired[int]
    product_id: NotRequired[int]
    product_price_point_id: NotRequired[int]
    product_revisable_number: NotRequired[int]
    name: NotRequired[str]
    handle: NotRequired[str]
    description: NotRequired[str | None]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    archived_at: NotRequired[RFC3339DateTime | None]
    offer_items: NotRequired[list[OfferItemDict]]
    offer_discounts: NotRequired[list[OfferDiscountDict]]
    product_family_name: NotRequired[str]
    product_name: NotRequired[str]
    product_price_point_name: NotRequired[str]
    product_price_in_cents: NotRequired[int]
    offer_signup_pages: NotRequired[list[OfferSignupPageDict]]
