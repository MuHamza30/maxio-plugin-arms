from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .register import Register, RegisterDict


class Contract(SdkBaseModel):
    """Contract linked to the scheduled renewal configuration."""

    id: Optional[int] = UNSET
    maxio_id: Optional[str] = UNSET
    number: OptionalNullable[str] = UNSET
    register: Optional[Register] = UNSET


class ContractDict(TypedDict):
    id: NotRequired[int]
    maxio_id: NotRequired[str]
    number: NotRequired[str | None]
    register: NotRequired[RegisterDict]
