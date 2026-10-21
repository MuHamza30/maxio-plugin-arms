from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .invoice_address import InvoiceAddress, InvoiceAddressDict


class AddressChange(SdkBaseModel):
    before: InvoiceAddress
    after: InvoiceAddress


class AddressChangeDict(TypedDict):
    before: InvoiceAddressDict
    after: InvoiceAddressDict
