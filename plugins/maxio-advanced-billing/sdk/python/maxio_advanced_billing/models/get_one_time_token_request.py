from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.payment_profile_model import PaymentProfileModel, PaymentProfileModelDict


class GetOneTimeTokenRequest(SdkBaseModel):
    payment_profile: PaymentProfileModel


class GetOneTimeTokenRequestDict(TypedDict):
    payment_profile: PaymentProfileModelDict
