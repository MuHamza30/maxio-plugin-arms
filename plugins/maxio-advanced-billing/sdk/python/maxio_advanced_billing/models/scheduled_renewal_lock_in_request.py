from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class ScheduledRenewalLockInRequest(SdkBaseModel):
    lock_in_at: Date
    """Date to lock in the renewal."""


class ScheduledRenewalLockInRequestDict(TypedDict):
    lock_in_at: Date
