from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FeatureValueType(str, Enum):
    """The data type of a feature's value. For ``access_right`` features this is always ``boolean``, and for
    ``usage_limit`` features this is always ``numeric``. For ``service_right`` features, you choose the value type
    explicitly."""

    TEXT = "text"
    BOOLEAN = "boolean"
    NUMERIC = "numeric"

    __str__ = str.__str__


FeatureValueTypeOrStr: TypeAlias = Annotated[FeatureValueType | str, open_enum_validator(FeatureValueType)]
