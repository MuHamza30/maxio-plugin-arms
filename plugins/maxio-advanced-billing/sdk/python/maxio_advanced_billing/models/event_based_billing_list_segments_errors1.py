from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .errors_model import ErrorsModel, ErrorsModelDict


class EventBasedBillingListSegmentsErrors1(SdkBaseModel):
    errors: Optional[ErrorsModel] = UNSET


class EventBasedBillingListSegmentsErrors1Dict(TypedDict):
    errors: NotRequired[ErrorsModelDict]
