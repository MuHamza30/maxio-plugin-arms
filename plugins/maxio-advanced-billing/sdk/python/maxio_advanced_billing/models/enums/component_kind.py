from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ComponentKind(str, Enum):
    """A handle for the component type"""

    METERED_COMPONENT = "metered_component"
    QUANTITY_BASED_COMPONENT = "quantity_based_component"
    ON_OFF_COMPONENT = "on_off_component"
    PREPAID_USAGE_COMPONENT = "prepaid_usage_component"
    EVENT_BASED_COMPONENT = "event_based_component"
    WALLET_PRODUCT = "wallet_product"

    __str__ = str.__str__


ComponentKindOrStr: TypeAlias = Annotated[ComponentKind | str, open_enum_validator(ComponentKind)]
