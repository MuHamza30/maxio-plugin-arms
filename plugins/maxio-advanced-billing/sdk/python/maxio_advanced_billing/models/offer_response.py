from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .offer import Offer, OfferDict


class OfferResponse(SdkBaseModel):
    offer: Optional[Offer] = UNSET


class OfferResponseDict(TypedDict):
    offer: NotRequired[OfferDict]
