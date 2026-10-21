from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AllocationPreviewLineItemKind(str, Enum):
    """A handle for the line item kind for allocation preview"""

    QUANTITY_BASED_COMPONENT = "quantity_based_component"
    ON_OFF_COMPONENT = "on_off_component"
    COUPON = "coupon"
    TAX = "tax"

    __str__ = str.__str__


AllocationPreviewLineItemKindOrStr: TypeAlias = Annotated[
    AllocationPreviewLineItemKind | str, open_enum_validator(AllocationPreviewLineItemKind)
]
