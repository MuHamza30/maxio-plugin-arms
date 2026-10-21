from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.credit_scheme import CreditSchemeOrStr


class CreditSchemeRequest(SdkBaseModel):
    credit_scheme: CreditSchemeOrStr


class CreditSchemeRequestDict(TypedDict):
    credit_scheme: CreditSchemeOrStr
