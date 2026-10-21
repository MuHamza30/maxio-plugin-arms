from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_component import UpdateComponent, UpdateComponentDict


class UpdateComponentRequest(SdkBaseModel):
    component: UpdateComponent


class UpdateComponentRequestDict(TypedDict):
    component: UpdateComponentDict
