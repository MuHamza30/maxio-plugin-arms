from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scheduled_renewal_configuration_item import (
    ScheduledRenewalConfigurationItem,
    ScheduledRenewalConfigurationItemDict,
)


class ScheduledRenewalConfigurationItemResponse(SdkBaseModel):
    scheduled_renewal_configuration_item: Optional[ScheduledRenewalConfigurationItem] = UNSET


class ScheduledRenewalConfigurationItemResponseDict(TypedDict):
    scheduled_renewal_configuration_item: NotRequired[ScheduledRenewalConfigurationItemDict]
