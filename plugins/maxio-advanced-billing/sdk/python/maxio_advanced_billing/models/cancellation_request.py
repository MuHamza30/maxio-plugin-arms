from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cancellation_options import CancellationOptions, CancellationOptionsDict


class CancellationRequest(SdkBaseModel):
    subscription: CancellationOptions


class CancellationRequestDict(TypedDict):
    subscription: CancellationOptionsDict
