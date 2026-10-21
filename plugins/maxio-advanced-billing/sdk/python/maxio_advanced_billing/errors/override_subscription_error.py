from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.single_error_response1 import SingleErrorResponse1

OverrideSubscriptionErrorBody: TypeAlias = SingleErrorResponse1 | RawError


@dataclass(frozen=True, slots=True)
class _OverrideSubscriptionError:
    def map(self, status_code: int, content: bytes) -> OverrideSubscriptionErrorBody:
        match status_code:
            case 422:
                return decode_json[SingleErrorResponse1](content)
            case _:
                return RawError(status_code, content)


override_subscription_error_mapper: Final[ErrorMapper[OverrideSubscriptionErrorBody]] = _OverrideSubscriptionError()
