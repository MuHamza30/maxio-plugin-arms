from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OkResponse(SdkBaseModel):
    ok: Optional[str] = UNSET


class OkResponseDict(TypedDict):
    ok: NotRequired[str]
