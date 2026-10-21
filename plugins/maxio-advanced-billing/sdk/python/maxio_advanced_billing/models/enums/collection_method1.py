from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CollectionMethod1(str, Enum):
    AUTOMATIC = "automatic"
    REMITTANCE = "remittance"
    PREPAID = "prepaid"

    __str__ = str.__str__


CollectionMethod1OrStr: TypeAlias = Annotated[CollectionMethod1 | str, open_enum_validator(CollectionMethod1)]
