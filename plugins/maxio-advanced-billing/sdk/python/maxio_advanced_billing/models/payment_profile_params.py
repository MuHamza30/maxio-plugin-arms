from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaymentProfileParams(SdkBaseModel):
    """PCI-safe cardholder fields only. Full card numbers, CVV, and billing address are never included."""

    first_name: Optional[str] = UNSET
    last_name: Optional[str] = UNSET
    card_type: Optional[str] = UNSET


class PaymentProfileParamsDict(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    card_type: NotRequired[str]
