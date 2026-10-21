from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BaseRefundError(SdkBaseModel):
    base: Optional[list[Any]] = UNSET


class BaseRefundErrorDict(TypedDict):
    base: NotRequired[list[Any]]
