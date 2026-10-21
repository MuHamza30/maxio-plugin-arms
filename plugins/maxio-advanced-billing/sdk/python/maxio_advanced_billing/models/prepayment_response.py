from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .prepayment import Prepayment, PrepaymentDict


class PrepaymentResponse(SdkBaseModel):
    prepayment: Prepayment


class PrepaymentResponseDict(TypedDict):
    prepayment: PrepaymentDict
