from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class ProductFamily(SdkBaseModel):
    id: Optional[int] = UNSET
    name: Optional[str] = UNSET
    handle: Optional[str] = UNSET
    accounting_code: OptionalNullable[str] = UNSET
    description: OptionalNullable[str] = UNSET
    surcharging: Optional[bool] = UNSET
    """Whether surcharging applies to this product family. Only included on sites where surcharging is enabled."""

    created_at: Optional[RFC3339DateTime] = UNSET
    updated_at: Optional[RFC3339DateTime] = UNSET
    archived_at: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp indicating when this product family was archived. ``null`` if the product family is not archived."""


class ProductFamilyDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    handle: NotRequired[str]
    accounting_code: NotRequired[str | None]
    description: NotRequired[str | None]
    surcharging: NotRequired[bool]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    archived_at: NotRequired[RFC3339DateTime | None]
