from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CancelGroupedSubscriptionsRequest(SdkBaseModel):
    charge_unbilled_usage: Optional[bool] = UNSET


class CancelGroupedSubscriptionsRequestDict(TypedDict):
    charge_unbilled_usage: NotRequired[bool]
