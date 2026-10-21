from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AppliedCreditNoteData(SdkBaseModel):
    uid: Optional[str] = UNSET
    """The UID of the credit note"""

    number: Optional[str] = UNSET
    """The number of the credit note"""


class AppliedCreditNoteDataDict(TypedDict):
    uid: NotRequired[str]
    number: NotRequired[str]
