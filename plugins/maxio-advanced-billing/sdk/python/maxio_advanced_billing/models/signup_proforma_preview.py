from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .proforma_invoice import ProformaInvoice, ProformaInvoiceDict


class SignupProformaPreview(SdkBaseModel):
    current_proforma_invoice: Optional[ProformaInvoice] = UNSET
    next_proforma_invoice: Optional[ProformaInvoice] = UNSET


class SignupProformaPreviewDict(TypedDict):
    current_proforma_invoice: NotRequired[ProformaInvoiceDict]
    next_proforma_invoice: NotRequired[ProformaInvoiceDict]
