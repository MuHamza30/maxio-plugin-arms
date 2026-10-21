from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .contract import Contract, ContractDict
from .scheduled_renewal_configuration_item import (
    ScheduledRenewalConfigurationItem,
    ScheduledRenewalConfigurationItemDict,
)


class ScheduledRenewalConfiguration(SdkBaseModel):
    id: Optional[int] = UNSET
    """ID of the renewal."""

    site_id: Optional[int] = UNSET
    """ID of the site to which the renewal belongs."""

    subscription_id: Optional[int] = UNSET
    """The id of the subscription."""

    starts_at: Optional[RFC3339DateTime] = UNSET
    ends_at: Optional[RFC3339DateTime] = UNSET
    lock_in_at: Optional[RFC3339DateTime] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET
    status: Optional[str] = UNSET
    scheduled_renewal_configuration_items: Optional[list[ScheduledRenewalConfigurationItem]] = UNSET
    contract: Optional[Contract] = UNSET
    """Contract linked to the scheduled renewal configuration."""


class ScheduledRenewalConfigurationDict(TypedDict):
    id: NotRequired[int]
    site_id: NotRequired[int]
    subscription_id: NotRequired[int]
    starts_at: NotRequired[RFC3339DateTime]
    ends_at: NotRequired[RFC3339DateTime]
    lock_in_at: NotRequired[RFC3339DateTime]
    created_at: NotRequired[RFC3339DateTime]
    status: NotRequired[str]
    scheduled_renewal_configuration_items: NotRequired[list[ScheduledRenewalConfigurationItemDict]]
    contract: NotRequired[ContractDict]
