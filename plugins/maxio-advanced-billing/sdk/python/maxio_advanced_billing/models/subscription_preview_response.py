from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subscription_preview import SubscriptionPreview, SubscriptionPreviewDict


class SubscriptionPreviewResponse(SdkBaseModel):
    subscription_preview: SubscriptionPreview


class SubscriptionPreviewResponseDict(TypedDict):
    subscription_preview: SubscriptionPreviewDict
