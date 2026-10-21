from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CompoundingStrategy(str, Enum):
    """Applicable only to stackable coupons. For ``compound``, Percentage-based discounts will be calculated against the
    remaining price, after prior discounts have been calculated. For ``full-price``, Percentage-based discounts will
    always be calculated against the original item price, before other discounts are applied."""

    COMPOUND = "compound"
    FULL_PRICE = "full-price"

    __str__ = str.__str__


CompoundingStrategyOrStr: TypeAlias = Annotated[CompoundingStrategy | str, open_enum_validator(CompoundingStrategy)]
