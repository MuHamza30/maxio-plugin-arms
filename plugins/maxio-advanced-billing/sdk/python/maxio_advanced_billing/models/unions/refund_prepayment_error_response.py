from __future__ import annotations

from typing import TypeAlias

from ..error_string_map_response1 import ErrorStringMapResponse1, ErrorStringMapResponse1Dict
from ..refund_prepayment_aggregated_errors_response import (
    RefundPrepaymentAggregatedErrorsResponse,
    RefundPrepaymentAggregatedErrorsResponseDict,
)

RefundPrepaymentErrorResponse: TypeAlias = RefundPrepaymentAggregatedErrorsResponse | ErrorStringMapResponse1

RefundPrepaymentErrorResponseDict: TypeAlias = (
    RefundPrepaymentAggregatedErrorsResponseDict | ErrorStringMapResponse1Dict
)
