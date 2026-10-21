from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CurrencyPriceRole(str, Enum):
    """Role for the price."""

    BASELINE = "baseline"
    TRIAL = "trial"
    INITIAL = "initial"

    __str__ = str.__str__


CurrencyPriceRoleOrStr: TypeAlias = Annotated[CurrencyPriceRole | str, open_enum_validator(CurrencyPriceRole)]
