from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.errors1 import Errors1, Errors1Dict


class CustomerErrorResponse1(SdkBaseModel):
    errors: Optional[Errors1] = UNSET


class CustomerErrorResponse1Dict(TypedDict):
    errors: NotRequired[Errors1Dict]
