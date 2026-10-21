from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .feature import Feature, FeatureDict


class CreateFeatureTemplateRequest(SdkBaseModel):
    feature: Feature


class CreateFeatureTemplateRequestDict(TypedDict):
    feature: FeatureDict
