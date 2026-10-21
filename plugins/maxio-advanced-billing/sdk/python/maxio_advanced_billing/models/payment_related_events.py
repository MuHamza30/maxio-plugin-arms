from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PaymentRelatedEvents(SdkBaseModel):
    product_id: int
    account_transaction_id: int


class PaymentRelatedEventsDict(TypedDict):
    product_id: int
    account_transaction_id: int
