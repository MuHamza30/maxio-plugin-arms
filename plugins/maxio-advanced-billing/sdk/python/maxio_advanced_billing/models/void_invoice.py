from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class VoidInvoice(SdkBaseModel):
    reason: str


class VoidInvoiceDict(TypedDict):
    reason: str
