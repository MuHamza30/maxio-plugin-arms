from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.event_based_billing_segment1 import EventBasedBillingSegment1

BulkCreateSegmentsErrorBody: TypeAlias = EventBasedBillingSegment1 | RawError


@dataclass(frozen=True, slots=True)
class _BulkCreateSegmentsError:
    def map(self, status_code: int, content: bytes) -> BulkCreateSegmentsErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case 422:
                return decode_json[EventBasedBillingSegment1](content)
            case _:
                return RawError(status_code, content)


bulk_create_segments_error_mapper: Final[ErrorMapper[BulkCreateSegmentsErrorBody]] = _BulkCreateSegmentsError()
