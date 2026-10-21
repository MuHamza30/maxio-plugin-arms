from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_prepayment import CreatePrepayment, CreatePrepaymentDict


class CreatePrepaymentRequest(SdkBaseModel):
    prepayment: CreatePrepayment


class CreatePrepaymentRequestDict(TypedDict):
    prepayment: CreatePrepaymentDict
