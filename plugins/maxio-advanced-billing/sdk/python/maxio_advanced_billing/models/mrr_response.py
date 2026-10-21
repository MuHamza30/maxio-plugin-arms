from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .mrr import Mrr, MrrDict


class MrrResponse(SdkBaseModel):
    mrr: Mrr


class MrrResponseDict(TypedDict):
    mrr: MrrDict
