from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bank_account_payment_profile import BankAccountPaymentProfile, BankAccountPaymentProfileDict


class BankAccountResponse(SdkBaseModel):
    payment_profile: BankAccountPaymentProfile


class BankAccountResponseDict(TypedDict):
    payment_profile: BankAccountPaymentProfileDict
