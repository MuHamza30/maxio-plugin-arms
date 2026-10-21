from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .wallet_product_list_item import WalletProductListItem, WalletProductListItemDict


class WalletProductsListResponse(SdkBaseModel):
    wallet_products: list[WalletProductListItem]
    total_count: int
    """Total number of Wallet Products matching the filters, across all pages."""

    archived_count: int
    """Not a simple count of archived products matching the filters. With ``status=archived``, equals ``total_count``
    (there's nothing else to report). With any other ``status``, it's ``0`` whenever ``total_count`` is non-zero, and
    only when ``total_count`` is ``0`` does it become the number of archived Wallet Products matching the same ``q``
    search term (ignoring ``status``): an empty-state hint, not a running total."""


class WalletProductsListResponseDict(TypedDict):
    wallet_products: list[WalletProductListItemDict]
    total_count: int
    archived_count: int
