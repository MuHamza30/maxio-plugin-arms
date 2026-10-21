from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

PreviewCustomerInformationChangesErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _PreviewCustomerInformationChangesError:
    def map(self, status_code: int, content: bytes) -> PreviewCustomerInformationChangesErrorBody:
        match status_code:
            case 404 | 422:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


preview_customer_information_changes_error_mapper: Final[
    ErrorMapper[PreviewCustomerInformationChangesErrorBody]
] = _PreviewCustomerInformationChangesError()
