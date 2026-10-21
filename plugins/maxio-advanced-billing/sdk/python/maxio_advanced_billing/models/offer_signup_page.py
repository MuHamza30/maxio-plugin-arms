from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OfferSignupPage(SdkBaseModel):
    id: Optional[int] = UNSET
    nickname: Optional[str] = UNSET
    enabled: Optional[bool] = UNSET
    return_url: Optional[str] = UNSET
    return_params: Optional[str] = UNSET
    url: Optional[str] = UNSET


class OfferSignupPageDict(TypedDict):
    id: NotRequired[int]
    nickname: NotRequired[str]
    enabled: NotRequired[bool]
    return_url: NotRequired[str]
    return_params: NotRequired[str]
    url: NotRequired[str]
