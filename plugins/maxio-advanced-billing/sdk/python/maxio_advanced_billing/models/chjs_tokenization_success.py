from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .tokenized_payment_profile import TokenizedPaymentProfile, TokenizedPaymentProfileDict


class ChjsTokenizationSuccess(SdkBaseModel):
    payment_profile: TokenizedPaymentProfile
    gateway_customer_id: OptionalNullable[int] = UNSET


class ChjsTokenizationSuccessDict(TypedDict):
    payment_profile: TokenizedPaymentProfileDict
    gateway_customer_id: NotRequired[int | None]
