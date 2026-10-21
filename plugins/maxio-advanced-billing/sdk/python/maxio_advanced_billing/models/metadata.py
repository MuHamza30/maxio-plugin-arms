from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class Metadata(SdkBaseModel):
    id: OptionalNullable[int] = UNSET
    value: OptionalNullable[str] = UNSET
    resource_id: OptionalNullable[int] = UNSET
    name: Optional[str] = UNSET
    deleted_at: OptionalNullable[RFC3339DateTime] = UNSET
    metafield_id: OptionalNullable[int] = UNSET


class MetadataDict(TypedDict):
    id: NotRequired[int | None]
    value: NotRequired[str | None]
    resource_id: NotRequired[int | None]
    name: NotRequired[str]
    deleted_at: NotRequired[RFC3339DateTime | None]
    metafield_id: NotRequired[int | None]
