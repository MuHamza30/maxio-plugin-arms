from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ItemCategory(str, Enum):
    """One of the following: Business Software, Consumer Software, Digital Services, Physical Goods, Other"""

    BUSINESS_SOFTWARE = "Business Software"
    CONSUMER_SOFTWARE = "Consumer Software"
    DIGITAL_SERVICES = "Digital Services"
    PHYSICAL_GOODS = "Physical Goods"
    OTHER = "Other"

    __str__ = str.__str__


ItemCategoryOrStr: TypeAlias = Annotated[ItemCategory | str, open_enum_validator(ItemCategory)]
