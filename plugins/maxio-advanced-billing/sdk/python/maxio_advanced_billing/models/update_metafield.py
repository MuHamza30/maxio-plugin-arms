from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.metafield_input import MetafieldInputOrStr
from .metafield_scope import MetafieldScope, MetafieldScopeDict


class UpdateMetafield(SdkBaseModel):
    current_name: Optional[str] = UNSET
    name: Optional[str] = UNSET
    scope: Optional[MetafieldScope] = UNSET
    """Warning: When updating a metafield's scope attribute, all scope attributes must be passed. Partially complete
    scope attributes will override the existing settings."""

    input_type: Optional[MetafieldInputOrStr] = UNSET
    """Indicates the type of metafield. A text metafield allows any string value. Dropdown and radio metafields have a
    set of values that can be selected. Defaults to 'text'."""

    enum: Optional[list[str]] = UNSET
    """Only applicable when input_type is radio or dropdown."""


class UpdateMetafieldDict(TypedDict):
    current_name: NotRequired[str]
    name: NotRequired[str]
    scope: NotRequired[MetafieldScopeDict]
    input_type: NotRequired[MetafieldInputOrStr]
    enum: NotRequired[list[str]]
