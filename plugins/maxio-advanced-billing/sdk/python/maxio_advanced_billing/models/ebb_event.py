from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .chargify_ebb import ChargifyEbb, ChargifyEbbDict


class EbbEvent(SdkBaseModel):
    chargify: Optional[ChargifyEbb] = UNSET


class EbbEventDict(TypedDict):
    chargify: NotRequired[ChargifyEbbDict]
