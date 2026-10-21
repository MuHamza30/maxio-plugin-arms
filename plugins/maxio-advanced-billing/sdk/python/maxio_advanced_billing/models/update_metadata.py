from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpdateMetadata(SdkBaseModel):
    current_name: Optional[str] = UNSET
    name: Optional[str] = UNSET
    value: Optional[str] = UNSET


class UpdateMetadataDict(TypedDict):
    current_name: NotRequired[str]
    name: NotRequired[str]
    value: NotRequired[str]
