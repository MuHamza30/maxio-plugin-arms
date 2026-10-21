from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class PublicKey(SdkBaseModel):
    public_key: Optional[str] = UNSET
    requires_security_token: Optional[bool] = UNSET
    created_at: Optional[RFC3339DateTime] = UNSET


class PublicKeyDict(TypedDict):
    public_key: NotRequired[str]
    requires_security_token: NotRequired[bool]
    created_at: NotRequired[RFC3339DateTime]
