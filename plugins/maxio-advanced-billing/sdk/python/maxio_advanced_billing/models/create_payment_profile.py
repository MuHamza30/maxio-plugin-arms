from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.all_vaults import AllVaultsOrStr
from .enums.bank_account_holder_type import BankAccountHolderTypeOrStr
from .enums.bank_account_type import BankAccountTypeOrStr
from .enums.card_type import CardTypeOrStr
from .enums.payment_type import PaymentTypeOrStr
from .unions.expiration_month1 import ExpirationMonth1, ExpirationMonth1Dict
from .unions.expiration_year1 import ExpirationYear1, ExpirationYear1Dict


class CreatePaymentProfile(SdkBaseModel):
    chargify_token: Optional[str] = UNSET
    """Token received after sending billing information using Maxio.js (formerly Chargify.js)."""

    id: Optional[int] = UNSET
    payment_type: Optional[PaymentTypeOrStr] = UNSET
    first_name: Optional[str] = UNSET
    """First name on card or bank account. If omitted, the first_name from customer attributes will be used."""

    last_name: Optional[str] = UNSET
    """Last name on card or bank account. If omitted, the last_name from customer attributes will be used."""

    masked_card_number: Optional[str] = UNSET
    full_number: Optional[str] = UNSET
    """The full credit card number"""

    card_type: Optional[CardTypeOrStr] = UNSET
    """The type of card used."""

    expiration_month: Optional[ExpirationMonth1] = UNSET
    """(Optional when performing an Import via vault_token, required otherwise) The 1- or 2-digit credit card expiration
    month, as an integer or string, e.g., 5"""

    expiration_year: Optional[ExpirationYear1] = UNSET
    """(Optional when performing an Import via vault_token, required otherwise) The 4-digit credit card expiration year,
    as an integer or string, e.g., 2012"""

    billing_address: Optional[str] = UNSET
    """The credit card or bank account billing street address (e.g., 123 Main St.). This value is merely passed through
    to the payment gateway."""

    billing_address_2: OptionalNullable[str] = UNSET
    """Second line of the customer’s billing address e.g., Apt. 100"""

    billing_city: Optional[str] = UNSET
    """The credit card or bank account billing address city (e.g., “Boston”). This value is merely passed through to the
    payment gateway."""

    billing_state: Optional[str] = UNSET
    """The credit card or bank account billing address state (e.g., MA). This value is merely passed through to the
    payment gateway. This must conform to the `ISO_3166-1 <https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes>`__ in
    order to be valid for tax locale purposes."""

    billing_country: Optional[str] = UNSET
    """“The credit card or bank account billing address country, required in `ISO_3166-1 alpha-2
    <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ format (e.g., “US”). This value is merely passed through to
    the payment gateway. Some gateways require country codes in a specific format. Check your gateway’s documentation.
    If creating an ACH subscription, only US is supported at this time.”"""

    billing_zip: Optional[str] = UNSET
    """The credit card or bank account billing address zip code (e.g., 12345). This value is merely passed through to
    the payment gateway."""

    current_vault: Optional[AllVaultsOrStr] = UNSET
    """The vault that stores the payment profile with the provided ``vault_token``. Use ``bogus`` for testing."""

    vault_token: Optional[str] = UNSET
    """The “token” provided by your vault storage for an already stored payment profile"""

    customer_vault_token: Optional[str] = UNSET
    """(only for Authorize.Net CIM storage or Square) The customerProfileId for the owner of the
    customerPaymentProfileId provided as the vault_token"""

    customer_id: Optional[int] = UNSET
    """(Required when creating a new payment profile) The Chargify customer id."""

    paypal_email: Optional[str] = UNSET
    """used by merchants that implemented BraintreeBlue javaScript libraries on their own. We recommend using Maxio.js
    (formerly Chargify.js) instead."""

    payment_method_nonce: Optional[str] = UNSET
    """used by merchants that implemented BraintreeBlue javaScript libraries on their own. We recommend using Maxio.js
    (formerly Chargify.js) instead."""

    gateway_handle: Optional[str] = UNSET
    """This attribute is only available if MultiGateway feature is enabled for your Site. This feature is in the Private
    Beta currently. gateway_handle is used to directly select a gateway where a payment profile will be stored in. Every
    connected gateway must have a unique gateway handle specified. Read `Multigateway description
    <https://chargify.zendesk.com/hc/en-us/articles/4407761759643#connecting-with-multiple-gateways>`__ to learn more
    about new concepts that MultiGateway introduces and the default behavior when this attribute is not passed."""

    cvv: Optional[str] = UNSET
    """The 3- or 4-digit Card Verification Value. This value is merely passed through to the payment gateway."""

    bank_name: Optional[str] = UNSET
    """(Required when creating with ACH or GoCardless, optional with Stripe Direct Debit). The name of the bank where
    the customerʼs account resides"""

    bank_iban: Optional[str] = UNSET
    """(Optional when creating with GoCardless, required with Stripe Direct Debit). International Bank Account Number.
    Alternatively, local bank details can be provided."""

    bank_routing_number: Optional[str] = UNSET
    """(Required when creating with ACH. Optional when creating a subscription with GoCardless). The routing number of
    the bank. It becomes bank_code while passing via GoCardless API."""

    bank_account_number: Optional[str] = UNSET
    """(Required when creating with ACH, GoCardless, Stripe BECS or BACS Direct Debit, and bank_iban is blank) The
    customerʼs bank account number"""

    bank_branch_code: Optional[str] = UNSET
    """(Optional when creating with GoCardless, required with Stripe BECS or BACS Direct Debit) Branch/Sort code.
    Alternatively, an IBAN can be provided."""

    bank_account_type: Optional[BankAccountTypeOrStr] = UNSET
    """Defaults to checking"""

    bank_account_holder_type: Optional[BankAccountHolderTypeOrStr] = UNSET
    """Defaults to personal"""

    last_four: Optional[str] = UNSET
    """(Optional) Used for creating subscription with payment profile imported using vault_token, for proper display in
    Advanced Billing UI"""


class CreatePaymentProfileDict(TypedDict):
    chargify_token: NotRequired[str]
    id: NotRequired[int]
    payment_type: NotRequired[PaymentTypeOrStr]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    masked_card_number: NotRequired[str]
    full_number: NotRequired[str]
    card_type: NotRequired[CardTypeOrStr]
    expiration_month: NotRequired[ExpirationMonth1Dict]
    expiration_year: NotRequired[ExpirationYear1Dict]
    billing_address: NotRequired[str]
    billing_address_2: NotRequired[str | None]
    billing_city: NotRequired[str]
    billing_state: NotRequired[str]
    billing_country: NotRequired[str]
    billing_zip: NotRequired[str]
    current_vault: NotRequired[AllVaultsOrStr]
    vault_token: NotRequired[str]
    customer_vault_token: NotRequired[str]
    customer_id: NotRequired[int]
    paypal_email: NotRequired[str]
    payment_method_nonce: NotRequired[str]
    gateway_handle: NotRequired[str]
    cvv: NotRequired[str]
    bank_name: NotRequired[str]
    bank_iban: NotRequired[str]
    bank_routing_number: NotRequired[str]
    bank_account_number: NotRequired[str]
    bank_branch_code: NotRequired[str]
    bank_account_type: NotRequired[BankAccountTypeOrStr]
    bank_account_holder_type: NotRequired[BankAccountHolderTypeOrStr]
    last_four: NotRequired[str]
