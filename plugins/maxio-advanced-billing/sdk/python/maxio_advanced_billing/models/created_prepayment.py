from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class CreatedPrepayment(SdkBaseModel):
    id: Optional[int] = UNSET
    subscription_id: Optional[int] = UNSET
    amount_in_cents: Optional[int] = UNSET
    memo: Optional[str] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    starting_balance_in_cents: Optional[int] = UNSET
    ending_balance_in_cents: Optional[int] = UNSET


class CreatedPrepaymentDict(TypedDict):
    id: NotRequired[int]
    subscription_id: NotRequired[int]
    amount_in_cents: NotRequired[int]
    memo: NotRequired[str]
    created_at: NotRequired[RFC3339DateTime]
    starting_balance_in_cents: NotRequired[int]
    ending_balance_in_cents: NotRequired[int]
