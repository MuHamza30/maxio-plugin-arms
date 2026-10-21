from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CreateProductFamily(SdkBaseModel):
    name: str
    handle: OptionalNullable[str] = UNSET
    description: OptionalNullable[str] = UNSET
    surcharging: Optional[bool] = UNSET
    """Whether surcharging applies to this product family. Defaults to ``true`` when omitted. Only applied on sites
    where surcharging is enabled."""


class CreateProductFamilyDict(TypedDict):
    name: str
    handle: NotRequired[str | None]
    description: NotRequired[str | None]
    surcharging: NotRequired[bool]
