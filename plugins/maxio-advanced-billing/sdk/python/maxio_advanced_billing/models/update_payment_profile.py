from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.all_vaults import AllVaultsOrStr
from .enums.card_type import CardTypeOrStr


class UpdatePaymentProfile(SdkBaseModel):
    first_name: Optional[str] = UNSET
    """The first name of the card holder."""

    last_name: Optional[str] = UNSET
    """The last name of the card holder."""

    full_number: Optional[str] = UNSET
    """The full credit card number"""

    card_type: Optional[CardTypeOrStr] = UNSET
    """The type of card used."""

    expiration_month: Optional[str] = UNSET
    """(Optional when performing an Import via vault_token, required otherwise) The 1- or 2-digit credit card expiration
    month, as an integer or string, e.g., 5"""

    expiration_year: Optional[str] = UNSET
    """(Optional when performing an Import via vault_token, required otherwise) The 4-digit credit card expiration year,
    as an integer or string, e.g., 2012"""

    current_vault: Optional[AllVaultsOrStr] = UNSET
    """The vault that stores the payment profile with the provided ``vault_token``. Use ``bogus`` for testing."""

    billing_address: Optional[str] = UNSET
    """The credit card or bank account billing street address (e.g., 123 Main St.). This value is merely passed through
    to the payment gateway."""

    billing_city: Optional[str] = UNSET
    """The credit card or bank account billing address city (e.g., “Boston”). This value is merely passed through to the
    payment gateway."""

    billing_state: Optional[str] = UNSET
    """The credit card or bank account billing address state (e.g., MA). This value is merely passed through to the
    payment gateway. This must conform to the `ISO_3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__ in
    order to be valid for tax locale purposes."""

    billing_zip: Optional[str] = UNSET
    """The credit card or bank account billing address zip code (e.g., 12345). This value is merely passed through to
    the payment gateway."""

    billing_country: Optional[str] = UNSET
    """The credit card or bank account billing address country, required in `ISO_3166-1 alpha-2
    <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ format (e.g., “US”). This value is merely passed through to
    the payment gateway. Some gateways require country codes in a specific format. Check your gateway’s documentation.
    If creating an ACH subscription, only US is supported at this time."""

    billing_address_2: OptionalNullable[str] = UNSET
    """Second line of the customer’s billing address, e.g., Apt. 100"""


class UpdatePaymentProfileDict(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    full_number: NotRequired[str]
    card_type: NotRequired[CardTypeOrStr]
    expiration_month: NotRequired[str]
    expiration_year: NotRequired[str]
    current_vault: NotRequired[AllVaultsOrStr]
    billing_address: NotRequired[str]
    billing_city: NotRequired[str]
    billing_state: NotRequired[str]
    billing_zip: NotRequired[str]
    billing_country: NotRequired[str]
    billing_address_2: NotRequired[str | None]
