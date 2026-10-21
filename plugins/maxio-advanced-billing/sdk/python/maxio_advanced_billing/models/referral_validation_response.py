from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .referral_code import ReferralCode, ReferralCodeDict


class ReferralValidationResponse(SdkBaseModel):
    referral_code: Optional[ReferralCode] = UNSET


class ReferralValidationResponseDict(TypedDict):
    referral_code: NotRequired[ReferralCodeDict]
