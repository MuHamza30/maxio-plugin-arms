from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CancellationMethod(str, Enum):
    """The process used to cancel the subscription, if the subscription has been canceled. It is nil if the
    subscription's state is not canceled."""

    MERCHANT_UI = "merchant_ui"
    MERCHANT_API = "merchant_api"
    DUNNING = "dunning"
    BILLING_PORTAL = "billing_portal"
    UNKNOWN = "unknown"
    IMPORTED = "imported"

    __str__ = str.__str__


CancellationMethodOrStr: TypeAlias = Annotated[CancellationMethod | str, open_enum_validator(CancellationMethod)]
