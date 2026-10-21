from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .address_change import AddressChange, AddressChangeDict
from .customer_custom_fields_change import CustomerCustomFieldsChange, CustomerCustomFieldsChangeDict
from .customer_payer_change import CustomerPayerChange, CustomerPayerChangeDict


class CustomerChange(SdkBaseModel):
    payer: OptionalNullable[CustomerPayerChange] = UNSET
    shipping_address: OptionalNullable[AddressChange] = UNSET
    billing_address: OptionalNullable[AddressChange] = UNSET
    custom_fields: OptionalNullable[CustomerCustomFieldsChange] = UNSET


class CustomerChangeDict(TypedDict):
    payer: NotRequired[CustomerPayerChangeDict | None]
    shipping_address: NotRequired[AddressChangeDict | None]
    billing_address: NotRequired[AddressChangeDict | None]
    custom_fields: NotRequired[CustomerCustomFieldsChangeDict | None]
