from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FeatureOwnerPricePointType(str, Enum):
    """Identifies which kind of price point a feature catalog item override applies to: ``ProductPricePoint`` for a
    product price point, ``PricePoint`` for a component price point. Only relevant when ``price_point_id`` is set."""

    PRODUCT_PRICE_POINT = "ProductPricePoint"
    PRICE_POINT = "PricePoint"

    __str__ = str.__str__


FeatureOwnerPricePointTypeOrStr: TypeAlias = Annotated[
    FeatureOwnerPricePointType | str, open_enum_validator(FeatureOwnerPricePointType)
]
