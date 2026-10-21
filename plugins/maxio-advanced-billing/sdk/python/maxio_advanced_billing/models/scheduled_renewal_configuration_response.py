from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scheduled_renewal_configuration import ScheduledRenewalConfiguration, ScheduledRenewalConfigurationDict


class ScheduledRenewalConfigurationResponse(SdkBaseModel):
    scheduled_renewal_configuration: Optional[ScheduledRenewalConfiguration] = UNSET


class ScheduledRenewalConfigurationResponseDict(TypedDict):
    scheduled_renewal_configuration: NotRequired[ScheduledRenewalConfigurationDict]
