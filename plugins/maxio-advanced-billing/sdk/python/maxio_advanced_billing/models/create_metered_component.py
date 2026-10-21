from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .metered_component import MeteredComponent, MeteredComponentDict


class CreateMeteredComponent(SdkBaseModel):
    metered_component: MeteredComponent


class CreateMeteredComponentDict(TypedDict):
    metered_component: MeteredComponentDict
