from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class CreditAccountBalanceChanged(SdkBaseModel):
    reason: str
    service_credit_account_balance_in_cents: int
    service_credit_balance_change_in_cents: int
    currency_code: str
    at_time: RFC3339DateTime


class CreditAccountBalanceChangedDict(TypedDict):
    reason: str
    service_credit_account_balance_in_cents: int
    service_credit_balance_change_in_cents: int
    currency_code: str
    at_time: RFC3339DateTime
