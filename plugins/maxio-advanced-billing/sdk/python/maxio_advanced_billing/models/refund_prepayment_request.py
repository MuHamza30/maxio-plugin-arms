from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .refund_prepayment import RefundPrepayment, RefundPrepaymentDict


class RefundPrepaymentRequest(SdkBaseModel):
    refund: RefundPrepayment


class RefundPrepaymentRequestDict(TypedDict):
    refund: RefundPrepaymentDict
