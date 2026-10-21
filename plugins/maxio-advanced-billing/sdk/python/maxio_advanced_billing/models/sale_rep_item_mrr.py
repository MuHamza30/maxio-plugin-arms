from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SaleRepItemMrr(SdkBaseModel):
    mrr: Optional[str] = UNSET
    usage: Optional[str] = UNSET
    recurring: Optional[str] = UNSET


class SaleRepItemMrrDict(TypedDict):
    mrr: NotRequired[str]
    usage: NotRequired[str]
    recurring: NotRequired[str]
