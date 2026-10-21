from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.metafields import Metafields, MetafieldsDict


class CreateMetafieldsRequest(SdkBaseModel):
    metafields: Metafields


class CreateMetafieldsRequestDict(TypedDict):
    metafields: MetafieldsDict
