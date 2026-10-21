from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PricingScheme(str, Enum):
    """The identifier for the pricing scheme. See `Product Components
    <https://help.chargify.com/products/product-components.html>`__ for an overview of pricing schemes."""

    STAIRSTEP = "stairstep"
    VOLUME = "volume"
    PER_UNIT = "per_unit"
    TIERED = "tiered"

    __str__ = str.__str__


PricingSchemeOrStr: TypeAlias = Annotated[PricingScheme | str, open_enum_validator(PricingScheme)]
