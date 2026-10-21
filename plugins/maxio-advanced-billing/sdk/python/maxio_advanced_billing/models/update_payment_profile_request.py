from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_payment_profile import UpdatePaymentProfile, UpdatePaymentProfileDict


class UpdatePaymentProfileRequest(SdkBaseModel):
    payment_profile: UpdatePaymentProfile


class UpdatePaymentProfileRequestDict(TypedDict):
    payment_profile: UpdatePaymentProfileDict
