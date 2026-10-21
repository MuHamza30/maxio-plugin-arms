from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .group_settings import GroupSettings, GroupSettingsDict


class AddSubscriptionToAGroup(SdkBaseModel):
    group: Optional[GroupSettings] = UNSET


class AddSubscriptionToAGroupDict(TypedDict):
    group: NotRequired[GroupSettingsDict]
