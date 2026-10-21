from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .feature_catalog_item import FeatureCatalogItem, FeatureCatalogItemDict


class FeatureCatalogItemsListResponse(SdkBaseModel):
    features: list[FeatureCatalogItem]
    subscriptions_count: int
    """The number of subscriptions on this product/component that would be affected if a feature catalog item change
    were propagated with ``propagate_to_subscriptions=true``."""


class FeatureCatalogItemsListResponseDict(TypedDict):
    features: list[FeatureCatalogItemDict]
    subscriptions_count: int
