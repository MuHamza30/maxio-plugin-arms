from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.custom_field_owner import CustomFieldOwnerOrStr


class InvoiceCustomField(SdkBaseModel):
    owner_id: Optional[int] = UNSET
    owner_type: Optional[CustomFieldOwnerOrStr] = UNSET
    name: Optional[str] = UNSET
    value: Optional[str] = UNSET
    metadatum_id: Optional[int] = UNSET


class InvoiceCustomFieldDict(TypedDict):
    owner_id: NotRequired[int]
    owner_type: NotRequired[CustomFieldOwnerOrStr]
    name: NotRequired[str]
    value: NotRequired[str]
    metadatum_id: NotRequired[int]
