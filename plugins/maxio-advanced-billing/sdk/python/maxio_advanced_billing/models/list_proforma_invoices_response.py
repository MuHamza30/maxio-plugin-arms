from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_proforma_invoices_meta import ListProformaInvoicesMeta, ListProformaInvoicesMetaDict
from .proforma_invoice import ProformaInvoice, ProformaInvoiceDict


class ListProformaInvoicesResponse(SdkBaseModel):
    proforma_invoices: Optional[list[ProformaInvoice]] = UNSET
    meta: Optional[ListProformaInvoicesMeta] = UNSET


class ListProformaInvoicesResponseDict(TypedDict):
    proforma_invoices: NotRequired[list[ProformaInvoiceDict]]
    meta: NotRequired[ListProformaInvoicesMetaDict]
