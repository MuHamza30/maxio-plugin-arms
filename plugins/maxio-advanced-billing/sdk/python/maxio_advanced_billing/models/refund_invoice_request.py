from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.refund import Refund, RefundDict


class RefundInvoiceRequest(SdkBaseModel):
    refund: Refund


class RefundInvoiceRequestDict(TypedDict):
    refund: RefundDict
