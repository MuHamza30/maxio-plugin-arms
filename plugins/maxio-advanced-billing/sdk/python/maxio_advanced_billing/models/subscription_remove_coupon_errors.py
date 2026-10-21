from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SubscriptionRemoveCouponErrors(SdkBaseModel):
    subscription: list[str]


class SubscriptionRemoveCouponErrorsDict(TypedDict):
    subscription: list[str]
