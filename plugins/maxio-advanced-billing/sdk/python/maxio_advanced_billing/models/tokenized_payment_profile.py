from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TokenizedPaymentProfile(SdkBaseModel):
    id: int
    vault_token: Optional[str] = UNSET
    gateway_handle: OptionalNullable[str] = UNSET
    customer_vault_token: OptionalNullable[str] = UNSET


class TokenizedPaymentProfileDict(TypedDict):
    id: int
    vault_token: NotRequired[str]
    gateway_handle: NotRequired[str | None]
    customer_vault_token: NotRequired[str | None]
