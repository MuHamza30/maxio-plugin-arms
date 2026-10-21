from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.collection_method import CollectionMethodOrStr
from .payer_attributes import PayerAttributes, PayerAttributesDict
from .subscription_group_bank_account import SubscriptionGroupBankAccount, SubscriptionGroupBankAccountDict
from .subscription_group_credit_card import SubscriptionGroupCreditCard, SubscriptionGroupCreditCardDict
from .subscription_group_signup_item import SubscriptionGroupSignupItem, SubscriptionGroupSignupItemDict


class SubscriptionGroupSignup(SdkBaseModel):
    payment_profile_id: Optional[int] = UNSET
    payer_id: Optional[int] = UNSET
    payer_reference: Optional[str] = UNSET
    payment_collection_method: Optional[CollectionMethodOrStr] = UNSET
    """The type of payment collection to be used in the subscription. For legacy Statements Architecture valid options
    are - ``invoice``, ``automatic``. For current Relationship Invoicing Architecture valid options are -
    ``remittance``, ``automatic``, ``prepaid``."""

    payer_attributes: Optional[PayerAttributes] = UNSET
    credit_card_attributes: Optional[SubscriptionGroupCreditCard] = UNSET
    bank_account_attributes: Optional[SubscriptionGroupBankAccount] = UNSET
    subscriptions: list[SubscriptionGroupSignupItem]


class SubscriptionGroupSignupDict(TypedDict):
    payment_profile_id: NotRequired[int]
    payer_id: NotRequired[int]
    payer_reference: NotRequired[str]
    payment_collection_method: NotRequired[CollectionMethodOrStr]
    payer_attributes: NotRequired[PayerAttributesDict]
    credit_card_attributes: NotRequired[SubscriptionGroupCreditCardDict]
    bank_account_attributes: NotRequired[SubscriptionGroupBankAccountDict]
    subscriptions: list[SubscriptionGroupSignupItemDict]
