from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProformaInvoiceDiscountSourceType(str, Enum):
    COUPON = "Coupon"
    REFERRAL = "Referral"

    __str__ = str.__str__


ProformaInvoiceDiscountSourceTypeOrStr: TypeAlias = Annotated[
    ProformaInvoiceDiscountSourceType | str, open_enum_validator(ProformaInvoiceDiscountSourceType)
]
