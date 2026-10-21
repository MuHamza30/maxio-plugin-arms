from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionListDateField(str, Enum):
    UPDATED_AT = "updated_at"

    __str__ = str.__str__


SubscriptionListDateFieldOrStr: TypeAlias = Annotated[
    SubscriptionListDateField | str, open_enum_validator(SubscriptionListDateField)
]
