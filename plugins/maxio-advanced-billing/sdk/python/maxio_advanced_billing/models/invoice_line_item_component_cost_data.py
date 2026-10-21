from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .component_cost_data import ComponentCostData, ComponentCostDataDict


class InvoiceLineItemComponentCostData(SdkBaseModel):
    rates: Optional[list[ComponentCostData]] = UNSET


class InvoiceLineItemComponentCostDataDict(TypedDict):
    rates: NotRequired[list[ComponentCostDataDict]]
