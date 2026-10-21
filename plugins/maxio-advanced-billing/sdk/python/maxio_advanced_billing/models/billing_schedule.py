from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel


class BillingSchedule(SdkBaseModel):
    """Billing schedule settings for component allocations or usages on multi-frequency subscriptions. Use this to start
    a component's billing period on a custom date instead of aligning with the product charge schedule."""

    initial_billing_at: OptionalNullable[Date] = UNSET
    """Custom start date (ISO 8601 date, YYYY-MM-DD) for the component's first billing period. If omitted or null,
    billing aligns with the product schedule. If provided, date must be on or after the minimum allowed date for the
    subscription or component."""


class BillingScheduleDict(TypedDict):
    initial_billing_at: NotRequired[Date | None]
