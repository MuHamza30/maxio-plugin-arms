from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subscription_note import SubscriptionNote, SubscriptionNoteDict


class SubscriptionNoteResponse(SdkBaseModel):
    note: SubscriptionNote


class SubscriptionNoteResponseDict(TypedDict):
    note: SubscriptionNoteDict
