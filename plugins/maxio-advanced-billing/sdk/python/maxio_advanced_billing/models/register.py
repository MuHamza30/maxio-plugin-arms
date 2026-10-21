from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Register(SdkBaseModel):
    id: Optional[int] = UNSET
    maxio_id: Optional[str] = UNSET
    name: Optional[str] = UNSET
    currency_code: Optional[str] = UNSET
    """The ISO 4217 currency code (3 character string) representing the currency of an invoice transaction."""


class RegisterDict(TypedDict):
    id: NotRequired[int]
    maxio_id: NotRequired[str]
    name: NotRequired[str]
    currency_code: NotRequired[str]
