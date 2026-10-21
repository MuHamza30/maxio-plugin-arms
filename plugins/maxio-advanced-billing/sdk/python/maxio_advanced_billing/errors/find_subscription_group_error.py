from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

FindSubscriptionGroupErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _FindSubscriptionGroupError:
    def map(self, status_code: int, content: bytes) -> FindSubscriptionGroupErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


find_subscription_group_error_mapper: Final[ErrorMapper[FindSubscriptionGroupErrorBody]] = _FindSubscriptionGroupError()
