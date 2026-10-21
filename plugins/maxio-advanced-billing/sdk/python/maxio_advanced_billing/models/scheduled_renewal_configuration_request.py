from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .scheduled_renewal_configuration_request_body import (
    ScheduledRenewalConfigurationRequestBody,
    ScheduledRenewalConfigurationRequestBodyDict,
)


class ScheduledRenewalConfigurationRequest(SdkBaseModel):
    renewal_configuration: ScheduledRenewalConfigurationRequestBody


class ScheduledRenewalConfigurationRequestDict(TypedDict):
    renewal_configuration: ScheduledRenewalConfigurationRequestBodyDict
