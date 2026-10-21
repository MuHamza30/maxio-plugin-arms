from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReferralCode(SdkBaseModel):
    id: Optional[int] = UNSET
    site_id: Optional[int] = UNSET
    subscription_id: Optional[int] = UNSET
    code: Optional[str] = UNSET


class ReferralCodeDict(TypedDict):
    id: NotRequired[int]
    site_id: NotRequired[int]
    subscription_id: NotRequired[int]
    code: NotRequired[str]
