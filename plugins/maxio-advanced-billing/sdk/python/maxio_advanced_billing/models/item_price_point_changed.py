from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .item_price_point_data import ItemPricePointData, ItemPricePointDataDict


class ItemPricePointChanged(SdkBaseModel):
    item_id: int
    item_type: str
    item_handle: str
    item_name: str
    previous_price_point: ItemPricePointData
    current_price_point: ItemPricePointData


class ItemPricePointChangedDict(TypedDict):
    item_id: int
    item_type: str
    item_handle: str
    item_name: str
    previous_price_point: ItemPricePointDataDict
    current_price_point: ItemPricePointDataDict
