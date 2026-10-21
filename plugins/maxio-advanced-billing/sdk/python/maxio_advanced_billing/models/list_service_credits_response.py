from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .service_credit1 import ServiceCredit1, ServiceCredit1Dict


class ListServiceCreditsResponse(SdkBaseModel):
    service_credits: Optional[list[ServiceCredit1]] = UNSET


class ListServiceCreditsResponseDict(TypedDict):
    service_credits: NotRequired[list[ServiceCredit1Dict]]
