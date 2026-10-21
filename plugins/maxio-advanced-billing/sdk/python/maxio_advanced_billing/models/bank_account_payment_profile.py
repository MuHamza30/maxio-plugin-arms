from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.bank_account_holder_type import BankAccountHolderTypeOrStr
from .enums.bank_account_type import BankAccountTypeOrStr
from .enums.bank_account_vault import BankAccountVaultOrStr
from .enums.payment_type import PaymentType, PaymentTypeOrStr


class BankAccountPaymentProfile(SdkBaseModel):
    id: Optional[int] = UNSET
    """The Chargify-assigned ID of the stored bank account. This value can be used as an input to payment_profile_id
    when creating a subscription, in order to re-use a stored payment profile for the same customer."""

    first_name: Optional[str] = UNSET
    """The first name of the bank account holder"""

    last_name: Optional[str] = UNSET
    """The last name of the bank account holder"""

    customer_id: Optional[int] = UNSET
    """The Chargify-assigned ID for the customer record to which the bank account belongs"""

    current_vault: Optional[BankAccountVaultOrStr] = UNSET
    """The vault that stores the payment profile with the provided vault_token. Use ``bogus`` for testing."""

    vault_token: Optional[str] = UNSET
    """The "token" provided by your vault storage for an already stored payment profile"""

    billing_address: OptionalNullable[str] = UNSET
    """The current billing street address for the bank account"""

    billing_city: OptionalNullable[str] = UNSET
    """The current billing address city for the bank account"""

    billing_state: OptionalNullable[str] = UNSET
    """The current billing address state for the bank account"""

    billing_zip: OptionalNullable[str] = UNSET
    """The current billing address zip code for the bank account"""

    billing_country: OptionalNullable[str] = UNSET
    """The current billing address country for the bank account"""

    customer_vault_token: OptionalNullable[str] = UNSET
    """(only for Authorize.Net CIM storage): the customerProfileId for the owner of the customerPaymentProfileId
    provided as the vault_token."""

    billing_address_2: OptionalNullable[str] = UNSET
    """The current billing street address, second line, for the bank account"""

    bank_name: Optional[str] = UNSET
    """The bank where the account resides"""

    masked_bank_routing_number: OptionalNullable[str] = UNSET
    """A string representation of the stored bank routing number with all but the last 4 digits marked with X's (i.e.
    'XXXXXXX1111'). payment_type will be bank_account."""

    masked_bank_account_number: OptionalNullable[str] = UNSET
    """A string representation of the stored bank account number with all but the last 4 digits marked with X's (i.e.
    'XXXXXXX1111')."""

    bank_account_type: Optional[BankAccountTypeOrStr] = UNSET
    """Defaults to checking"""

    bank_account_holder_type: Optional[BankAccountHolderTypeOrStr] = UNSET
    """Defaults to personal"""

    payment_type: PaymentTypeOrStr = PaymentType.BANK_ACCOUNT
    verified: bool = False
    """Denotes whether a bank account has been verified by providing the amounts of two small deposits made into the
    account."""

    site_gateway_setting_id: OptionalNullable[int] = UNSET
    gateway_handle: OptionalNullable[str] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    """A timestamp indicating when this payment profile was created"""

    updated_at: Optional[RFC3339DateTime] = UNSET
    """A timestamp indicating when this payment profile was last updated"""


class BankAccountPaymentProfileDict(TypedDict):
    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    customer_id: NotRequired[int]
    current_vault: NotRequired[BankAccountVaultOrStr]
    vault_token: NotRequired[str]
    billing_address: NotRequired[str | None]
    billing_city: NotRequired[str | None]
    billing_state: NotRequired[str | None]
    billing_zip: NotRequired[str | None]
    billing_country: NotRequired[str | None]
    customer_vault_token: NotRequired[str | None]
    billing_address_2: NotRequired[str | None]
    bank_name: NotRequired[str]
    masked_bank_routing_number: NotRequired[str | None]
    masked_bank_account_number: NotRequired[str | None]
    bank_account_type: NotRequired[BankAccountTypeOrStr]
    bank_account_holder_type: NotRequired[BankAccountHolderTypeOrStr]
    payment_type: PaymentTypeOrStr
    verified: NotRequired[bool]
    site_gateway_setting_id: NotRequired[int | None]
    gateway_handle: NotRequired[str | None]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
