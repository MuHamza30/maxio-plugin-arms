from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BankAccountVerification(SdkBaseModel):
    deposit_1_in_cents: Optional[int] = UNSET
    deposit_2_in_cents: Optional[int] = UNSET


class BankAccountVerificationDict(TypedDict):
    deposit_1_in_cents: NotRequired[int]
    deposit_2_in_cents: NotRequired[int]
