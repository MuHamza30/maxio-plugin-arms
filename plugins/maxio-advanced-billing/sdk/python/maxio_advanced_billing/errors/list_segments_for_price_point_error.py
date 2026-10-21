from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.event_based_billing_list_segments_errors1 import EventBasedBillingListSegmentsErrors1

ListSegmentsForPricePointErrorBody: TypeAlias = EventBasedBillingListSegmentsErrors1 | RawError


@dataclass(frozen=True, slots=True)
class _ListSegmentsForPricePointError:
    def map(self, status_code: int, content: bytes) -> ListSegmentsForPricePointErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case 422:
                return decode_json[EventBasedBillingListSegmentsErrors1](content)
            case _:
                return RawError(status_code, content)


list_segments_for_price_point_error_mapper: Final[
    ErrorMapper[ListSegmentsForPricePointErrorBody]
] = _ListSegmentsForPricePointError()
