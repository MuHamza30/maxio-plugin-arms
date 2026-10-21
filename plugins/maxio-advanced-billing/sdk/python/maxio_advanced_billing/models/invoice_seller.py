from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .invoice_address import InvoiceAddress, InvoiceAddressDict


class InvoiceSeller(SdkBaseModel):
    """Information about the seller (merchant) listed on the masthead of the invoice."""

    name: Optional[str] = UNSET
    address: Optional[InvoiceAddress] = UNSET
    phone: Optional[str] = UNSET
    logo_url: OptionalNullable[str] = UNSET


class InvoiceSellerDict(TypedDict):
    name: NotRequired[str]
    address: NotRequired[InvoiceAddressDict]
    phone: NotRequired[str]
    logo_url: NotRequired[str | None]
