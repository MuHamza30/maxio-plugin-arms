from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PayerAttributes(SdkBaseModel):
    first_name: Optional[str] = UNSET
    last_name: Optional[str] = UNSET
    email: Optional[str] = UNSET
    cc_emails: Optional[str] = UNSET
    organization: Optional[str] = UNSET
    reference: Optional[str] = UNSET
    address: Optional[str] = UNSET
    address_2: Optional[str] = UNSET
    city: Optional[str] = UNSET
    state: Optional[str] = UNSET
    zip: Optional[str] = UNSET
    country: Optional[str] = UNSET
    phone: Optional[str] = UNSET
    locale: Optional[str] = UNSET
    vat_number: Optional[str] = UNSET
    tax_exempt: Optional[bool] = UNSET
    tax_exempt_reason: Optional[str] = UNSET
    metafields: Optional[dict[str, str]] = UNSET
    """(Optional) A set of key/value pairs representing custom fields and their values. Metafields will be created
    “on-the-fly” in your site for a given key, if they have not been created yet."""


class PayerAttributesDict(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    cc_emails: NotRequired[str]
    organization: NotRequired[str]
    reference: NotRequired[str]
    address: NotRequired[str]
    address_2: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    phone: NotRequired[str]
    locale: NotRequired[str]
    vat_number: NotRequired[str]
    tax_exempt: NotRequired[bool]
    tax_exempt_reason: NotRequired[str]
    metafields: NotRequired[dict[str, str]]
