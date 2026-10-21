from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class QScope(str, Enum):
    FULL_NAME = "full_name"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    ORGANIZATION = "organization"
    CUSTOMER_REFERENCE = "customer_reference"
    SUBSCRIPTION_REFERENCE = "subscription_reference"

    __str__ = str.__str__


QScopeOrStr: TypeAlias = Annotated[QScope | str, open_enum_validator(QScope)]
