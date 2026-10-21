from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

UpdateCustomerInformationErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateCustomerInformationError:
    def map(self, status_code: int, content: bytes) -> UpdateCustomerInformationErrorBody:
        match status_code:
            case 404 | 422:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


update_customer_information_error_mapper: Final[
    ErrorMapper[UpdateCustomerInformationErrorBody]
] = _UpdateCustomerInformationError()
