from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PayerError(SdkBaseModel):
    last_name: Optional[list[str]] = UNSET
    first_name: Optional[list[str]] = UNSET
    email: Optional[list[str]] = UNSET


class PayerErrorDict(TypedDict):
    last_name: NotRequired[list[str]]
    first_name: NotRequired[list[str]]
    email: NotRequired[list[str]]
