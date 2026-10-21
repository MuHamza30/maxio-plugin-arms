from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResumeOptions(SdkBaseModel):
    require_resume: Optional[bool] = UNSET
    """Chargify will only attempt to resume the subscription's billing period. If not resumable, the subscription will
    be left in its current state."""

    forgive_balance: Optional[bool] = UNSET
    """Indicates whether or not Chargify should clear the subscription's existing balance before attempting to resume
    the subscription. If subscription cannot be resumed, the balance will remain as it was before the attempt to resume
    was made."""


class ResumeOptionsDict(TypedDict):
    require_resume: NotRequired[bool]
    forgive_balance: NotRequired[bool]
