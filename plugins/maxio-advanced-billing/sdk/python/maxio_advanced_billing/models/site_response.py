from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .site import Site, SiteDict


class SiteResponse(SdkBaseModel):
    site: Site


class SiteResponseDict(TypedDict):
    site: SiteDict
