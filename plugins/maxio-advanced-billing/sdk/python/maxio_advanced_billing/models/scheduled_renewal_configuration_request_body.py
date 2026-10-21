from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ScheduledRenewalConfigurationRequestBody(SdkBaseModel):
    starts_at: Optional[RFC3339DateTime] = UNSET
    """(Optional) Start of the renewal term."""

    ends_at: Optional[RFC3339DateTime] = UNSET
    """(Optional) End of the renewal term."""

    lock_in_at: Optional[RFC3339DateTime] = UNSET
    """(Optional) Lock-in date for the renewal."""

    contract_id: Optional[int] = UNSET
    """(Optional) Existing contract to associate with the scheduled renewal. Contracts must be enabled for your site."""

    create_new_contract: Optional[bool] = UNSET
    """(Optional) Set to true to create a new contract when contracts are enabled. Contracts must be enabled for your
    site."""


class ScheduledRenewalConfigurationRequestBodyDict(TypedDict):
    starts_at: NotRequired[RFC3339DateTime]
    ends_at: NotRequired[RFC3339DateTime]
    lock_in_at: NotRequired[RFC3339DateTime]
    contract_id: NotRequired[int]
    create_new_contract: NotRequired[bool]
