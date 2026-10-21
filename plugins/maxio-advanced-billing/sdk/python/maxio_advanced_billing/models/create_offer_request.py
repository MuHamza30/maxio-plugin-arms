from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_offer import CreateOffer, CreateOfferDict


class CreateOfferRequest(SdkBaseModel):
    offer: CreateOffer


class CreateOfferRequestDict(TypedDict):
    offer: CreateOfferDict
