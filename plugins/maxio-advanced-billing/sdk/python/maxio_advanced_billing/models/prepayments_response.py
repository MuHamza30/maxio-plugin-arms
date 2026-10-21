from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .prepayment import Prepayment, PrepaymentDict


class PrepaymentsResponse(SdkBaseModel):
    prepayments: Optional[list[Prepayment]] = UNSET


class PrepaymentsResponseDict(TypedDict):
    prepayments: NotRequired[list[PrepaymentDict]]
