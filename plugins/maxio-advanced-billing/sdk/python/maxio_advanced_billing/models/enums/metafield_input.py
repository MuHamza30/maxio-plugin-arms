from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MetafieldInput(str, Enum):
    """Indicates the type of metafield. A text metafield allows any string value. Dropdown and radio metafields have a
    set of values that can be selected. Defaults to 'text'."""

    BALANCE_TRACKER = "balance_tracker"
    TEXT = "text"
    RADIO = "radio"
    DROPDOWN = "dropdown"

    __str__ = str.__str__


MetafieldInputOrStr: TypeAlias = Annotated[MetafieldInput | str, open_enum_validator(MetafieldInput)]
