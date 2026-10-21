from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

ReadSubscriptionComponentErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ReadSubscriptionComponentError:
    def map(self, status_code: int, content: bytes) -> ReadSubscriptionComponentErrorBody:
        match status_code:
            case 404:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


read_subscription_component_error_mapper: Final[
    ErrorMapper[ReadSubscriptionComponentErrorBody]
] = _ReadSubscriptionComponentError()
