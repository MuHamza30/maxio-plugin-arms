from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.errors11 import Errors11, Errors11Dict


class SubscriptionGroupCreateErrorResponse(SdkBaseModel):
    errors: Errors11


class SubscriptionGroupCreateErrorResponseDict(TypedDict):
    errors: Errors11Dict
