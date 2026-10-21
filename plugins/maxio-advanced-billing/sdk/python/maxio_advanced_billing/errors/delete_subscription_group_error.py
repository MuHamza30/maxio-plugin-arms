from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

DeleteSubscriptionGroupErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteSubscriptionGroupError:
    def map(self, status_code: int, content: bytes) -> DeleteSubscriptionGroupErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


delete_subscription_group_error_mapper: Final[
    ErrorMapper[DeleteSubscriptionGroupErrorBody]
] = _DeleteSubscriptionGroupError()
