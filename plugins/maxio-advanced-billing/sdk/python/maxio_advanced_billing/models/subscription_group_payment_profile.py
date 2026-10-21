from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SubscriptionGroupPaymentProfile(SdkBaseModel):
    id: Optional[int] = UNSET
    first_name: Optional[str] = UNSET
    last_name: Optional[str] = UNSET
    masked_card_number: Optional[str] = UNSET


class SubscriptionGroupPaymentProfileDict(TypedDict):
    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    masked_card_number: NotRequired[str]
