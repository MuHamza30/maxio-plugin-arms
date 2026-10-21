from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UpdateSubscriptionNote(SdkBaseModel):
    """Updatable fields for Subscription Note"""

    body: str
    sticky: bool


class UpdateSubscriptionNoteDict(TypedDict):
    body: str
    sticky: bool
