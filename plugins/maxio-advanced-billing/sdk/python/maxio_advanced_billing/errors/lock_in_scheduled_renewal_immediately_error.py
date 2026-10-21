from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_response1 import ErrorListResponse1

LockInScheduledRenewalImmediatelyErrorBody: TypeAlias = ErrorListResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _LockInScheduledRenewalImmediatelyError:
    def map(self, status_code: int, content: bytes) -> LockInScheduledRenewalImmediatelyErrorBody:
        match status_code:
            case 422:
                return decode_json[ErrorListResponse1](content)
            case _:
                return RawError(status_code, content)


lock_in_scheduled_renewal_immediately_error_mapper: Final[
    ErrorMapper[LockInScheduledRenewalImmediatelyErrorBody]
] = _LockInScheduledRenewalImmediatelyError()
