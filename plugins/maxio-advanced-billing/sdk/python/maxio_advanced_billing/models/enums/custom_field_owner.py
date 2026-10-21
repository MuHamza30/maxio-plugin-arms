from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CustomFieldOwner(str, Enum):
    CUSTOMER = "Customer"
    SUBSCRIPTION = "Subscription"

    __str__ = str.__str__


CustomFieldOwnerOrStr: TypeAlias = Annotated[CustomFieldOwner | str, open_enum_validator(CustomFieldOwner)]
