from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AgreementAcceptance(SdkBaseModel):
    """Required when creating a subscription with Maxio Payments."""

    ip_address: Optional[str] = UNSET
    """Required when providing agreement acceptance params."""

    terms_url: Optional[str] = UNSET
    """Required when creating a subscription with Maxio Payments. Either terms_url or privacy_policy_url is required
    when providing agreement_acceptance params."""

    privacy_policy_url: Optional[str] = UNSET
    return_refund_policy_url: Optional[str] = UNSET
    delivery_policy_url: Optional[str] = UNSET
    secure_checkout_policy_url: Optional[str] = UNSET


class AgreementAcceptanceDict(TypedDict):
    ip_address: NotRequired[str]
    terms_url: NotRequired[str]
    privacy_policy_url: NotRequired[str]
    return_refund_policy_url: NotRequired[str]
    delivery_policy_url: NotRequired[str]
    secure_checkout_policy_url: NotRequired[str]
