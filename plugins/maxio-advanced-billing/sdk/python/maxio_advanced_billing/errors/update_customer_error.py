from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.customer_error_response1 import CustomerErrorResponse1

UpdateCustomerErrorBody: TypeAlias = CustomerErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateCustomerError:
    def map(self, status_code: int, content: bytes) -> UpdateCustomerErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case 422:
                return decode_json[CustomerErrorResponse1](content)
            case _:
                return RawError(status_code, content)


update_customer_error_mapper: Final[ErrorMapper[UpdateCustomerErrorBody]] = _UpdateCustomerError()
