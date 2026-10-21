from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.compounding_strategy import CompoundingStrategyOrStr
from .unions.amount2 import Amount2, Amount2Dict
from .unions.percentage1 import Percentage1, Percentage1Dict
from .unions.product_family_id import ProductFamilyId, ProductFamilyIdDict


class CreateInvoiceCoupon(SdkBaseModel):
    code: Optional[str] = UNSET
    subcode: Optional[str] = UNSET
    percentage: Optional[Percentage1] = UNSET
    amount: Optional[Amount2] = UNSET
    description: Optional[str] = UNSET
    product_family_id: Optional[ProductFamilyId] = UNSET
    compounding_strategy: Optional[CompoundingStrategyOrStr] = UNSET
    """Applicable only to stackable coupons. For ``compound``, Percentage-based discounts will be calculated against the
    remaining price, after prior discounts have been calculated. For ``full-price``, Percentage-based discounts will
    always be calculated against the original item price, before other discounts are applied."""


class CreateInvoiceCouponDict(TypedDict):
    code: NotRequired[str]
    subcode: NotRequired[str]
    percentage: NotRequired[Percentage1Dict]
    amount: NotRequired[Amount2Dict]
    description: NotRequired[str]
    product_family_id: NotRequired[ProductFamilyIdDict]
    compounding_strategy: NotRequired[CompoundingStrategyOrStr]
