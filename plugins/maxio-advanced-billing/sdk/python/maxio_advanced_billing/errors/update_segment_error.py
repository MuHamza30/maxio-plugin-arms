from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.event_based_billing_segment_errors1 import EventBasedBillingSegmentErrors1

UpdateSegmentErrorBody: TypeAlias = EventBasedBillingSegmentErrors1 | RawError


@dataclass(frozen=True, slots=True)
class _UpdateSegmentError:
    def map(self, status_code: int, content: bytes) -> UpdateSegmentErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case 422:
                return decode_json[EventBasedBillingSegmentErrors1](content)
            case _:
                return RawError(status_code, content)


update_segment_error_mapper: Final[ErrorMapper[UpdateSegmentErrorBody]] = _UpdateSegmentError()
