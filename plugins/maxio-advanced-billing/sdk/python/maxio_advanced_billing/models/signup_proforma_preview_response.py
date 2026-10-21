from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .signup_proforma_preview import SignupProformaPreview, SignupProformaPreviewDict


class SignupProformaPreviewResponse(SdkBaseModel):
    proforma_invoice_preview: SignupProformaPreview


class SignupProformaPreviewResponseDict(TypedDict):
    proforma_invoice_preview: SignupProformaPreviewDict
