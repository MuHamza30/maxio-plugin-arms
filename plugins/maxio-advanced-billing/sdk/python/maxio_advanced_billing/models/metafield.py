from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.metafield_input import MetafieldInputOrStr
from .metafield_scope import MetafieldScope, MetafieldScopeDict
from .unions.enum_model import EnumModel, EnumModelDict


class Metafield(SdkBaseModel):
    id: Optional[int] = UNSET
    name: Optional[str] = UNSET
    scope: Optional[MetafieldScope] = UNSET
    """Warning: When updating a metafield's scope attribute, all scope attributes must be passed. Partially complete
    scope attributes will override the existing settings."""

    data_count: Optional[int] = UNSET
    """The amount of subscriptions this metafield has been applied to in Advanced Billing."""

    input_type: Optional[MetafieldInputOrStr] = UNSET
    """Indicates the type of metafield. A text metafield allows any string value. Dropdown and radio metafields have a
    set of values that can be selected. Defaults to 'text'."""

    enum: OptionalNullable[EnumModel] = UNSET


class MetafieldDict(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    scope: NotRequired[MetafieldScopeDict]
    data_count: NotRequired[int]
    input_type: NotRequired[MetafieldInputOrStr]
    enum: NotRequired[EnumModelDict | None]
