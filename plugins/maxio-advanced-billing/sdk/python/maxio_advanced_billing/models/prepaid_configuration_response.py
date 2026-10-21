from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .prepaid_configuration import PrepaidConfiguration, PrepaidConfigurationDict


class PrepaidConfigurationResponse(SdkBaseModel):
    prepaid_configuration: PrepaidConfiguration


class PrepaidConfigurationResponseDict(TypedDict):
    prepaid_configuration: PrepaidConfigurationDict
