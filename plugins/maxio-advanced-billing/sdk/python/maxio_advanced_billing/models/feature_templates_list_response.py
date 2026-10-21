from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .feature_template import FeatureTemplate, FeatureTemplateDict


class FeatureTemplatesListResponse(SdkBaseModel):
    items: list[FeatureTemplate]
    total_count: int
    """Total number of feature templates matching the filters, across all pages."""

    archived_count: int
    """Number of archived feature templates matching the filters. Returned as ``0`` unless the active result set is
    empty or ``status=archived`` was requested."""


class FeatureTemplatesListResponseDict(TypedDict):
    items: list[FeatureTemplateDict]
    total_count: int
    archived_count: int
