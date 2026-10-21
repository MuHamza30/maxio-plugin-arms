from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .created_prepayment import CreatedPrepayment, CreatedPrepaymentDict


class CreatePrepaymentResponse(SdkBaseModel):
    prepayment: CreatedPrepayment


class CreatePrepaymentResponseDict(TypedDict):
    prepayment: CreatedPrepaymentDict
