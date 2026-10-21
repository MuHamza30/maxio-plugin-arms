from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_payment import CreatePayment, CreatePaymentDict


class RecordPaymentRequest(SdkBaseModel):
    payment: CreatePayment


class RecordPaymentRequestDict(TypedDict):
    payment: CreatePaymentDict
