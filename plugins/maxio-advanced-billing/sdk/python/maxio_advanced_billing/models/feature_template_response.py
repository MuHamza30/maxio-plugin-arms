from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .feature_template import FeatureTemplate, FeatureTemplateDict


class FeatureTemplateResponse(SdkBaseModel):
    feature: FeatureTemplate
    """A feature that can be granted to subscribers, defined once at the site level and then attached to products or
    components."""


class FeatureTemplateResponseDict(TypedDict):
    feature: FeatureTemplateDict
