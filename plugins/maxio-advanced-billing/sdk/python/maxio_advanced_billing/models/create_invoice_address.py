from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateInvoiceAddress(SdkBaseModel):
    """Overrides the default address."""

    first_name: Optional[str] = UNSET
    last_name: Optional[str] = UNSET
    phone: Optional[str] = UNSET
    address: Optional[str] = UNSET
    address_2: Optional[str] = UNSET
    city: Optional[str] = UNSET
    state: Optional[str] = UNSET
    zip: Optional[str] = UNSET
    country: Optional[str] = UNSET


class CreateInvoiceAddressDict(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    phone: NotRequired[str]
    address: NotRequired[str]
    address_2: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
