from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.pay_pal_vault import PayPalVaultOrStr
from .enums.payment_type import PaymentType, PaymentTypeOrStr


class PaypalPaymentProfile(SdkBaseModel):
    id: Optional[int] = UNSET
    """The Chargify-assigned ID of the stored PayPal payment profile."""

    first_name: Optional[str] = UNSET
    """The first name of the PayPal account holder"""

    last_name: Optional[str] = UNSET
    """The last name of the PayPal account holder"""

    customer_id: Optional[int] = UNSET
    """The Chargify-assigned id for the customer record to which the PayPal account belongs"""

    current_vault: Optional[PayPalVaultOrStr] = UNSET
    """The vault that stores the payment profile with the provided vault_token."""

    vault_token: Optional[str] = UNSET
    """The “token” provided by your vault storage for an already stored payment profile"""

    billing_address: OptionalNullable[str] = UNSET
    """The current billing street address for the PayPal account"""

    billing_city: OptionalNullable[str] = UNSET
    """The current billing address city for the PayPal account"""

    billing_state: OptionalNullable[str] = UNSET
    """The current billing address state for the PayPal account"""

    billing_zip: OptionalNullable[str] = UNSET
    """The current billing address zip code for the PayPal account"""

    billing_country: OptionalNullable[str] = UNSET
    """The current billing address country for the PayPal account"""

    customer_vault_token: OptionalNullable[str] = UNSET
    billing_address_2: OptionalNullable[str] = UNSET
    """The current billing street address, second line, for the PayPal account"""

    payment_type: PaymentTypeOrStr = PaymentType.PAYPAL_ACCOUNT
    site_gateway_setting_id: OptionalNullable[int] = UNSET
    gateway_handle: OptionalNullable[str] = UNSET
    paypal_email: Optional[str] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    """A timestamp indicating when this payment profile was created"""

    updated_at: Optional[RFC3339DateTime] = UNSET
    """A timestamp indicating when this payment profile was last updated"""


class PaypalPaymentProfileDict(TypedDict):
    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    customer_id: NotRequired[int]
    current_vault: NotRequired[PayPalVaultOrStr]
    vault_token: NotRequired[str]
    billing_address: NotRequired[str | None]
    billing_city: NotRequired[str | None]
    billing_state: NotRequired[str | None]
    billing_zip: NotRequired[str | None]
    billing_country: NotRequired[str | None]
    customer_vault_token: NotRequired[str | None]
    billing_address_2: NotRequired[str | None]
    payment_type: PaymentTypeOrStr
    site_gateway_setting_id: NotRequired[int | None]
    gateway_handle: NotRequired[str | None]
    paypal_email: NotRequired[str]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
