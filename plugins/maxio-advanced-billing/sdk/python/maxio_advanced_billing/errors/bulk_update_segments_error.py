from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.event_based_billing_segment1 import EventBasedBillingSegment1

BulkUpdateSegmentsErrorBody: TypeAlias = EventBasedBillingSegment1 | RawError


@dataclass(frozen=True, slots=True)
class _BulkUpdateSegmentsError:
    def map(self, status_code: int, content: bytes) -> BulkUpdateSegmentsErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case 422:
                return decode_json[EventBasedBillingSegment1](content)
            case _:
                return RawError(status_code, content)


bulk_update_segments_error_mapper: Final[ErrorMapper[BulkUpdateSegmentsErrorBody]] = _BulkUpdateSegmentsError()
