from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_invoice import UpdateInvoice, UpdateInvoiceDict


class UpdateInvoiceRequest(SdkBaseModel):
    """Request payload for updating a draft ad hoc invoice."""

    invoice: UpdateInvoice
    """Attributes of a draft ad hoc invoice which can be updated. Only the submitted attributes are changed."""


class UpdateInvoiceRequestDict(TypedDict):
    invoice: UpdateInvoiceDict
