from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.card_type import CardTypeOrStr
from .enums.credit_card_vault import CreditCardVaultOrStr
from .enums.payment_type import PaymentType, PaymentTypeOrStr


class CreditCardPaymentProfile(SdkBaseModel):
    id: Optional[int] = UNSET
    """The Chargify-assigned ID of the stored card. This value can be used as an input to payment_profile_id when
    creating a subscription, in order to re-use a stored payment profile for the same customer."""

    first_name: Optional[str] = UNSET
    """The first name of the card holder."""

    last_name: Optional[str] = UNSET
    """The last name of the card holder."""

    masked_card_number: Optional[str] = UNSET
    """A string representation of the credit card number with all but the last 4 digits masked with X’s (e.g.,
    ‘XXXX-XXXX-XXXX-1234’)."""

    card_type: OptionalNullable[CardTypeOrStr] = UNSET
    """The type of card used."""

    expiration_month: Optional[int] = UNSET
    """An integer representing the expiration month of the card(1 – 12)."""

    expiration_year: Optional[int] = UNSET
    """An integer representing the 4-digit expiration year of the card(e.g., ‘2012’)."""

    customer_id: Optional[int] = UNSET
    """The Chargify-assigned id for the customer record to which the card belongs."""

    current_vault: Optional[CreditCardVaultOrStr] = UNSET
    """The vault that stores the payment profile with the provided ``vault_token``. Use ``bogus`` for testing."""

    vault_token: OptionalNullable[str] = UNSET
    """The “token” provided by your vault storage for an already stored payment profile."""

    billing_address: OptionalNullable[str] = UNSET
    """The current billing street address for the card."""

    billing_city: OptionalNullable[str] = UNSET
    """The current billing address city for the card."""

    billing_state: OptionalNullable[str] = UNSET
    """The current billing address state for the card."""

    billing_zip: OptionalNullable[str] = UNSET
    """The current billing address zip code for the card."""

    billing_country: OptionalNullable[str] = UNSET
    """The current billing address country for the card."""

    customer_vault_token: OptionalNullable[str] = UNSET
    """(only for Authorize.Net CIM storage): the customerProfileId for the owner of the customerPaymentProfileId
    provided as the vault_token."""

    billing_address_2: OptionalNullable[str] = UNSET
    """The current billing street address, second line, for the card."""

    payment_type: PaymentTypeOrStr = PaymentType.CREDIT_CARD
    disabled: Optional[bool] = UNSET
    chargify_token: Optional[str] = UNSET
    """Token received after sending billing information using Maxio.js (formerly Chargify.js). This token will only be
    received if passed as a sole attribute of credit_card_attributes (e.g., tok_9g6hw85pnpt6knmskpwp4ttt)."""

    site_gateway_setting_id: OptionalNullable[int] = UNSET
    gateway_handle: OptionalNullable[str] = UNSET
    """An identifier of connected gateway."""

    created_at: Optional[RFC3339DateTime] = UNSET
    """A timestamp indicating when this payment profile was created"""

    updated_at: Optional[RFC3339DateTime] = UNSET
    """A timestamp indicating when this payment profile was last updated"""


class CreditCardPaymentProfileDict(TypedDict):
    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    masked_card_number: NotRequired[str]
    card_type: NotRequired[CardTypeOrStr | None]
    expiration_month: NotRequired[int]
    expiration_year: NotRequired[int]
    customer_id: NotRequired[int]
    current_vault: NotRequired[CreditCardVaultOrStr]
    vault_token: NotRequired[str | None]
    billing_address: NotRequired[str | None]
    billing_city: NotRequired[str | None]
    billing_state: NotRequired[str | None]
    billing_zip: NotRequired[str | None]
    billing_country: NotRequired[str | None]
    customer_vault_token: NotRequired[str | None]
    billing_address_2: NotRequired[str | None]
    payment_type: PaymentTypeOrStr
    disabled: NotRequired[bool]
    chargify_token: NotRequired[str]
    site_gateway_setting_id: NotRequired[int | None]
    gateway_handle: NotRequired[str | None]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
