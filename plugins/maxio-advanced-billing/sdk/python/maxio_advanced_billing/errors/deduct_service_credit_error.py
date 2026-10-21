from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unions.deduct_service_credit_error_response import DeductServiceCreditErrorResponse

DeductServiceCreditErrorBody: TypeAlias = DeductServiceCreditErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _DeductServiceCreditError:
    def map(self, status_code: int, content: bytes) -> DeductServiceCreditErrorBody:
        match status_code:
            case 422:
                return decode_json[DeductServiceCreditErrorResponse](content)
            case _:
                return RawError(status_code, content)


deduct_service_credit_error_mapper: Final[ErrorMapper[DeductServiceCreditErrorBody]] = _DeductServiceCreditError()
