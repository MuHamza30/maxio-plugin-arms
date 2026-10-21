from __future__ import annotations

from typing import TypeAlias

from ..error_list_response1 import ErrorListResponse1, ErrorListResponse1Dict
from ..error_string_map_response1 import ErrorStringMapResponse1, ErrorStringMapResponse1Dict

PrepaidConfigurationErrorResponse: TypeAlias = ErrorStringMapResponse1 | ErrorListResponse1

PrepaidConfigurationErrorResponseDict: TypeAlias = ErrorStringMapResponse1Dict | ErrorListResponse1Dict
