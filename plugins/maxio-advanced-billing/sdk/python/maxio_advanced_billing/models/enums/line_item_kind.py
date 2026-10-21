from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LineItemKind(str, Enum):
    """A handle for the line item kind"""

    BASELINE = "baseline"
    INITIAL = "initial"
    TRIAL = "trial"
    QUANTITY_BASED_COMPONENT = "quantity_based_component"
    PREPAID_USAGE_COMPONENT = "prepaid_usage_component"
    ON_OFF_COMPONENT = "on_off_component"
    METERED_COMPONENT = "metered_component"
    EVENT_BASED_COMPONENT = "event_based_component"
    COUPON = "coupon"
    TAX = "tax"

    __str__ = str.__str__


LineItemKindOrStr: TypeAlias = Annotated[LineItemKind | str, open_enum_validator(LineItemKind)]
