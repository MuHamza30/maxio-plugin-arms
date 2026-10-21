from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .refund_prepayment_aggregated_error import RefundPrepaymentAggregatedError, RefundPrepaymentAggregatedErrorDict


class RefundPrepaymentAggregatedErrorsResponse(SdkBaseModel):
    """Errors returned on creating a refund prepayment, grouped by field, as arrays of strings."""

    errors: Optional[RefundPrepaymentAggregatedError] = UNSET


class RefundPrepaymentAggregatedErrorsResponseDict(TypedDict):
    errors: NotRequired[RefundPrepaymentAggregatedErrorDict]
