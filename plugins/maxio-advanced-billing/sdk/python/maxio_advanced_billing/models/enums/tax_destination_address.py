from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TaxDestinationAddress(str, Enum):
    SHIPPING_THEN_BILLING = "shipping_then_billing"
    BILLING_THEN_SHIPPING = "billing_then_shipping"
    SHIPPING_ONLY = "shipping_only"
    BILLING_ONLY = "billing_only"

    __str__ = str.__str__


TaxDestinationAddressOrStr: TypeAlias = Annotated[
    TaxDestinationAddress | str, open_enum_validator(TaxDestinationAddress)
]
