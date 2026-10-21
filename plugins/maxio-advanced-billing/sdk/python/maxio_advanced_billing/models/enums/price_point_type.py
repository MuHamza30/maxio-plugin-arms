from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PricePointType(str, Enum):
    """Price point type. We expose the following types:
    1. **default**: a price point that is marked as a default price for a certain product.
    2. **custom**: a custom price point.
    3. **catalog**: a price point that is **not** marked as a default price for a certain product and is **not** a
        custom one."""

    CATALOG = "catalog"
    DEFAULT = "default"
    CUSTOM = "custom"

    __str__ = str.__str__


PricePointTypeOrStr: TypeAlias = Annotated[PricePointType | str, open_enum_validator(PricePointType)]
