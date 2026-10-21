from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .reactivation_billing import ReactivationBilling, ReactivationBillingDict
from .unions.resume import Resume, ResumeDict


class ReactivateSubscriptionRequest(SdkBaseModel):
    calendar_billing: Optional[ReactivationBilling] = UNSET
    """These values are only applicable to subscriptions using calendar billing."""

    include_trial: Optional[bool] = UNSET
    """If ``true`` is sent, the reactivated Subscription will include a trial if one is available. If ``false`` is sent,
    the trial period will be ignored."""

    preserve_balance: Optional[bool] = UNSET
    """If ``true`` is passed, the existing subscription balance will NOT be cleared/reset before adding the additional
    reactivation charges."""

    coupon_code: Optional[str] = UNSET
    """The coupon code to be applied during reactivation."""

    use_credits_and_prepayments: Optional[bool] = UNSET
    """If true is sent, Advanced Billing will use service credits and prepayments upon reactivation. If false is sent,
    the service credits and prepayments will be ignored."""

    resume: Optional[Resume] = UNSET
    """If ``true``, Advanced Billing will attempt to resume the subscription's billing period. If not resumable, the
    subscription will be reactivated with a new billing period. If ``false`` or omitted, Advanced Billing will only
    attempt to reactivate the subscription with a new billing period, regardless of whether or not the subscription is
    resumable."""


class ReactivateSubscriptionRequestDict(TypedDict):
    calendar_billing: NotRequired[ReactivationBillingDict]
    include_trial: NotRequired[bool]
    preserve_balance: NotRequired[bool]
    coupon_code: NotRequired[str]
    use_credits_and_prepayments: NotRequired[bool]
    resume: NotRequired[ResumeDict]
