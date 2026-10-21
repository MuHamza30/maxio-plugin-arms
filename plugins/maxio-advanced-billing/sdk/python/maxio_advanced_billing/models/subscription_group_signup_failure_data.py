from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payer_attributes import PayerAttributes, PayerAttributesDict
from .subscription_group_bank_account import SubscriptionGroupBankAccount, SubscriptionGroupBankAccountDict
from .subscription_group_credit_card import SubscriptionGroupCreditCard, SubscriptionGroupCreditCardDict
from .subscription_group_signup_item import SubscriptionGroupSignupItem, SubscriptionGroupSignupItemDict


class SubscriptionGroupSignupFailureData(SdkBaseModel):
    payer_id: Optional[int] = UNSET
    payer_reference: Optional[str] = UNSET
    payment_profile_id: Optional[int] = UNSET
    payment_collection_method: Optional[str] = UNSET
    payer_attributes: Optional[PayerAttributes] = UNSET
    credit_card_attributes: Optional[SubscriptionGroupCreditCard] = UNSET
    bank_account_attributes: Optional[SubscriptionGroupBankAccount] = UNSET
    subscriptions: Optional[list[SubscriptionGroupSignupItem]] = UNSET


class SubscriptionGroupSignupFailureDataDict(TypedDict):
    payer_id: NotRequired[int]
    payer_reference: NotRequired[str]
    payment_profile_id: NotRequired[int]
    payment_collection_method: NotRequired[str]
    payer_attributes: NotRequired[PayerAttributesDict]
    credit_card_attributes: NotRequired[SubscriptionGroupCreditCardDict]
    bank_account_attributes: NotRequired[SubscriptionGroupBankAccountDict]
    subscriptions: NotRequired[list[SubscriptionGroupSignupItemDict]]
