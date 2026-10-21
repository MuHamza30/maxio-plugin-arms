from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.subscription_group_create_error_response1 import SubscriptionGroupCreateErrorResponse1

CreateSubscriptionGroupErrorBody: TypeAlias = SubscriptionGroupCreateErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _CreateSubscriptionGroupError:
    def map(self, status_code: int, content: bytes) -> CreateSubscriptionGroupErrorBody:
        match status_code:
            case 422:
                return decode_json[SubscriptionGroupCreateErrorResponse1](content)
            case _:
                return RawError(status_code, content)


create_subscription_group_error_mapper: Final[
    ErrorMapper[CreateSubscriptionGroupErrorBody]
] = _CreateSubscriptionGroupError()
