from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ComponentAllocationErrorItem(SdkBaseModel):
    component_id: Optional[int] = UNSET
    message: Optional[str] = UNSET
    kind: Optional[str] = UNSET
    on: Optional[str] = UNSET


class ComponentAllocationErrorItemDict(TypedDict):
    component_id: NotRequired[int]
    message: NotRequired[str]
    kind: NotRequired[str]
    on: NotRequired[str]
