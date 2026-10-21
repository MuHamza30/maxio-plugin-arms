from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class PendingCancellationChange(SdkBaseModel):
    cancellation_state: str
    cancels_at: RFC3339DateTime


class PendingCancellationChangeDict(TypedDict):
    cancellation_state: str
    cancels_at: RFC3339DateTime
