from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .feature1 import Feature1, Feature1Dict


class UpdateFeatureTemplateRequest(SdkBaseModel):
    feature: Feature1
    """``key`` cannot be changed once set. ``kind`` cannot be changed once any feature catalog item has been created
    from this template."""


class UpdateFeatureTemplateRequestDict(TypedDict):
    feature: Feature1Dict
