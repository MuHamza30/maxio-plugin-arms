from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CleanupScope(str, Enum):
    """all: Will clear all products, customers, and related subscriptions from the site. customers: Will clear only
    customers and related subscriptions (leaving the products untouched) for the site. Revenue will also be reset to
    0."""

    ALL = "all"
    CUSTOMERS = "customers"

    __str__ = str.__str__


CleanupScopeOrStr: TypeAlias = Annotated[CleanupScope | str, open_enum_validator(CleanupScope)]
