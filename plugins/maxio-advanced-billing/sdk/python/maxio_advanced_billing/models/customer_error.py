from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CustomerError(SdkBaseModel):
    customer: Optional[str] = UNSET


class CustomerErrorDict(TypedDict):
    customer: NotRequired[str]
