from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subscription_migration_preview import SubscriptionMigrationPreview, SubscriptionMigrationPreviewDict


class SubscriptionMigrationPreviewResponse(SdkBaseModel):
    migration: SubscriptionMigrationPreview


class SubscriptionMigrationPreviewResponseDict(TypedDict):
    migration: SubscriptionMigrationPreviewDict
