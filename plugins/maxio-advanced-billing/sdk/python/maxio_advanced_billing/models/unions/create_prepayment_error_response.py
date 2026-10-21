from __future__ import annotations

from typing import TypeAlias

from ..error_list_response1 import ErrorListResponse1, ErrorListResponse1Dict
from ..error_string_map_response1 import ErrorStringMapResponse1, ErrorStringMapResponse1Dict

CreatePrepaymentErrorResponse: TypeAlias = ErrorListResponse1 | ErrorStringMapResponse1

CreatePrepaymentErrorResponseDict: TypeAlias = ErrorListResponse1Dict | ErrorStringMapResponse1Dict
