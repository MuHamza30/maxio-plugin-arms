from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .prepayment_aggregated_error import PrepaymentAggregatedError, PrepaymentAggregatedErrorDict


class RefundPrepaymentAggregatedError(SdkBaseModel):
    refund: Optional[PrepaymentAggregatedError] = UNSET


class RefundPrepaymentAggregatedErrorDict(TypedDict):
    refund: NotRequired[PrepaymentAggregatedErrorDict]
