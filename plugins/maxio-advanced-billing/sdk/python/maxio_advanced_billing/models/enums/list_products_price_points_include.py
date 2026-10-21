from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ListProductsPricePointsInclude(str, Enum):
    CURRENCY_PRICES = "currency_prices"

    __str__ = str.__str__


ListProductsPricePointsIncludeOrStr: TypeAlias = Annotated[
    ListProductsPricePointsInclude | str, open_enum_validator(ListProductsPricePointsInclude)
]
