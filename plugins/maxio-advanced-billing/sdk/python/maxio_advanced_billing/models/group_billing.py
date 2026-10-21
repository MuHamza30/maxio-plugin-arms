from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class GroupBilling(SdkBaseModel):
    """(Optional) Attributes related to billing date and accrual. Note: Only applicable for new subscriptions."""

    accrue: bool = False
    """A flag indicating whether or not to accrue charges on the new subscription."""

    align_date: bool = False
    """A flag indicating whether or not to align the billing date of the new subscription with the billing date of the
    primary subscription of the hierarchy's default subscription group. Required to be true if prorate is also true."""

    prorate: bool = False
    """A flag indicating whether or not to prorate billing of the new subscription for the current period. A value of
    true is ignored unless align_date is also true."""


class GroupBillingDict(TypedDict):
    accrue: NotRequired[bool]
    align_date: NotRequired[bool]
    prorate: NotRequired[bool]
