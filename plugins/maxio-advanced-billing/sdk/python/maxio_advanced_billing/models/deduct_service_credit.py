from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.amount2 import Amount2, Amount2Dict


class DeductServiceCredit(SdkBaseModel):
    amount: Amount2
    memo: Optional[str] = UNSET


class DeductServiceCreditDict(TypedDict):
    amount: Amount2Dict
    memo: NotRequired[str]
