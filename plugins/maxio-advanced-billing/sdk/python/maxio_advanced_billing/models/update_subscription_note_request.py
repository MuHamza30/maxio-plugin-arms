from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_subscription_note import UpdateSubscriptionNote, UpdateSubscriptionNoteDict


class UpdateSubscriptionNoteRequest(SdkBaseModel):
    """Updatable fields for Subscription Note"""

    note: UpdateSubscriptionNote
    """Updatable fields for Subscription Note"""


class UpdateSubscriptionNoteRequestDict(TypedDict):
    note: UpdateSubscriptionNoteDict
