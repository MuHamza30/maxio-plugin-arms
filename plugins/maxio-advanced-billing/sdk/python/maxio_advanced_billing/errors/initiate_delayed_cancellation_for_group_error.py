from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

InitiateDelayedCancellationForGroupErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _InitiateDelayedCancellationForGroupError:
    def map(self, status_code: int, content: bytes) -> InitiateDelayedCancellationForGroupErrorBody:
        match status_code:
            case 422:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


initiate_delayed_cancellation_for_group_error_mapper: Final[
    ErrorMapper[InitiateDelayedCancellationForGroupErrorBody]
] = _InitiateDelayedCancellationForGroupError()
