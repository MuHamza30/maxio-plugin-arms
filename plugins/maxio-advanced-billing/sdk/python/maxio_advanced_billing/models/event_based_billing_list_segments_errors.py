from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .errors_model import ErrorsModel, ErrorsModelDict


class EventBasedBillingListSegmentsErrors(SdkBaseModel):
    errors: Optional[ErrorsModel] = UNSET


class EventBasedBillingListSegmentsErrorsDict(TypedDict):
    errors: NotRequired[ErrorsModelDict]
