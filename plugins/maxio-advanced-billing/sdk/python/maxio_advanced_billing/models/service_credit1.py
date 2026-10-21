from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.service_credit_type import ServiceCreditTypeOrStr


class ServiceCredit1(SdkBaseModel):
    id: Optional[int] = UNSET
    amount_in_cents: Optional[int] = UNSET
    """The amount in cents of the entry"""

    ending_balance_in_cents: Optional[int] = UNSET
    """The new balance for the credit account"""

    entry_type: Optional[ServiceCreditTypeOrStr] = UNSET
    """The type of entry"""

    memo: Optional[str] = UNSET
    """The memo attached to the entry"""

    invoice_uid: OptionalNullable[str] = UNSET
    """The invoice uid associated with the entry. Only present for debit entries."""

    remaining_balance_in_cents: Optional[int] = UNSET
    """The remaining balance for the entry"""

    created_at: Optional[RFC3339DateTime] = UNSET
    """The date and time the entry was created"""


class ServiceCredit1Dict(TypedDict):
    id: NotRequired[int]
    amount_in_cents: NotRequired[int]
    ending_balance_in_cents: NotRequired[int]
    entry_type: NotRequired[ServiceCreditTypeOrStr]
    memo: NotRequired[str]
    invoice_uid: NotRequired[str | None]
    remaining_balance_in_cents: NotRequired[int]
    created_at: NotRequired[RFC3339DateTime]
