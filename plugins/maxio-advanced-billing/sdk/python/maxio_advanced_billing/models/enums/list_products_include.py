from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ListProductsInclude(str, Enum):
    PREPAID_PRODUCT_PRICE_POINT = "prepaid_product_price_point"

    __str__ = str.__str__


ListProductsIncludeOrStr: TypeAlias = Annotated[ListProductsInclude | str, open_enum_validator(ListProductsInclude)]
