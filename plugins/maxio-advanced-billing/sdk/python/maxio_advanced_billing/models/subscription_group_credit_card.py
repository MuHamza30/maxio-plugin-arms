from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.card_type import CardTypeOrStr
from .enums.credit_card_vault import CreditCardVaultOrStr
from .unions.expiration_month import ExpirationMonth, ExpirationMonthDict
from .unions.expiration_year import ExpirationYear, ExpirationYearDict
from .unions.full_number import FullNumber, FullNumberDict


class SubscriptionGroupCreditCard(SdkBaseModel):
    chargify_token: Optional[str] = UNSET
    vault_token: Optional[str] = UNSET
    current_vault: Optional[CreditCardVaultOrStr] = UNSET
    """The vault that stores the payment profile with the provided ``vault_token``. Use ``bogus`` for testing."""

    gateway_handle: Optional[str] = UNSET
    first_name: Optional[str] = UNSET
    last_name: Optional[str] = UNSET
    billing_address: Optional[str] = UNSET
    billing_address_2: Optional[str] = UNSET
    billing_city: Optional[str] = UNSET
    billing_state: Optional[str] = UNSET
    billing_zip: Optional[str] = UNSET
    billing_country: Optional[str] = UNSET
    full_number: Optional[FullNumber] = UNSET
    expiration_month: Optional[ExpirationMonth] = UNSET
    expiration_year: Optional[ExpirationYear] = UNSET
    last_four: Optional[str] = UNSET
    card_type: Optional[CardTypeOrStr] = UNSET
    """The type of card used."""

    customer_vault_token: Optional[str] = UNSET
    cvv: Optional[str] = UNSET
    payment_type: Optional[str] = UNSET


class SubscriptionGroupCreditCardDict(TypedDict):
    chargify_token: NotRequired[str]
    vault_token: NotRequired[str]
    current_vault: NotRequired[CreditCardVaultOrStr]
    gateway_handle: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    billing_address: NotRequired[str]
    billing_address_2: NotRequired[str]
    billing_city: NotRequired[str]
    billing_state: NotRequired[str]
    billing_zip: NotRequired[str]
    billing_country: NotRequired[str]
    full_number: NotRequired[FullNumberDict]
    expiration_month: NotRequired[ExpirationMonthDict]
    expiration_year: NotRequired[ExpirationYearDict]
    last_four: NotRequired[str]
    card_type: NotRequired[CardTypeOrStr]
    customer_vault_token: NotRequired[str]
    cvv: NotRequired[str]
    payment_type: NotRequired[str]
