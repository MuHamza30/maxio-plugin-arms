from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_balance import AccountBalance, AccountBalanceDict


class AccountBalances(SdkBaseModel):
    open_invoices: Optional[AccountBalance] = UNSET
    """The balance, in cents, of the sum of the subscription's open, payable invoices."""

    pending_invoices: Optional[AccountBalance] = UNSET
    """The balance, in cents, of the sum of the subscription's pending, payable invoices."""

    pending_discounts: Optional[AccountBalance] = UNSET
    """The balance, in cents, of the subscription's Pending Discount account."""

    service_credits: Optional[AccountBalance] = UNSET
    """The balance, in cents, of the subscription's Service Credit account."""

    prepayments: Optional[AccountBalance] = UNSET
    """The balance, in cents, of the subscription's Prepayment account."""


class AccountBalancesDict(TypedDict):
    open_invoices: NotRequired[AccountBalanceDict]
    pending_invoices: NotRequired[AccountBalanceDict]
    pending_discounts: NotRequired[AccountBalanceDict]
    service_credits: NotRequired[AccountBalanceDict]
    prepayments: NotRequired[AccountBalanceDict]
