from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .invoice_custom_field import InvoiceCustomField, InvoiceCustomFieldDict


class CustomerCustomFieldsChange(SdkBaseModel):
    before: list[InvoiceCustomField]
    after: list[InvoiceCustomField]


class CustomerCustomFieldsChangeDict(TypedDict):
    before: list[InvoiceCustomFieldDict]
    after: list[InvoiceCustomFieldDict]
