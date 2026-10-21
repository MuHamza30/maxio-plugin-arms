from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OriginInvoice(SdkBaseModel):
    uid: Optional[str] = UNSET
    """The UID of the invoice serving as an origin invoice."""

    number: Optional[str] = UNSET
    """The number of the invoice serving as an origin invoice."""


class OriginInvoiceDict(TypedDict):
    uid: NotRequired[str]
    number: NotRequired[str]
