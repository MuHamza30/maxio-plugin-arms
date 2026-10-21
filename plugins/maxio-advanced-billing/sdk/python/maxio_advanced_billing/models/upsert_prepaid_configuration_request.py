from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .upsert_prepaid_configuration import UpsertPrepaidConfiguration, UpsertPrepaidConfigurationDict


class UpsertPrepaidConfigurationRequest(SdkBaseModel):
    prepaid_configuration: UpsertPrepaidConfiguration


class UpsertPrepaidConfigurationRequestDict(TypedDict):
    prepaid_configuration: UpsertPrepaidConfigurationDict
