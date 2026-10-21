from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ChangeInvoiceCollectionMethodEventData(SdkBaseModel):
    """Example schema for an ``change_invoice_collection_method`` event"""

    from_collection_method: str
    """The previous collection method of the invoice."""

    to_collection_method: str
    """The new collection method of the invoice."""


class ChangeInvoiceCollectionMethodEventDataDict(TypedDict):
    from_collection_method: str
    to_collection_method: str
