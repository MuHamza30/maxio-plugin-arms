from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .feature_catalog_item import FeatureCatalogItem, FeatureCatalogItemDict


class FeatureCatalogItemResponse(SdkBaseModel):
    feature: FeatureCatalogItem
    """A feature template attached to a specific product or component (or one of their price points), with a concrete
    value. When a subscriber signs up for or is assigned this product/component, the feature catalog item is provisioned
    as an entitlement on their subscription."""


class FeatureCatalogItemResponseDict(TypedDict):
    feature: FeatureCatalogItemDict
