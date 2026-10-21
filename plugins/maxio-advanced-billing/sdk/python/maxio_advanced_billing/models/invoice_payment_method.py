from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class InvoicePaymentMethod(SdkBaseModel):
    details: Optional[str] = UNSET
    kind: Optional[str] = UNSET
    memo: Optional[str] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")
    card_brand: Optional[str] = UNSET
    card_expiration: Optional[str] = UNSET
    last_four: OptionalNullable[str] = UNSET
    masked_card_number: Optional[str] = UNSET


class InvoicePaymentMethodDict(TypedDict):
    details: NotRequired[str]
    kind: NotRequired[str]
    memo: NotRequired[str]
    type_: NotRequired[str]
    card_brand: NotRequired[str]
    card_expiration: NotRequired[str]
    last_four: NotRequired[str | None]
    masked_card_number: NotRequired[str]
