from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class InvoiceAvataxDetails(SdkBaseModel):
    id: OptionalNullable[int] = UNSET
    status: OptionalNullable[str] = UNSET
    document_code: OptionalNullable[str] = UNSET
    commit_date: OptionalNullable[RFC3339DateTime] = UNSET
    modify_date: OptionalNullable[RFC3339DateTime] = UNSET


class InvoiceAvataxDetailsDict(TypedDict):
    id: NotRequired[int | None]
    status: NotRequired[str | None]
    document_code: NotRequired[str | None]
    commit_date: NotRequired[RFC3339DateTime | None]
    modify_date: NotRequired[RFC3339DateTime | None]
