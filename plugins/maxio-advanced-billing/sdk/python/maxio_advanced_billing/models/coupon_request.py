from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .coupon_payload import CouponPayload, CouponPayloadDict


class CouponRequest(SdkBaseModel):
    coupon: Optional[CouponPayload] = UNSET
    restricted_products: Optional[dict[str, bool]] = UNSET
    """An object where the keys are product IDs or handles (prefixed with 'handle:'), and the values are booleans
    indicating if the coupon should be applicable to the product."""

    restricted_components: Optional[dict[str, bool]] = UNSET
    """An object where the keys are component IDs or handles (prefixed with 'handle:'), and the values are booleans
    indicating if the coupon should be applicable to the component."""


class CouponRequestDict(TypedDict):
    coupon: NotRequired[CouponPayloadDict]
    restricted_products: NotRequired[dict[str, bool]]
    restricted_components: NotRequired[dict[str, bool]]
