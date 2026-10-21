from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .subscription_product_migration import SubscriptionProductMigration, SubscriptionProductMigrationDict


class SubscriptionProductMigrationRequest(SdkBaseModel):
    migration: SubscriptionProductMigration


class SubscriptionProductMigrationRequestDict(TypedDict):
    migration: SubscriptionProductMigrationDict
