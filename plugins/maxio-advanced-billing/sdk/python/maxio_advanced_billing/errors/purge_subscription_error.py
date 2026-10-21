from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.subscription_response import SubscriptionResponse

PurgeSubscriptionErrorBody: TypeAlias = SubscriptionResponse | RawError


@dataclass(frozen=True, slots=True)
class _PurgeSubscriptionError:
    def map(self, status_code: int, content: bytes) -> PurgeSubscriptionErrorBody:
        match status_code:
            case 400:
                return decode_json[SubscriptionResponse](content)
            case _:
                return RawError(status_code, content)


purge_subscription_error_mapper: Final[ErrorMapper[PurgeSubscriptionErrorBody]] = _PurgeSubscriptionError()
