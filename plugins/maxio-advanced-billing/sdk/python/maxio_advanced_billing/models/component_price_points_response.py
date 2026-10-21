from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .component_price_point import ComponentPricePoint, ComponentPricePointDict
from .list_public_keys_meta import ListPublicKeysMeta, ListPublicKeysMetaDict


class ComponentPricePointsResponse(SdkBaseModel):
    price_points: Optional[list[ComponentPricePoint]] = UNSET
    meta: Optional[ListPublicKeysMeta] = UNSET


class ComponentPricePointsResponseDict(TypedDict):
    price_points: NotRequired[list[ComponentPricePointDict]]
    meta: NotRequired[ListPublicKeysMetaDict]
