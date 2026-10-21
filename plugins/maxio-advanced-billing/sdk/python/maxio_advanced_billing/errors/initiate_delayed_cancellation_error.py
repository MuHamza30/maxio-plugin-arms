from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

InitiateDelayedCancellationErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _InitiateDelayedCancellationError:
    def map(self, status_code: int, content: bytes) -> InitiateDelayedCancellationErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case 422:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


initiate_delayed_cancellation_error_mapper: Final[
    ErrorMapper[InitiateDelayedCancellationErrorBody]
] = _InitiateDelayedCancellationError()
