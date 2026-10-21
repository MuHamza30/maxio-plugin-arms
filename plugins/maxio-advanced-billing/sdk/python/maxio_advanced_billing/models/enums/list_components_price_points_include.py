from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ListComponentsPricePointsInclude(str, Enum):
    CURRENCY_PRICES = "currency_prices"

    __str__ = str.__str__


ListComponentsPricePointsIncludeOrStr: TypeAlias = Annotated[
    ListComponentsPricePointsInclude | str, open_enum_validator(ListComponentsPricePointsInclude)
]
