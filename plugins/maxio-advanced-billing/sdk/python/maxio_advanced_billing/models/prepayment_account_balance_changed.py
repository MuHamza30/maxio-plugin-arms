from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PrepaymentAccountBalanceChanged(SdkBaseModel):
    reason: str
    prepayment_account_balance_in_cents: int
    prepayment_balance_change_in_cents: int
    currency_code: str


class PrepaymentAccountBalanceChangedDict(TypedDict):
    reason: str
    prepayment_account_balance_in_cents: int
    prepayment_balance_change_in_cents: int
    currency_code: str
