from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unions.cancel_subscription_error_response import CancelSubscriptionErrorResponse

CancelSubscriptionErrorBody: TypeAlias = CancelSubscriptionErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _CancelSubscriptionError:
    def map(self, status_code: int, content: bytes) -> CancelSubscriptionErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case 422:
                return decode_json[CancelSubscriptionErrorResponse](content)
            case _:
                return RawError(status_code, content)


cancel_subscription_error_mapper: Final[ErrorMapper[CancelSubscriptionErrorBody]] = _CancelSubscriptionError()
