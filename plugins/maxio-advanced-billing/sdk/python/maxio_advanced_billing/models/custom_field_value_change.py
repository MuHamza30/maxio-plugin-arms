from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CustomFieldValueChange(SdkBaseModel):
    event_type: str
    metafield_name: str
    metafield_id: int
    old_value: str | None
    new_value: str | None
    resource_type: str
    resource_id: int


class CustomFieldValueChangeDict(TypedDict):
    event_type: str
    metafield_name: str
    metafield_id: int
    old_value: str | None
    new_value: str | None
    resource_type: str
    resource_id: int
