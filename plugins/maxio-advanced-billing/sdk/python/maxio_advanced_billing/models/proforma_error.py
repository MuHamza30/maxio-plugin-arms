from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .base_string_error import BaseStringError, BaseStringErrorDict


class ProformaError(SdkBaseModel):
    subscription: Optional[BaseStringError] = UNSET
    """The error is base if it is not directly associated with a single attribute."""


class ProformaErrorDict(TypedDict):
    subscription: NotRequired[BaseStringErrorDict]
