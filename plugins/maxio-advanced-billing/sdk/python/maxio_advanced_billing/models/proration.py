from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Proration(SdkBaseModel):
    preserve_period: Optional[bool] = UNSET
    """The alternative to sending preserve_period as a direct attribute to migration"""


class ProrationDict(TypedDict):
    preserve_period: NotRequired[bool]
