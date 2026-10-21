from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.card_type import CardTypeOrStr
from .enums.credit_card_vault import CreditCardVaultOrStr


class GetOneTimeTokenPaymentProfile(SdkBaseModel):
    id: OptionalNullable[str] = UNSET
    first_name: str
    last_name: str
    masked_card_number: str
    card_type: CardTypeOrStr
    """The type of card used."""

    expiration_month: float
    expiration_year: float
    customer_id: OptionalNullable[str] = UNSET
    current_vault: CreditCardVaultOrStr
    """The vault that stores the payment profile with the provided ``vault_token``. Use ``bogus`` for testing."""

    vault_token: str
    billing_address: str
    billing_address_2: Optional[str] = UNSET
    billing_city: str
    billing_country: str
    billing_state: str
    billing_zip: str
    payment_type: str
    disabled: bool
    site_gateway_setting_id: int
    customer_vault_token: OptionalNullable[str] = UNSET
    gateway_handle: OptionalNullable[str] = UNSET


class GetOneTimeTokenPaymentProfileDict(TypedDict):
    id: NotRequired[str | None]
    first_name: str
    last_name: str
    masked_card_number: str
    card_type: CardTypeOrStr
    expiration_month: float
    expiration_year: float
    customer_id: NotRequired[str | None]
    current_vault: CreditCardVaultOrStr
    vault_token: str
    billing_address: str
    billing_address_2: NotRequired[str]
    billing_city: str
    billing_country: str
    billing_state: str
    billing_zip: str
    payment_type: str
    disabled: bool
    site_gateway_setting_id: int
    customer_vault_token: NotRequired[str | None]
    gateway_handle: NotRequired[str | None]
