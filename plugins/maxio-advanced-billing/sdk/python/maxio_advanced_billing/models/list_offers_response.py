from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .offer import Offer, OfferDict


class ListOffersResponse(SdkBaseModel):
    offers: Optional[list[Offer]] = UNSET


class ListOffersResponseDict(TypedDict):
    offers: NotRequired[list[OfferDict]]
