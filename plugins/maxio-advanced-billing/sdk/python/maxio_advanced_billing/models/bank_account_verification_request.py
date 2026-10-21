from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bank_account_verification import BankAccountVerification, BankAccountVerificationDict


class BankAccountVerificationRequest(SdkBaseModel):
    bank_account_verification: BankAccountVerification


class BankAccountVerificationRequestDict(TypedDict):
    bank_account_verification: BankAccountVerificationDict
