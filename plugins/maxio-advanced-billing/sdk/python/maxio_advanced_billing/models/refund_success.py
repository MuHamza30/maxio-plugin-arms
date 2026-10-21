from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RefundSuccess(SdkBaseModel):
    refund_id: int
    gateway_transaction_id: int
    product_id: int


class RefundSuccessDict(TypedDict):
    refund_id: int
    gateway_transaction_id: int
    product_id: int
