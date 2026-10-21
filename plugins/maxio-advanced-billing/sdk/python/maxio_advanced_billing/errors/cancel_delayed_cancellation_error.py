from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

CancelDelayedCancellationErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _CancelDelayedCancellationError:
    def map(self, status_code: int, content: bytes) -> CancelDelayedCancellationErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


cancel_delayed_cancellation_error_mapper: Final[
    ErrorMapper[CancelDelayedCancellationErrorBody]
] = _CancelDelayedCancellationError()
