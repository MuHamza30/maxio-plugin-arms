from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.prepayment_method import PrepaymentMethodOrStr


class ListSubscriptionGroupPrepaymentItem(SdkBaseModel):
    id: Optional[int] = UNSET
    subscription_group_uid: Optional[str] = UNSET
    amount_in_cents: Optional[int] = UNSET
    remaining_amount_in_cents: Optional[int] = UNSET
    details: Optional[str] = UNSET
    external: Optional[bool] = UNSET
    memo: Optional[str] = UNSET
    payment_type: Optional[PrepaymentMethodOrStr] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET


class ListSubscriptionGroupPrepaymentItemDict(TypedDict):
    id: NotRequired[int]
    subscription_group_uid: NotRequired[str]
    amount_in_cents: NotRequired[int]
    remaining_amount_in_cents: NotRequired[int]
    details: NotRequired[str]
    external: NotRequired[bool]
    memo: NotRequired[str]
    payment_type: NotRequired[PrepaymentMethodOrStr]
    created_at: NotRequired[RFC3339DateTime]
