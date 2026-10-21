from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .component import Component, ComponentDict


class ComponentResponse(SdkBaseModel):
    component: Component


class ComponentResponseDict(TypedDict):
    component: ComponentDict
