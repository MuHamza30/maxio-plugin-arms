from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class CancellationOptions(SdkBaseModel):
    cancellation_message: Optional[str] = UNSET
    """An indication as to why the subscription is being canceled. For your internal use."""

    reason_code: Optional[str] = UNSET
    """The reason code associated with the cancellation. Use the `List Reason Codes
    <$e/Reason%20Codes/listReasonCodes>`__ endpoint to retrieve the reason codes associated with your site."""

    cancel_at_end_of_period: Optional[bool] = UNSET
    """When true, the subscription is cancelled at the current period end instead of immediately. To use this option,
    the Schedule Subscription Cancellation feature must be enabled on your site."""

    scheduled_cancellation_at: OptionalNullable[RFC3339DateTime] = UNSET
    """Schedules the cancellation on the provided date. This option is not applicable for prepaid subscriptions. To use
    this option, the Schedule Subscription Cancellation feature must be enabled on your site."""

    refund_prepayment_account_balance: Optional[bool] = UNSET
    """Applies to prepaid subscriptions. When true, which is the default, the remaining prepaid balance is refunded as
    part of cancellation processing. When false, prepaid balance is not refunded as part of cancellation processing. To
    use this option, the Schedule Subscription Cancellation feature must be enabled on your site."""


class CancellationOptionsDict(TypedDict):
    cancellation_message: NotRequired[str]
    reason_code: NotRequired[str]
    cancel_at_end_of_period: NotRequired[bool]
    scheduled_cancellation_at: NotRequired[RFC3339DateTime | None]
    refund_prepayment_account_balance: NotRequired[bool]
