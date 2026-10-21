from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

CancelDunningErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _CancelDunningError:
    def map(self, status_code: int, content: bytes) -> CancelDunningErrorBody:
        match status_code:
            case 422:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


cancel_dunning_error_mapper: Final[ErrorMapper[CancelDunningErrorBody]] = _CancelDunningError()
