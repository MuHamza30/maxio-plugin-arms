from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionInclude(str, Enum):
    COUPONS = "coupons"
    SELF_SERVICE_PAGE_TOKEN = "self_service_page_token"

    __str__ = str.__str__


SubscriptionIncludeOrStr: TypeAlias = Annotated[SubscriptionInclude | str, open_enum_validator(SubscriptionInclude)]
