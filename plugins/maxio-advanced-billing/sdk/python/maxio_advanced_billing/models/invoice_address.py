from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class InvoiceAddress(SdkBaseModel):
    street: OptionalNullable[str] = UNSET
    line2: OptionalNullable[str] = UNSET
    city: OptionalNullable[str] = UNSET
    state: OptionalNullable[str] = UNSET
    zip: OptionalNullable[str] = UNSET
    country: OptionalNullable[str] = UNSET


class InvoiceAddressDict(TypedDict):
    street: NotRequired[str | None]
    line2: NotRequired[str | None]
    city: NotRequired[str | None]
    state: NotRequired[str | None]
    zip: NotRequired[str | None]
    country: NotRequired[str | None]
