from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scheduled_renewal_configuration import ScheduledRenewalConfiguration, ScheduledRenewalConfigurationDict


class ScheduledRenewalConfigurationsResponse(SdkBaseModel):
    scheduled_renewal_configurations: Optional[list[ScheduledRenewalConfiguration]] = UNSET


class ScheduledRenewalConfigurationsResponseDict(TypedDict):
    scheduled_renewal_configurations: NotRequired[list[ScheduledRenewalConfigurationDict]]
