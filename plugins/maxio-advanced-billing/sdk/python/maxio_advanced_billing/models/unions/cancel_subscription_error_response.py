from __future__ import annotations

from typing import TypeAlias

from ..error_list_response1 import ErrorListResponse1, ErrorListResponse1Dict
from ..single_error_response1 import SingleErrorResponse1, SingleErrorResponse1Dict

CancelSubscriptionErrorResponse: TypeAlias = ErrorListResponse1 | SingleErrorResponse1

CancelSubscriptionErrorResponseDict: TypeAlias = ErrorListResponse1Dict | SingleErrorResponse1Dict
