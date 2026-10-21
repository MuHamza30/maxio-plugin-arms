from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .component_price_point_assignment import ComponentPricePointAssignment, ComponentPricePointAssignmentDict


class BulkComponentsPricePointAssignment(SdkBaseModel):
    components: Optional[list[ComponentPricePointAssignment]] = UNSET


class BulkComponentsPricePointAssignmentDict(TypedDict):
    components: NotRequired[list[ComponentPricePointAssignmentDict]]
