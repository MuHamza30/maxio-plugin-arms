from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

ReadPaymentProfileErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ReadPaymentProfileError:
    def map(self, status_code: int, content: bytes) -> ReadPaymentProfileErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


read_payment_profile_error_mapper: Final[ErrorMapper[ReadPaymentProfileErrorBody]] = _ReadPaymentProfileError()
