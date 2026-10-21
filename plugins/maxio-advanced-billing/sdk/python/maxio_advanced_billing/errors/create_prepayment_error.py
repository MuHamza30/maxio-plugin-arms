from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unions.create_prepayment_error_response import CreatePrepaymentErrorResponse

CreatePrepaymentErrorBody: TypeAlias = CreatePrepaymentErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _CreatePrepaymentError:
    def map(self, status_code: int, content: bytes) -> CreatePrepaymentErrorBody:
        match status_code:
            case 422:
                return decode_json[CreatePrepaymentErrorResponse](content)
            case _:
                return RawError(status_code, content)


create_prepayment_error_mapper: Final[ErrorMapper[CreatePrepaymentErrorBody]] = _CreatePrepaymentError()
