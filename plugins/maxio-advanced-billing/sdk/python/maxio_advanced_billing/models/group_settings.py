from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .group_billing import GroupBilling, GroupBillingDict
from .group_target import GroupTarget, GroupTargetDict


class GroupSettings(SdkBaseModel):
    target: GroupTarget
    """Attributes of the target customer who will be the responsible payer of the created subscription. Required."""

    billing: Optional[GroupBilling] = UNSET
    """(Optional) Attributes related to billing date and accrual. Note: Only applicable for new subscriptions."""


class GroupSettingsDict(TypedDict):
    target: GroupTargetDict
    billing: NotRequired[GroupBillingDict]
