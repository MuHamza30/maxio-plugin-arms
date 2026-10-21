from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.include_option import IncludeOptionOrStr


class MetafieldScope(SdkBaseModel):
    """Warning: When updating a metafield's scope attribute, all scope attributes must be passed. Partially complete
    scope attributes will override the existing settings."""

    csv: Optional[IncludeOptionOrStr] = UNSET
    """Include (1) or exclude (0) metafields from the csv export."""

    invoices: Optional[IncludeOptionOrStr] = UNSET
    """Include (1) or exclude (0) metafields from invoices."""

    statements: Optional[IncludeOptionOrStr] = UNSET
    """Include (1) or exclude (0) metafields from statements."""

    portal: Optional[IncludeOptionOrStr] = UNSET
    """Include (1) or exclude (0) metafields from the portal."""

    public_show: Optional[IncludeOptionOrStr] = UNSET
    """Include (1) or exclude (0) metafields used in `Embeddable Components
    <page:development-tools/embeddable-components/overview>`__ from being viewable by your ecosystem."""

    public_edit: Optional[IncludeOptionOrStr] = UNSET
    """Include (1) or exclude (0) metafields used in `Embeddable Components
    <page:development-tools/embeddable-components/overview>`__ from being editable by your ecosystem."""

    hosted: Optional[list[str]] = UNSET


class MetafieldScopeDict(TypedDict):
    csv: NotRequired[IncludeOptionOrStr]
    invoices: NotRequired[IncludeOptionOrStr]
    statements: NotRequired[IncludeOptionOrStr]
    portal: NotRequired[IncludeOptionOrStr]
    public_show: NotRequired[IncludeOptionOrStr]
    public_edit: NotRequired[IncludeOptionOrStr]
    hosted: NotRequired[list[str]]
