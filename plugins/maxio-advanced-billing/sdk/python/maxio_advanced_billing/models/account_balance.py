from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class AccountBalance(SdkBaseModel):
    balance_in_cents: Optional[int] = UNSET
    """The balance in cents."""

    automatic_balance_in_cents: OptionalNullable[int] = UNSET
    """The automatic balance in cents."""

    remittance_balance_in_cents: OptionalNullable[int] = UNSET
    """The remittance balance in cents."""


class AccountBalanceDict(TypedDict):
    balance_in_cents: NotRequired[int]
    automatic_balance_in_cents: NotRequired[int | None]
    remittance_balance_in_cents: NotRequired[int | None]
