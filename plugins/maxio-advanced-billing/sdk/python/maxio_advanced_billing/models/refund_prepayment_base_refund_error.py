from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .base_refund_error import BaseRefundError, BaseRefundErrorDict


class RefundPrepaymentBaseRefundError(SdkBaseModel):
    refund: Optional[BaseRefundError] = UNSET


class RefundPrepaymentBaseRefundErrorDict(TypedDict):
    refund: NotRequired[BaseRefundErrorDict]
