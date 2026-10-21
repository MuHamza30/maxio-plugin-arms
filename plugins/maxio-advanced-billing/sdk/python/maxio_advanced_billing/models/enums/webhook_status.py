from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WebhookStatus(str, Enum):
    SUCCESSFUL = "successful"
    FAILED = "failed"
    PENDING = "pending"
    PAUSED = "paused"

    __str__ = str.__str__


WebhookStatusOrStr: TypeAlias = Annotated[WebhookStatus | str, open_enum_validator(WebhookStatus)]
