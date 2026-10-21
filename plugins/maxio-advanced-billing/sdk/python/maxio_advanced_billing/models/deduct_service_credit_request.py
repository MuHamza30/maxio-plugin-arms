from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .deduct_service_credit import DeductServiceCredit, DeductServiceCreditDict


class DeductServiceCreditRequest(SdkBaseModel):
    deduction: DeductServiceCredit


class DeductServiceCreditRequestDict(TypedDict):
    deduction: DeductServiceCreditDict
