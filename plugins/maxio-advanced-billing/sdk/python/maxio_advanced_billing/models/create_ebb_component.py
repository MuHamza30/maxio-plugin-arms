from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .ebb_component import EbbComponent, EbbComponentDict


class CreateEbbComponent(SdkBaseModel):
    event_based_component: EbbComponent


class CreateEbbComponentDict(TypedDict):
    event_based_component: EbbComponentDict
