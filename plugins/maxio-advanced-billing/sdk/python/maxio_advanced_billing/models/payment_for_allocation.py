from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaymentForAllocation(SdkBaseModel):
    """Information for captured payment, if applicable"""

    id: Optional[int] = UNSET
    amount_in_cents: Optional[int] = UNSET
    success: Optional[bool] = UNSET
    memo: Optional[str] = UNSET


class PaymentForAllocationDict(TypedDict):
    id: NotRequired[int]
    amount_in_cents: NotRequired[int]
    success: NotRequired[bool]
    memo: NotRequired[str]
