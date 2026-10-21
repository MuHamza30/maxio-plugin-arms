from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.collection_method import CollectionMethodOrStr
from .subscription_group_payment_profile import SubscriptionGroupPaymentProfile, SubscriptionGroupPaymentProfileDict


class SubscriptionGroup(SdkBaseModel):
    uid: Optional[str] = UNSET
    customer_id: Optional[int] = UNSET
    payment_profile: Optional[SubscriptionGroupPaymentProfile] = UNSET
    payment_collection_method: Optional[CollectionMethodOrStr] = UNSET
    """The type of payment collection to be used in the subscription. For legacy Statements Architecture valid options
    are - ``invoice``, ``automatic``. For current Relationship Invoicing Architecture valid options are -
    ``remittance``, ``automatic``, ``prepaid``."""

    subscription_ids: Optional[list[int]] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET


class SubscriptionGroupDict(TypedDict):
    uid: NotRequired[str]
    customer_id: NotRequired[int]
    payment_profile: NotRequired[SubscriptionGroupPaymentProfileDict]
    payment_collection_method: NotRequired[CollectionMethodOrStr]
    subscription_ids: NotRequired[list[int]]
    created_at: NotRequired[RFC3339DateTime]
