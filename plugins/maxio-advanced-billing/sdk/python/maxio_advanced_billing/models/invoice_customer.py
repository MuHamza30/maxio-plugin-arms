from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class InvoiceCustomer(SdkBaseModel):
    """Information about the customer who is owner or recipient of the invoiced subscription."""

    chargify_id: OptionalNullable[int] = UNSET
    first_name: Optional[str] = UNSET
    last_name: Optional[str] = UNSET
    organization: OptionalNullable[str] = UNSET
    email: Optional[str] = UNSET
    vat_number: OptionalNullable[str] = UNSET
    reference: OptionalNullable[str] = UNSET


class InvoiceCustomerDict(TypedDict):
    chargify_id: NotRequired[int | None]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    organization: NotRequired[str | None]
    email: NotRequired[str]
    vat_number: NotRequired[str | None]
    reference: NotRequired[str | None]
