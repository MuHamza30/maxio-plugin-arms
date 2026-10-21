from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreditCardAttributes(SdkBaseModel):
    full_number: Optional[str] = UNSET
    expiration_month: Optional[str] = UNSET
    expiration_year: Optional[str] = UNSET


class CreditCardAttributesDict(TypedDict):
    full_number: NotRequired[str]
    expiration_month: NotRequired[str]
    expiration_year: NotRequired[str]
