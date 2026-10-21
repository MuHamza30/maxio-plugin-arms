from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .billing_manifest import BillingManifest, BillingManifestDict


class SubscriptionPreview(SdkBaseModel):
    current_billing_manifest: Optional[BillingManifest] = UNSET
    next_billing_manifest: Optional[BillingManifest] = UNSET


class SubscriptionPreviewDict(TypedDict):
    current_billing_manifest: NotRequired[BillingManifestDict]
    next_billing_manifest: NotRequired[BillingManifestDict]
