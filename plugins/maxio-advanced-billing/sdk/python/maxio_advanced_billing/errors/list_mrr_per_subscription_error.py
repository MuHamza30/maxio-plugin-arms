from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.subscriptions_mrr_error_response1 import SubscriptionsMrrErrorResponse1

ListMrrPerSubscriptionErrorBody: TypeAlias = SubscriptionsMrrErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _ListMrrPerSubscriptionError:
    def map(self, status_code: int, content: bytes) -> ListMrrPerSubscriptionErrorBody:
        match status_code:
            case 400:
                return decode_json[SubscriptionsMrrErrorResponse1](content)
            case _:
                return RawError(status_code, content)


list_mrr_per_subscription_error_mapper: Final[
    ErrorMapper[ListMrrPerSubscriptionErrorBody]
] = _ListMrrPerSubscriptionError()
