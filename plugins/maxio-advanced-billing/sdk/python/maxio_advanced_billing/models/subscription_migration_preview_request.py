from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subscription_migration_preview_options import (
    SubscriptionMigrationPreviewOptions,
    SubscriptionMigrationPreviewOptionsDict,
)


class SubscriptionMigrationPreviewRequest(SdkBaseModel):
    migration: SubscriptionMigrationPreviewOptions


class SubscriptionMigrationPreviewRequestDict(TypedDict):
    migration: SubscriptionMigrationPreviewOptionsDict
