from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.renewal_configuration_item import RenewalConfigurationItem, RenewalConfigurationItemDict


class ScheduledRenewalConfigurationItemRequest(SdkBaseModel):
    renewal_configuration_item: RenewalConfigurationItem


class ScheduledRenewalConfigurationItemRequestDict(TypedDict):
    renewal_configuration_item: RenewalConfigurationItemDict
