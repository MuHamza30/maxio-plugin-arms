from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.bank_account_holder_type import BankAccountHolderTypeOrStr
from .enums.bank_account_type import BankAccountTypeOrStr
from .enums.bank_account_vault import BankAccountVaultOrStr
from .enums.payment_type import PaymentTypeOrStr


class BankAccountAttributes(SdkBaseModel):
    chargify_token: Optional[str] = UNSET
    bank_name: Optional[str] = UNSET
    """(Required when creating a subscription with ACH or GoCardless) The name of the bank where the customer’s account
    resides"""

    bank_routing_number: Optional[str] = UNSET
    """(Required when creating a subscription with ACH; optional when creating a subscription with GoCardless). The
    routing number of the bank. It becomes bank_code while passing via GoCardless API."""

    bank_account_number: Optional[str] = UNSET
    """(Required when creating a subscription with ACH. Required when creating a subscription with GoCardless and
    bank_iban is blank) The customerʼs bank account number"""

    bank_account_type: Optional[BankAccountTypeOrStr] = UNSET
    """Defaults to checking"""

    bank_branch_code: Optional[str] = UNSET
    """(Optional when creating a subscription with GoCardless) Branch code. Alternatively, an IBAN can be provided."""

    bank_iban: Optional[str] = UNSET
    """(Optional when creating a subscription with GoCardless). International Bank Account Number. Alternatively, local
    bank details can be provided."""

    bank_account_holder_type: Optional[BankAccountHolderTypeOrStr] = UNSET
    """Defaults to personal"""

    payment_type: Optional[PaymentTypeOrStr] = UNSET
    current_vault: Optional[BankAccountVaultOrStr] = UNSET
    """The vault that stores the payment profile with the provided vault_token. Use ``bogus`` for testing."""

    vault_token: Optional[str] = UNSET
    customer_vault_token: Optional[str] = UNSET
    """(only for Authorize.Net CIM storage or Square) The customerProfileId for the owner of the
    customerPaymentProfileId provided as the vault_token"""


class BankAccountAttributesDict(TypedDict):
    chargify_token: NotRequired[str]
    bank_name: NotRequired[str]
    bank_routing_number: NotRequired[str]
    bank_account_number: NotRequired[str]
    bank_account_type: NotRequired[BankAccountTypeOrStr]
    bank_branch_code: NotRequired[str]
    bank_iban: NotRequired[str]
    bank_account_holder_type: NotRequired[BankAccountHolderTypeOrStr]
    payment_type: NotRequired[PaymentTypeOrStr]
    current_vault: NotRequired[BankAccountVaultOrStr]
    vault_token: NotRequired[str]
    customer_vault_token: NotRequired[str]
