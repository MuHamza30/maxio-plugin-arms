from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

ReadReasonCodeErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ReadReasonCodeError:
    def map(self, status_code: int, content: bytes) -> ReadReasonCodeErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


read_reason_code_error_mapper: Final[ErrorMapper[ReadReasonCodeErrorBody]] = _ReadReasonCodeError()
