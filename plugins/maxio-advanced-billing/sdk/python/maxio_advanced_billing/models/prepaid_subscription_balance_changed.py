from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PrepaidSubscriptionBalanceChanged(SdkBaseModel):
    reason: str
    current_account_balance_in_cents: int
    prepayment_account_balance_in_cents: int
    current_usage_amount_in_cents: int


class PrepaidSubscriptionBalanceChangedDict(TypedDict):
    reason: str
    current_account_balance_in_cents: int
    prepayment_account_balance_in_cents: int
    current_usage_amount_in_cents: int
