from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WebhookOrder(str, Enum):
    NEWEST_FIRST = "newest_first"
    OLDEST_FIRST = "oldest_first"

    __str__ = str.__str__


WebhookOrderOrStr: TypeAlias = Annotated[WebhookOrder | str, open_enum_validator(WebhookOrder)]
