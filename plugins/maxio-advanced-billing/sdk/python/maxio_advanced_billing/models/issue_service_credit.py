from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.amount3 import Amount3, Amount3Dict


class IssueServiceCredit(SdkBaseModel):
    amount: Amount3
    memo: Optional[str] = UNSET


class IssueServiceCreditDict(TypedDict):
    amount: Amount3Dict
    memo: NotRequired[str]
