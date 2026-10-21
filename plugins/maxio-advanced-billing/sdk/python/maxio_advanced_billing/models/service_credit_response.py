from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .service_credit import ServiceCredit, ServiceCreditDict


class ServiceCreditResponse(SdkBaseModel):
    service_credit: ServiceCredit


class ServiceCreditResponseDict(TypedDict):
    service_credit: ServiceCreditDict
