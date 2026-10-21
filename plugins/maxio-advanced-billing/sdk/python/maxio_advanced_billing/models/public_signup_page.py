from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PublicSignupPage(SdkBaseModel):
    id: Optional[int] = UNSET
    """The id of the signup page (public_signup_pages only)"""

    return_url: OptionalNullable[str] = UNSET
    """The url to which a customer will be returned after a successful signup (public_signup_pages only)."""

    return_params: OptionalNullable[str] = UNSET
    """The params to be appended to the return_url (public_signup_pages only)"""

    url: Optional[str] = UNSET
    """The url where the signup page can be viewed (public_signup_pages only)."""


class PublicSignupPageDict(TypedDict):
    id: NotRequired[int]
    return_url: NotRequired[str | None]
    return_params: NotRequired[str | None]
    url: NotRequired[str]
