from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .component_allocation_error_item import ComponentAllocationErrorItem, ComponentAllocationErrorItemDict


class ComponentAllocationError1(SdkBaseModel):
    errors: Optional[list[ComponentAllocationErrorItem]] = UNSET


class ComponentAllocationError1Dict(TypedDict):
    errors: NotRequired[list[ComponentAllocationErrorItemDict]]
