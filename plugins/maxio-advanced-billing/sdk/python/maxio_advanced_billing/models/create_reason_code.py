from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateReasonCode(SdkBaseModel):
    code: str
    """The unique identifier for the ReasonCode"""

    description: str
    """The friendly summary of what the code signifies"""

    position: Optional[int] = UNSET
    """The order that code appears in lists"""


class CreateReasonCodeDict(TypedDict):
    code: str
    description: str
    position: NotRequired[int]
