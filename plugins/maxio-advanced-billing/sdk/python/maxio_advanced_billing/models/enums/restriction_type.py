from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RestrictionType(str, Enum):
    COMPONENT = "Component"
    PRODUCT = "Product"

    __str__ = str.__str__


RestrictionTypeOrStr: TypeAlias = Annotated[RestrictionType | str, open_enum_validator(RestrictionType)]
