from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SubscriptionGroupSubscriptionError(SdkBaseModel):
    """Object which contains subscription errors."""

    product: Optional[list[str]] = UNSET
    product_price_point_id: Optional[list[str]] = UNSET
    payment_profile: Optional[list[str]] = UNSET
    payment_profile_chargify_token: Optional[list[str]] = Field(default=UNSET, alias="payment_profile.chargify_token")
    base: Optional[list[str]] = UNSET
    payment_profile_expiration_month: Optional[list[str]] = Field(
        default=UNSET, alias="payment_profile.expiration_month"
    )
    payment_profile_expiration_year: Optional[list[str]] = Field(default=UNSET, alias="payment_profile.expiration_year")
    payment_profile_full_number: Optional[list[str]] = Field(default=UNSET, alias="payment_profile.full_number")


class SubscriptionGroupSubscriptionErrorDict(TypedDict):
    product: NotRequired[list[str]]
    product_price_point_id: NotRequired[list[str]]
    payment_profile: NotRequired[list[str]]
    payment_profile_chargify_token: NotRequired[list[str]]
    base: NotRequired[list[str]]
    payment_profile_expiration_month: NotRequired[list[str]]
    payment_profile_expiration_year: NotRequired[list[str]]
    payment_profile_full_number: NotRequired[list[str]]
