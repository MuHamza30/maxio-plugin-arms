from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

ReadOneTimeTokenErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ReadOneTimeTokenError:
    def map(self, status_code: int, content: bytes) -> ReadOneTimeTokenErrorBody:
        match status_code:
            case 404:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


read_one_time_token_error_mapper: Final[ErrorMapper[ReadOneTimeTokenErrorBody]] = _ReadOneTimeTokenError()
