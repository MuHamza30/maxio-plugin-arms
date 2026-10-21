from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.bank_account_holder_type import BankAccountHolderTypeOrStr
from .enums.bank_account_type import BankAccountTypeOrStr
from .enums.bank_account_vault import BankAccountVaultOrStr


class GetOneTimeTokenBankAccountPaymentProfile(SdkBaseModel):
    id: OptionalNullable[str] = UNSET
    first_name: str
    last_name: str
    customer_id: OptionalNullable[str] = UNSET
    current_vault: BankAccountVaultOrStr
    """The vault that stores the payment profile with the provided vault_token. Use ``bogus`` for testing."""

    vault_token: str
    billing_address: str
    billing_address_2: Optional[str] = UNSET
    billing_city: str
    billing_country: str
    billing_state: str
    billing_zip: str
    bank_name: str
    masked_bank_routing_number: str
    masked_bank_account_number: str
    bank_account_type: BankAccountTypeOrStr
    """Defaults to checking"""

    bank_account_holder_type: BankAccountHolderTypeOrStr
    """Defaults to personal"""

    payment_type: str
    disabled: bool
    site_gateway_setting_id: int
    customer_vault_token: OptionalNullable[str] = UNSET
    gateway_handle: OptionalNullable[str] = UNSET
    verified: OptionalNullable[bool] = UNSET


class GetOneTimeTokenBankAccountPaymentProfileDict(TypedDict):
    id: NotRequired[str | None]
    first_name: str
    last_name: str
    customer_id: NotRequired[str | None]
    current_vault: BankAccountVaultOrStr
    vault_token: str
    billing_address: str
    billing_address_2: NotRequired[str]
    billing_city: str
    billing_country: str
    billing_state: str
    billing_zip: str
    bank_name: str
    masked_bank_routing_number: str
    masked_bank_account_number: str
    bank_account_type: BankAccountTypeOrStr
    bank_account_holder_type: BankAccountHolderTypeOrStr
    payment_type: str
    disabled: bool
    site_gateway_setting_id: int
    customer_vault_token: NotRequired[str | None]
    gateway_handle: NotRequired[str | None]
    verified: NotRequired[bool | None]
