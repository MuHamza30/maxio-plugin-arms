from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.metafields1 import Metafields1, Metafields1Dict


class UpdateMetafieldsRequest(SdkBaseModel):
    metafields: Optional[Metafields1] = UNSET


class UpdateMetafieldsRequestDict(TypedDict):
    metafields: NotRequired[Metafields1Dict]
