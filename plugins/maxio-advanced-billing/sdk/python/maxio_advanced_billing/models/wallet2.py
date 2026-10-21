from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Wallet2(SdkBaseModel):
    name: OptionalNullable[str] = UNSET
    """A merchant-facing label for the wallet. Surrounding spaces are stripped; a blank or ``null`` value clears it."""


class Wallet2Dict(TypedDict):
    name: NotRequired[str | None]
