from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .feature3 import Feature3, Feature3Dict


class UpdateFeatureCatalogItemRequest(SdkBaseModel):
    feature: Feature3


class UpdateFeatureCatalogItemRequestDict(TypedDict):
    feature: Feature3Dict
