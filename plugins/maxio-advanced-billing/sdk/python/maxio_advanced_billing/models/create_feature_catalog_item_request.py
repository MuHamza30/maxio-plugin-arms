from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .feature2 import Feature2, Feature2Dict


class CreateFeatureCatalogItemRequest(SdkBaseModel):
    """The owning product or component is taken from the URL and must not be included in the request body."""

    feature: Feature2


class CreateFeatureCatalogItemRequestDict(TypedDict):
    feature: Feature2Dict
