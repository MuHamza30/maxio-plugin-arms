from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_string_map_response1 import ErrorStringMapResponse1

UpdatePaymentProfileErrorBody: TypeAlias = ErrorStringMapResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdatePaymentProfileError:
    def map(self, status_code: int, content: bytes) -> UpdatePaymentProfileErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case 422:
                return decode_json[ErrorStringMapResponse1](content)
            case _:
                return RawError(status_code, content)


update_payment_profile_error_mapper: Final[ErrorMapper[UpdatePaymentProfileErrorBody]] = _UpdatePaymentProfileError()
