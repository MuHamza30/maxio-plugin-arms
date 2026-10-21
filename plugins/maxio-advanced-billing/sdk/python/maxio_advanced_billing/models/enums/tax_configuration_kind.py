from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TaxConfigurationKind(str, Enum):
    CUSTOM = "custom"
    MANAGED_AVALARA = "managed avalara"
    LINKED_AVALARA = "linked avalara"
    DIGITAL_RIVER = "digital river"

    __str__ = str.__str__


TaxConfigurationKindOrStr: TypeAlias = Annotated[TaxConfigurationKind | str, open_enum_validator(TaxConfigurationKind)]
