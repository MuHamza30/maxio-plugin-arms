from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class InvoicePayer(SdkBaseModel):
    chargify_id: Optional[int] = UNSET
    first_name: Optional[str] = UNSET
    last_name: Optional[str] = UNSET
    organization: OptionalNullable[str] = UNSET
    email: Optional[str] = UNSET
    vat_number: OptionalNullable[str] = UNSET


class InvoicePayerDict(TypedDict):
    chargify_id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    organization: NotRequired[str | None]
    email: NotRequired[str]
    vat_number: NotRequired[str | None]
