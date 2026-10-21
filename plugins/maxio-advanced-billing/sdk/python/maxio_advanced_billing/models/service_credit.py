from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.service_credit_type import ServiceCreditTypeOrStr


class ServiceCredit(SdkBaseModel):
    id: Optional[int] = UNSET
    amount_in_cents: Optional[int] = UNSET
    """The amount in cents of the entry"""

    ending_balance_in_cents: Optional[int] = UNSET
    """The new balance for the credit account"""

    entry_type: Optional[ServiceCreditTypeOrStr] = UNSET
    """The type of entry"""

    memo: Optional[str] = UNSET
    """The memo attached to the entry"""


class ServiceCreditDict(TypedDict):
    id: NotRequired[int]
    amount_in_cents: NotRequired[int]
    ending_balance_in_cents: NotRequired[int]
    entry_type: NotRequired[ServiceCreditTypeOrStr]
    memo: NotRequired[str]
