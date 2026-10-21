from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .refund_prepayment_base_refund_error import RefundPrepaymentBaseRefundError, RefundPrepaymentBaseRefundErrorDict


class RefundPrepaymentBaseErrorsResponse1(SdkBaseModel):
    """Errors returned on creating a refund prepayment when bad request"""

    errors: Optional[RefundPrepaymentBaseRefundError] = UNSET


class RefundPrepaymentBaseErrorsResponse1Dict(TypedDict):
    errors: NotRequired[RefundPrepaymentBaseRefundErrorDict]
