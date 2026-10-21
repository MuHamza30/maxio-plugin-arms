from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoiceDiscountSourceType(str, Enum):
    COUPON = "Coupon"
    REFERRAL = "Referral"
    AD_HOC_COUPON = "Ad Hoc Coupon"

    __str__ = str.__str__


InvoiceDiscountSourceTypeOrStr: TypeAlias = Annotated[
    InvoiceDiscountSourceType | str, open_enum_validator(InvoiceDiscountSourceType)
]
