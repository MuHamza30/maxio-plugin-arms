from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class BatchJob(SdkBaseModel):
    id: Optional[int] = UNSET
    finished_at: OptionalNullable[RFC3339DateTime] = UNSET
    row_count: OptionalNullable[int] = UNSET
    created_at: OptionalNullable[RFC3339DateTime] = UNSET
    completed: Optional[str] = UNSET


class BatchJobDict(TypedDict):
    id: NotRequired[int]
    finished_at: NotRequired[RFC3339DateTime | None]
    row_count: NotRequired[int | None]
    created_at: NotRequired[RFC3339DateTime | None]
    completed: NotRequired[str]
