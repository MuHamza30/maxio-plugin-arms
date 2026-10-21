from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payment_profile_params import PaymentProfileParams, PaymentProfileParamsDict


class ChjsTokenizationFailure(SdkBaseModel):
    errors: str
    payment_profile_params: Optional[PaymentProfileParams] = UNSET
    """PCI-safe cardholder fields only. Full card numbers, CVV, and billing address are never included."""


class ChjsTokenizationFailureDict(TypedDict):
    errors: str
    payment_profile_params: NotRequired[PaymentProfileParamsDict]
