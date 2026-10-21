from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpdateReasonCode(SdkBaseModel):
    code: Optional[str] = UNSET
    """The unique identifier for the ReasonCode"""

    description: Optional[str] = UNSET
    """The friendly summary of what the code signifies"""

    position: Optional[int] = UNSET
    """The order that code appears in lists"""


class UpdateReasonCodeDict(TypedDict):
    code: NotRequired[str]
    description: NotRequired[str]
    position: NotRequired[int]
