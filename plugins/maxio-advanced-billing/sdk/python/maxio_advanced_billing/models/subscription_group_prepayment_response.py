from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.service_credit_type import ServiceCreditTypeOrStr


class SubscriptionGroupPrepaymentResponse(SdkBaseModel):
    id: Optional[int] = UNSET
    amount_in_cents: Optional[int] = UNSET
    """The amount in cents of the entry."""

    ending_balance_in_cents: Optional[int] = UNSET
    """The ending balance in cents of the account."""

    entry_type: Optional[ServiceCreditTypeOrStr] = UNSET
    """The type of entry"""

    memo: OptionalNullable[str] = UNSET
    """A memo attached to the entry."""


class SubscriptionGroupPrepaymentResponseDict(TypedDict):
    id: NotRequired[int]
    amount_in_cents: NotRequired[int]
    ending_balance_in_cents: NotRequired[int]
    entry_type: NotRequired[ServiceCreditTypeOrStr]
    memo: NotRequired[str | None]
