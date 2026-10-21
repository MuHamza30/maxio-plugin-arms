from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.bank_account_holder_type import BankAccountHolderTypeOrStr
from .enums.bank_account_type import BankAccountTypeOrStr
from .enums.bank_account_vault import BankAccountVaultOrStr
from .enums.payment_type import PaymentTypeOrStr


class SubscriptionGroupBankAccount(SdkBaseModel):
    bank_name: Optional[str] = UNSET
    """(Required when creating a subscription with ACH or GoCardless) The name of the bank where the customer’s account
    resides"""

    bank_account_number: Optional[str] = UNSET
    """(Required when creating a subscription with ACH. Required when creating a subscription with GoCardless and
    bank_iban is blank) The customerʼs bank account number"""

    bank_routing_number: Optional[str] = UNSET
    """(Required when creating a subscription with ACH. Optional when creating a subscription with GoCardless.) The
    routing number of the bank. It becomes bank_code while passing via GoCardless API."""

    bank_iban: Optional[str] = UNSET
    """(Optional when creating a subscription with GoCardless). International Bank Account Number. Alternatively, local
    bank details can be provided."""

    bank_branch_code: Optional[str] = UNSET
    """(Optional when creating a subscription with GoCardless) Branch code. Alternatively, an IBAN can be provided."""

    bank_account_type: Optional[BankAccountTypeOrStr] = UNSET
    """Defaults to checking"""

    bank_account_holder_type: Optional[BankAccountHolderTypeOrStr] = UNSET
    """Defaults to personal"""

    payment_type: Optional[PaymentTypeOrStr] = UNSET
    billing_address: Optional[str] = UNSET
    billing_city: Optional[str] = UNSET
    billing_state: Optional[str] = UNSET
    billing_zip: Optional[str] = UNSET
    billing_country: Optional[str] = UNSET
    chargify_token: Optional[str] = UNSET
    current_vault: Optional[BankAccountVaultOrStr] = UNSET
    """The vault that stores the payment profile with the provided vault_token. Use ``bogus`` for testing."""

    gateway_handle: Optional[str] = UNSET


class SubscriptionGroupBankAccountDict(TypedDict):
    bank_name: NotRequired[str]
    bank_account_number: NotRequired[str]
    bank_routing_number: NotRequired[str]
    bank_iban: NotRequired[str]
    bank_branch_code: NotRequired[str]
    bank_account_type: NotRequired[BankAccountTypeOrStr]
    bank_account_holder_type: NotRequired[BankAccountHolderTypeOrStr]
    payment_type: NotRequired[PaymentTypeOrStr]
    billing_address: NotRequired[str]
    billing_city: NotRequired[str]
    billing_state: NotRequired[str]
    billing_zip: NotRequired[str]
    billing_country: NotRequired[str]
    chargify_token: NotRequired[str]
    current_vault: NotRequired[BankAccountVaultOrStr]
    gateway_handle: NotRequired[str]
