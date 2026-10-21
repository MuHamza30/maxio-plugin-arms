from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_payment_profile import CreatePaymentProfile, CreatePaymentProfileDict


class CreatePaymentProfileRequest(SdkBaseModel):
    payment_profile: CreatePaymentProfile


class CreatePaymentProfileRequestDict(TypedDict):
    payment_profile: CreatePaymentProfileDict
