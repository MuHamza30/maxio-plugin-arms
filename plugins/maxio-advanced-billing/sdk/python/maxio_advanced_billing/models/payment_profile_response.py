from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.payment_profile import PaymentProfile, PaymentProfileDict


class PaymentProfileResponse(SdkBaseModel):
    payment_profile: PaymentProfile


class PaymentProfileResponseDict(TypedDict):
    payment_profile: PaymentProfileDict
